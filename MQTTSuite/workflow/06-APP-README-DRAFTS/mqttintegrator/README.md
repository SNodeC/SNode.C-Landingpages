# MQTTIntegrator

MQTTIntegrator is the MQTTSuite MQTT 3.1.1 transformation service. It connects to a broker as an MQTT client, subscribes according to a mapping document, transforms matching topics and/or payloads, and republishes the resulting messages through the same MQTT connection.

Use it when incoming MQTT traffic is valid but not in the namespace, payload shape, units, or event/state representation that the rest of your system should consume. MQTTIntegrator is deliberately different from [MQTTBridge](../mqttbridge/README.md): Bridge forwards selected messages between broker members; Integrator executes `MqttMapper` rules and can change both topic and payload.

The suite-level build and common configuration model live in the [MQTTSuite README](../README.md). This README is the operational guide for `mqttintegrator` and the mapping format.

## Quick Start

Create `mapping.json`:

```json
{
  "connection": {
    "client_id": "integrator-demo",
    "keep_alive": 60,
    "clean_session": true
  },
  "mapping": {
    "topic_level": {
      "name": "devices",
      "topic_level": {
        "name": "button",
        "subscription": {
          "qos": 1,
          "static": {
            "mapped_topic": "actuators/light/set",
            "qos": 1,
            "message_mapping": [
              { "message": "pressed", "mapped_message": "on" },
              { "message": "released", "mapped_message": "off" }
            ]
          }
        }
      }
    }
  }
}
```

Start MQTTIntegrator against a local Broker:

```bash
mqttintegrator \
  --config-file /dev/null \
  integrator --mqtt-mapping-file ./mapping.json \
  in-mqtt remote --host 127.0.0.1 --port 1883 \
  in-mqtts --disabled \
  in6-mqtt --disabled \
  in6-mqtts --disabled \
  un-mqtt --disabled \
  un-mqtts --disabled \
  in-wsmqtt --disabled \
  in-wsmqtts --disabled \
  in6-wsmqtt --disabled \
  in6-wsmqtts --disabled \
  un-wsmqtt --disabled \
  un-wsmqtts --disabled \
  in-http --disabled \
  in-https --disabled
```

Subscribe to the mapped output with MQTTCli:

```bash
mqttcli \
  --config-file /dev/null \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 1883 \
    session --client-id integrator-check-sub --qos 1 \
    sub --topic actuators/light/set
```

Publish an input:

```bash
mqttcli \
  --config-file /dev/null \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 1883 \
    session --client-id integrator-check-pub --qos 1 \
    pub --topic devices/button --message pressed
```

The output subscriber should receive:

```text
topic:   actuators/light/set
payload: on
```

The mapping's `subscription.qos` controls how MQTTIntegrator subscribes. The mapping output's `qos` controls the republished message. Those are separate decisions.

## How the Integrator is assembled

MQTTIntegrator is an SNode.C MQTT client application. Its `SocketContextFactory` receives an established SNode.C connection and injects the shared MQTTSuite mapper into the per-connection MQTT behavior:

```cpp
return new iot::mqtt::SocketContext(
    socketConnection,
    new mqtt::mqttintegrator::lib::Mqtt(
        socketConnection->getConnectionName(),
        config->getMqttMapper(),
        config->getSessionStore()));
```

The transport/client endpoint is therefore separate from the mapping behavior. A direct TCP connection, Unix-domain connection, or HTTP/WebSocket upgrade can all end in the same Integrator MQTT context.

On successful MQTT CONNACK, the application subscribes to the topics extracted from the mapping tree. For each received PUBLISH, it asks `MqttMapper` for immediate and scheduled mapped publishes and sends those results back through the client connection.

> **Figure placeholder — MQTTIntegrator mapping pipeline.** Show broker subscription → matching topic tree → mapping rule → immediate or delayed output → republish on the same MQTT connection, with subscribe QoS and publish QoS labeled separately.

## Build and install result

`mqttintegrator` is built and installed by the repository's top-level CMake project. The Integrator CMake target requires the SNode.C client/stream components selected by its build options plus HTTP server components for its mapping-admin API.

A complete suite install places:

```text
${CMAKE_INSTALL_PREFIX}/bin/mqttintegrator
```

The current Integrator target does not install a Web UI directory. Its source router contains a maintainer-local static UI path; treat that as a development artifact, not a portable installed user interface.

