# MQTTBridge

MQTTBridge is the MQTTSuite client-side broker interconnection application. It creates one or more **logical bridges**, connects each logical bridge to multiple MQTT brokers as clients, subscribes to configured topic filters, and forwards received publishes to the other connected members.

MQTTBridge is **not** an MQTT broker. It is also **not** MQTTIntegrator: it does not run `MqttMapper`, parse/transform payloads, or render mapping templates. Its integration-like behavior comes from selecting subscriptions and constructing forwarded topic prefixes while preserving the original payload, QoS, and retain flag.

The suite-level build and common configuration model are in the [MQTTSuite README](../README.md). This README documents `mqttbridge`, its required bridge-definition JSON, forwarding semantics, admin surface, and current transport boundaries.

## Quick Start: bridge two local brokers

Assume two brokers are already listening on:

```text
Broker A: 127.0.0.1:18831
Broker B: 127.0.0.1:18832
```

Create `bridge.json`:

```json
{
  "bridges": [
    {
      "name": "lab",
      "brokers": [
        {
          "network": {
            "instance_name": "broker-a",
            "protocol": "in",
            "encryption": "legacy",
            "transport": "stream",
            "in": {
              "host": "127.0.0.1",
              "port": 18831
            }
          },
          "mqtt": {
            "client_id": "bridge-a",
            "clean_session": true,
            "loop_prevention": false
          },
          "topics": [
            { "topic": "a/#", "qos": 1 }
          ]
        },
        {
          "network": {
            "instance_name": "broker-b",
            "protocol": "in",
            "encryption": "legacy",
            "transport": "stream",
            "in": {
              "host": "127.0.0.1",
              "port": 18832
            }
          },
          "mqtt": {
            "client_id": "bridge-b",
            "clean_session": true,
            "loop_prevention": false
          },
          "topics": [
            { "topic": "b/#", "qos": 1 }
          ]
        }
      ]
    }
  ]
}
```

Start the bridge. `--definition` belongs to the required `bridge` application subcommand:

```bash
mqttbridge \
  --config-file /dev/null \
  bridge --definition ./bridge.json \
  admin-legacy --disabled \
  admin-tls --disabled
```

The definition deliberately uses non-overlapping input filters. A message received from Broker A on `a/#` is published to Broker B unchanged; the Bridge's Broker B member subscribes only to `b/#`, so that forwarded `a/#` message does not immediately re-enter the bridge through B.

Subscribe on Broker B:

```bash
mqttcli \
  --config-file /dev/null \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 18832 \
    session --client-id bridge-observer --qos 1 \
    sub --topic 'a/#'
```

Publish on Broker A:

```bash
mqttcli \
  --config-file /dev/null \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 18831 \
    session --client-id bridge-source --qos 1 \
    pub --topic a/temperature \
        --message '{"value":21.7,"unit":"C"}'
```

The Broker B observer should receive the same topic, payload, QoS, and retain state.

## Why Bridge is not Integrator

Both applications can change where a message appears, so the distinction deserves to be explicit.

| MQTTBridge | MQTTIntegrator |
| --- | --- |
| connects multiple broker members | connects as a transformation client |
| subscribes selected input filters | subscribes topic-tree mapping filters |
| forwards payload unchanged | can transform payload |
| can prepend configured topic prefixes | can render arbitrary mapped topics |
| preserves incoming QoS/retain when forwarding | output QoS/retain are mapping decisions |
| no `MqttMapper` | built around `MqttMapper` |
| fan-out is to other bridge members | fan-out is mapping-rule output |

If all you need is “messages in this selected topic domain should also appear on those broker domains,” use Bridge. If you need “this vendor message should become this normalized contract,” use Integrator.

## How the Bridge is assembled

The definition file creates logical configuration objects first. `BridgeStore` validates the file, applies schema defaults, and builds a map of logical bridges and broker members.

Each broker member is then turned into an SNode.C client connection. When that connection is established, `SocketContextFactory` looks up the member by its full internal instance name and injects it into an MQTT context:

```cpp
return new iot::mqtt::SocketContext(
    socketConnection,
    new mqtt::bridge::lib::Mqtt(
        socketConnection->getConnectionName(), *broker));
```

On CONNACK, that MQTT client subscribes to the member's configured topics. On PUBLISH, it hands the message to the owning logical bridge for forwarding.

> **Figure placeholder — Bridge definition to runtime clients.** Show `bridges[]` → logical bridge → `brokers[]` → SNode.C client connection/MQTT context, including the internal relationship between a definition member and its runtime client.

## Build and install result

`mqttbridge` is built by the top-level MQTTSuite CMake project. A complete install places the executable at:

