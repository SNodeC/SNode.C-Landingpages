# MQTTIntegrator

MQTTIntegrator is the MQTTSuite MQTT 3.1.1 transformation service. It connects to a broker as an MQTT client, subscribes according to a mapping document, transforms matching topics and/or payloads, and republishes the resulting messages through the same MQTT connection.

Use it when incoming MQTT traffic is valid but not in the namespace, payload shape, units, or event/state representation that the rest of your system should consume. MQTTIntegrator is deliberately different from [MQTTBridge](../mqttbridge/README.md): Bridge forwards selected messages between broker members; Integrator can change both topic and payload.

The suite-level build and shared configuration model live in the [MQTTSuite README](../README.md). This README focuses on running and operating `mqttintegrator`. The complete mapping grammar belongs to the [mapping reference](../docs/integrator-mapping.md), and the exact administration contract belongs to the [Integrator HTTP API reference](../docs/integrator-http-api.md).

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

## How it works

MQTTIntegrator is an SNode.C MQTT client application. The selected SNode.C connection instance establishes the transport; the Integrator attaches MQTTSuite mapping behavior to that connection.

After MQTT CONNACK, the application subscribes to the topic filters derived from the mapping. Each received PUBLISH is matched against the mapping tree and may produce zero, one, or many immediate or delayed output publications on the same MQTT client connection.

> **Figure placeholder — MQTTIntegrator mapping pipeline.** Show broker subscription → matching topic tree → mapping rule → immediate or delayed output → republish on the same MQTT connection, with subscribe QoS and publish QoS labeled separately.

## Build and install result

`mqttintegrator` is built and installed by the repository's top-level CMake project. A complete suite install places:

```text
${CMAKE_INSTALL_PREFIX}/bin/mqttintegrator
```

The current Integrator target does not install a Web UI directory. Its portable documented administration surface is the HTTP API.