See [Build and install](../README.md#build-and-install) for the whole-suite command sequence.

## Connecting to a broker

The Integrator contains source paths for these connection families when compiled in:

```text
in-mqtt       in-mqtts
in6-mqtt      in6-mqtts
un-mqtt       un-mqtts
in-wsmqtt     in-wsmqtts
in6-wsmqtt    in6-wsmqtts
un-wsmqtt     un-wsmqtts
```

They represent IPv4, IPv6, and Unix-domain streams; direct MQTT or MQTT-over-WebSocket; plain or TLS variants.

### Plain IPv4

```bash
mqttintegrator \
  integrator --mqtt-mapping-file ./mapping.json \
  in-mqtt remote --host 127.0.0.1 --port 1883
```

### TLS/IPv4

```bash
mqttintegrator \
  integrator --mqtt-mapping-file ./mapping.json \
  in-mqtts remote --host broker.example.net --port 8883
```

Configure the selected instance's SNode.C TLS section for the certificate/trust model required by the peer:

```bash
mqttintegrator in-mqtts --help=expanded
```

### MQTT over WebSocket

```bash
mqttintegrator \
  integrator --mqtt-mapping-file ./mapping.json \
  in-wsmqtt remote --host 127.0.0.1 --port 8080
```

The current Integrator WebSocket client requests `/ws` with subprotocol `mqtt`.

### WSS

```bash
mqttintegrator \
  integrator --mqtt-mapping-file ./mapping.json \
  in-wsmqtts remote --host broker.example.net --port 8088
```

Again, configure the instance's SNode.C TLS settings separately.

### Unix-domain MQTT

```bash
mqttintegrator \
  integrator --mqtt-mapping-file ./mapping.json \
  un-mqtt remote --sun-path /run/mqttsuite/broker.sock
```

Use an explicit stable socket path when Integrator and Broker should communicate only on the same host.

## Application configuration

The Integrator application subcommand is `integrator`. Its shared MQTTSuite application options include:

```text
--mqtt-mapping-file <file>
--mqtt-session-store <file>
```

The first selects the mapping document. The second provides a persistent MQTT client session-store path.

For repeatable operation, first verify the mapping and broker connection explicitly, then persist the SNode.C configuration:

```bash
mqttintegrator \
  --config-file /dev/null \
  integrator \
    --mqtt-mapping-file ./mapping.json \
    --mqtt-session-store ./mqttintegrator-session.json \
  in-mqtt remote --host 127.0.0.1 --port 1883 \
  --write-config ./mqttintegrator.conf
```

Then:

```bash
mqttintegrator --config-file ./mqttintegrator.conf
```

The mapping JSON remains its own domain document. Writing the SNode.C application config does not inline the mapping rules; it persists the option that points to the mapping file.

## Mapping files

The current schema is [`../lib/mapping-schema.json`](../lib/mapping-schema.json). MQTTIntegrator validates the document and applies schema defaults before using it.

At the top level, the schema admits:

- optional metadata;
- `discover_prefix`;
- MQTT `connection` settings;
- required `mapping`.

The executable currently reads the `connection` object and `mapping` tree directly. `discover_prefix` is accepted by the schema but the reviewed `MqttMapper` execution path does not use it to alter matching or publication; treat it as schema vocabulary rather than an active routing feature in this source revision.

Similarly, metadata and `subscription.type` can describe a document/subscription but do not drive the mapper's matching decision.

## Connection settings inside the mapping

The mapping's `connection` object supplies MQTT session values used by Integrator's MQTT behavior:

```json
{
  "connection": {
    "client_id": "normalizer-01",
    "keep_alive": 60,
    "clean_session": true,
    "will_topic": "",
    "will_message": "",
    "will_qos": 0,
    "will_retain": false,
    "username": "",
    "password": ""
  }
}
```

These values are different from the SNode.C transport address. The SNode.C instance answers **where/how to connect**; the mapping connection object answers **which MQTT session to establish**.

A mapping deployment that changes the `connection` object has special runtime consequences described under [Deploy behavior: hot update or reconnect](#deploy-behavior-hot-update-or-reconnect).

## The topic tree

Mappings are organized as recursive `topic_level` objects. A level has a `name` and either another level (or array of sibling levels) or a `subscription`.

For:

```text
devices/room-01/temperature
```

the literal tree is:

```json
{
  "mapping": {
    "topic_level": {
      "name": "devices",
      "topic_level": {
        "name": "room-01",
        "topic_level": {
          "name": "temperature",
          "subscription": {
            "qos": 1,
            "value": {
              "mapped_topic": "normalized/room-01/temperature",
              "mapping_template": "{{ message }}"
            }
          }
        }
      }
    }
  }
}
```

MQTTIntegrator extracts the subscription topic from the tree and subscribes with the declared `subscription.qos`.

### `+` and `#`

`topic_level.name` can also use MQTT wildcards.

Single-level wildcard:

```json
{
  "name": "devices",
  "topic_level": {
    "name": "+",
    "topic_level": {
      "name": "temperature",
      "subscription": {
        "qos": 1,
        "value": {
          "mapped_topic": "normalized/{{ topic }}",
          "mapping_template": "{{ message }}"
        }
      }
    }
  }
}
```

This produces the subscription:

```text
devices/+/temperature
```

A terminal `#` can represent the remaining subtree:

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

When sibling topic-level entries could both match, the current mapper searches them in document order and stops at the first matching branch. Keep overlapping literal/wildcard branches intentional and ordered.

> **Figure placeholder — Topic-tree matching.** Show a nested `devices/+/temperature` mapping tree beside several concrete MQTT topics, including which branch matches and where the subscription QoS is attached.

## Three mapping modes

A subscription can contain `static`, `value`, and/or `json` mapping sections. Each mapping section can be a single object or an array, which enables fan-out.

### Static mapping

Use `static` when exact incoming strings should become exact outgoing strings.

```json
{
  "static": {
    "mapped_topic": "actuators/light/set",
    "qos": 1,
    "retain": false,
    "message_mapping": [
      { "message": "pressed", "mapped_message": "on" },
      { "message": "released", "mapped_message": "off" }
    ]
  }
}
```

If the incoming payload does not match one of the `message` strings, this static rule produces no mapped publish.

### Scalar/value template

Use `value` when the entire incoming payload should be available to an INJA template as scalar `message`:

```json
{
  "value": {
    "mapped_topic": "normalized/status",
    "mapping_template": "front {{ message }}",
    "qos": 0,
    "retain": false
  }
}
```

Input:

```text
open
```

Output payload:

```text
front open
```

### JSON template

Use `json` when the MQTT payload is JSON. The mapper parses it and exposes the parsed value as `message`:

```json
{
  "json": {
    "mapped_topic": "normalized/room-01/temperature",
    "mapping_template": "{{ message.value }}",
    "qos": 1
  }
}
```

Input:

```json
{"value":21.7,"unit":"C"}
```

Output payload:

```text
21.7
```

If the incoming payload is not valid JSON, the current JSON mapping path logs the parse failure and produces no JSON-template output for that rule.

## Template context and mapped topics

For `value` and `json` rules, the INJA environment receives more than `message`. The mapper also exposes current publish metadata:

```text
topic
qos
retain
package_identifier
```

The output topic is itself rendered as an INJA template before the message template. After rendering, the mapper also makes the rendered value available as `mapped_topic`.

Example:

```json
{
  "value": {
    "mapped_topic": "{{ topic }}_normalized",
    "mapping_template": "{{ message }}",
    "qos": 1
  }
}
```

An input on:

```text
devices/pump/state
```

is republished to:

```text
devices/pump/state_normalized
```

Use templated topics to carry an existing namespace forward; use literal mapped topics when the target contract should be independent of the input name.

## QoS, retain, delay, and suppressions

Every output rule shares these controls:

- `qos`: publish QoS, independent of `subscription.qos`;
- `retain`: retain flag for the mapped publish;
- `delay`: negative means immediate; zero or positive is placed on the Integrator's scheduled-publish path;
- `suppressions`: template-output strings that should not be published for `value`/`json` mappings.

For example:

```json
{
  "value": {
    "mapped_topic": "normalized/state",
    "mapping_template": "{% if message == \"valid\" %}ok{% endif %}",
    "suppressions": [""],
    "qos": 1,
    "retain": false
  }
}
```

If the template renders an empty string, the rule is suppressed. The current mapper deliberately allows an empty retained output through even when `""` appears in `suppressions`, preserving the ability to emit retained-state deletion semantics.

The numeric delay is validated by the schema and handed to the application's timer queue. Keep delayed mappings sparse and observable: changing when a derived state appears can be as significant as changing its value.

## One input, multiple outputs

Mapping sections accept arrays. This lets one input fan out into multiple output contracts without a second Integrator process.

Example: transform one JSON temperature value into three topics:

```json
{
  "json": [
    {
      "mapped_topic": "normalized/temperature/celsius",
      "mapping_template": "{{ message.value }}",
      "qos": 1,
      "retain": true
    },
    {
      "mapped_topic": "normalized/temperature/kelvin",
      "mapping_template": "{{ message.value + 273.15 }}",
      "qos": 0,
      "retain": false
    },
    {
      "mapped_topic": "normalized/temperature/fahrenheit",
      "mapping_template": "{{ message.value * 1.8 + 32 }}",
      "qos": 0,
      "retain": false
    }
  ]
}
```

> **Figure placeholder — Static, scalar, JSON, and fan-out mapping.** Compare the three mapping modes on one page and show one JSON input branching into multiple independently configured output publishes.

## Plugins

The `mapping` object can name dynamically loaded plugins:

```json
{
  "mapping": {
    "plugins": [
      "/path/to/mapper-plugin.so"
    ],
    "topic_level": {
      "...": "..."
    }
  }
}
```

The mapper loads each library and looks for exported `functions` and `voidFunctions` collections defined by [`../lib/MqttMapperPlugin.h`](../lib/MqttMapperPlugin.h). Registered callbacks are added to the INJA environment.

The repository's `lib/plugins/` directory contains example plugin implementations, including calculation/state examples used by the sample mapping. Treat this as an extension interface tied to the current C++ plugin ABI and deployment layout; the README does not promise cross-version binary compatibility.

## Validate before deployment

The application validates mappings against the embedded schema during load/deploy. For an external preflight, use any JSON Schema tool that supports the schema dialect used by [`../lib/mapping-schema.json`](../lib/mapping-schema.json).

The most important validation is still semantic:

- does the topic tree describe the intended MQTT subscription?
- do wildcard branches overlap?
- is subscribe QoS distinct from publish QoS?
- can JSON inputs actually satisfy the template?
- should outputs be retained?
- can a templated topic create an accidental feedback path?
- do delayed/fan-out outputs match downstream expectations?

## Mapping administration API

MQTTIntegrator also creates an HTTP mapping-admin router. The current source starts IPv4 admin listeners named:

```text
in-http   (plain HTTP, source default port 8085)
in-https  (HTTPS, source default port 8086)
```

The router uses HTTP Basic Authentication. The reviewed source initializes the admin credentials to:

```text
admin / admin
```

Those defaults are development defaults, not a remote-management policy. Change the relevant configuration and bind/filter the admin listener according to your trust boundary.

The API includes:

| Method | Route | Purpose |
| --- | --- | --- |
| `GET` | `/schema` | return mapping schema |
| `GET` | `/config` | return active mapping |
| `PATCH` | `/config` | apply JSON Patch to the active document and save a draft |
| `POST` | `/config` | replace/save a draft mapping document |
| `POST` | `/config/validate` | validate a supplied mapping |
| `GET` | `/config/validateDraft` | validate the staged draft |
| `POST` | `/config/deploy` | deploy the draft |
| `GET` | `/config/history` | list mapping history |
| `POST` | `/config/rollback` | activate a selected historical version |

The current source also redirects `/` to `/ui`, but its static UI path is a maintainer-local build directory and the Integrator CMake target has no corresponding install rule. Use the HTTP API as the portable documented admin surface unless your deployment separately provides a UI build.

> **Figure placeholder — Draft, validate, deploy, history, rollback.** Show active mapping and draft as separate states, validation before deploy, then either hot subscription changes or reconnect, with history feeding rollback.

## Deploy behavior: hot update or reconnect

Deploying a new mapping does not always restart the MQTT connection.

The mapper compares the new `connection` object with the active one.

### Mapping rules changed, connection unchanged

The application computes the old and new subscription sets by topic and QoS. It sends only the required unsubscribe/subscribe changes and reports a `hot` reload.

That means changes such as:

- mapped topic/payload template;
- output QoS/retain/delay;
- suppressions;
- adding/removing a mapping branch whose connection settings stay the same

can be applied without deliberately reconnecting the MQTT session. Subscription changes are adjusted in place.

### Connection object changed

If mapper connection settings change, the deploy path reports `reconnect` and sends MQTT DISCONNECT. The client connection is configured for reconnect, so the new MQTT connection/session values take effect on the subsequent connection.

This distinction matters operationally: editing a username, client ID, keep-alive, clean-session setting, or will in the mapping is not merely a template change.

## Practical examples

### Normalize a device namespace

Input:

```text
vendor/acme/room-01/temp
{"v":21.7}
```

Map to:

```text
normalized/room-01/temperature
{"value":21.7,"unit":"C"}
```

This is a good fit for JSON templates and templated topics.

### Convert event vocabulary

Input:

```text
devices/button
pressed
```

Map to:

```text
actuators/light/set
on
```

This is a good fit for `static`.

### Build derived state

An input JSON document can render a concise scalar/status output and set `retain: true` so new subscribers immediately see the latest derived state.

### Normalize before persistence

A common composition is:

```text
device topics -> MQTTIntegrator -> normalized/... -> MQTTStore -> MariaDB
```

Let Integrator own transformation; let Store keep the resulting raw MQTT envelope and optional typed projections.

## Verification with MQTTCli

Use a subscriber on the expected mapped output before publishing a known input.

For a wildcard output check:

```bash
mqttcli \
  --config-file /dev/null \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 1883 \
    session --client-id mapping-observer --qos 1 \
    sub --topic 'normalized/#'
```

Then publish one input that matches exactly one intended mapping branch.

For debugging, verify in this order:

1. Integrator connected successfully.
2. Mapping validation succeeded.
3. Extracted subscriptions include the input topic/filter.
4. Broker receives the input.
5. Integrator receives the input.
6. A mapping branch matches.
7. Template/static conversion succeeds.
8. Output is not suppressed or waiting on a delay.
9. Broker sees the mapped publish.
10. Output subscriber matches the mapped topic.

That sequence avoids treating every missing output as a template problem.

## Trust and credential boundaries

- Mapping `connection.username` and `connection.password` are MQTT client credentials and may be persisted in the mapping file/history.
- The mapping-admin API uses Basic Authentication with weak source defaults. Do not expose those defaults as an administrative security model.
- TLS on `in-https` encrypts the admin transport when correctly configured; it does not fix weak credentials or broad network exposure.
- Mapping files and saved application config should have filesystem ownership/permissions appropriate to their credentials and operational meaning.
- Plugins execute native code in the Integrator process. Load only libraries you intentionally deploy and trust.
- Debug/trace logs may reveal mapping contents, MQTT payloads, or credential-related configuration.

## Troubleshooting

### Mapping file is rejected

Validate against [`../lib/mapping-schema.json`](../lib/mapping-schema.json). Check field names carefully: the current schema uses singular `mapping`, `topic_level`, `subscription`, `mapped_topic`, `mapping_template`, `message_mapping`, `qos`, `retain`, `delay`, and `suppressions`.

Do not copy older examples that use different pluralization or renamed fields without revalidating them against the current schema.

### Integrator connects but does not subscribe

Check that:

- the mapping has a `subscription` at the intended topic-tree leaf;
- wildcard/literal nesting yields the expected full filter;
- the broker CONNACK succeeded;
- the selected connection instance is the one pointing at the intended broker.

### Input arrives but no mapped publish appears

Check:

- correct mapping mode (`static`, `value`, or `json`);
- exact static payload match;
- valid JSON for `json`;
- INJA expressions and variable names;
- `suppressions`;
- delay;
- mapped topic;
- overlapping wildcard branches/document order.

### Admin deploy reconnects unexpectedly

Compare the old and new mapping `connection` objects. Any difference there selects reconnect rather than hot subscription adjustment.

### Admin UI route does not serve a portable UI

That is expected for a normal install from this source revision: the router's `/ui` static directory is not installed by the Integrator target. Use the documented API or supply your own separately built UI assets.

## Related documentation

- [MQTTSuite overview and build](../README.md)
- [MQTTBroker](../mqttbroker/README.md)
- [MQTTBridge](../mqttbridge/README.md)
- [MQTTCli](../mqttcli/README.md)
- [MQTTStore](../mqttstore/README.md)
- [Mapping schema](../lib/mapping-schema.json)
- [Mapper plugin interface](../lib/MqttMapperPlugin.h)

## License

MQTTSuite is available under:

```text
MIT OR GPL-3.0-or-later
```