```text
${CMAKE_INSTALL_PREFIX}/bin/mqttbridge
```

and copies the Bridge Web assets to:

```text
${CMAKE_INSTALL_PREFIX}/var/www/mqttsuite/mqttbridge
```

The runtime `--html-dir` option is separate from that install rule. The current source does not automatically set the installed directory as the `--html-dir` default, so provide it explicitly when you want the shipped Web assets. Both `--definition` and `--html-dir` belong to the `bridge` subcommand:

```bash
mqttbridge \
  bridge \
    --definition ./bridge.json \
    --html-dir /usr/local/var/www/mqttsuite/mqttbridge
```

Adjust the path for your chosen install prefix.

## The required bridge definition

MQTTBridge requires the `bridge` subcommand's definition option:

```text
bridge --definition <file>
```

The current schema is [`lib/bridge-schema.json`](lib/bridge-schema.json).

At the top level:

```json
{
  "bridges": [
    {
      "name": "lab",
      "disabled": false,
      "prefix": "",
      "brokers": []
    }
  ]
}
```

`bridges` must contain at least one logical bridge.

> **Figure placeholder — Bridge-definition hierarchy.** Show root `bridges[]`, one bridge's `name/disabled/prefix`, and nested broker members with network, MQTT session, subscriptions, member prefix, and session store.

## Logical bridge fields

### `name`

Required logical bridge identifier.

```json
"name": "building-a"
```

The runtime combines the bridge name with each network `instance_name` internally to identify a concrete client member.

### `disabled`

Optional, default `false`.

A disabled logical bridge does not start its broker clients.

### `prefix`

Optional, default empty.

This prefix is prepended to every message forwarded by the logical bridge.

## Broker member fields

A `brokers` array contains the MQTT client members of the logical bridge. Each member can define:

- `disabled`;
- `session_store`;
- `network`;
- `mqtt`;
- member `prefix`;
- `topics`.

### Network

Every member requires a `network` object containing:

```json
{
  "instance_name": "broker-a",
  "protocol": "in",
  "encryption": "legacy",
  "transport": "stream",
  "in": {
    "host": "127.0.0.1",
    "port": 1883
  }
}
```

The fields select the runtime stack:

- `protocol`: address family/endpoint type;
- `encryption`: `legacy` for the plain stream stack or `tls`;
- `transport`: `stream` or `websocket`;
- protocol-specific address object.

For IPv4 (`in`) and IPv6 (`in6`), the address object uses `host` and `port`.

### MQTT session settings

A member's `mqtt` object can set:

```json
{
  "client_id": "bridge-a",
  "keep_alive": 60,
  "clean_session": true,
  "will_topic": "",
  "will_message": "",
  "will_qos": 0,
  "will_retain": false,
  "username": "",
  "password": "",
  "loop_prevention": false
}
```

These are client-side MQTT connection values. Username/password presence does not imply anything about the remote broker's authentication policy; it only tells MQTTBridge what to send in CONNECT.

### Persistent session store

`session_store` is a per-member path for persistent MQTT client session state.

```json
"session_store": "/var/lib/mqttsuite/bridge-a-session.json"
```

Use a stable path with appropriate filesystem ownership when session persistence is required.

### Subscriptions

Each member's `topics` array contains the filters it should receive from that broker:

```json
"topics": [
  { "topic": "sensors/+/temperature", "qos": 1 },
  { "topic": "alerts/#", "qos": 2 }
]
```

The configured QoS is subscription QoS. When Bridge forwards an incoming publish, it preserves the PUBLISH QoS it received.

A member's subscription list selects **inputs from that broker**. It does not filter which messages are allowed to be published **to** that member as a destination; every received bridge message is sent to every other currently connected member.

## Prefix construction

The forwarding topic is constructed exactly as:

```text
bridge prefix
+ source-member prefix
+ destination-member prefix
+ original MQTT topic
```

Suppose:

```json
{
  "name": "lab",
  "prefix": "bridge/",
  "brokers": [
    {
      "prefix": "from-a/",
      "...": "source member"
    },
    {
      "prefix": "to-b/",
      "...": "destination member"
    }
  ]
}
```

An input on Broker A:

```text
a/temperature
```

is published to Broker B as:

```text
bridge/from-a/to-b/a/temperature
```

The payload, QoS, and retain flag are preserved.

Prefixes are literal concatenation. Include separators such as `/` deliberately; Bridge does not insert topic separators for you.

> **Figure placeholder — Prefix and forwarding construction.** Trace one publish from source member to destination member and build the output topic token by token as bridge prefix + source prefix + destination prefix + original topic.

