# MQTTSuite

**Five focused MQTT 3.1.1 applications for brokerage, integration, bridging, inspection, and storage.**

MQTTSuite is a C++20 application suite built on [SNode.C](https://github.com/SNodeC/snode.c). Instead of combining every MQTT concern in one process, it provides five executables with separate responsibilities. Run only the pieces a deployment needs, or compose several of them around the same MQTT infrastructure.

| Application | Use it when you need to… | Detailed README |
| --- | --- | --- |
| **MQTTBroker** | accept MQTT 3.1.1 clients, keep broker/session state, expose a live dashboard, and optionally map publishes in-process | [`mqttbroker/README.md`](mqttbroker/README.md) |
| **MQTTIntegrator** | subscribe, transform topics or payloads, and republish normalized/derived messages | [`mqttintegrator/README.md`](mqttintegrator/README.md) |
| **MQTTBridge** | connect multiple broker domains as MQTT clients and forward selected topics between them | [`mqttbridge/README.md`](mqttbridge/README.md) |
| **MQTTCli** | inspect traffic, publish test messages, subscribe interactively, and verify the other applications | [`mqttcli/README.md`](mqttcli/README.md) |
| **MQTTStore** | persist raw MQTT envelopes in MariaDB and optionally project JSON fields into typed tables | [`mqttstore/README.md`](mqttstore/README.md) |

If you are new to the repository, start with [Build and install](#build-and-install), then run the [Quick Start](#quick-start-broker-and-cli), and use the table above to continue into the application you actually need.

> **Figure placeholder — Five applications, five responsibilities.** Show the five executables around MQTT message flows, emphasizing that they are separate processes that can be composed without forcing all five into one deployment.

## Quick Start: Broker and CLI

The shortest useful MQTTSuite path is one Broker, one subscriber, and one publisher. The example below uses an isolated configuration (`--config-file /dev/null`) and port `18885` so it does not depend on previously saved settings or a conventional broker on `1883`.

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

The subscriber should print a publish for:

```text
edge-lab/room-01/temperature
QoS: 1
Retain: false
Dup: false
```

and display the JSON payload in readable form.

The current CLI connection path is configured to reconnect. For a one-shot publisher, stop it with `Ctrl-C` after the first successful result if it reconnects; then stop the subscriber and broker cleanly with `Ctrl-C`.

This exact Broker + CLI path is the suite's baseline first-success example. It proves a real MQTT 3.1.1 message path; it is not intended to demonstrate every transport variant or deployment mode.

## Build and install

### Prerequisites

The top-level CMake project builds the complete suite. A current whole-suite build requires:

- a C++20 compiler;
- CMake 3.14 or newer;
- an installed SNode.C 2.0.0-compatible development installation with the components requested by the five applications;
- `nlohmann_json` 3.7.0 or newer;
- MariaDB client/development support through the SNode.C `db-mariadb` component required by MQTTStore;
- Git, including recursive checkout of the repository submodules.

MQTTSuite vendors its JSON-schema validator as a submodule. Clone recursively; a checkout without submodules is incomplete for the current build.

Because the top-level project unconditionally adds all five application directories, the default whole-suite build also includes MQTTStore and therefore its database dependency. The repository is not currently structured as five independent standalone CMake projects.

### Clone, configure, build

```bash
git clone --recurse-submodules https://github.com/SNodeC/mqttsuite.git

cmake -S mqttsuite \
      -B mqttsuite/cmake-build-release \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_INSTALL_PREFIX=/usr/local

cmake --build mqttsuite/cmake-build-release --parallel
```

### Install

```bash
sudo cmake --install mqttsuite/cmake-build-release
```

With the prefix above, the executable install set is:

```text
/usr/local/bin/mqttbroker
/usr/local/bin/mqttintegrator
/usr/local/bin/mqttbridge
/usr/local/bin/mqttcli
/usr/local/bin/mqttstore
```

MQTTBroker and MQTTBridge also install their repository Web assets below the selected prefix:

```text
/usr/local/var/www/mqttsuite/mqttbroker
/usr/local/var/www/mqttsuite/mqttbridge
```

The exact prefix is yours to choose; the paths above simply follow the example `CMAKE_INSTALL_PREFIX`.

### Build-time connection families

The application CMake files expose options for IPv4, IPv6, Unix-domain stream connections, TLS variants, WebSocket, and WSS. These options decide which SNode.C components and connection paths are compiled into each executable.

The source contains those connection families for Broker, Integrator, CLI, and Store. Bridge definition/runtime selection is narrower: current IPv4/IPv6 stream and WebSocket branches are source-consistent, while its Unix-domain and additional schema tokens have implementation discrepancies documented in the Bridge README. The Quick Start above is the qualified plain IPv4 path; treat the broader source inventory as implemented/configurable paths, not as a claim that every combination has been exercised by the same runtime check.

## Why five applications?

MQTTSuite separates concerns that often change on different schedules.

**Brokerage** is about accepting MQTT sessions, subscriptions, retained messages, and routing publishes. **Integration** is about transforming the meaning or shape of MQTT traffic. **Bridging** is about moving selected traffic between broker domains without becoming another broker. **Inspection** is about making those flows visible and testable from a terminal. **Storage** is about recording messages and extracting query-friendly data.

That separation leads to useful combinations without requiring a monolith:

- develop locally with **MQTTBroker + MQTTCli**;
- normalize vendor/device topics with **MQTTBroker + MQTTIntegrator**;
- persist normalized telemetry with **MQTTIntegrator + MQTTStore**;
- connect broker domains with **MQTTBridge**;
- test any of those paths with **MQTTCli**.

> **Figure placeholder — Representative deployment topologies.** Compare several small deployments—local Broker + CLI, normalization, persistence, and broker-domain bridging—and answer which executable belongs in each message path.

## How MQTTSuite extends SNode.C

MQTTSuite is also a concrete example of turning SNode.C's networking composition into complete applications.

SNode.C supplies the endpoint, transport, socket connection, protocol context, and configuration machinery. Each MQTTSuite application supplies a `SocketContextFactory` that turns an established SNode.C `SocketConnection` into an MQTT `SocketContext` with application-specific MQTT behavior.

The Broker factory is representative:

```cpp
return new iot::mqtt::SocketContext(
    socketConnection,
    new mqtt::mqttbroker::lib::Mqtt(
        socketConnection->getConnectionName(), broker, mqttMapper));
```

MQTTIntegrator uses the same seam but injects its mapper and persistent session-store path:

```cpp
return new iot::mqtt::SocketContext(
    socketConnection,
    new mqtt::mqttintegrator::lib::Mqtt(
        socketConnection->getConnectionName(),
        config->getMqttMapper(),
        config->getSessionStore()));
```

MQTTCli and MQTTStore read their connection instance's `session`, `sub`, and application-specific subcommands before constructing their MQTT behavior. MQTTBridge looks up the logical bridge member represented by the connection instance and injects that member into its MQTT client behavior.

The important pattern is:

**SNode.C provides endpoint, transport, protocol and configuration composition; MQTTSuite supplies application-specific MQTT behavior and deployment composition.**

> **Figure placeholder — From SNode.C endpoint to MQTTSuite behavior.** Show endpoint/transport → established `SocketConnection` → application `SocketContextFactory` → MQTT `SocketContext` → Broker/Integrator/Bridge/CLI/Store behavior.

### Direct MQTT and MQTT over WebSocket

The application behavior does not need to become a different application just because the transport stack changes.

A direct path is conceptually:

```text
TCP / Unix stream
  -> SNode.C socket connection
  -> MQTT SocketContext
  -> MQTTSuite MQTT behavior
```

A WebSocket path inserts SNode.C HTTP and WebSocket composition before the MQTT subprotocol:

```text
TCP / Unix stream
  -> HTTP client/server
  -> WebSocket upgrade ("mqtt" subprotocol)
  -> MQTT SocketContext
  -> MQTTSuite MQTT behavior
```

MQTTCli and MQTTStore make the WebSocket request target configurable through `http --target` and default it to `/ws`. MQTTIntegrator and MQTTBridge currently request `/ws`. MQTTBroker accepts the `mqtt` WebSocket subprotocol on `/ws`, `/mqtt`, and `/` through its HTTP router.

> **Figure placeholder — Direct MQTT versus MQTT-over-WebSocket.** Place the two stacks side by side and make clear that transport/upgrade composition changes while the MQTT application behavior remains above it.

## The shared configuration model

SNode.C gives the suite a hierarchical command/configuration model. It is worth understanding once because the same grammar appears throughout Broker, Integrator, CLI, and Store.

A typical client command has this shape:

```text
mqttcli
  in-mqtt
    remote --host 127.0.0.1 --port 1883
    session --client-id inspector --qos 1
    sub --topic sensors/#
```

Read it from left to right:

1. `mqttcli` is the application.
2. `in-mqtt` is a named connection instance.
3. `remote` configures that connection's peer address.
4. `session` configures MQTT CONNECT/session behavior.
5. `sub` or `pub` configures what the CLI should do after connection.

Server applications use analogous instance sections such as `local` for listener addresses. WebSocket clients add an `http` section. Application-specific sections add mapper, bridge, database, or storage behavior where appropriate.

> **Figure placeholder — Configuration hierarchy and persistence.** Show application → named connection instance → address/transport section → MQTT session → application action, then show the same values flowing into a saved configuration file.

### Defaults, configuration files, and command-line values

SNode.C can obtain configurable values from defaults/API configuration, a configuration file, and the command line. For values present in more than one source, the current SNode.C model gives command-line values precedence over configuration-file values, which in turn override API/default values.

For isolated experiments, `--config-file /dev/null` avoids inheriting saved configuration. For repeatable services, the opposite workflow is useful: get one command right, then write it as configuration.

### Persist a known-good command

The root option `-w` / `--write-config` writes the resolved configurable state and exits. You can optionally provide an explicit output file.

For example, after adapting the CLI command to your broker:

```bash
mqttcli \
  --config-file /dev/null \
  in-mqtt --disabled=false \
    remote --host 127.0.0.1 --port 1883 \
    session --client-id inspector --qos 1 \
    sub --topic sensors/# \
  --write-config ./mqttcli.conf
```

Then reuse it:

```bash
mqttcli --config-file ./mqttcli.conf
```

Use the same pattern for service-style Broker, Integrator, and Store configurations: verify an explicit command first, persist it, review the generated file, and then start from the saved configuration.

### Three different kinds of configuration

Do not treat every JSON or config file in MQTTSuite as the same layer:

| Configuration | Owned by | Purpose |
| --- | --- | --- |
| SNode.C application configuration | all applications | connection instances, addresses, TLS/HTTP/session/application options, logging, daemon/service settings |
| MQTT mapping JSON | MQTTIntegrator and optional Broker mapper | topic matching, transformation, output topics/payloads, QoS/retain/delay, plugins |
| MQTTBridge definition JSON | MQTTBridge | logical bridges, broker members, network composition, subscriptions, forwarding prefixes |
| MQTTStore projection JSON | MQTTStore | optional extraction of JSON/topic values into typed MariaDB tables |

The application READMEs document the domain-specific files in depth.

## Connection and transport composition

### Broker listeners

A default-feature Broker build has source paths for these MQTT listener families:

| Instance | Meaning | Default port/path behavior |
| --- | --- | --- |
| `in-mqtt` | MQTT over plain IPv4 stream | `1883` |
| `in-mqtts` | MQTT over TLS/IPv4 stream | `8883` |
| `in6-mqtt` | MQTT over plain IPv6 stream | `1883` |
| `in6-mqtts` | MQTT over TLS/IPv6 stream | `8883` |
| `un-mqtt` | MQTT over Unix-domain stream | application/instance socket path |
| `un-mqtts` | MQTT over TLS over Unix-domain stream | application/instance socket path |

The same Broker process also creates HTTP/HTTPS server instances for its dashboard, API, SSE, and MQTT WebSocket upgrades: `in-http`, `in-https`, `in6-http`, `in6-https`, `un-http`, and `un-https`. The IPv4/IPv6 defaults are `8080` for plain HTTP and `8088` for HTTPS.

### Client connection families

MQTTIntegrator, MQTTCli, and MQTTStore contain direct and WebSocket client paths across IPv4, IPv6, and Unix-domain streams. MQTTCli and MQTTStore expose the following instance names when their build options are enabled:

```text
in-mqtt       in-mqtts
in6-mqtt      in6-mqtts
un-mqtt       un-mqtts
in-wsmqtt     in-wsmqtts
in6-wsmqtt    in6-wsmqtts
un-wsmqtt     un-wsmqtts
```

For CLI and Store, those client instances are created disabled and you enable the one you want with `--disabled=false`.

MQTTBridge chooses its client stack from each broker member's definition. The current source has consistent IPv4/IPv6 runtime branches for direct stream and WebSocket transports, with plain/TLS selection where compiled. Its Bridge README records the schema/runtime mismatches that prevent treating every declared protocol token as a runnable path.

### TLS is transport protection, not application authorization

Choosing an `*-mqtts`, `*-https`, or `*-wsmqtts` path changes transport protection. It does not, by itself, create MQTT authorization or protect an administrative route from an authenticated-but-overprivileged user. Configure SNode.C's TLS trust/certificate settings for the selected connection and separately apply the access controls appropriate to the application surface.

## Mapping: normalize and derive MQTT traffic

Mapping is MQTTSuite's transformation model. MQTTIntegrator owns it as a standalone service; MQTTBroker can optionally use the same shared mapper in-process.

A mapping document describes:

- MQTT client connection metadata used by the mapper;
- a recursive topic tree;
- subscription points and subscription QoS;
- `static`, `value`, and `json` mapping rules;
- output topic, payload, QoS, retain, and optional delay;
- suppressions for template output;
- optional dynamically loaded mapper plugins.

A minimal static rule can turn an event payload into a command:

```json
{
  "mapping": {
    "topic_level": {
      "name": "devices",
      "topic_level": {
        "name": "button",
        "subscription": {
          "qos": 1,
          "static": {
            "mapped_topic": "actuators/light/set",
            "message_mapping": [
              { "message": "pressed", "mapped_message": "on" },
              { "message": "released", "mapped_message": "off" }
            ]
          }
        }
      }
    }
  }
}
```

The same topic tree can use `+` and `#`, render scalar or JSON payloads through INJA templates, render output topics, emit multiple outputs from one subscription, delay an output, suppress selected rendered payloads, and call registered plugin callbacks.

> **Figure placeholder — Mapping pipeline.** Show subscribed topic/payload → topic-tree match → static/value/JSON rule → rendered topic/payload → QoS/retain/delay → republish, including one-to-many fan-out.

Continue with the [MQTTIntegrator README](mqttintegrator/README.md) for a complete operational mapping walkthrough and the admin mapping lifecycle.

## Bridging: connect broker domains without mapping payloads

MQTTBridge is a client-side bridge. A logical bridge contains two or more broker client members. Each member defines:

- how to connect;
- its MQTT session values;
- which topics it subscribes to and at what QoS;
- an optional forwarding prefix.

When one member receives a subscribed publish, MQTTBridge forwards it to the other connected members. The payload, QoS, and retain flag are preserved. The outgoing topic is constructed from the logical bridge prefix, the source-member prefix, the destination-member prefix, and the original topic.

MQTTBridge therefore can look integration-like when prefixes and subscription selection reshape where traffic appears, but it is not MQTTIntegrator: it does not execute `MqttMapper`, parse/transform payloads, or render mapping templates.

The bridge excludes the immediate source member from forwarding. It also has an optional private origin-reflection mechanism intended for cooperating SNode.C MQTT endpoints. That mechanism is not a standard MQTT 3.1.1 loop-prevention feature and should not be treated as a universal cycle detector for arbitrary multi-bridge topologies.

> **Figure placeholder — Logical bridge forwarding.** Show two or three broker members, source-member exclusion, subscribed inputs, and the exact prefix order used to construct each forwarded topic.

Continue with the [MQTTBridge README](mqttbridge/README.md) for the bridge-definition schema, examples, apply/restart lifecycle, and loop boundaries.

## Storage: raw envelope first, typed projections second

MQTTStore is an MQTT client backed by MariaDB. Its default model is intentionally loss-minimizing:

1. receive a subscribed MQTT publish;
2. store the raw MQTT envelope in a MariaDB table;
3. classify the payload as JSON, text, or binary;
4. keep a text representation when appropriate;
5. keep a parsed JSON representation when parsing succeeds;
6. independently attempt any matching optional typed projections.

Raw storage is not conditional on a projection succeeding. Projection tables are domain schemas and are not auto-created by MQTTStore; the operator/DBA owns those tables and migrations.

A projection can combine values from:

- an RFC 6901 JSON Pointer such as `/value`;
- a zero-based MQTT `topic_level`;
- a literal constant.

> **Figure placeholder — Raw envelope and optional projections.** Show one incoming publish always producing a raw row, then a separate JSON-only branch extracting typed fields into zero or more operator-managed projection tables.

Continue with the [MQTTStore README](mqttstore/README.md) for database bootstrap, raw table fields, projection examples, and SQL verification.

## Deployment patterns

### Local development and inspection

```text
MQTTCli <-> MQTTBroker <-> MQTTCli
```

Use this to establish transport, topic, QoS, and retained-message behavior before adding transformations or storage.

### Edge normalization

```text
devices -> MQTTBroker <-> MQTTIntegrator
                         |
                         +-> normalized/... topics
```

MQTTIntegrator subscribes to device/vendor topics and republishes a normalized namespace on the same MQTT connection.

### Normalized persistence

```text
devices -> Broker -> Integrator -> normalized topics -> MQTTStore -> MariaDB
```

Keep raw MQTT envelopes in Store even when projections are enabled. Let Integrator own semantic normalization and Store own persistence.

### Broker-domain interconnection

```text
Broker A <-> MQTTBridge <-> Broker B
```

Use Bridge when the messages should remain messages and only selected topic domains need to cross broker boundaries. Use Integrator when payload/topic transformation is the real requirement.

### Encrypted remote link

Select the appropriate TLS or WSS connection instance for the client application and configure the corresponding SNode.C TLS section. Keep application credentials and administrative exposure decisions separate from the encryption choice.

### Browser or WebSocket MQTT clients

MQTTBroker's HTTP(S) server also accepts MQTT WebSocket upgrades using the `mqtt` subprotocol. This lets browser/WebSocket MQTT clients share the Broker process's HTTP transport surface.

### Same-host local IPC

For processes on the same host, the Unix-domain MQTT and MQTT-over-WebSocket paths avoid binding a TCP listener. Configure the client's `remote --sun-path` to the Broker's corresponding Unix listener path and enable only the instances you need.

## Practical trust boundaries

MQTTSuite exposes powerful operational surfaces. Deploy them deliberately.

- MQTT username/password fields are MQTT CONNECT data. In the current Broker source, their presence does not establish a general broker-side authentication/authorization backend.
- TLS/WSS protects a transport when configured correctly; it is not a substitute for application authorization.
- MQTTBroker's dashboard and mutating `/api/mqtt/*` operations share its HTTP router and do not add an application-level authentication layer in the reviewed source. Bind or filter that surface according to your trust boundary.
- MQTTIntegrator's mapping admin API uses HTTP Basic Authentication with current default credentials `admin` / `admin`; replace defaults and avoid exposing it as though those defaults were a remote-management policy.
- MQTTBridge's configuration API can expose and persist definition content that may contain credentials. Its current debug logging also prints member credential values.
- Mapping files, bridge definitions, saved application configuration, and MQTT session-store files can contain operational or credential material; protect them with appropriate filesystem ownership and permissions.
- MQTTStore intentionally persists raw payloads. Database access, backups, retention, and deletion policy belong to the operator.

For diagnostics, prefer increasing the relevant application-origin/component logging scope rather than globally emitting every framework detail. Review logs before sharing them because current application debug paths can contain connection metadata or secrets.

## Where to continue

- [MQTTBroker](mqttbroker/README.md): listeners, broker state, Web dashboard/API/SSE, embedded mapper, verification.
- [MQTTIntegrator](mqttintegrator/README.md): mapping files, templates, plugins, admin draft/validate/deploy/history/rollback lifecycle.
- [MQTTBridge](mqttbridge/README.md): logical bridge definitions, forwarding, prefixes, restart/apply behavior, loop limitations.
- [MQTTCli](mqttcli/README.md): command patterns for subscription, publication, sessions, transports, and verification.
- [MQTTStore](mqttstore/README.md): MariaDB bootstrap, raw envelopes, projections, SQL verification, operational ownership.

For framework-level endpoint, configuration, TLS, HTTP, WebSocket, MQTT, and logging details, continue with the [SNode.C repository](https://github.com/SNodeC/snode.c).

## License

MQTTSuite is available under:

```text
MIT OR GPL-3.0-or-later
```

See the repository license files for the full terms.
