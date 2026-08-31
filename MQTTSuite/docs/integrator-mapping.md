# MQTTIntegrator mapping reference

[← MQTTSuite](../README.md) · [MQTTIntegrator README](../mqttintegrator/README.md) · [Sibling topic branches example](integrator-sibling-topics-example.md) · [Integrator HTTP API](integrator-http-api.md) · [Configuration](configuration.md) · [Capabilities](capabilities.md)

MQTTIntegrator subscribes to MQTT 3.1.1 topics, matches received publications against a hierarchical mapping document, and republishes zero, one, or many derived publications through the same MQTT client connection. MQTTBroker can reuse the same mapper in process.

This reference describes the mapping engine in merged MQTTSuite `master` at [`6c0ff62c612694a6111ff971c446327938130cf0`](https://github.com/SNodeC/mqttsuite/tree/6c0ff62c612694a6111ff971c446327938130cf0). That revision includes the narrow wildcard correction from [PR #22](https://github.com/SNodeC/mqttsuite/pull/22) / [`d15f70a`](https://github.com/SNodeC/mqttsuite/commit/d15f70a2818d291638c50aa2e2116a9e49ebd9e1): `#` now has MQTT multi-level wildcard behavior, including zero remaining levels, while `+` remains single-level. The landing-page qualification did not execute a complete mapping scenario, so wildcard behavior here is source-verified rather than newly runtime-qualified.

The authoritative machine-readable shape is [`lib/mapping-schema.json`](https://github.com/SNodeC/mqttsuite/blob/6c0ff62c612694a6111ff971c446327938130cf0/lib/mapping-schema.json). PR #22 did not change the schema.

## What a mapping contains

A mapping document has these top-level concerns:

```text
meta             optional version/comment metadata
discover_prefix  schema field; no mapper behavior established in current source
connection       MQTT session used by standalone MQTTIntegrator
mapping          recursive topic tree and mapping rules
```

The `mapping` tree is required. `connection` is optional in schema and supplies defaults when omitted.

A representative skeleton is:

```json
{
  "connection": {
    "client_id": "integrator-01",
    "keep_alive": 60,
    "clean_session": true,
    "username": "",
    "password": ""
  },
  "mapping": {
    "plugins": [],
    "topic_level": [
      {
        "name": "sensors",
        "topic_level": [
          {
            "name": "+",
            "topic_level": [
              {
                "name": "temperature",
                "subscription": { "qos": 1 },
                "json": []
              }
            ]
          }
        ]
      }
    ]
  }
}
```

> **Figure placeholder — Mapping pipeline.** Show incoming MQTT topic/payload → subscription/matching tree → first matching topic branch → static/value/JSON rule → template rendering → QoS/retain/delay → zero/one/many republishes.

## Connection block

The standalone Integrator obtains its MQTT CONNECT/session parameters from the mapping `connection` object. Current schema defaults are:

| Field | Default | Meaning |
| --- | ---: | --- |
| `client_id` | `""` | MQTT client ID |
| `keep_alive` | `60` | keepalive seconds |
| `clean_session` | `true` | MQTT clean-session flag |
| `will_topic` | `""` | will topic |
| `will_message` | `""` | will payload |
| `will_qos` | `0` | will QoS 0–2 |
| `will_retain` | `false` | will retain flag |
| `username` | `""` | MQTT CONNECT username |
| `password` | `""` | MQTT CONNECT password |

Changing connection settings through a deployed mapping causes MQTTIntegrator to reconnect. When connection settings stay equal, the administration reload path can update the subscription delta without replacing the connection.

Mapping files and mapping history can therefore contain credentials. Current administration read-back/error behavior does not provide write-only secret semantics; protect those files and the administration API as secret-bearing state.

## Topic tree

Topics are represented as a tree of MQTT topic levels rather than one flat filter string. Each node has a `name` and may contain child `topic_level` nodes, a `subscription`, and mapping-rule arrays.

For topic:

```text
sensors/room-01/temperature
```

a literal tree is conceptually:

```text
sensors
  room-01
    temperature
```

### Literal matching

A literal node matches the corresponding topic level exactly.

```json
{ "name": "temperature" }
```

### `+`

A node named `+` matches exactly one topic level. This is appropriate for trees such as:

```text
sensors/+/temperature
```

The matched topic itself remains available to the template context; the mapper does not create a separate named capture variable for `+`.

<a id="hash-multi-level-wildcard"></a>
### Multi-level wildcard (`#`)

A terminal node named `#` now has normal MQTT multi-level wildcard behavior in the mapper. It matches **zero or more remaining topic levels**.

A mapping tree representing `devices/#` can be written as:

```json
{
  "name": "devices",
  "topic_level": {
    "name": "#",
    "subscription": {
      "qos": 0,
      "value": {
        "mapped_topic": "archive/{{ topic }}",
        "mapping_template": "{{ message }}"
      }
    }
  }
}
```

That terminal `#` branch can match all of these:

```text
devices
devices/button
devices/room-01/temperature
devices/room-01/sensor/value
```

The first line is the MQTT **zero-level** case. The post-fix mapper specifically checks for a terminal `#` child when the concrete parent topic has been fully consumed. If the parent node itself has no `subscription`, the child `#` becomes the match. If the parent already has its own subscription mapping, that exact parent mapping remains the direct match.

Use `#` as a terminal multi-level wildcard. PR #22 changed only `MqttMapper::findMatchingTopicLevel()`; schema and unrelated mapping behavior were unchanged.

## Branch ordering and precedence

At a given tree level, current `MqttMapper` scans the configured `topic_level` array in document order and stops at the **first** branch that matches.

Relevant sibling types are:

- an exact literal;
- `+`, which matches one level;
- `#`, which matches the remaining subtree.

Order is therefore significant when siblings overlap. Prefer the most specific branches before broader wildcard branches. A useful ordering is:

```text
literal siblings
then + fallback
then # fallback
```

For example:

```json
"topic_level": [
  { "name": "temperature", "...": "specific rule" },
  { "name": "+", "...": "one-level fallback" },
  { "name": "#", "...": "remaining-subtree fallback" }
]
```

Putting `+` or `#` first can shadow later literal siblings. See the complete [sibling topic branches example](integrator-sibling-topics-example.md) for a runnable literal-plus-`+` case.

## Subscription extraction

A topic-tree node can contain:

```json
"subscription": {
  "qos": 1
}
```

MQTTIntegrator walks the tree and converts subscription points into MQTT topic filters. Subscription QoS is independent from the QoS later chosen for mapped output publications.

A terminal `#` subscription is extracted as an MQTT `#` filter and the mapper now applies the same multi-level meaning when processing delivered publications.

After CONNACK, the Integrator subscribes to the mapper-derived filters. On a mapping administration update, it computes subscribed/unsubscribed deltas when no reconnect is required.

## Mapping modes

A matching leaf/node can contain three kinds of mapping rules. The arrays can contain multiple entries, so one input publication can fan out to multiple outputs.

### Static mapping

Static mapping compares the incoming payload string to configured exact values.

Example:

```json
"static": [
  {
    "mapped_topic": "normalized/pump/state",
    "message_mapping": [
      { "message": "1", "mapped_message": "on" },
      { "message": "0", "mapped_message": "off" }
    ],
    "qos": 1,
    "retain": true
  }
]
```

When input payload is `1`, the mapper emits:

```text
Topic:   normalized/pump/state
Payload: on
QoS:     1
Retain:  true
```

A static rule whose `message_mapping` has no matching input produces no output for that rule.

### Scalar/value template mapping

Value mapping treats the incoming MQTT payload as a scalar string and makes it available to Inja templates.

Example:

```json
"value": [
  {
    "mapped_topic": "normalized/room-01/temperature",
    "mapping_template": "{{ message }}",
    "qos": 1,
    "retain": false
  }
]
```

Use this mode when the payload is already a useful scalar but the output topic or representation needs templating.

### JSON template mapping

JSON mapping parses the incoming payload with `nlohmann::json` and exposes the parsed JSON to the template environment.

Example:

```json
"json": [
  {
    "mapped_topic": "normalized/{{ message.device }}/temperature",
    "mapping_template": "{\"value\":{{ message.value }},\"unit\":\"{{ message.unit }}\"}",
    "qos": 1,
    "retain": false
  }
]
```

For an input such as:

```json
{"device":"room-01","value":21.7,"unit":"C"}
```

the templates can derive both topic and payload.

If the incoming payload is not valid JSON, JSON-template mappings do not produce an output. Raw storage or a scalar mapping may be more appropriate when payload shape is not guaranteed.

## Template context

Current mapper code constructs template state from the incoming publication. The context includes the MQTT message and metadata needed by the built-in templates, including:

- message/payload;
- topic;
- QoS;
- retain flag;
- packet/package identifier representation used by the mapper.

After rendering the configured output topic, the mapper also exposes the rendered `mapped_topic` while producing the mapped payload.

The template engine is [Inja](https://github.com/pantor/inja). MQTTSuite adds plugin functions to the same environment; it does not define a separate template language.

## Output fields

Each mapping output controls publication behavior independently.

### `mapped_topic`

The outgoing MQTT topic. For template modes this can itself contain an Inja expression.

### `mapping_template` / mapped message

- static rules select a `mapped_message` from `message_mapping`;
- value/JSON rules render `mapping_template`.

### QoS

Mapped outputs can choose QoS `0`, `1`, or `2`. This is **publish QoS**, not the subscription QoS used to receive the input.

### Retain

`retain` controls the outgoing PUBLISH retain flag. Schema default: `false`.

### Delay

Schema default is `-1`, which means immediate output in current mapper usage. A non-negative delay is placed in the Integrator's scheduled/delayed output list and emitted later by timer handling.

Treat delay as a delayed publish, not as durable queueing. This documentation does not claim persistence of scheduled outputs across process restart.

### Suppressions

Template mappings can declare suppressions. Current mapper checks rendered output against configured suppression values and omits matching outputs. Use suppression when a template result represents “do not publish” rather than a valid MQTT message.

## Fan-out

The mapping arrays are iterated, so a single matched input can emit more than one mapped publication.

A common pattern is:

```text
vendor/device payload
  ├─► normalized/device/temperature
  ├─► normalized/device/status
  └─► derived/alerts/device
```

Keep fan-out rules deterministic: overlapping topic branches are subject to first-branch precedence, while multiple rules inside the selected branch can all contribute outputs.

## A non-trivial example

The following example demonstrates literal matching, `+`, JSON templating, fan-out, output QoS/retain, and suppression. For terminal multi-level `#`, use the dedicated example in [Multi-level wildcard (`#`)](#hash-multi-level-wildcard).

```json
{
  "connection": {
    "client_id": "edge-normalizer",
    "keep_alive": 60,
    "clean_session": true
  },
  "mapping": {
    "plugins": [],
    "topic_level": [
      {
        "name": "vendor-a",
        "topic_level": [
          {
            "name": "+",
            "topic_level": [
              {
                "name": "telemetry",
                "subscription": { "qos": 1 },
                "json": [
                  {
                    "mapped_topic": "normalized/{{ message.device }}/temperature",
                    "mapping_template": "{\"value\":{{ message.temperature }},\"unit\":\"C\"}",
                    "qos": 1,
                    "retain": false
                  },
                  {
                    "mapped_topic": "normalized/{{ message.device }}/status",
                    "mapping_template": "{{ message.status }}",
                    "qos": 0,
                    "retain": true,
                    "suppressions": [""]
                  }
                ]
              }
            ]
          }
        ]
      }
    ]
  }
}
```

This is a **source-aligned example**, not recorded runtime output from the landing-page qualification.

## Plugins

The mapping document can list dynamic mapper plugins. The mapper opens each plugin through SNode.C's dynamic loader and looks for two C-linkage exported vectors:

```cpp
extern "C" std::vector<mqtt::lib::Function> functions;
extern "C" std::vector<mqtt::lib::VoidFunction> voidFunctions;
```

Each entry supplies:

- function name;
- number of arguments;
- callback operating on Inja JSON arguments.

The public ABI types are declared in [`lib/MqttMapperPlugin.h`](https://github.com/SNodeC/mqttsuite/blob/6c0ff62c612694a6111ff971c446327938130cf0/lib/MqttMapperPlugin.h).

Plugins extend template evaluation; they are native code loaded into the Integrator/Broker process. Treat plugin files as trusted executable code and match them to the MQTTSuite binary/ABI they were built against. This documentation does not claim a stable cross-version plugin ABI.

## Mapping-file selection and current startup behavior

`ConfigApplication` exposes:

```text
--mqtt-mapping-file <filename>
--mqtt-session-store <filename>
```

The Integrator application sets a default `mapping.json`, then current main seeds an inline demo mapping before SNode.C performs its later config/command-line parse. An **explicit** `--mqtt-mapping-file` supplied through the supported configuration parse can load and replace that effective mapping.

The important current behavior is therefore:

- do not assume the default `mapping.json` contents are the effective startup mapping;
- explicitly set `--mqtt-mapping-file` for a real deployment;
- inspect the administration `/config` view after startup when you need to confirm the active mapping;
- remember that `/config` can reveal credential-bearing connection fields.

## Validation

Mappings are validated against the JSON schema when set/loaded and by the administration validation endpoints.

Current validation/error construction can include the full mapping document in diagnostics. Because the mapping can contain passwords, do not paste unredacted validation errors or verbose logs into public issue trackers.

## Administration API and lifecycle

MQTTIntegrator creates an administration router and serves it through its HTTP/HTTPS admin listeners. Current main applies SNode.C Basic Authentication with hard-coded defaults:

```text
user:  admin
pass:  admin
realm: mqttsuite-admin
```

Those defaults are not currently wired to an MQTTSuite/SNode.C configuration option. Treat them as a known development credential, not a secure deployment boundary. Restrict listener exposure and add external controls where appropriate.

The router provides:

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/schema` | return mapping JSON schema |
| GET | `/config` | return active mapping |
| PATCH | `/config` | JSON Patch current config into a draft |
| POST | `/config` | replace draft with supplied mapping |
| POST | `/config/validate` | validate supplied mapping |
| GET | `/config/validateDraft` | validate current draft |
| POST | `/config/deploy` | deploy the current draft |
| GET | `/config/history` | list retained deployed versions |
| POST | `/config/rollback` | restore a selected version |
| GET | `/` | redirect to `/ui` |
| GET | `/ui` | static UI entry point if available |

### Draft

Draft mutations are written beside the active mapping as:

```text
<mapping-file>.draft
```

PATCH uses JSON Patch semantics; POST replaces the draft with the supplied JSON.

### Validate

Validation can be performed without deploying. A deployment should be treated as a configuration change only after schema validation succeeds.

### Deploy

Deploying a draft:

1. validates/loads the draft;
2. may add/update `meta.created` and `meta.version`;
3. backs up an existing active mapping;
4. writes the new active mapping;
5. removes the draft;
6. updates the in-memory mapper;
7. invokes the application reload callback.

When connection settings changed, the reload path reports reconnect semantics. Otherwise it can report subscription additions/removals.

### History

Backups live in a sibling `versions/` directory and are named from the active mapping filename plus a timestamp/version identifier. Current code prunes history to approximately the newest 50 backup files.

History is local filesystem state, not a remote configuration database.

### Rollback

Rollback accepts a `version_id`, loads and validates that backup against the current schema, restores it as active configuration, discards a pending draft, and invokes the same mapper reload path.

### Current UI portability limitation

The API is real, but current `MappingAdminRouter.cpp` serves `/ui` from a hard-coded maintainer-local absolute path:

```text
/home/voc/tmp/integrator/mqtt-integrator-ui/dist/mqtt-integrator-ui/browser
```

No matching portable installed Integrator UI artifact is established by the reviewed repository. Do not use `/ui` availability as an installation promise.

## Operational consequences

- Mapping changes can alter MQTT subscriptions immediately or force a reconnect.
- `+` matches one level; terminal `#` matches zero or more remaining levels after PR #22.
- Sibling literal/`+`/`#` branches remain first-match in document order.
- Delayed mapped publications are in-process scheduled work, not documented durable jobs.
- Mapping/history files can contain credentials.
- Administration read-back can reveal active connection credentials.
- The shipped Basic Auth defaults are known and reusable.
- Plugins execute native code inside the process.

## Troubleshooting

### Input is subscribed but not mapped

Check:

1. topic-tree order;
2. literal/`+`/`#` sibling precedence;
3. whether `+` is being used for exactly one level and `#` as a terminal remaining-subtree wildcard;
4. selected mapping mode;
5. JSON validity for `json` mode;
6. static payload equality for `static` mode;
7. suppression values.

For `parent/#`, remember that the zero-level `parent` topic selects the child `#` only when the parent itself has no subscription mapping.

### Mapping changed but client reconnected

Connection settings are part of the mapping. A change there requires reconnect; a topic/rule-only change can use the hot subscription delta path.

### `/ui` is missing

Use the administration JSON API. Current main does not establish a portable installed Integrator UI path.

### Active mapping differs from the default file

Pass `--mqtt-mapping-file` explicitly and inspect `/config`. Current startup seeds an inline demo before the final supported config parse.

## Source anchors

- [MQTTSuite master containing PR #22](https://github.com/SNodeC/mqttsuite/tree/6c0ff62c612694a6111ff971c446327938130cf0)
- [Mapping schema](https://github.com/SNodeC/mqttsuite/blob/6c0ff62c612694a6111ff971c446327938130cf0/lib/mapping-schema.json)
- [`MqttMapper.cpp` after the wildcard fix](https://github.com/SNodeC/mqttsuite/blob/6c0ff62c612694a6111ff971c446327938130cf0/lib/MqttMapper.cpp)
- [PR #22 — fix MQTT mapper `#` wildcard matching](https://github.com/SNodeC/mqttsuite/pull/22)
- [`ConfigApplication.cpp`](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/lib/ConfigApplication.cpp)
- [`MappingAdminRouter.cpp`](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/lib/MappingAdminRouter.cpp)
- [`JsonMappingReader.cpp`](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/lib/JsonMappingReader.cpp)
- [`MqttMapperPlugin.h`](https://github.com/SNodeC/mqttsuite/blob/6c0ff62c612694a6111ff971c446327938130cf0/lib/MqttMapperPlugin.h)
- [MQTTIntegrator startup](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttintegrator/mqttintegrator.cpp)
