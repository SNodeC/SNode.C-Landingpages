# MQTTStore storage and projection reference

[← MQTTSuite](../README.md) · [MQTTStore README](../mqttstore/README.md) · [Configuration](configuration.md) · [Capabilities](capabilities.md)

The complete operator-facing MariaDB bootstrap, raw-envelope schema, payload classification, projection grammar, SQL verification, and failure-boundary documentation currently lives in the [MQTTStore README](../mqttstore/README.md). This page is the stable deeper-reference route used by the shared MQTTSuite documentation without duplicating the application-owned storage manual.

**Evidence baseline:** [`SNodeC/mqttsuite@52de5631245c6318bfa5b7cca700f0754014f34d`](https://github.com/SNodeC/mqttsuite/tree/52de5631245c6318bfa5b7cca700f0754014f34d).

Primary machine-readable and implementation anchors:

- [projection schema](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttstore/lib/projection-schema.json)
- [projection loading/matching](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttstore/lib/StoragePlan.cpp)
- [MariaDB raw/projection storage](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttstore/lib/MariaDbStorage.cpp)
- [Store context creation](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttstore/SocketContextFactory.cpp)

Important current boundaries are summarized in [capabilities](capabilities.md): Store manages the raw table but not projection-table migrations/retention, raw and projection writes are independent operations, and malformed projection-plan lifecycle timing remains partly `UNVERIFIED-RUNTIME`.