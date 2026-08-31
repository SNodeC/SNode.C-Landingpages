# MQTTCli

MQTTCli is the MQTTSuite command-line MQTT 3.1.1 client. It can subscribe, publish, or do both on one connection, and it is the fastest way to verify MQTTBroker, MQTTIntegrator, MQTTBridge, and MQTTStore without introducing another client implementation.

Use `mqttcli` when you want to answer concrete questions such as:

- Can I connect to this broker endpoint?
- Does this subscription receive the expected topic and QoS?
- Did MQTTIntegrator produce the mapped output?
- Did MQTTBridge forward the message to the other broker?
- Did MQTTStore receive the test event I am about to query in MariaDB?

The suite-level build and shared SNode.C configuration model are in the [MQTTSuite README](../README.md). This README focuses on commands and observable behavior.

## Quick Start

Subscribe:

```bash
mqttcli \
  --config-file /dev/null \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 1883 \
    session --client-id cli-subscriber --qos 1 \
    sub --topic edge-lab/room-01/temperature
```

Publish from another terminal:

```bash
mqttcli \
  --config-file /dev/null \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 1883 \
    session --client-id cli-publisher --qos 1 \
    pub --topic edge-lab/room-01/temperature \
        --message '{"value":21.7,"unit":"C"}'
```

Received publishes are printed with topic, QoS, retain, duplicate flag, and payload. If the payload parses as JSON, MQTTCli pretty-prints it.

The current client connection is configured for reconnect. A publish-only command can therefore reconnect after the first acknowledged result; for a one-shot check, stop it with `Ctrl-C` after the first success.

## Command anatomy

A normal MQTTCli invocation follows the SNode.C hierarchy:

```text
mqttcli
  <connection-instance>
    remote ...
    http ...          # WebSocket connections only
    session ...
    sub ...
    pub ...
```

Example:

```bash
mqttcli \
  in-wsmqtt --disabled=false \
    remote --host 127.0.0.1 --port 8080 \
    http --target /ws \
    session --client-id browser-path-check --qos 1 \
    sub --topic 'demo/#'
```

> **Figure placeholder — MQTTCli command hierarchy.** Show root application → enabled connection instance → remote/HTTP transport settings → session → subscribe/publish actions, with one real command aligned to the tree.

Use expanded help at any level to inspect the options compiled into your current SNode.C/MQTTSuite installation:

```bash
mqttcli --help=expanded
mqttcli in-mqtt --help=expanded
mqttcli in-mqtt session --help=expanded
```

## Connection instances

When their build options are enabled, MQTTCli creates:

```text
in-mqtt       in-mqtts
in6-mqtt      in6-mqtts
un-mqtt       un-mqtts
in-wsmqtt     in-wsmqtts
in6-wsmqtt    in6-wsmqtts
un-wsmqtt     un-wsmqtts
```

These instances are created disabled by the current application startup code. Enable the one you want with:

```text
--disabled=false
```

This makes CLI commands explicit and avoids accidental parallel connection attempts.

## Session settings

The `session` subcommand controls MQTT CONNECT/session behavior.

Current application options include:

```text
--client-id <string>
--qos <0..2>
--retain-session
--keep-alive <seconds>
--will-topic <topic>
--will-message <message>
--will-qos <qos>
--will-retain
--username <string>
--password <string>
```

### Client ID

```bash
session --client-id inspector-01
```

Use a stable unique client ID when you need a persistent MQTT session. For quick disposable checks, choose a descriptive test ID.

### QoS

`session --qos` is the CLI's default QoS value used by its MQTT behavior. It is used for publish QoS and as the default subscription QoS unless a topic-specific subscription override is supplied.

```bash
session --qos 1
```

### Retained session / clean-session semantics

The current option name is:

```text
--retain-session
```

When true, the factory passes `clean_session=false` to the MQTT client. In other words:

```text
--retain-session=false   -> clean_session=true
--retain-session=true    -> clean_session=false
```

`--retain-session` requires a client ID.

MQTTCli itself does not expose the persistent session-store path option that Integrator/Store do; the flag controls MQTT session semantics on the broker connection.

### Keep alive

```bash
session --keep-alive 60
```

The source default is 60 seconds.

### Username and password

```bash
session --username alice --password 'example-secret'
```