See [Build and install](../README.md#build-and-install) for the whole-suite command sequence.

## Connecting to a broker

The Integrator contains direct MQTT and MQTT-over-WebSocket client families over IPv4, IPv6, and Unix-domain streams where the corresponding build options are enabled:

```text
in-mqtt       in-mqtts
in6-mqtt      in6-mqtts
un-mqtt       un-mqtts
in-wsmqtt     in-wsmqtts
in6-wsmqtt    in6-wsmqtts
un-wsmqtt     un-wsmqtts
```

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

The Integrator WebSocket client requests `/ws` with subprotocol `mqtt`.

### WSS

```bash
mqttintegrator \
  integrator --mqtt-mapping-file ./mapping.json \
  in-wsmqtts remote --host broker.example.net --port 8088
```

### Unix-domain MQTT

```bash
mqttintegrator \
  integrator --mqtt-mapping-file ./mapping.json \
  un-mqtt remote --sun-path /run/mqttsuite/broker.sock
```

The shared [configuration reference](../docs/configuration.md) documents the non-obvious client-side default ports and common SNode.C instance behavior.

## Application configuration

The Integrator application subcommand is `integrator`. Its shared MQTTSuite application options include:

```text
--mqtt-mapping-file <file>
--mqtt-session-store <file>
```

The first selects the mapping document. The second provides a persistent MQTT client session-store path.

For repeatable operation, make the explicit command work first, then persist the SNode.C application configuration:

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

The mapping JSON remains a separate domain document; writing the SNode.C application config persists the option pointing to that mapping file.

Use `--mqtt-mapping-file` explicitly for predictable deployments rather than relying on the application's implicit startup mapping state.

## Mapping model

Mappings are recursive MQTT topic trees. A `subscription` attaches receive QoS plus one or more mapping rules to a selected topic branch.

The current mapper supports:

- literal topic levels;
- single-level `+` wildcard matching;
- terminal multi-level `#` matching;
- static string mapping;
- scalar/value templates;
- JSON templates;
- templated output topics;
- fan-out;
- output QoS and retain;
- delayed output;
- suppressions;
- dynamically loaded Inja callbacks.

The complete schema, defaults, wildcard precedence, exact Inja context keys, suppression semantics, plugin interface, and worked examples are documented in [Integrator mapping](../docs/integrator-mapping.md).

### Topic matching

For a mapping corresponding to:

```text
devices/+/temperature
```

`+` matches one topic level. A terminal `#` matches zero or more remaining levels. When overlapping sibling branches are used, order them from specific to broad so the intended mapping branch is selected.

For a complete literal-plus-wildcard example, see [Sibling topic branches](../docs/integrator-sibling-topics-example.md).

> **Figure placeholder — Topic-tree matching.** Show a nested `devices/+/temperature` mapping tree and a terminal `devices/#` branch beside concrete MQTT topics, including the zero-level `devices` case and where subscription QoS is attached.

## Three mapping modes

Use `static` when exact incoming strings should become exact outgoing strings:

```json
"static": {
  "mapped_topic": "actuators/light/set",
  "qos": 1,
  "message_mapping": [
    { "message": "pressed", "mapped_message": "on" },
    { "message": "released", "mapped_message": "off" }
  ]
}
```

Use `value` when the whole incoming payload should be available to an Inja template:

```json
"value": {
  "mapped_topic": "normalized/status",
  "mapping_template": "front {{ message }}",
  "qos": 0
}
```

Use `json` when the incoming payload is JSON:

```json
"json": {
  "mapped_topic": "normalized/room-01/temperature",
  "mapping_template": "{{ message.value }}",
  "qos": 1
}
```

Each mode can fan out to multiple independently configured outputs.

> **Figure placeholder — Static, scalar, JSON, and fan-out mapping.** Compare the three mapping modes and show one input branching into multiple independently configured output publishes.

## QoS, retain, delay, and suppressions

Output rules can choose their own publish QoS and retain flag independently from subscription QoS. Template mappings can also delay an output or suppress selected rendered values.

An empty retained output is a special case because MQTT uses an empty retained publication to clear retained state. See the [mapping reference](../docs/integrator-mapping.md#suppressions) for the exact suppression behavior.

## Validate before deployment

MQTTIntegrator validates mappings against the embedded schema during load/deploy. For external preflight, use a JSON Schema tool against [`../lib/mapping-schema.json`](../lib/mapping-schema.json).

Also verify the semantic contract:

- does the topic tree describe the intended subscription?
- are overlapping literal/`+`/`#` branches intentional?
- are subscribe QoS and publish QoS correct?
- can the input payload satisfy the selected template?
- should outputs be retained or delayed?
- can a mapped topic create an accidental feedback path?

## Mapping administration API

MQTTIntegrator creates IPv4 administration listeners named:

```text
in-http   (HTTP, source default port 8085)
in-https  (HTTPS, source default port 8086)
```

The API provides mapping schema/config read-back, draft creation/replacement, validation, deploy, history, and rollback.

Current HTTP Basic Authentication credentials are fixed to:

```text
admin / admin
```

They are not configurable through the MQTTSuite/SNode.C application configuration in this revision. Keep the admin listeners inside a trusted management boundary or place them behind deployment-specific external access control. HTTPS protects transport but does not make the fixed credentials suitable for broad exposure.

The complete route/status/body contract is documented in [Integrator HTTP API](../docs/integrator-http-api.md).

## Deploy behavior: hot update or reconnect

Deploying a mapping does not always replace the MQTT connection.

When the mapping's MQTT `connection` settings stay unchanged, Integrator can apply subscription changes in place. When the `connection` object changes, the client reconnects so the new MQTT session values take effect.

That distinction matters for edits to client ID, credentials, keep-alive, clean-session settings, or will configuration.

## Practical examples

### Normalize a device namespace

```text
vendor/acme/room-01/temp
{"v":21.7}
```

can become:

```text
normalized/room-01/temperature
{"value":21.7,"unit":"C"}
```

### Convert event vocabulary

```text
devices/button  pressed
```

can become:

```text
actuators/light/set  on
```

### Normalize before persistence

```text
device topics -> MQTTIntegrator -> normalized/... -> MQTTStore -> MariaDB
```

Let Integrator own transformation; let Store own persistence.

## Verification with MQTTCli

Subscribe to the expected mapped output before publishing a known input:

```bash
mqttcli \
  --config-file /dev/null \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 1883 \
    session --client-id mapping-observer --qos 1 \
    sub --topic 'normalized/#'
```

For debugging, verify in this order:

1. Integrator connected successfully.
2. Mapping validation succeeded.
3. The expected input filter was subscribed.
4. Integrator receives the input.
5. The intended mapping branch matches.
6. Conversion succeeds and is not suppressed or delayed unexpectedly.
7. The broker receives the mapped publish.
8. The output subscriber matches the mapped topic.

## Trust and credential boundaries

- Mapping `connection.username` and `connection.password` are MQTT client credentials and may be persisted in mapping/history files.
- The mapping administration API uses fixed source-known `admin/admin` credentials in this revision.
- Mapping read-back/history/error paths can expose credential-bearing configuration.
- Plugins execute native code in the Integrator process; load only libraries you intentionally deploy and trust.
- Debug/trace logs may reveal mapping contents, MQTT payloads, or credential-related configuration.

Protect mapping files and the admin listener according to their operational sensitivity.

## Troubleshooting

### Mapping does not produce output

Check the broker connection, effective mapping file, extracted input subscriptions, branch order, payload format, template/static conversion, suppressions, and delay.

### Mapping changed but client reconnected

Connection settings are part of the mapping. Changes to those settings require reconnect; topic/rule-only changes can use the hot subscription-update path.

### `/ui` is missing

Use the administration JSON API. The current source tree does not establish a portable installed Integrator UI.

### Active mapping differs from the file you expected

Pass `--mqtt-mapping-file` explicitly and inspect the active configuration through the application/API.

## Related documentation

- [MQTTSuite overview and build](../README.md)
- [Integrator mapping reference](../docs/integrator-mapping.md)
- [Sibling topic branches example](../docs/integrator-sibling-topics-example.md)
- [Integrator HTTP API](../docs/integrator-http-api.md)
- [Configuration](../docs/configuration.md)
- [Capabilities and evidence](../docs/capabilities.md)
- [MQTTBroker](../mqttbroker/README.md)
- [MQTTBridge](../mqttbridge/README.md)
- [MQTTCli](../mqttcli/README.md)
- [MQTTStore](../mqttstore/README.md)

## License

MQTTSuite is available under:

```text
MIT OR GPL-3.0-or-later
```
