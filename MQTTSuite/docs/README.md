# MQTTSuite documentation

This directory contains the deeper references behind the MQTTSuite root and application READMEs. Start from the application you want to operate; use these pages when you need shared configuration, exact mapping semantics, HTTP/SSE contracts, or complete worked examples.

## Reference index

| Reference | Purpose |
| --- | --- |
| [Configuration](configuration.md) | shared SNode.C/MQTTSuite configuration hierarchy, defaults, persistence, transports, retry/reconnect, TLS and logging |
| [Capabilities and evidence](capabilities.md) | source/runtime qualification scope, limitations and explicit non-claims |
| [Integrator mapping](integrator-mapping.md) | complete mapping grammar, matching, templates, fan-out, plugins and lifecycle semantics |
| [Integrator sibling-topic example](integrator-sibling-topics-example.md) | complete literal/wildcard sibling mapping with extracted subscriptions and runnable commands |
| [Broker HTTP API and SSE](broker-http-api.md) | Broker dashboard/admin routes, responses, trust boundary and SSE behavior |
| [Integrator HTTP API](integrator-http-api.md) | mapping administration API, authentication, drafts, validation, deploy/history/rollback and errors |
| [Bridge definition](bridge-definition.md) | routing page to Bridge definition/forwarding material |
| [Bridge multi-broker example](bridge-multi-broker-example.md) | complete three-broker logical bridge and resulting topics |
| [Bridge HTTP API and SSE](bridge-http-api.md) | Bridge configuration API, restart/apply lifecycle, SSE events and trust boundary |
| [Store storage](store-storage.md) | routing page to Store raw-envelope/projection material |

## Complete worked examples

- [MQTTIntegrator sibling topic branches](integrator-sibling-topics-example.md) shows literal siblings with a `+` fallback, document-order precedence, extracted subscriptions, and runnable commands.
- [MQTTBridge with three broker members](bridge-multi-broker-example.md) gives a complete `bridge.json`, one-to-many forwarding, exact prefixed topics, and loop-relevant subscription design.

## Application entry points

- [MQTTSuite overview](../README.md)
- [MQTTBroker](../mqttbroker/README.md)
- [MQTTIntegrator](../mqttintegrator/README.md)
- [MQTTBridge](../mqttbridge/README.md)
- [MQTTCli](../mqttcli/README.md)
- [MQTTStore](../mqttstore/README.md)

## HTTP and event interfaces

| Application | REST-style HTTP | SSE |
| --- | --- | --- |
| MQTTBroker | yes | yes |
| MQTTIntegrator | yes | no |
| MQTTBridge | yes | yes |

Authentication and exposure differ by application. Use the application-specific HTTP reference rather than assuming one shared security or event model.
