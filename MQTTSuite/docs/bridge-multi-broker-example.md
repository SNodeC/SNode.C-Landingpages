# MQTTBridge multi-broker bridge — complete example

[← Documentation index](README.md) · [Bridge definition reference](bridge-definition.md) · [MQTTBridge README](../mqttbridge/README.md)

This example shows one logical MQTTBridge with **three broker members**. It is source-aligned with [`SNodeC/mqttsuite@52de5631245c6318bfa5b7cca700f0754014f34d`](https://github.com/SNodeC/mqttsuite/tree/52de5631245c6318bfa5b7cca700f0754014f34d) and the current [`bridge-schema.json`](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttbridge/lib/bridge-schema.json).

A logical bridge is not restricted to two brokers. When a member receives a subscribed PUBLISH, MQTTBridge forwards it to **every other currently connected member** in that logical bridge and excludes only the client that delivered the message.

## Topology

Assume three brokers:

```text
Broker A: 127.0.0.1:18831
Broker B: 127.0.0.1:18832
Broker C: 127.0.0.1:18833
```

Each broker contributes one distinct input namespace:

```text
Broker A -> site-a/#
Broker B -> site-b/#
Broker C -> site-c/#
```

The bridge adds a common prefix plus source/destination member prefixes:

```text
bridge prefix: mesh/
A member prefix: a/
B member prefix: b/
C member prefix: c/
```

For one publication received from A, MQTTBridge produces two publications:

```text
A input
  ├─► B
  └─► C
```

## Complete `bridge.json`

```json
{
  "bridges": [
    {
      "name": "three-site-mesh",
      "disabled": false,
      "prefix": "mesh/",
      "brokers": [
        {
          "disabled": false,
          "session_store": "",
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
            "client_id": "three-site-a",
            "keep_alive": 60,
            "clean_session": true,
            "will_topic": "",
            "will_message": "",
            "will_qos": 0,
            "will_retain": false,
            "username": "",
            "password": "",
            "loop_prevention": false
          },
          "prefix": "a/",
          "topics": [
            {
              "topic": "site-a/#",
              "qos": 1
            }
          ]
        },
        {
          "disabled": false,
          "session_store": "",
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
            "client_id": "three-site-b",
            "keep_alive": 60,
            "clean_session": true,
            "will_topic": "",
            "will_message": "",
            "will_qos": 0,
            "will_retain": false,
            "username": "",
            "password": "",
            "loop_prevention": false
          },
          "prefix": "b/",
          "topics": [
            {
              "topic": "site-b/#",
              "qos": 1
            }
          ]
        },
        {
          "disabled": false,
          "session_store": "",
          "network": {
            "instance_name": "broker-c",
            "protocol": "in",
            "encryption": "legacy",
            "transport": "stream",
            "in": {
              "host": "127.0.0.1",
              "port": 18833
            }
          },
          "mqtt": {
            "client_id": "three-site-c",
            "keep_alive": 60,
            "clean_session": true,
            "will_topic": "",
            "will_message": "",
            "will_qos": 0,
            "will_retain": false,
            "username": "",
            "password": "",
            "loop_prevention": false
          },
          "prefix": "c/",
          "topics": [
            {
              "topic": "site-c/#",
              "qos": 1
            }
          ]
        }
      ]
    }
  ]
}
```

## Start the bridge

```bash
mqttbridge \
  --config-file /dev/null \
  --definition ./bridge.json \
  admin-legacy --disabled \
  admin-tls --disabled
```

The two admin listeners are disabled here only to keep the forwarding example focused. Their REST/SSE contract is documented in [Bridge HTTP API and SSE](bridge-http-api.md).

## Observe Broker B and Broker C

On Broker B:

```bash
mqttcli \
  --config-file /dev/null \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 18832 \
    session --client-id observe-b --qos 1 \
    sub --topic 'mesh/#'
```

On Broker C:

```bash
mqttcli \
  --config-file /dev/null \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 18833 \
    session --client-id observe-c --qos 1 \
    sub --topic 'mesh/#'
```

## Publish on Broker A

```bash
mqttcli \
  --config-file /dev/null \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 18831 \
    session --client-id source-a --qos 1 \
    pub --topic site-a/room-01/temperature \
        --message '{"value":21.7,"unit":"C"}'
```

MQTTBridge receives that publication through the A member because A subscribes to `site-a/#`.

## Resulting fan-out

The forwarding topic is constructed as:

```text
bridge prefix
+ source-member prefix
+ destination-member prefix
+ original topic
```

Therefore Broker B receives:

```text
mesh/a/b/site-a/room-01/temperature
```

and Broker C receives:

```text
mesh/a/c/site-a/room-01/temperature
```

Both forwarded publications preserve the incoming payload, PUBLISH QoS and retain flag.

Broker A is not a destination for this forwarding pass because it is the member that delivered the original publication.

## What happens in the other directions

A publication entering through B on:

```text
site-b/plant/status
```

is forwarded to A and C as:

```text
mesh/b/a/site-b/plant/status
mesh/b/c/site-b/plant/status
```

A publication entering through C on:

```text
site-c/power/state
```

is forwarded to A and B as:

```text
mesh/c/a/site-c/power/state
mesh/c/b/site-c/power/state
```

This is true multi-member fan-out: one received message produces `N - 1` outgoing publications when all `N` members are connected.

## Why these subscriptions avoid immediate re-entry

The member input filters are deliberately narrow:

```text
A subscribes only site-a/#
B subscribes only site-b/#
C subscribes only site-c/#
```

Forwarded topics begin with `mesh/`, so a message forwarded from A to B does **not** match B's `site-b/#` input subscription and therefore does not immediately re-enter the bridge through B.

This is topology design, not a universal loop guarantee. If you instead subscribe members broadly—for example all members to `#`—a forwarded message can be received again by another Bridge member and be forwarded onward or back toward its origin.

## More than three brokers

The same rule generalizes. With four connected members A/B/C/D, one message received from A is forwarded to B, C and D. MQTTBridge iterates the connected members and excludes only the source MQTT client for that forwarding pass.

As the member count grows, review:

- input subscription overlap;
- prefix construction;
- third-party clients that republish bridge output;
- cyclic paths through other bridges;
- use of the private `loop_prevention` extension only with cooperating SNode.C endpoints.

Do not treat `loop_prevention: true` as proof that arbitrary multi-broker cycles are safe.

**Evidence class:** source-aligned example. The landing-page qualification did not execute this exact three-broker topology end to end.