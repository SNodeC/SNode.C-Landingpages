# MQTTIntegrator mapping reference

[← MQTTSuite](../README.md) · [MQTTIntegrator README](../mqttintegrator/README.md) · [Sibling topic branches example](integrator-sibling-topics-example.md) · [Integrator HTTP API](integrator-http-api.md) · [Configuration](configuration.md) · [Capabilities](capabilities.md)

MQTTIntegrator subscribes to MQTT 3.1.1 topics, matches received publications against a hierarchical mapping document, and republishes zero, one, or many derived publications through the same MQTT client connection. MQTTBroker can reuse the same mapper in-process.

The authoritative machine-readable shape is [`lib/mapping-schema.json`](https://github.com/SNodeC/mqttsuite/blob/6c0ff62c612694a6111ff971c446327938130cf0/lib/mapping-schema.json).

## Mapping structure

A mapping document contains:

```text
meta             optional version/comment metadata
discover_prefix  schema field; no mapper routing behavior established here
connection       MQTT session used by standalone MQTTIntegrator
mapping          recursive topic tree and mapping rules
```

The structural rule used throughout the document is:

```text
topic_level
  └─ subscription
       ├─ qos
       └─ static | value | json
```

`static`, `value`, and `json` are properties of `subscription`, not siblings of it.

Representative skeleton:

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
    "topic_level": {
      "name": "sensors",
      "topic_level": {
        "name": "+",
        "topic_level": {
          "name": "temperature",
          "subscription": {
            "qos": 1,
            "json": {
              "mapped_topic": "normalized/{{ message.device }}/temperature",
              "mapping_template": "{{ message.value }}",
              "qos": 1,
              "retain": false
            }
          }
        }
      }
    }
  }
}
```

## Connection block

The standalone Integrator obtains MQTT CONNECT/session parameters from `connection`. Current schema defaults are:

| Field | Default | Meaning |
| --- | ---: | --- |
| `client_id` | `""` | MQTT client ID |
| `keep_alive` | `60` | keepalive seconds |
| `clean_session` | `true` | MQTT clean-session flag |
| `will_topic` | `""` | will topic |
| `will_message` | `""` | will payload |
| `will_qos` | `0` | will QoS |
| `will_retain` | `false` | will retain flag |
| `username` | `""` | MQTT CONNECT username |
| `password` | `""` | MQTT CONNECT password |

Changing the `connection` object through a deployed mapping requires MQTTIntegrator to reconnect. Mapping files and history can therefore contain MQTT credentials and should be protected as secret-bearing configuration.

## Topic tree and subscriptions

A topic tree is made from recursive `topic_level` nodes. A node has a `name` and may contain child topic levels or a `subscription`.

For:

```text
sensors/room-01/temperature
```

a literal tree is conceptually:

```text
sensors
  room-01
    temperature
```

A subscription point carries receive QoS and mapping rules. MQTTIntegrator walks the tree and converts those points into MQTT topic filters.

### Literal matching

A literal node matches the corresponding topic level exactly.

### `+`

A node named `+` matches exactly one topic level:

```text
sensors/+/temperature
```

<a id="hash-multi-level-wildcard"></a>
### Multi-level `#`

A terminal `#` node matches zero or more remaining topic levels.

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

This branch can match:

```text
devices
devices/button
devices/room-01/temperature
devices/room-01/sensor/value
```

The zero-level `devices` case selects the terminal `#` child when the `devices` parent itself has no subscription mapping. If the parent has its own subscription mapping, that exact parent mapping remains the direct match.

Use `#` as a terminal multi-level wildcard.

### Sibling order

When `topic_level` is an array, branches are tested in document order and the first matching branch wins. A practical ordering is:

```text
literal siblings
then + fallback
then # fallback
```

Putting a broad `+` or `#` first can shadow later literal branches. See [Sibling topic branches](integrator-sibling-topics-example.md) for a complete example.

## Mapping modes

A selected subscription can contain `static`, `value`, and/or `json` rules. Each mode can be a single object or an array where allowed by the schema, enabling fan-out.

### Static mapping

Static mapping compares the incoming payload string to configured exact values:

```json
"subscription": {
  "qos": 1,
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
}
```

If no `message_mapping` value matches, that static rule produces no output.

### Value mapping

Value mapping exposes the incoming payload string to Inja as `message`:

```json
"subscription": {
  "qos": 1,
  "value": {
    "mapped_topic": "normalized/room-01/temperature",
    "mapping_template": "{{ message }}",
    "qos": 1,
    "retain": false
  }
}
```

### JSON mapping

JSON mapping parses the payload and exposes the parsed value as `message`:

