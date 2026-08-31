# MQTTIntegrator sibling topic branches — complete example

[← Documentation index](README.md) · [Integrator mapping reference](integrator-mapping.md) · [MQTTIntegrator README](../mqttintegrator/README.md)

This example shows a complete mapping with **sibling `topic_level` branches at the same depth**, including a literal-first fallback pattern. It is source-aligned with [`SNodeC/mqttsuite@6c0ff62c612694a6111ff971c446327938130cf0`](https://github.com/SNodeC/mqttsuite/tree/6c0ff62c612694a6111ff971c446327938130cf0), including the MQTT multi-level `#` fix merged in [PR #22](https://github.com/SNodeC/mqttsuite/pull/22).

The current mapper scans sibling `topic_level` entries in document order and selects the **first** matching literal, `+`, or `#` branch. Put specific literal siblings before wildcard fallbacks. `+` matches one level; terminal `#` matches zero or more remaining levels and therefore normally belongs last when used as the broadest sibling fallback.

## Goal

Accept these input topics:

```text
sensors/room-01/temperature
sensors/room-01/humidity
sensors/room-01/co2
sensors/room-02/temperature
```

and treat the final topic level differently:

```text
temperature -> explicit temperature branch
humidity    -> explicit humidity branch
anything else at that depth -> + fallback branch
```

## Complete mapping

Save as `mapping-siblings.json`:

```json
{
  "connection": {
    "client_id": "sibling-topic-demo",
    "keep_alive": 60,
    "clean_session": true
  },
  "mapping": {
    "plugins": [],
    "topic_level": {
      "name": "sensors",
      "topic_level": {
        "name": "+",
        "topic_level": [
          {
            "name": "temperature",
            "subscription": {
              "qos": 1,
              "value": {
                "mapped_topic": "normalized/temperature",
                "mapping_template": "source={{ topic }} value={{ message }}",
                "qos": 1,
                "retain": false
              }
            }
          },
          {
            "name": "humidity",
            "subscription": {
              "qos": 1,
              "value": {
                "mapped_topic": "normalized/humidity",
                "mapping_template": "source={{ topic }} value={{ message }}",
                "qos": 1,
                "retain": false
              }
            }
          },
          {
            "name": "+",
            "subscription": {
              "qos": 0,
              "value": {
                "mapped_topic": "normalized/other",
                "mapping_template": "source={{ topic }} value={{ message }}",
                "qos": 0,
                "retain": false
              }
            }
          }
        ]
      }
    }
  }
}
```

The middle `+` consumes exactly one device/location level (`room-01`, `room-02`, ...). The three entries in the final `topic_level` array are **siblings**.

## Effective subscriptions

MQTTIntegrator extracts a subscription at each sibling branch:

```text
sensors/+/temperature   QoS 1
sensors/+/humidity      QoS 1
sensors/+/+             QoS 0
```

The broad `sensors/+/+` fallback overlaps the two literal filters at the broker-subscription level. The mapper still resolves each delivered publication by its own first-match sibling order.

## What matches

| Input topic | Selected sibling | Output topic |
| --- | --- | --- |
| `sensors/room-01/temperature` | literal `temperature` | `normalized/temperature` |
| `sensors/room-01/humidity` | literal `humidity` | `normalized/humidity` |
| `sensors/room-01/co2` | wildcard `+` fallback | `normalized/other` |
| `sensors/room-02/temperature` | literal `temperature` | `normalized/temperature` |

For input:

```text
Topic:   sensors/room-01/temperature
Payload: 21.7
```

the selected branch renders:

```text
Topic:   normalized/temperature
Payload: source=sensors/room-01/temperature value=21.7
QoS:     1
```

For:

```text
Topic:   sensors/room-01/co2
Payload: 612
```

the two literal siblings do not match, so the final `+` sibling is selected:

```text
Topic:   normalized/other
Payload: source=sensors/room-01/co2 value=612
QoS:     0
```

## Why order matters

Do **not** put the fallback `+` first unless it is supposed to shadow all literals at that depth.

This ordering:

```json
"topic_level": [
  { "name": "+", "...": "fallback" },
  { "name": "temperature", "...": "specific" }
]
```

causes `temperature` to match the first `+` sibling before the mapper reaches the literal branch.

The same principle is even more important for `#`: a `#` sibling matches the entire remaining subtree, so placing it before more specific siblings makes it the selected branch for those topics as well.

The recommended pattern is therefore:

```text
specific literal siblings
        then
single-level + fallback if needed
        then
multi-level # fallback if needed
```

## Run the example

With an MQTTBroker on `127.0.0.1:1883`:

```bash
mqttintegrator \
  --config-file /dev/null \
  integrator --mqtt-mapping-file ./mapping-siblings.json \
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

Observe all outputs:

```bash
mqttcli \
  --config-file /dev/null \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 1883 \
    session --client-id sibling-observer --qos 1 \
    sub --topic 'normalized/#'
```

Then publish representative inputs with a second MQTTCli process.

## Wildcard boundary

This particular example uses `+` because its fallback is exactly one topic level deep. In the post-fix mapper, terminal `#` has normal MQTT multi-level behavior: it consumes zero or more remaining levels. For example, a `sensors/#` mapping can match `sensors` itself (when the `sensors` parent has no own subscription mapping) as well as `sensors/room-01`, `sensors/room-01/temperature`, and deeper descendants. See [`#` multi-level wildcard](integrator-mapping.md#-multi-level-wildcard) for the full behavior.

**Evidence class:** source-aligned example. The landing-page qualification did not execute this exact sibling-branch scenario end to end.