These fields are sent in MQTT CONNECT. Whether they authenticate or authorize anything depends on the broker.

### Last Will

```bash
session \
  --client-id monitored-client \
  --will-topic clients/monitored-client/status \
  --will-message offline \
  --will-qos 1 \
  --will-retain
```

The MQTT will is intended for an unexpected connection loss. A normal client shutdown that sends DISCONNECT should not be used to test will delivery.

## Subscribing

### One topic filter

```bash
mqttcli \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 1883 \
    session --client-id sub-one --qos 0 \
    sub --topic sensors/room-01/temperature
```

### Wildcard filter

```bash
sub --topic 'sensors/+/temperature'
```

or:

```bash
sub --topic 'sensors/#'
```

Quote wildcard-containing filters in shell commands.

### Multiple topics

`sub --topic` accepts multiple values:

```bash
sub \
  --topic 'sensors/+/temperature' \
  --topic 'alerts/#' \
  --topic system/status
```

### Per-topic QoS override

MQTTCli accepts the MQTTSuite suffix:

```text
<topic-filter>##<qos>
```

For example:

```bash
session --qos 0 \
sub \
  --topic 'sensors/+/temperature##1' \
  --topic 'alerts/###2'
```

The first means filter `sensors/+/temperature` at QoS 1. The second looks unusual because the MQTT filter itself ends in `#`: `alerts/###2` is parsed as filter `alerts/#` plus override `##2`.

Use the explicit suffix only when the topic's subscription QoS should differ from `session --qos`.

## Publishing

### Simple text publish

```bash
mqttcli \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 1883 \
    session --client-id pub-text --qos 0 \
    pub --topic demo/state --message online
```

### QoS 1 publish

```bash
mqttcli \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 1883 \
    session --client-id pub-qos1 --qos 1 \
    pub --topic demo/value --message 42
```

For publish-only operation, QoS 0 disconnects after sending; QoS 1 waits for PUBACK; QoS 2 waits for the QoS 2 completion path before requesting disconnect.

### JSON publish

```bash
pub \
  --topic normalized/room-01/temperature \
  --message '{"value":21.7,"unit":"C"}'
```

MQTTCli does not assign semantic meaning to the JSON; it is just the MQTT payload. Pretty-printing occurs on received messages when parsing succeeds.

### Retained publish

```bash
mqttcli \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 1883 \
    session --client-id pub-retained --qos 1 \
    pub --topic devices/pump-1/status \
        --message online \
        --retain
```

A newly connected subscriber to that topic should receive the retained state according to broker behavior.

## Subscribe and publish on one connection

The CLI factory configures both `sub` and `pub` behavior on the same MQTT client. If both are present, MQTTCli subscribes and publishes after connection:

```bash
mqttcli \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 1883 \
    session --client-id pubsub-demo --qos 1 \
    sub --topic 'demo/replies/#' \
    pub --topic demo/request --message ping
```

Because a subscription is active, the client remains connected to receive matching messages instead of behaving like a one-shot publisher.

## Transport examples

The application behavior stays the same; choose a different connection instance and transport/address section.

### IPv4

```bash
in-mqtt --disabled=false \
  remote --host 127.0.0.1 --port 1883
```

### IPv6

```bash
in6-mqtt --disabled=false \
  remote --host ::1 --port 1883
```

### TLS

```bash
in-mqtts --disabled=false \
  remote --host broker.example.net --port 8883
```

Configure the instance's SNode.C TLS section for CA/certificate/key verification appropriate to your peer:

```bash
mqttcli in-mqtts --help=expanded
```

Selecting `in-mqtts` gives you the TLS stream path; it does not by itself define broker authorization.

### MQTT over WebSocket

```bash
mqttcli \
  in-wsmqtt --disabled=false \
    remote --host 127.0.0.1 --port 8080 \
    http --target /ws \
    session --client-id ws-check --qos 1 \
    sub --topic 'demo/#'
```

The WebSocket client requests subprotocol `mqtt`. `http --target` defaults to `/ws`.

### WSS

```bash
mqttcli \
  in-wsmqtts --disabled=false \
    remote --host broker.example.net --port 8088 \
    http --target /ws \
    session --client-id wss-check --qos 1 \
    sub --topic 'demo/#'
```

Configure SNode.C TLS settings for that instance separately.

### Unix-domain MQTT

