# MQTTSuite documentation

This directory is the reference layer behind the MQTTSuite root and application READMEs. The application suite remains the primary documentation entry point; these pages own details that would otherwise overload those READMEs.

**Current source baseline:** [`SNodeC/mqttsuite@6c0ff62c612694a6111ff971c446327938130cf0`](https://github.com/SNodeC/mqttsuite/tree/6c0ff62c612694a6111ff971c446327938130cf0). This includes the narrow MQTTIntegrator wildcard fix from [PR #22](https://github.com/SNodeC/mqttsuite/pull/22) / [`d15f70a`](https://github.com/SNodeC/mqttsuite/commit/d15f70a2818d291638c50aa2e2116a9e49ebd9e1), where `#` became a true multi-level wildcard while `+` remains single-level. The recorded landing-page runtime qualification predates that narrow fix; pages distinguish source behavior from runtime-exercised evidence where relevant. Shared SNode.C behavior is pinned from the revisions named by each reference.

## Reference index

| Reference | Owns |
| --- | --- |
| [Configuration](configuration.md) | shared SNode.C/MQTTSuite configuration hierarchy, precedence, persistence, transports, retry/reconnect, TLS and logging |
| [Capabilities and evidence](capabilities.md) | Available vs Exercised scope, limitations and explicit non-claims |
| [Integrator mapping](integrator-mapping.md) | complete mapping grammar, matching, templates, fan-out, plugins and mapping lifecycle |
| [Integrator sibling-topic example](integrator-sibling-topics-example.md) | complete mapping with literal and wildcard sibling `topic_level` branches, extracted subscriptions, precedence and runnable commands |
| [Broker HTTP API and SSE](broker-http-api.md) | Broker dashboard/admin HTTP routes, responses, trust boundary, SSE events and replay behavior |
| [Integrator HTTP API](integrator-http-api.md) | mapping administration REST-style API, Basic authentication, drafts, validation, deploy/history/rollback and error contracts |
| [Bridge definition](bridge-definition.md) | bridge-definition entry point and forwarding/configuration semantics |
| [Bridge multi-broker example](bridge-multi-broker-example.md) | complete three-broker logical bridge, `N - 1` fan-out, prefixes, input subscriptions and loop implications |
| [Bridge HTTP API and SSE](bridge-http-api.md) | Bridge configuration API, restart/apply lifecycle, status SSE events, replay and trust boundary |
| [Store storage](store-storage.md) | MQTTStore raw-envelope and projection reference entry point |

Every document in this directory is intentionally referenced from this README so the reference layer has no orphan pages.

## Complete configuration examples

Two examples make behaviors that are easy to misunderstand explicit:

- [MQTTIntegrator sibling topic branches](integrator-sibling-topics-example.md) shows several real sibling `topic_level` entries under one parent, why document order matters, how literal branches interact with a `+` fallback, and which MQTT subscriptions are extracted.
- [MQTTBridge with three broker members](bridge-multi-broker-example.md) gives a complete `bridge.json`, shows one input being forwarded to two destinations, derives the exact prefixed topics, and explains why input subscription design matters for loops.

Both are **source-aligned examples**, not additional runtime-qualification claims.

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
