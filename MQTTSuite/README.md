# MQTTSuite

**Five focused MQTT 3.1.1 applications for brokerage, integration, bridging, inspection, and storage.**

MQTTSuite is a C++20 application suite built on [SNode.C](https://github.com/SNodeC/snode.c). Instead of putting every MQTT concern into one process, it provides five independently runnable applications with separate responsibilities. Start with the applications a deployment needs and compose additional roles around the same MQTT infrastructure.

**C++20** · **MQTT 3.1.1** · **Project version 1.0.1** · **MIT OR GPL-3.0-or-later**

The latest published GitHub release is [`v1.0.1`](https://github.com/SNodeC/mqttsuite/releases/tag/v1.0.1), published 7 March 2025. Current `master` contains later development than that release.

**[Run the Broker + CLI quick start](#quick-start-broker-and-cli)** · **[Choose an application](#five-applications-one-suite)** · **[Configure MQTTSuite](docs/configuration.md)** · **[Browse reference docs](docs/README.md)** · **[Check capabilities and limits](docs/capabilities.md)**

## Five applications, one suite

| Application | Use it when you need to… | Detailed README |
| --- | --- | --- |
| **MQTTBroker** · `mqttbroker` | accept MQTT 3.1.1 clients, own broker/session state, expose the bundled dashboard, and optionally map publishes in-process | [`mqttbroker/README.md`](mqttbroker/README.md) |
| **MQTTIntegrator** · `mqttintegrator` | subscribe, transform topics or payloads, and republish normalized or derived messages | [`mqttintegrator/README.md`](mqttintegrator/README.md) |
| **MQTTBridge** · `mqttbridge` | connect multiple broker domains as MQTT clients and forward selected traffic between them | [`mqttbridge/README.md`](mqttbridge/README.md) |
| **MQTTCli** · `mqttcli` | publish, subscribe, inspect traffic, and verify the other applications from a terminal | [`mqttcli/README.md`](mqttcli/README.md) |
| **MQTTStore** · `mqttstore` | persist raw MQTT envelopes in MariaDB and optionally project JSON/topic values into typed tables | [`mqttstore/README.md`](mqttstore/README.md) |

The applications are separate processes. MQTTBroker is not the whole product, MQTTBridge is not another broker, and MQTTIntegrator is not a general-purpose stream-processing platform.

> **Figure placeholder — Five applications, five responsibilities.** Show one representative MQTT message around the five applications, making brokerage, transformation, forwarding, inspection, and persistence visually distinct while preserving the separate-process boundaries.

## Quick Start: Broker and CLI

The shortest useful MQTTSuite path is one Broker, one subscriber, and one publisher. The commands below use an isolated configuration and port `18885`, so they do not depend on an existing user configuration or a conventional broker on `1883`.

Start MQTTBroker:

```bash
./cmake-build-release/mqttbroker/mqttbroker \
  --config-file /dev/null \
  --log-level 5 \
  in-mqtt local --host 127.0.0.1 --port 18885 \
  in-mqtts --disabled \
  in6-mqtt --disabled \
  in6-mqtts --disabled \
  un-mqtt --disabled \
  un-mqtts --disabled \
  in-http --disabled \
  in-https --disabled \
  in6-http --disabled \
  in6-https --disabled \
  un-http --disabled \
  un-https --disabled
```

In a second terminal, subscribe at QoS 1:

```bash
./cmake-build-release/mqttcli/mqttcli \
  --config-file /dev/null \
  --log-level 4 \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 18885 \
    session --client-id landing-subscriber --qos 1 \
    sub --topic edge-lab/room-01/temperature
```

In a third terminal, publish one JSON value at QoS 1:

```bash
./cmake-build-release/mqttcli/mqttcli \
  --config-file /dev/null \
  --log-level 4 \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 18885 \
    session --client-id landing-publisher --qos 1 \
    pub --topic edge-lab/room-01/temperature \
        --message '{"value":21.7,"unit":"C"}'
```

The subscriber prints the topic together with QoS/retain/dup metadata and the payload. JSON payloads are pretty-printed. A real captured result from this scenario is available in [`assets/src/first-success/subscriber-raw.png`](assets/src/first-success/subscriber-raw.png).

MQTTCli client endpoints reconnect. For an interactive one-shot verification, stop the publisher with `Ctrl-C` after the first intended result.

> **Figure placeholder — Broker + CLI first success.** Show the real Broker, subscriber, and publisher terminal result for the canonical `edge-lab/room-01/temperature` QoS 1 message.

## Build and install

The top-level CMake project builds all five applications. A complete current source workflow needs:

- a C++20 compiler;
- **CMake 3.18 or newer** for the complete MQTTSuite + current SNode.C source workflow;
- an installed SNode.C 2.0.0-compatible development installation with the components requested by MQTTSuite;
- **nlohmann/json 3.11 or newer** for the complete current SNode.C + MQTTSuite workflow; MQTTSuite itself declares `3.7.0` in `lib/CMakeLists.txt`, while the current SNode.C MQTT component requires `3.11+`;
- MariaDB client/development support for MQTTStore;
- Git and the MQTTSuite `json-schema-validator` submodule.

MQTTSuite's own top-level CMake file still declares CMake `3.14`; current SNode.C requires `3.18`, so `3.18+` is the practical minimum for the documented complete source workflow.

Clone recursively and configure against an installed SNode.C prefix:

```bash
git clone --recurse-submodules https://github.com/SNodeC/mqttsuite.git

cmake -S mqttsuite \
      -B mqttsuite/cmake-build-release \
      -G Ninja \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_PREFIX_PATH=/path/to/snodec-install \
      -DCMAKE_INSTALL_PREFIX=/usr/local

cmake --build mqttsuite/cmake-build-release --parallel
```

Install:

```bash
sudo cmake --install mqttsuite/cmake-build-release
```

With `/usr/local` as the prefix, the executable install set is:

```text
/usr/local/bin/mqttbroker
/usr/local/bin/mqttintegrator
/usr/local/bin/mqttbridge
/usr/local/bin/mqttcli
/usr/local/bin/mqttstore
```

MQTTBroker and MQTTBridge also install Web assets below:

```text
/usr/local/var/www/mqttsuite/mqttbroker
/usr/local/var/www/mqttsuite/mqttbridge
```

For non-standard install prefixes, verify the runtime library search path in the target deployment. See [Capabilities and evidence](docs/capabilities.md) for the exact qualification boundary.

## Why the applications stay separate

MQTTSuite separates concerns that often change, fail, scale, or get operated independently.

**Brokerage** owns MQTT sessions, subscriptions, retained state, and publish routing. **Integration** changes topic/payload contracts. **Bridging** moves selected traffic between broker domains. **Inspection** makes message paths observable and testable from a terminal. **Storage** records messages and optionally extracts query-friendly data.

Useful combinations include:

```text
Local development
MQTTCli <-> MQTTBroker <-> MQTTCli

Normalization
Devices -> MQTTBroker <-> MQTTIntegrator
                         -> normalized/... topics

Normalized persistence
Devices -> MQTTBroker <-> MQTTIntegrator -> normalized topics -> MQTTStore -> MariaDB

Broker-domain interconnection
Broker A <-> MQTTBridge <-> Broker B
```

Use Integrator when the contract of a message should change. Use Bridge when selected MQTT traffic should cross broker boundaries while remaining MQTT traffic.

## Shared configuration model

MQTTSuite inherits SNode.C's hierarchical configuration model. A typical client command reads left-to-right:

```text
mqttcli
  in-mqtt
    remote --host 127.0.0.1 --port 1883
    session --client-id inspector --qos 1
    sub --topic sensors/#
```

The effective configurable value follows this precedence:

```text
API / compiled default < configuration file < command line
```

Useful inspection and persistence commands include:

```bash
<application> --help=expanded
<application> --show-config
<application> --command-line=active
<application> --write-config ./application.conf
```

MQTTSuite also uses domain configuration documents that are separate from the SNode.C application configuration:

| Configuration layer | Owner | Purpose |
| --- | --- | --- |
| SNode.C application configuration | all applications | endpoints, addresses, TLS/HTTP/session/application settings, logging and runtime options |
| mapping JSON | MQTTIntegrator; optional Broker mapper | topic matching and topic/payload transformation |
| bridge-definition JSON | MQTTBridge | logical bridges, broker members, subscriptions, prefixes and sessions |
| projection JSON | MQTTStore | optional typed extraction from topic/JSON data into MariaDB tables |

See the [configuration reference](docs/configuration.md) for named instances, client defaults, persistence, retry/reconnect, TLS, logging, and application-local admin listener names.

> **Figure placeholder — Configuration hierarchy and persistence.** Show defaults/config files/CLI converging on a named endpoint hierarchy, then separate that SNode.C configuration from mapping, bridge, and Store projection documents.

## Connection and transport composition

MQTTBroker provides direct MQTT listeners and HTTP/HTTPS listener families for the dashboard, administration/SSE, and MQTT-over-WebSocket upgrades.

MQTTIntegrator, MQTTCli, and MQTTStore provide direct and MQTT-over-WebSocket client paths across the SNode.C connection families compiled into the application. MQTTCli and MQTTStore create their client instances disabled, so the intended instance is enabled explicitly with `--disabled=false`.

MQTTBridge uses the transport selected by each bridge member. Its detailed transport support and current schema/runtime limitations are documented in the [MQTTBridge README](mqttbridge/README.md).

TLS and WSS protect transport when configured correctly. They do not create MQTT authorization or HTTP administration authorization by themselves.

## Mapping: normalize and derive MQTT traffic

MQTTIntegrator subscribes as an MQTT client, matches publications against a mapping tree, and republishes zero, one, or many mapped messages. MQTTBroker can reuse the same mapper in-process.

The mapping system supports literal topic matching, MQTT `+`/`#` wildcards, static/value/JSON mappings, templated output topics and payloads, fan-out, output QoS/retain, delay, suppressions, and mapper plugins.

MQTTIntegrator also exposes a draft/validate/deploy/history/rollback administration API. Its current Basic Auth defaults are `admin/admin` and are not configurable through the application in this revision, so protect the admin listener with deployment-specific network/access controls.

See the [MQTTIntegrator README](mqttintegrator/README.md), [mapping reference](docs/integrator-mapping.md), [sibling topic example](docs/integrator-sibling-topics-example.md), and [Integrator HTTP API](docs/integrator-http-api.md).

## Bridging: connect broker domains

A logical MQTTBridge owns multiple outbound MQTT client members. Each member supplies a connection/session, subscriptions, and an optional prefix. A publication received from one member is forwarded to the other currently connected members; the immediate source member is excluded.

The forwarded topic is constructed from:

```text
bridge prefix
+ source-member prefix
+ destination-member prefix
+ original topic
```

Payload, QoS, and retain are preserved.

Bridge is a forwarding application, not a mapper. Loops must be controlled through topology/subscription design; the optional private `loop_prevention` mechanism is not a general MQTT loop-proofing guarantee.

See the [MQTTBridge README](mqttbridge/README.md), [complete three-broker example](docs/bridge-multi-broker-example.md), and [Bridge HTTP API and SSE](docs/bridge-http-api.md).

> **Figure placeholder — Logical bridge forwarding.** Show one message entering a logical bridge member, source exclusion, forwarding to peer members, and the prefix order used to construct each destination topic.

## Inspection: verify paths with MQTTCli

MQTTCli is the suite's direct verification tool. It can subscribe, publish, or do both on one selected client connection.

A typical use is to subscribe to the expected output first, then publish one known input. Both subscription filters and publication topics support a trailing `##<qos>` override when a topic needs a QoS different from the session default.

See the [MQTTCli README](mqttcli/README.md) for session options, direct/TLS/WebSocket/Unix-domain examples, QoS overrides, output formatting, and reconnect behavior.

## Storage: raw envelope first

MQTTStore subscribes as an MQTT client and writes every received publication to MariaDB as a raw envelope. It can additionally project selected topic/JSON values into operator-managed typed tables.

Raw storage preserves the original topic, payload, QoS, retain/dup state, and packet identifier representation independently from the optional projection layer.

A typical pipeline is:

```text
device topics
  -> MQTTIntegrator (optional normalization)
  -> normalized/... topics
  -> MQTTStore
  -> raw MQTT table
  -> optional typed projections
```

See the [MQTTStore README](mqttstore/README.md) for database bootstrap, raw-table schema, payload classification, permissions, projections, and verification.

> **Figure placeholder — Raw envelope and optional projections.** Show every received MQTT publication going to the raw table, with valid JSON optionally feeding one or more typed projection tables independently.

## Trust and deployment boundaries

MQTTSuite is deliberately explicit about the current trust model:

- **MQTTBroker:** the dashboard/admin/SSE surfaces do not add application authentication in the current source; protect them with a trusted network boundary or external access control.
- **MQTTIntegrator:** the admin API uses fixed source-known `admin/admin` credentials in this revision; do not expose it as a public management endpoint.
- **MQTTBridge:** the configuration/admin surface has no application authentication in the current source; bridge definitions can contain MQTT credentials.
- **MQTTCli / MQTTBridge:** debug logging can include configured credentials.
- **Configuration/state files:** mapping, bridge, session-store, database and saved application configuration can contain sensitive operational data.

TLS protects transport; it is not a substitute for application authorization.

For exact source/runtime qualification boundaries and explicit non-claims, see [Capabilities and evidence](docs/capabilities.md).

## Documentation map

| Need | Go to |
| --- | --- |
| Choose an application / build the suite | this README |
| Operate MQTTBroker | [MQTTBroker](mqttbroker/README.md) |
| Transform MQTT traffic | [MQTTIntegrator](mqttintegrator/README.md) |
| Forward between broker domains | [MQTTBridge](mqttbridge/README.md) |
| Publish / subscribe / inspect | [MQTTCli](mqttcli/README.md) |
| Persist to MariaDB | [MQTTStore](mqttstore/README.md) |
| Understand shared configuration | [Configuration](docs/configuration.md) |
| Design mappings | [Integrator mapping](docs/integrator-mapping.md) |
| Use Broker administration/SSE | [Broker HTTP API and SSE](docs/broker-http-api.md) |
| Use Integrator administration | [Integrator HTTP API](docs/integrator-http-api.md) |
| Use Bridge administration/SSE | [Bridge HTTP API and SSE](docs/bridge-http-api.md) |
| Check support/evidence boundaries | [Capabilities and evidence](docs/capabilities.md) |

## License

MQTTSuite is available under:

```text
MIT OR GPL-3.0-or-later
```

See the source repository license files for the full terms.