## Multi-member bridges

A logical bridge can have more than two members. For one received message, Bridge iterates the currently connected member clients and forwards to every destination except the client that delivered that message.

For a three-member bridge:

```text
A -> B
 \-> C
```

an input received from A is sent to B and C. A is excluded from that forwarding pass.

This fan-out is useful, but it also means loops need to be considered at topology level rather than only pairwise.

## Loop behavior

### Immediate source-member exclusion

Bridge never sends a received message straight back through the same MQTT client object that delivered it. That prevents the simplest immediate reflection.

It does **not** by itself prevent:

```text
A -> B -> A
```

when the message published to B is received again by the Bridge's B member and then forwarded back to A.

Subscription partitioning and prefix design can avoid many such cycles. The Quick Start uses non-overlapping `a/#` and `b/#` inputs for exactly that reason.

### `loop_prevention`

The definition also exposes:

```json
"loop_prevention": true
```

The current MQTTSuite/SNode.C client path passes this as a private origin-reflection request in MQTT CONNECT. It is not a standard MQTT 3.1.1 loop-prevention feature and should only be expected to have the intended effect with cooperating SNode.C MQTT behavior.

Do not use it as proof that arbitrary cycles involving third-party brokers, additional bridges, or other clients are impossible.

> **Figure placeholder — Loop boundaries.** Contrast immediate source exclusion, subscription/prefix topology design, and the private cooperating-endpoint mechanism, and show one cycle that still requires operator reasoning.

## Transport selection

### IPv4 and IPv6 stream

The current runtime has direct stream branches for `protocol: "in"` and `protocol: "in6"`, each with `encryption: "legacy"` or `"tls"` when the corresponding CMake option is built.

Plain IPv4 member:

```json
{
  "network": {
    "instance_name": "remote-a",
    "protocol": "in",
    "encryption": "legacy",
    "transport": "stream",
    "in": {
      "host": "192.0.2.10",
      "port": 1883
    }
  }
}
```

TLS/IPv4:

```json
{
  "network": {
    "instance_name": "remote-a-tls",
    "protocol": "in",
    "encryption": "tls",
    "transport": "stream",
    "in": {
      "host": "broker.example.net",
      "port": 8883
    }
  }
}
```

Transport encryption does not define MQTT authorization. The remote broker and SNode.C TLS configuration still determine trust and credentials.

### WebSocket and WSS

Set:

```json
"transport": "websocket"
```

with `encryption: "legacy"` for plain WebSocket or `encryption: "tls"` for WSS. The current Bridge HTTP client requests `/ws` with WebSocket subprotocol `mqtt`.

Example:

```json
{
  "network": {
    "instance_name": "ws-a",
    "protocol": "in",
    "encryption": "legacy",
    "transport": "websocket",
    "in": {
      "host": "127.0.0.1",
      "port": 8080
    }
  }
}
```

### Unix-domain source discrepancy

The schema defines `protocol: "un"` with:

```json
"un": {
  "path": "/run/mqttsuite/broker.sock"
}
```

and the runtime contains Unix-domain client branches.

However, the current **direct stream** branches read the address key `host`, while the schema requires `path`. The WebSocket Unix-domain branch reads `path` consistently.

Because schema and direct-stream runtime disagree, this README does not present direct Unix-domain Bridge deployment as a verified usable path in this source revision. Treat the mismatch as an implementation issue to resolve rather than inventing a definition that satisfies both.

### Schema/build tokens without runtime instantiation

The bridge schema also admits `protocol` values `rc` and `l2`, and the Bridge CMake file requests corresponding SNode.C components as optional components.

The current `mqttbridge.cpp` runtime selection has no `rc` or `l2` branches. Therefore those schema values are not runnable Bridge network choices in this source revision. Schema vocabulary and optional dependency discovery are not sufficient evidence of runtime support.

## Admin configuration and state surface

MQTTBridge always constructs an IPv4 admin router with two server instances:

```text
admin-legacy   source default port 8081
admin-tls      source default port 8082
```

You can disable them through the normal SNode.C instance configuration when no Web/admin surface is needed.

### Active configuration

```text
GET /api/bridge/config
```

returns the active bridge definition.

### Patch and apply

```text
PATCH /api/bridge/config
```

expects JSON Patch. The application:

1. patches the active JSON into a staged document;
2. validates the staged document against the bridge schema and applies defaults;
3. begins closing active bridge connections;
4. activates/persists the staged document when flows are closed;
5. rebuilds the logical bridge/member objects;
6. starts the new bridge connections;
7. reparses SNode.C configuration.

A patch is rejected while a previous restart is still in progress.

