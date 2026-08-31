# MQTTBridge definition and forwarding reference

[← MQTTSuite](../README.md) · [MQTTBridge README](../mqttbridge/README.md) · [Configuration](configuration.md) · [Capabilities](capabilities.md)

The complete operator-facing bridge-definition, forwarding, prefix, transport, administration, restart/apply, and loop-boundary documentation currently lives in the [MQTTBridge README](../mqttbridge/README.md). This page exists as the stable deeper-reference route used by the shared MQTTSuite documentation without duplicating that application-owned material.

**Evidence baseline:** [`SNodeC/mqttsuite@52de5631245c6318bfa5b7cca700f0754014f34d`](https://github.com/SNodeC/mqttsuite/tree/52de5631245c6318bfa5b7cca700f0754014f34d).

Primary machine-readable and implementation anchors:

- [bridge-definition schema](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttbridge/lib/bridge-schema.json)
- [MQTTBridge runtime assembly](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttbridge/mqttbridge.cpp)
- [logical forwarding](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttbridge/lib/Bridge.cpp)
- [definition/store lifecycle](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttbridge/lib/BridgeStore.cpp)

Important current boundaries are summarized in [capabilities](capabilities.md): schema vocabulary is broader than current runtime dispatch, direct Unix-domain schema/runtime address handling is inconsistent, and the private loop-prevention mechanism does not establish arbitrary cyclic-topology safety.