```json
"subscription": {
  "qos": 1,
  "json": {
    "mapped_topic": "normalized/{{ message.device }}/temperature",
    "mapping_template": "{\"value\":{{ message.value }},\"unit\":\"{{ message.unit }}\"}",
    "qos": 1,
    "retain": false
  }
}
```

Invalid JSON produces no JSON-template output for that rule.

## Template context

`value` and `json` mappings use the same Inja environment. The current mapper exposes:

| Key | Value |
| --- | --- |
| `message` | payload string for `value`; parsed JSON for `json` |
| `topic` | incoming MQTT topic |
| `qos` | incoming PUBLISH QoS |
| `retain` | incoming PUBLISH retain flag |
| `package_identifier` | incoming MQTT packet identifier representation |
| `mapped_topic` | rendered output topic, available while rendering the payload template |

The output topic is rendered first. The rendered result is then stored as `mapped_topic` before `mapping_template` is rendered.

The template engine is [Inja](https://github.com/pantor/inja).

## Output controls

Output rules can set:

- `qos` — outgoing PUBLISH QoS;
- `retain` — outgoing retain flag;
- `delay` — `-1` for immediate output or a non-negative delayed path;
- `suppressions` — rendered payload strings that normally suppress an output.

Subscription QoS and output QoS are separate decisions.

### Retained-empty suppression exception

An empty retained output is still published even when `""` is listed in `suppressions`. This preserves the MQTT pattern for deleting retained state with an empty retained PUBLISH.

```text
rendered message is in suppressions -> normally no publish
rendered message == "" and retain == true -> publish anyway
```

## Fan-out

Arrays of mapping rules allow one selected subscription to emit multiple publications. Each output can choose its own topic, payload template, QoS, retain, delay, and suppression behavior.

Keep fan-out deterministic: sibling topic-tree precedence selects one branch, while multiple rules inside that selected subscription can all contribute outputs.

## Plugins

The mapping object can list dynamically loaded native plugins:

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

The mapper looks for exported callback collections defined by [`../lib/MqttMapperPlugin.h`](../lib/MqttMapperPlugin.h) and registers them with Inja. Plugins execute native code in the Integrator process; load only libraries you intentionally deploy and trust.

## Administration lifecycle

The application-level administration API supports active mapping read-back, draft creation/replacement, validation, deploy, history, and rollback. A mapping-only change can update subscriptions in place; a changed `connection` object requires reconnect behavior.

Use [Integrator HTTP API](integrator-http-api.md) for the exact route, status, response, authentication, draft/history, and UI contracts.

## Example: literal branch with wildcard fallback

A common pattern is:

```json
"topic_level": [
  {
    "name": "temperature",
    "subscription": {
      "qos": 1,
      "value": {
        "mapped_topic": "normalized/temperature",
        "mapping_template": "{{ message }}"
      }
    }
  },
  {
    "name": "+",
    "subscription": {
      "qos": 0,
      "value": {
        "mapped_topic": "normalized/other",
        "mapping_template": "{{ message }}"
      }
    }
  }
]
```

Specific literal branches belong before wildcard fallbacks. For a complete copyable file and commands, see [Sibling topic branches](integrator-sibling-topics-example.md).

## Troubleshooting

### No mapped output

Check:

1. topic-tree order and wildcard placement;
2. that the selected node contains `subscription`;
3. mapping mode and JSON validity where applicable;
4. static payload equality for `static` rules;
5. template errors;
6. suppression and delay settings.

### `parent/#` does not behave as expected

The zero-level parent topic selects the terminal `#` child only when the parent itself has no subscription mapping.

### Mapping changed but client reconnected

Connection settings are part of the mapping. Changing them requires reconnect; topic/rule-only changes can use the hot subscription-delta path.

### Active mapping differs from the file you expected

Pass `--mqtt-mapping-file` explicitly and inspect `/config`.

## Source references

- [Mapping schema](https://github.com/SNodeC/mqttsuite/blob/6c0ff62c612694a6111ff971c446327938130cf0/lib/mapping-schema.json)
- [`MqttMapper.cpp`](https://github.com/SNodeC/mqttsuite/blob/6c0ff62c612694a6111ff971c446327938130cf0/lib/MqttMapper.cpp)
- [`ConfigApplication.cpp`](https://github.com/SNodeC/mqttsuite/blob/6c0ff62c612694a6111ff971c446327938130cf0/lib/ConfigApplication.cpp)
- [`JsonMappingReader.cpp`](https://github.com/SNodeC/mqttsuite/blob/6c0ff62c612694a6111ff971c446327938130cf0/lib/JsonMappingReader.cpp)
- [`MqttMapperPlugin.h`](https://github.com/SNodeC/mqttsuite/blob/6c0ff62c612694a6111ff971c446327938130cf0/lib/MqttMapperPlugin.h)