Activation writes the normalized active JSON back to the definition file. Treat that file as mutable application state when using the API, not as read-only startup input.

### Server-sent events

```text
GET /api/bridge/sse
```

provides bridge lifecycle state through SSE, including bridge starting/stopping and broker member connection/disconnection events.

### Shipped Web assets

The router redirects:

```text
/ -> /config
/config -> /config/index.html
```

and serves `/config` from `--html-dir`.

When using installed assets, point `bridge --html-dir` at the installed Bridge Web directory for your prefix.

> **Figure placeholder — Patch, close, activate, restart, SSE.** Show JSON Patch producing validated staged config, active clients closing, staged activation/persistence, rebuilt clients starting, and lifecycle updates emitted through SSE.

## Persisting the application command

The Bridge definition is already a persistent domain file. The SNode.C application configuration can separately persist options such as which admin listener is enabled and which definition/html paths to use.

For example:

```bash
mqttbridge \
  --config-file /dev/null \
  bridge \
    --definition /etc/mqttsuite/bridge.json \
    --html-dir /usr/local/var/www/mqttsuite/mqttbridge \
  admin-legacy --disabled \
  admin-tls --disabled \
  --write-config ./mqttbridge.conf
```

Review both the generated application config and the definition file; they own different concerns.

## Verification patterns with MQTTCli

### Verify one direction first

Subscribe on the destination broker to the exact expected forwarded topic, then publish one source message. Do not begin with `#` on every bridge member because broad symmetric subscriptions make loop analysis unnecessarily difficult.

### Verify prefixes

If prefixes are enabled, write the expected concatenation before testing:

```text
<bridge-prefix><source-prefix><destination-prefix><original-topic>
```

Subscribe to that exact result on the destination broker.

### Verify QoS/retain preservation

Publish a retained QoS 1 test message and inspect MQTTCli output on the destination. Bridge uses the received publish's QoS and retain flag when forwarding.

### Verify Bridge versus Integrator behavior

Send a JSON payload and confirm that Bridge forwards the exact payload bytes/string unchanged. If transformation is expected, put MQTTIntegrator in the message path instead.

## Trust and credential boundaries

- Bridge definitions can contain broker usernames/passwords and MQTT will data.
- The admin configuration API can return the active definition, including those fields.
- The reviewed Bridge router does not add an application-level authentication layer around `/api/bridge/config`.
- The current Bridge debug logging prints broker username and password values along with connection settings. Do not enable/share broad debug output without considering credential exposure.
- Activating a staged configuration rewrites the definition file. Give the process only the filesystem permissions it needs and back up/version operational definitions intentionally.
- TLS protects a selected connection/admin transport; it does not substitute for API authorization.
- Session-store files are persistent client state and should have appropriate ownership.

Bind or filter the admin surface to a trusted management boundary rather than treating it as a public configuration endpoint.

## Troubleshooting

### `bridge --definition` is rejected

The option is required inside the `bridge` application subcommand and the path must exist. Validate the JSON against [`lib/bridge-schema.json`](lib/bridge-schema.json) and check that each network object includes the address object matching its `protocol`.

### A bridge member never connects

Check:

- logical bridge/member `disabled`;
- protocol/transport/encryption combination is compiled and instantiated by current runtime;
- IPv4/IPv6 host and port;
- remote Broker listener;
- TLS configuration for encrypted paths;
- MQTT client credentials accepted by the remote Broker.

### A message is not forwarded

Check:

- source member is connected;
- source member subscribed to a filter that matches the input;
- destination member is currently connected;
- expected prefix concatenation;
- destination observer subscribed to the forwarded topic.

### Messages loop

Reduce the topology to two members and use non-overlapping source filters. Then inspect:

- member subscriptions;
- bridge/source/destination prefixes;
- other clients or bridges that can republish into subscribed namespaces;
- whether `loop_prevention` is actually understood by every cooperating endpoint involved.

### Web configuration page is missing

Confirm `bridge --html-dir` points to the installed Bridge Web directory. The install rule and runtime path option are not automatically connected by the current source.

### A config patch returns conflict

The Bridge is still in its close/restart cycle. Let the current apply complete before sending another patch.

## Related documentation

- [MQTTSuite overview and build](../README.md)
- [MQTTBroker](../mqttbroker/README.md)
- [MQTTIntegrator](../mqttintegrator/README.md)
- [MQTTCli](../mqttcli/README.md)
- [MQTTStore](../mqttstore/README.md)
- [Bridge schema](lib/bridge-schema.json)

## License

MQTTSuite is available under:

```text
MIT OR GPL-3.0-or-later
```