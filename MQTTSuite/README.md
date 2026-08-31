# MQTTSuite

**Five focused MQTT 3.1.1 applications for brokerage, integration, bridging, inspection, and storage.**

MQTTSuite is a C++20 application suite built on [SNode.C](https://github.com/SNodeC/snode.c). Instead of putting every MQTT concern into one process, it provides five independently runnable applications with separate responsibilities. Start with the applications a deployment needs and compose additional roles around the same MQTT infrastructure.

**C++20** · **MQTT 3.1.1** · **MIT OR GPL-3.0-or-later**

**[Run the Broker + CLI quick start](#quick-start-broker-and-cli)** · **[Choose an application](#five-applications-one-suite)** · **[Configure MQTTSuite](docs/configuration.md)** · **[Check evidence and limits](docs/capabilities.md)**

> [!NOTE]
> The MQTTSuite implementation reviewed for this publication is [`52de563`](https://github.com/SNodeC/mqttsuite/commit/52de5631245c6318bfa5b7cca700f0754014f34d). Shared SNode.C behavior was source-reviewed at [`5d6453c`](https://github.com/SNodeC/snode.c/commit/5d6453c21df4894083b445cce00b627e7794932a). Current SNode.C `master` subsequently advanced to `1f872517…` with a documentation-only logging inventory commit; the implementation surface used here is unchanged. The recorded runtime qualification rebuilt and installed MQTTSuite `52de563…` against SNode.C `60f26d9…` on Debian x86-64. Source availability and runtime qualification are kept separate below.

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

From a built source tree, start MQTTBroker:

```bash
./cmake-build-release/mqttbroker/mqttbroker \
  --config-file /dev/null \
  --log-level 4 \
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

The subscriber's current formatter shows the topic and MQTT delivery metadata together with the payload. The qualified run included:

```text
edge-lab/room-01/temperature
QoS: 1
Retain: false
Dup: false
```

and the JSON payload was printed in readable form.

MQTTCli client endpoints are configured to reconnect. A publish-only command disconnects after the MQTT QoS completion path, but the outer client can reconnect and publish again. For an interactive one-shot verification, stop the publisher with `Ctrl-C` after the first intended result, then stop the subscriber and Broker.

This is the suite's baseline first-success proof. It demonstrates a real plain-IPv4 MQTT 3.1.1 QoS 1 message path; it is not evidence for every transport, application, QoS, session, or deployment combination.

> **Figure placeholder — Broker + CLI first success.** Show the real Broker, subscriber, and publisher terminal result for the canonical `edge-lab/room-01/temperature` QoS 1 message; do not synthesize terminal output.

## Build and install

The top-level CMake project builds all five applications. A complete current source workflow needs:

- a C++20 compiler;
- **CMake 3.18 or newer** for the complete MQTTSuite + current SNode.C source workflow;
- an installed SNode.C 2.0.0-compatible development installation with the components requested by MQTTSuite;
- nlohmann/json development support;
- MariaDB client/development support for MQTTStore;
- Git and the MQTTSuite `json-schema-validator` submodule.

MQTTSuite's own top-level [`CMakeLists.txt`](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/CMakeLists.txt) still declares CMake `3.14`, while current SNode.C declares `3.18`. The practical minimum for the documented complete source workflow is therefore 3.18. The mismatch is a project declaration limitation, not a reason to advertise 3.14 as the current whole-suite minimum.

Because the top-level project unconditionally adds `mqttstore`, the normal complete build also pulls in Store's MariaDB dependency. The repository is not currently organized as five independent standalone CMake projects.

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

The documentation workflow built and installed the suite into an isolated prefix. It did **not** separately prove that all five installed executables run from an arbitrary clean custom prefix without runtime-loader assistance. MQTTSuite currently has no explicit install-RPATH/RUNPATH policy establishing that guarantee. Treat clean custom-prefix execution as **UNVERIFIED-RUNTIME** and inspect the installed binaries/loader environment for the deployment you intend to use.

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

> **Figure placeholder — Representative deployment topologies.** Compare local Broker + CLI, normalization, normalized persistence, and broker-domain bridging so a reader can choose the minimum application set for each job.

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

Named endpoint instances expose role-specific sections such as `local`, `remote`, connection/socket/TLS settings, HTTP settings for WebSocket clients, MQTT session settings, and application-specific actions. The `--config-file` option accepts more than one file; when layering files, inspect the resulting state rather than assuming a particular undocumented merge pattern.

Useful inspection and persistence commands include:

```bash
<application> --help=expanded
<application> --show-config
<application> --command-line=standard
<application> --command-line=active
<application> --command-line=complete
<application> --write-config ./application.conf
```

MQTTSuite also uses **domain configuration documents** that are not another SNode.C config section:

| Configuration layer | Owner | Purpose |
| --- | --- | --- |
| SNode.C application configuration | all applications | endpoints, addresses, TLS/HTTP/session/application settings, logging and runtime options |
| mapping JSON | MQTTIntegrator; optional Broker mapper | topic matching and topic/payload transformation |
| bridge-definition JSON | MQTTBridge | logical bridges, broker members, subscriptions, prefixes and sessions |
| projection JSON | MQTTStore | optional typed extraction from topic/JSON data into MariaDB tables |

See the [MQTTSuite configuration reference](docs/configuration.md) for named instances, precedence, multiple config files, `--write-config`, introspection, retry/reconnect, TLS, semantic logging, and daemon/service-facing options.

> **Figure placeholder — Configuration hierarchy and persistence.** Show defaults/config files/CLI converging on a named endpoint hierarchy, then separate that SNode.C configuration from mapping, bridge, and Store projection documents.

## Connection and transport composition

MQTTBroker contains source paths for direct MQTT listeners over IPv4, IPv6, and Unix-domain streams, with TLS variants where built. It also creates HTTP/HTTPS listener families for the dashboard, administration/SSE surface, and MQTT-over-WebSocket upgrades.

MQTTIntegrator, MQTTCli, and MQTTStore contain direct and MQTT-over-WebSocket client paths across IPv4, IPv6, and Unix-domain streams where the corresponding build options are enabled. MQTTCli and MQTTStore create those client instances disabled, so the intended instance is enabled explicitly with `--disabled=false`.

MQTTBridge is narrower. Current runtime selection is source-consistent for IPv4/IPv6 stream and WebSocket members. Its schema also admits Unix-domain, RFCOMM (`rc`), and L2CAP (`l2`) vocabulary, but current runtime dispatch does not support every declared token consistently: direct Unix address handling disagrees with the schema, and there are no `rc`/`l2` runtime branches. Schema/build vocabulary is not a runtime-support claim.

TLS and WSS protect transport when configured correctly. They do not create MQTT authorization or HTTP administration authorization by themselves.

## Mapping: normalize and derive MQTT traffic

MQTTIntegrator subscribes as an MQTT client, matches received publications against a recursive mapping tree, and republishes zero, one, or many mapped messages through the same client connection. MQTTBroker can reuse the same `MqttMapper` in-process.

The mapper provides:

- mapping-derived subscriptions and subscription QoS;
- literal and `+` topic-level matching;
- static message mapping;
- scalar/value templates;
- JSON templates;
- templated output topics;
- fan-out;
- output QoS and retain;
- delayed output;
- suppression values;
- dynamically loaded Inja callback plugins;
- an Integrator admin lifecycle for draft, validate, deploy, history, and rollback.

Two current implementation details matter when operating MQTTIntegrator:

1. **`#` is not MQTT-standard multi-level matching inside the mapper at this revision.** Subscription extraction can produce an MQTT `#` filter, but the mapper's own matching consumes `#` as a one-level candidate. Do not design mappings that rely on normal MQTT remaining-subtree semantics.
2. **The startup mapping source is not simply the default `mapping.json`.** Current `mqttintegrator.cpp` seeds an inline demo mapping during startup; an explicit mapping file supplied through the supported configuration parse can replace it. Select the mapping file explicitly and inspect the active configuration instead of relying on the implicit default.

The administration API currently uses HTTP Basic Authentication with known defaults `admin/admin`, and those credentials are not exposed through a supported application configuration option in the reviewed source. The active mapping can itself contain MQTT credentials.

See the [MQTTIntegrator README](mqttintegrator/README.md) and the deeper [mapping reference](docs/integrator-mapping.md).

> **Figure placeholder — Mapping pipeline.** Show subscribed topic/payload → first matching topic-tree branch → static/value/JSON mapping → rendered output topic/payload → QoS/retain/delay → zero/one/many republishes.

## Bridging: connect broker domains

A logical MQTTBridge owns multiple outbound MQTT client members. Each member supplies a connection/session, subscriptions, and an optional prefix. A publication received from one member is forwarded to the other currently connected members; the immediate source member is excluded.

The forwarded topic is constructed from:

```text
logical bridge prefix
+ source-member prefix
+ destination-member prefix
+ original MQTT topic
```

Payload, incoming QoS, and retain state are preserved by the forwarding path.

`loop_prevention` uses a private SNode.C origin-reflection mechanism. It is not standard MQTT 3.1.1 and does not establish arbitrary cyclic-topology safety, especially with third-party brokers or additional bridge processes. Subscription partitioning and prefix/topology design remain operational responsibilities.

See the [MQTTBridge README](mqttbridge/README.md) for the complete definition shape, transport discrepancies, configuration apply/restart lifecycle, and loop boundaries.

> **Figure placeholder — Logical bridge forwarding.** Show a received publication fanning to every other connected member, the source exclusion, subscription-selected inputs, and the prefix construction order.

## Storage: raw envelope first

MQTTStore subscribes as an MQTT client and writes every received publication to a MariaDB raw-envelope table. The raw row preserves topic, payload, QoS, retain/DUP state, packet identifier representation, source instance, and payload classification.

When the payload is JSON, optional projections can independently insert selected values into operator-managed typed tables. Projection sources can be:

- JSON Pointer;
- zero-based topic level;
- literal value.

MQTTStore creates/ensures its raw table when configured to do so. It does **not** manage projection-table migrations, retention, backup policy, or broader database operations. Raw and projection inserts are separate asynchronous operations rather than one atomic transaction.

Projection configuration is currently loaded from `SocketContextFactory::create()` when an MQTT connection reaches context creation. The exact process/reconnect consequence of a malformed projection file was not separately runtime-qualified; do not claim that validation always occurs before every connection attempt.

See the [MQTTStore README](mqttstore/README.md) for database bootstrap, raw schema, projection examples, and SQL verification.

> **Figure placeholder — Raw envelope and optional projections.** Show every incoming publication producing a raw-envelope insert attempt, with a separate JSON-only branch for zero or more typed projection inserts.

## Practical trust boundaries

The current implementation has several security-sensitive operational surfaces. They are documented as current behavior, not hidden behind a future-fix prerequisite.

- MQTT CONNECT username/password fields do not establish a general MQTTBroker authentication/authorization backend in the reviewed application layer.
- MQTTBroker's dashboard, mutating `/api/mqtt/*` routes, `/api/mqtt/events`, and legacy `/sse` do not apply application-level authentication. `/api/mqtt` and `/api/mqtt/events` use permissive CORS in current source.
- MQTTBroker's client event representation currently includes the supplied MQTT password value, and live client event JSON can also be written through the Broker information log path. Treat event streams and logs as credential-sensitive.
- MQTTIntegrator's admin router uses the known Basic Auth defaults `admin/admin` and can read back credential-bearing mapping state.
- Mapping validation errors can include the full mapping JSON, which may contain credentials.
- MQTTCli and MQTTBridge currently contain debug paths that print configured MQTT password values.
- Mapping files, bridge definitions, saved application configuration, session stores, database configuration, logs, and MQTTStore raw payloads can all contain sensitive data.

Bind administrative listeners to an appropriate trusted interface or place them behind the network/reverse-proxy/firewall controls required by the deployment. TLS is transport protection; it does not repair missing application authorization.

See [MQTTBroker HTTP/event administration](docs/broker-http-api.md) for the current route, CORS, event, replay, payload, and error contract.

## Available versus exercised

The source surface is broader than the runtime proof. Use this distinction when evaluating MQTTSuite:

| Area | Available in the reviewed source | Exercised by the landing-page qualification |
| --- | --- | --- |
| five applications | all five executables and top-level build/install | all five built and installed |
| MQTT protocol | MQTT 3.1.1 client/server paths, QoS/session/retain/will implementation | plain IPv4 Broker + CLI, QoS 1 publish/delivery |
| Broker Web UI | dashboard/SSE/admin/WebSocket route source | real bundled Broker dashboard |
| Integrator mapping | mapper, schema, admin lifecycle, plugins | source-reviewed; no complete mapping fixture in this pass |
| Bridge | logical bridges, forwarding/prefix/session/admin source | source-reviewed; no multi-broker runtime fixture in this pass |
| Store | raw MariaDB storage and typed projection source | source-reviewed; no MariaDB end-to-end fixture in this pass |
| IPv6 / Unix / TLS / WS / WSS | multiple source/configuration paths depending on application/build | not a complete transport matrix |
| custom-prefix installed runtime | install rules exist and installation completed | clean self-resolving installed execution is UNVERIFIED-RUNTIME |

The detailed [capability and evidence boundaries](docs/capabilities.md) record current limitations and explicit non-claims.

This documentation does **not** claim MQTT 5, complete MQTT conformance, equal qualification of every transport combination, arbitrary Bridge cycle safety, automatic database lifecycle management, a stable plugin ABI, performance/footprint characteristics, broad platform support, or production readiness.

## How MQTTSuite is built on SNode.C

This is the secondary perspective, after the application-suite story.

SNode.C supplies endpoint creation, address/transport composition, stream/TLS connection mechanics, HTTP/WebSocket/MQTT protocol contexts, event-driven lifecycle, and hierarchical configuration. MQTTSuite supplies the application behavior attached at the connection/context boundary.

Each application has a `SocketContextFactory` or equivalent runtime assembly seam that turns an established SNode.C connection into the appropriate Broker, Integrator, Bridge, CLI, or Store MQTT behavior. MQTT-over-WebSocket inserts SNode.C HTTP/WebSocket upgrade handling below the same MQTT application role.

The shared mapper is another deliberate extension surface. Mapper plugins expose native Inja callback vectors and are loaded into the process; they should be treated as trusted native code built for the MQTTSuite ABI in use, not as a sandbox or a promised stable cross-version plugin interface.

Source anchors for this secondary perspective include the pinned [Broker factory/application](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttbroker/mqttbroker.cpp), [Integrator startup](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttintegrator/mqttintegrator.cpp), [Bridge runtime](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttbridge/mqttbridge.cpp), [CLI runtime](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttcli/mqttcli.cpp), [Store runtime](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttstore/mqttstore.cpp), and the [shared mapper](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/lib/MqttMapper.cpp).

## Choose your next step

| If you want to… | Go here |
| --- | --- |
| Run or operate the MQTT server role | [MQTTBroker](mqttbroker/README.md) |
| Transform topics or payloads | [MQTTIntegrator](mqttintegrator/README.md) |
| Forward selected traffic between broker domains | [MQTTBridge](mqttbridge/README.md) |
| Publish, subscribe, inspect, or verify a path | [MQTTCli](mqttcli/README.md) |
| Persist raw messages and optional typed projections | [MQTTStore](mqttstore/README.md) |
| Understand shared command/configuration behavior | [Configuration](docs/configuration.md) |
| Design or administer mappings | [Integrator mapping](docs/integrator-mapping.md) |
| Use the Broker HTTP/SSE administration surface | [Broker HTTP/event API](docs/broker-http-api.md) |
| Check exactly what is source-only vs runtime-exercised | [Capabilities and evidence](docs/capabilities.md) |
| Inspect the underlying networking/configuration foundation | [SNode.C](https://github.com/SNodeC/snode.c) |

## License

MQTTSuite is available under:

```text
MIT OR GPL-3.0-or-later
```

See the source repository license files for the full terms.