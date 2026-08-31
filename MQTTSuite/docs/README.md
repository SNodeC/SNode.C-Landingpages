# MQTTSuite documentation

This directory is the reference layer behind the MQTTSuite root and application READMEs. The application suite remains the primary documentation entry point; these pages own details that would otherwise overload those READMEs.

**Evidence baseline:** [`SNodeC/mqttsuite@52de5631245c6318bfa5b7cca700f0754014f34d`](https://github.com/SNodeC/mqttsuite/tree/52de5631245c6318bfa5b7cca700f0754014f34d). Shared SNode.C behavior is pinned from the revisions named by each reference.

## Reference index

| Reference | Owns |
| --- | --- |
| [Configuration](configuration.md) | shared SNode.C/MQTTSuite configuration hierarchy, precedence, persistence, transports, retry/reconnect, TLS and logging |
| [Capabilities and evidence](capabilities.md) | Available vs Exercised scope, limitations and explicit non-claims |
| [Integrator mapping](integrator-mapping.md) | complete mapping grammar, matching, templates, fan-out, plugins and mapping lifecycle |
| [Broker HTTP API and SSE](broker-http-api.md) | Broker dashboard/admin HTTP routes, responses, trust boundary, SSE events and replay behavior |
| [Integrator HTTP API](integrator-http-api.md) | mapping administration REST-style API, Basic authentication, drafts, validation, deploy/history/rollback and error contracts |
| [Bridge definition](bridge-definition.md) | bridge-definition entry point and forwarding/configuration semantics |
| [Bridge HTTP API and SSE](bridge-http-api.md) | Bridge configuration API, restart/apply lifecycle, status SSE events, replay and trust boundary |
| [Store storage](store-storage.md) | MQTTStore raw-envelope and projection reference entry point |

Every document in this directory is intentionally referenced from this README so the reference layer has no orphan pages.

## Application entry points

- [MQTTSuite overview](../README.md)
- [MQTTBroker](../mqttbroker/README.md)
- [MQTTIntegrator](../mqttintegrator/README.md)
- [MQTTBridge](../mqttbridge/README.md)
- [MQTTCli](../mqttcli/README.md)
- [MQTTStore](../mqttstore/README.md)

## HTTP and event interfaces

Three applications expose operator-facing HTTP interfaces in the reviewed source:

| Application | REST-style HTTP | SSE |
| --- | --- | --- |
| MQTTBroker | yes | yes |
| MQTTIntegrator | yes | **no SSE route in the reviewed source** |
| MQTTBridge | yes | yes |

The API references document current implementation behavior rather than a generic stability or security guarantee. In particular, authentication, credential exposure, CORS, replay and error behavior differ by application and must not be assumed to be uniform across the suite.