```bash
mqttcli \
  un-mqtt --disabled=false \
    remote --sun-path /run/mqttsuite/broker.sock \
    session --client-id unix-check --qos 1 \
    sub --topic 'demo/#'
```

The Broker must be listening on the same socket path.

### MQTT over Unix-domain WebSocket

```bash
mqttcli \
  un-wsmqtt --disabled=false \
    remote --sun-path /run/mqttsuite/broker-http.sock \
    http --target /ws \
    session --client-id unix-ws-check --qos 1 \
    sub --topic 'demo/#'
```

This uses the same HTTP upgrade and `mqtt` subprotocol over a Unix-domain stream.

## Persist a command

Once a command is correct, `--write-config` writes the resolved configurable state and exits.

Subscriber example:

```bash
mqttcli \
  --config-file /dev/null \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 1883 \
    session --client-id persistent-inspector --qos 1 \
    sub --topic 'normalized/#' \
  --write-config ./mqttcli.conf
```

Then:

```bash
mqttcli --config-file ./mqttcli.conf
```

Review saved files before treating them as service configuration, especially when they contain MQTT credentials.

Persisting a publish action means the client will publish whenever that configured connection reaches its normal publication point. For truly one-off messages, an explicit command is usually clearer than a saved publisher config.

## Verify the other MQTTSuite applications

### MQTTBroker

Use one subscriber and one publisher against the same listener. The suite [Quick Start](../README.md#quick-start-broker-and-cli) is the canonical example.

### MQTTIntegrator

Subscribe to the expected mapped output before publishing one known input:

```bash
mqttcli \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 1883 \
    session --client-id mapped-observer --qos 1 \
    sub --topic 'normalized/#'
```

Then publish the exact topic/payload your mapping file matches.

### MQTTBridge

Connect the observer to the **destination** broker and subscribe to the exact topic Bridge should construct after prefixes. Publish on the source broker. This isolates forwarding from broker routing.

### MQTTStore

Start Store on a narrow test filter, publish JSON/text/retained/QoS examples with MQTTCli, then query MariaDB. MQTTStore's README includes the expected raw-table fields.

## Current reconnect behavior

MQTTCli's client endpoints enable retry/reconnect. That is helpful for long-lived subscribers but surprising for a one-shot publisher: after a successful publish and disconnect, the connection machinery can reconnect and republish.

For manual one-shot verification:

1. wait for the first successful publish result;
2. confirm it at the subscriber/destination;
3. stop the publisher with `Ctrl-C`.

Do not mistake repeated output from a reconnecting test publisher for Broker duplication until you have ruled this behavior out.

## Trust and diagnostic boundaries

- `session --username` and `--password` are command-line/configuration data; command histories, process inspection, and saved config files may expose them.
- The current MQTTCli debug logging path includes username and password values. Avoid broad debug logs when credentials are present.
- TLS/WSS protects the connection when configured correctly, but broker access control is separate.
- Received payloads are printed to the terminal. Treat terminal logs/transcripts as data-bearing artifacts.

## Troubleshooting

### No connection

Check:

- selected instance has `--disabled=false`;
- host/port or `--sun-path`;
- Broker listener is enabled;
- transport pairing matches (plain vs TLS, direct vs WebSocket);
- WebSocket target is correct;
- TLS trust material/options for encrypted instances.

### Connected but no subscription data

Check:

- topic filter spelling and shell quoting;
- wildcard placement;
- per-topic `##qos` parsing;
- publisher topic;
- Broker routing/retained-state expectations.

### Publish exits or reconnects unexpectedly

Publish-only operation intentionally disconnects after the required MQTT acknowledgement path. The SNode.C client endpoint can then reconnect. Use `Ctrl-C` after the first intended result for a manual one-shot test.

### JSON is not pretty-printed

Pretty printing is only a display convenience. If payload parsing fails, MQTTCli prints the payload as ordinary data; it does not reject non-JSON MQTT messages.

## Related documentation

- [MQTTSuite overview and build](../README.md)
- [MQTTBroker](../mqttbroker/README.md)
- [MQTTIntegrator](../mqttintegrator/README.md)
- [MQTTBridge](../mqttbridge/README.md)
- [MQTTStore](../mqttstore/README.md)

## License

MQTTSuite is available under:

```text
MIT OR GPL-3.0-or-later
```
