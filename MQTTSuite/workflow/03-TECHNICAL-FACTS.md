# Step 3 — MQTTSuite technical facts

**Review date:** 30 August 2026  
**Workflow stage:** Step 3 — Technical Truth  
**Public MQTTSuite baseline:** `SNodeC/mqttsuite` `master`/`HEAD` at [`52de5631245c6318bfa5b7cca700f0754014f34d`](https://github.com/SNodeC/mqttsuite/commit/52de5631245c6318bfa5b7cca700f0754014f34d)  
**Current SNode.C baseline:** `SNodeC/snode.c` `master`/`HEAD` at [`60f26d9ae54b3e9ffde954d0ca75e53f79f31d79`](https://github.com/SNodeC/snode.c/commit/60f26d9ae54b3e9ffde954d0ca75e53f79f31d79)  
**Last runtime-qualified SNode.C dependency:** [`bf01683a53b48220a840522e8ccaf3b48e58c240`](https://github.com/SNodeC/snode.c/commit/bf01683a53b48220a840522e8ccaf3b48e58c240)  
**OpenWrt package-source baseline:** `SNodeC/OpenWRT` `main` at tree/HEAD [`c9378fe95f7c015752c748fc4ab012b585d294d1`](https://github.com/SNodeC/OpenWRT)

This document is the self-contained technical handoff for later MQTTSuite README design, visual qualification, writing, validation and publication. Repository source and recorded qualification evidence, not chat history, control all later technical claims.

The workflow targets current public `master`/`HEAD`. Historical releases and package metadata are recorded because they matter to availability and installation, but they do **not** replace current public heads as the technical truth baseline.

Existing Landingpages READMEs, proposals, figures and screenshots remain research inputs only. Where they conflict with the evidence boundaries below, this file controls later MQTTSuite work.

## Evidence vocabulary

- **Current-head source-verified** — directly established by current MQTTSuite and/or SNode.C source at the SHAs above.
- **Runtime-qualified** — reproduced by the existing isolated landing-page qualification with recorded commands and visible output.
- **Carried forward by source-delta review** — prior runtime evidence remains relevant because the source changes since that run do not touch the consumed implementation surface. This is not a fresh current-head rerun.
- **Package-source verified** — packaging definitions or install scripts exist in current public source, without implying that a feed/package was built, published or executed successfully.
- **Runtime-pending** — implemented in source but not reproduced by the landing-page qualification.
- **Open** — current evidence is insufficient for a public claim.

## 1. Current-head status and dependency compatibility

MQTTSuite `master` is unchanged from the 28 August application qualification baseline at `52de563...`. Its top-level CMake build adds all five application directories and requires C++20.

SNode.C advanced after that MQTTSuite runtime run from `bf01683...` to `60f26d9...`. The exact comparison is:

<https://github.com/SNodeC/snode.c/compare/bf01683a53b48220a840522e8ccaf3b48e58c240...60f26d9ae54b3e9ffde954d0ca75e53f79f31d79>

The five intervening SNode.C commits add/document the external echo example, its tests and CI wiring. They do not change the MQTTSuite-consumed MQTT, networking, HTTP/WebSocket, MariaDB, configuration or exported component implementation. Therefore the earlier MQTTSuite broker/CLI runtime proof can be carried forward by source-delta review to the current dependency surface. It remains **not a fresh run against SNode.C `60f26d9...`**.

Current SNode.C HEAD has one CI run for `60f26d9...`, run `33293707417`, and that run concludes **failure** at the newly added external-echo validation path. The failure is outside the MQTTSuite-consumed source delta reviewed above, but later ecosystem copy must not claim that all current public heads are green.

MQTTSuite itself has no application build/test CI job and no MQTTSuite test directory on current master. Its current workflows:

- update the README table of contents when the README changes; and
- create/upload a source archive when a GitHub release is published.

Runtime statements below therefore come from explicit landing-page qualification, not MQTTSuite CI.

## 2. Canonical project identity

MQTTSuite is a toolkit of **five independently runnable MQTT applications**, not one monolithic daemon and not five modes of a single executable.

| Application | Executable | Exact role | Primary boundary |
| --- | --- | --- | --- |
| **MQTTBroker** | `mqttbroker` | MQTT broker/server with bundled browser dashboard and optional in-process mapping | accepts MQTT clients and distributes publications |
| **MQTTIntegrator** | `mqttintegrator` | MQTT client integration process that subscribes, transforms and republishes | subscribed input → mapping → republished output |
| **MQTTBridge** | `mqttbridge` | group of outbound MQTT client connections forwarding selected broker traffic | configured brokers grouped into logical bridges |
| **MQTTCli** | `mqttcli` | terminal MQTT client for publishing, subscribing and inspecting messages | one selected MQTT client transport/session |
| **MQTTStore** | `mqttstore` | MQTT subscriber persisting raw message envelopes and optional typed JSON projections to MariaDB | MQTT subscription → storage plan → MariaDB |

The current top-level `CMakeLists.txt` unconditionally adds `mqttbroker`, `mqttintegrator`, `mqttbridge`, `mqttcli` and `mqttstore`.

A safe architectural relationship model is:

```text
publishers / devices
        │
        ▼
   MQTTBroker  ◄──────────── MQTTCli
        │                     publish / subscribe / inspect
        ├──────────────► MQTTIntegrator ── map + republish ──► MQTT
        │
        ├──────────────► MQTTStore ─────────────────────────► MariaDB
        │
        └──────────────► MQTTBridge ────────────────────────► other brokers
```

This is a role/composition model, **not** evidence that all five applications have been executed together. Only the broker/CLI path is currently runtime-qualified by the landing-page evidence.

## 3. MQTT protocol scope

### Safe current-head claim

MQTTSuite targets **MQTT 3.1.1** through SNode.C's MQTT implementation.

Current SNode.C uses MQTT protocol name `MQTT` and protocol level `0x04` for ordinary MQTT 3.1.1 connections. The server CONNECT path validates the protocol name and, after masking the private reflection bit described under MQTTBridge, requires protocol level 4.

Relevant current SNode.C source includes:

- `src/iot/mqtt/packets/Connect.{h,cpp}`;
- `src/iot/mqtt/server/packets/Connect.cpp`;
- `src/iot/mqtt/client/Mqtt.cpp`;
- `src/iot/mqtt/server/Mqtt.cpp`;
- `src/iot/mqtt/server/broker/Broker.cpp`;
- `src/iot/mqtt/server/broker/Session.cpp`;
- `src/iot/mqtt/server/broker/SubscriptionTree.cpp`.

Current source contains CONNECT, PUBLISH, QoS acknowledgement flows, SUBSCRIBE/UNSUBSCRIBE, PING and DISCONNECT handling. The broker implementation also contains retained-message state, persistent-session state, subscription matching and offline QoS 1/2 queues.

### Runtime boundary

The public runtime proof is deliberately narrower: one plain-IPv4 broker/subscriber/publisher exchange at QoS 1.

For later wording:

- **Runtime-qualified:** CONNECT + subscribe + publish + delivered QoS 1 message in the documented local scenario.
- **Current-head source-verified, runtime-pending here:** QoS 2 paths, retained messages, wills, persistent-session recovery, offline queues and `+`/`#` subscription matching.
- **Not eligible:** `full MQTT`, complete MQTT conformance, MQTT 5 support, or a claim that all MQTT feature combinations are tested.

MQTT username/password fields are supported in client CONNECT construction. The reviewed SNode.C broker CONNECT path parses and stores supplied credentials but does not invoke a credential-verification backend. Therefore **do not describe MQTTBroker as authenticating MQTT usernames/passwords** on the basis of these fields alone.

## 4. MQTTBroker

### Role

MQTTBroker is the server-side application. It accepts MQTT client connections, owns the broker/session/subscription/retained-message model through SNode.C, exposes the bundled browser-facing broker dashboard, and can optionally execute the shared mapping engine inside the broker process.

### Source transport surface

Current `mqttbroker/CMakeLists.txt` exposes build options for:

- IPv4 direct MQTT stream;
- IPv4 direct MQTT over TLS;
- IPv6 direct MQTT stream;
- IPv6 direct MQTT over TLS;
- Unix-domain direct MQTT stream;
- Unix-domain direct MQTT over TLS;
- MQTT over WebSocket and WSS through corresponding HTTP/HTTPS server surfaces.

The broker WebSocket upgrade requires the `mqtt` WebSocket subprotocol. Current routes `/ws`, `/mqtt` and `/` can accept that upgrade.

These are **source implementation paths**, not a tested transport matrix. Only the plain IPv4 MQTT listener is runtime-qualified in the principal first-success scenario.

### Bundled Web UI

The broker dashboard is a genuine current-master product surface. Current source installs HTML/CSS/JavaScript from `mqttbroker/html/` below the broker web root and routes `/clients` to the dashboard.

The current broker router exposes live/event and mutating HTTP endpoints including:

- `GET /api/mqtt/events` — SSE event stream;
- `GET /sse` — SSE event stream;
- `POST /api/mqtt/disconnect` — close a selected client connection;
- `POST /api/mqtt/unsubscribe` — remove a selected client subscription;
- `POST /api/mqtt/release` — publish an empty retained value for a topic;
- `POST /api/mqtt/subscribe` — add a subscription for a selected connected client.

The existing Landingpages broker screenshot was captured from the real MQTTSuite `52de563...` dashboard with synthetic client/topic state. Since MQTTSuite HEAD has not moved, that visible dashboard state remains current-MQTTSuite-HEAD runtime evidence. It does **not** prove every mutating dashboard/API action.

### Broker HTTP security boundary

The `/api/mqtt` middleware sets permissive CORS including `Access-Control-Allow-Origin: *`. No application-level Basic Authentication middleware appears in the reviewed broker router, while the API can disconnect clients and mutate subscriptions/retained state.

Therefore:

- treat the broker HTTP surface as an administrative/trusted-network surface unless separately protected;
- TLS encrypts a listener but does not provide authorization by itself;
- do not call the dashboard/API authenticated or remote-safe without additional evidence;
- do not infer MQTT client authentication from username/password CONNECT fields.

### Embedded mapping

`mqttbroker/lib/Mqtt.cpp` receives a shared `MqttMapper`. For each incoming publication it updates the broker model, then—when a mapper is present—derives immediate and delayed mapped publications and republishes those outputs through the same broker.

This is in-process mapper behavior, **not** a hidden `mqttintegrator` child process. It is source-verified; the canonical mapped-message scenario remains runtime-pending.

## 5. MQTTIntegrator

### Role

MQTTIntegrator is an outbound MQTT client integration process. It derives MQTT subscriptions from mapping configuration, receives matching publications, transforms them and republishes immediate or delayed mapped outputs.

`mqttintegrator/lib/Mqtt.cpp` establishes the lifecycle:

1. on socket connection, send CONNECT using mapping connection settings;
2. after an accepted CONNACK with no existing session, subscribe to mapper-derived topics;
3. on PUBLISH, derive immediate and scheduled mappings;
4. publish immediate outputs and timer-schedule delayed outputs;
5. on mapping update, reconnect if connection settings changed, otherwise hot subscribe/unsubscribe the delta.

### Source transport surface

Current source instantiates client roles for:

- IPv4, IPv6 and Unix-domain direct MQTT streams;
- plain and TLS variants;
- MQTT over WS/WSS for IPv4, IPv6 and Unix-domain HTTP clients.

These are source paths, not an application support matrix.

### Mapping administration API

MQTTIntegrator creates IPv4 HTTP and HTTPS administration servers and uses the shared `MappingAdminRouter`. That router provides mapping schema/config/history, validation, replace/PATCH, deploy and rollback operations.

The router applies SNode.C `BasicAuthentication`. Current defaults in `MappingAdminRouter.h` are:

```text
user = admin
pass = admin
realm = mqttsuite-admin
```

This is a development/default credential boundary, not a security guarantee. Public/deployed use must replace/protect those credentials and explicitly decide bind/TLS/exposure policy.

### Portable UI limitation

Current `MappingAdminRouter.cpp` serves `/ui` from this hard-coded maintainer-local absolute path:

```text
/home/voc/tmp/integrator/mqtt-integrator-ui/dist/mqtt-integrator-ui/browser
```

No corresponding packaged MQTTIntegrator UI artifact is present in current MQTTSuite source. Therefore:

- the mapping admin API is real current-head functionality;
- a portable installed/shipped MQTTIntegrator Web UI is **not established** by current master;
- do not use an integrator UI screenshot as shipped-product proof until that packaging/path boundary is corrected and qualified.

## 6. Mapping semantics

The shared mapping engine is defined by `lib/mapping-schema.json`, `MqttMapper`, `JsonMappingReader` and the plugin interface. MQTTIntegrator uses it directly; MQTTBroker can use the same mapper in process.

### Topic matching and subscriptions

The schema describes a hierarchical topic tree. Current mapper source recognizes literal topic levels plus `+` and `#` names and derives MQTT subscriptions from the configured tree. Treat this as source-level wildcard behavior, not exhaustive MQTT wildcard conformance evidence.

### Three mapping modes

**Static mapping** compares the incoming MQTT payload string against configured `message` values. A match emits `mapped_message` to `mapped_topic`.

**Value-template mapping** exposes the incoming payload as a scalar string in the template context and renders configured topic/message templates.

**JSON-template mapping** parses the incoming payload as JSON and exposes the parsed value to the template context. Invalid JSON does not produce a JSON-template mapping.

Mapped output definitions can specify:

- `mapped_topic`;
- output QoS 0–2;
- retain flag;
- delay (`-1` default for immediate; non-negative values schedule output);
- suppressions for template mappings.

Template rendering uses embedded Inja. Dynamically loaded mapper plugins can register additional template callbacks.

### Mapping connection/security boundary

The mapping `connection` object includes MQTT client ID, keepalive, clean session, will fields, username and password. Mapping administration can write draft/history/current mapping files to the filesystem. Those files can therefore contain credentials.

Treat mapping configuration/history as credential-bearing state. No encrypted secret-store abstraction is established by current MQTTSuite source.

### Evidence boundary

Mapping behavior is current-head source-verified. No deterministic end-to-end mapping run is part of the existing landing-page runtime qualification. Step 5 must execute a real input → mapped output scenario before a figure/output is labelled as runtime proof.

## 7. MQTTBridge

### Role and logical-bridge model

MQTTBridge is **not** a broker. It creates outbound MQTT client connections to configured brokers and groups them into named logical bridges.

Each configured broker member can define:

- network endpoint;
- MQTT client ID, keepalive and clean-session settings;
- will settings;
- username/password;
- client session-store file;
- subscriptions with QoS;
- broker prefix;
- `loop_prevention` flag;
- disabled state.

On accepted CONNACK, the client joins its logical bridge and subscribes to its configured topics. Traffic selection is therefore primarily expressed as MQTT subscriptions on each source broker connection.

### Exact forwarding behavior

When one broker member receives a PUBLISH, `Bridge::publish()` forwards it to every **other connected member** in the same logical bridge and does not send it immediately back over the origin connection.

The outgoing topic is constructed as:

```text
bridge prefix
+ origin-broker prefix
+ destination-broker prefix
+ original MQTT topic
```

The bridge forwarding step carries payload, QoS and retain flag through unchanged.

Do not describe MQTTBridge as a payload transformation engine. Mapping/transformation belongs to MQTTIntegrator/the shared mapper. Also do not invent a separate arbitrary bridge-filter language beyond the configured MQTT subscriptions and prefixes present in source.

### Loop prevention: two bounded mechanisms

Two mechanisms exist and must not be collapsed into “loops are solved”:

1. **Within a logical bridge**, the process never immediately forwards a received message back through the exact connection from which it arrived.
2. A per-broker `loop_prevention=true` setting is passed into SNode.C's MQTT CONNECT packet construction.

The second mechanism is a private extension. Current SNode.C sets the high bit of the MQTT protocol-level byte (`0x84` instead of ordinary `0x04`). Its own server deserializer interprets this bit as “do not reflect messages to origin”, masks it and then validates the remaining protocol level as MQTT 3.1.1. Broker-session delivery suppresses reflection to the origin client when reflection is disabled.

This is **not standard MQTT 3.1.1 behavior**. It cannot be assumed to interoperate with arbitrary third-party brokers and it does not establish safety for arbitrary cyclic broker topologies.

Safe later wording: MQTTSuite provides explicit origin-reflection suppression mechanisms; cyclic topologies and third-party broker behavior require topology-specific qualification.

### Bridge admin/status surface

Current `mqttbridge` source exposes a configuration/status HTTP surface including:

- active bridge configuration retrieval;
- PATCH/stage/validate/apply behavior that can restart bridge connections and persist configuration;
- lifecycle/status SSE at `/api/bridge/sse`;
- bundled static configuration UI under `/config`.

Current source creates IPv4 plain/TLS admin HTTP servers. No application-level Basic Authentication middleware is established for this bridge router.

This is security-relevant because active bridge configuration contains broker credentials and the API can modify live behavior.

### Bridge credential/logging boundary

Current bridge code persists active bridge JSON and its debug logging prints broker username, broker password, will message, address and other configuration values.

Therefore:

- bridge definition files are credential-bearing state;
- debug logs can contain secrets;
- qualification screenshots must use synthetic/no credentials and be reviewed for log output as well as command lines;
- remote admin exposure requires an explicit external trust/authentication boundary.

### Bluetooth schema mismatch — current-head defect

Current `mqttbridge/lib/bridge-schema.json` accepts network protocols:

```text
in, in6, rc, l2, un
```

including Bluetooth RFCOMM (`rc`) and L2CAP (`l2`). However, current `mqttbridge` executable code only includes/instantiates IPv4, IPv6 and Unix-domain client paths with their stream/TLS and WebSocket variants. `mqttbridge/CMakeLists.txt` has no MQTTSuite bridge RFCOMM/L2CAP build option; it only names SNode.C Bluetooth components as optional components.

**Conclusion:** RFCOMM/L2CAP MQTTBridge operation is not established by current MQTTSuite master. The schema is broader than the executable implementation. A schema-valid Bluetooth bridge definition is not proof that the executable can create that connection.

Any Landingpages claim instructing users to enable MQTTSuite RFCOMM/L2CAP targets is stale/unsupported and must be removed or corrected.

## 8. MQTTCli

### Role

MQTTCli is the terminal MQTT client and the correct tool for the shortest visible first success. One enabled client instance can publish, subscribe or do both. Received-message output includes topic, payload, QoS, retain and duplicate state; JSON payloads are pretty-printed when parsing succeeds.

### Source transport surface

Current source instantiates:

- `in-mqtt`, `in-mqtts`;
- `in6-mqtt`, `in6-mqtts`;
- `un-mqtt`, `un-mqtts`;
- `in-wsmqtt`, `in-wsmqtts`;
- `in6-wsmqtt`, `in6-wsmqtts`;
- `un-wsmqtt`, `un-wsmqtts`.

WebSocket clients use subprotocol `mqtt` and default target `/ws`.

Session configuration includes client ID, QoS 0–2, persistent-session selection, keepalive, will, username and password. Topic strings can carry the application's `##<qos>` suffix to override default QoS; publication also supports retain.

### CLI security boundary

Current debug logging can print MQTT username/password and will data. Public terminal captures must use synthetic/no credentials and inspect logs before publication.

## 9. MQTTStore

### Role

MQTTStore is an outbound MQTT subscriber that writes received publications to MariaDB. Its key architectural distinction is **raw MQTT envelope first, optional typed projections second**.

### MQTT/client source surface

Current executable provides the same IPv4, IPv6 and Unix-domain direct/TLS plus WS/WSS client family as MQTTCli. It has configurable client ID, default subscription QoS, persistent-session choice, keepalive, will, username/password and session-store path. Subscription strings can use `topic##qos` to override the default QoS.

### Raw envelope

For every received PUBLISH, `mqttstore/lib/Mqtt.cpp` constructs a record containing:

- source connection name;
- MQTT topic;
- original payload;
- QoS;
- retain flag;
- DUP flag;
- packet identifier.

`MariaDbStorage::store()` always attempts the configured raw-table insert first. Current auto-create support can create a raw table containing receive timestamp, source instance, topic, QoS, retain/DUP, packet identifier, raw payload, text representation, JSON representation and `json|text|binary` payload-format marker.

JSON parsing changes the derived representation and projection eligibility; it does not replace the raw storage path.

### Typed projections

Typed projection inserts are attempted **only when the payload parses as JSON**. Projection definitions target an operator-defined table and can derive columns from:

- RFC 6901 JSON Pointer;
- zero-based MQTT topic level;
- literal string.

A projection includes an MQTT topic filter. Current `StoragePlan` matching supports literal levels, `+`, and terminal `#` wildcard behavior.

Only the raw table has source support for automatic creation. Projection tables are application/domain schemas and are not auto-created or migrated by MQTTStore.

### MariaDB/security/ownership boundaries

Current configuration exposes database host, username, password, database, TCP port, Unix socket and flags. Credentials are ordinary configuration values, not secret-store handles.

No current-head evidence establishes:

- projection-table migration policy;
- retention/expiry policy;
- database backup policy;
- atomicity between raw and projection inserts;
- retry/failure guarantees across database loss;
- supported MariaDB version matrix.

Raw payloads are persisted unredacted. Database schema lifecycle, retention, access control, backup and data classification remain operator responsibilities.

The repository's `docs/mqttstore-user-guide.md` contains useful setup guidance, but its phrase “production pipeline” is documentation prose, not production-readiness evidence. Do not promote it into a public maturity claim.

## 10. Source transport inventory — not a support matrix

| Application | MQTT role | Direct MQTT source paths | MQTT-over-WebSocket source paths | HTTP/admin surface |
| --- | --- | --- | --- | --- |
| MQTTBroker | server | IPv4, IPv6, Unix; plain/TLS | WS/WSS via IPv4, IPv6 and Unix HTTP(S) servers | broker dashboard/API/SSE |
| MQTTIntegrator | client | IPv4, IPv6, Unix; plain/TLS | WS/WSS via IPv4, IPv6 and Unix HTTP clients | mapping admin IPv4 HTTP/HTTPS, BasicAuth |
| MQTTBridge | outbound client group | IPv4, IPv6, Unix; plain/TLS | WS/WSS via IPv4, IPv6 and Unix HTTP clients | bridge config/status IPv4 HTTP/HTTPS; no app auth established |
| MQTTCli | client | IPv4, IPv6, Unix; plain/TLS | WS/WSS via IPv4, IPv6 and Unix HTTP clients | none |
| MQTTStore | client | IPv4, IPv6, Unix; plain/TLS | WS/WSS via IPv4, IPv6 and Unix HTTP clients | none |

Do not label this table `supported` or `tested`. The principal runtime proof is plain IPv4 MQTTBroker + MQTTCli. TLS, WSS, IPv6, Unix-domain and every per-application combination remain runtime-pending.

Do not add Bluetooth to this matrix on current master. The bridge schema's `rc`/`l2` entries are not backed by current executable connection paths.

## 11. Shortest real broker/subscriber/publisher first success

The shortest **already runtime-qualified** MQTTSuite evaluation path is one local MQTTBroker listener plus two MQTTCli processes: subscriber and publisher.

The run used current MQTTSuite HEAD `52de563...` with SNode.C `bf01683...`. Source-delta review establishes no MQTTSuite-consumed SNode.C changes between `bf01683...` and current `60f26d9...`, but Step 5 should still rerun this exact path against then-current heads before capturing final terminal imagery.

### Terminal 1 — broker

```sh
./cmake-build-release/mqttbroker/mqttbroker --config-file /dev/null --log-level 4 \
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

This intentionally leaves only one loopback IPv4 MQTT listener active.

### Terminal 2 — subscriber

```sh
./cmake-build-release/mqttcli/mqttcli --config-file /dev/null --log-level 4 \
  in-mqtt --disabled=false remote --host 127.0.0.1 --port 18885 \
  session --client-id landing-subscriber --qos 1 \
  sub --topic edge-lab/room-01/temperature
```

### Terminal 3 — publisher

```sh
./cmake-build-release/mqttcli/mqttcli --config-file /dev/null --log-level 4 \
  in-mqtt --disabled=false remote --host 127.0.0.1 --port 18885 \
  session --client-id landing-publisher --qos 1 \
  pub --topic edge-lab/room-01/temperature \
      --message '{"value":21.7,"unit":"C"}'
```

### Observed success

The subscriber printed the topic, pretty-printed JSON payload, `QoS: 1`, `Retain: false` and duplicate state. Ctrl-C teardown was clean.

This is the public first-success candidate. Do not substitute a shorter but unexecuted command merely for presentation convenience.

## 12. Build and dependency facts

Current source establishes:

- CMake minimum `3.14`;
- C++20 required;
- `nlohmann_json` version floor `3.7.0`;
- recursive `lib/json-schema-validator` submodule;
- installed SNode.C package;
- application CMake requests `snodec 2.0.0` as a package-version floor for the relevant components, **not** as an exact release/tag dependency;
- SNode.C MQTT, networking, TLS, HTTP/Express and WebSocket components according to enabled application options;
- SNode.C `db-mariadb` for MQTTStore, making MariaDB client development support part of a complete all-five-app build;
- embedded Inja mapping/template implementation;
- Git for cloning/submodules, not as an application runtime dependency.

The publication technical baseline remains current SNode.C `master`/`HEAD`, independent of package-version metadata.

Transport options default on broadly for IPv4, IPv6, Unix, TLS and WebSocket families, so a complete default build expects the corresponding SNode.C components.

Doxygen/Graphviz, IWYU, clang-format, cmake-format, js-beautify and Prettier are documentation/maintainer tooling, not core application runtime dependencies.

## 13. Release and source-distribution scope

### GitHub release state

The latest public GitHub release is **`v1.0.1`**, published 7 March 2025. Its tag resolves to commit:

```text
0138b1c5a4bd95c5c586a6be26c18aa50b9f300e
```

The release workflow publishes a source archive named `mqttsuite.tar.gz` including submodules.

Current master `52de563...` is **560 commits ahead** of `v1.0.1`. Current top-level CMake still reports project version `1.0.1`, so the version string does not identify the current technical state or the qualified source revision.

Safe later wording:

- a historical `v1.0.1` GitHub release and source archive exist;
- this workflow documents and qualifies current public master instead;
- do not present `v1.0.1` as equivalent to current master or as the source of current five-application behavior without separate release qualification.

### Current-master install surface

Current master contains CMake build/install rules for all five executables, their libraries and the MQTTBroker/MQTTBridge web assets. This establishes a source build/install surface.

No current-head evidence establishes a binary release, distribution repository, container image or broad package-manager publication corresponding exactly to `52de563...`.

## 14. OpenWrt package evidence and boundary

OpenWrt is **not merely hypothetical**, but the available package source is not equivalent to current MQTTSuite master and must be described precisely.

### MQTTSuite install helper

Current `SNodeC/mqttsuite` contains `misc/owrt-install`. The script:

- adds an external `vchrist` opkg feed selected by architecture;
- installs a signing key from `SNodeC/OpenWRT`;
- removes a potentially installed Mosquitto package;
- installs `mqttsuite-full`.

This proves an intended installation path. It does **not** prove that the external feed currently resolves, that every architecture is built, or that a package install/run is currently qualified.

### Public package source

The separate public `SNodeC/OpenWRT` repository contains `net/mqttsuite/Config.in`, `net/mqttsuite/Makefile` and init scripts for MQTTBroker, MQTTIntegrator and MQTTBridge.

At the reviewed `SNodeC/OpenWRT` `main` state, `net/mqttsuite/Makefile` declares:

```text
PKG_NAME:=mqttsuite
PKG_VERSION:=1.0.0
PKG_RELEASE:=4
PKG_SOURCE_URL:=https://github.com/SNodeC/mqttsuite
PKG_SOURCE_VERSION:=OpenWRT
```

`PKG_SOURCE_VERSION:=OpenWRT` resolves to the MQTTSuite tag:

```text
OpenWRT -> 24b601818dcb650f28e35ede35a41e6cf6bc573b
```

That tag is from 9 June 2026 and current MQTTSuite master is six commits ahead. The six-commit delta includes changes across mapping, broker, bridge, CLI, store and semantic logging source, so the OpenWrt package source is **not current master**.

### Package contents are incomplete relative to the five-app suite

The OpenWrt package definitions build:

- `mqttsuite-broker`;
- `mqttsuite-integrator`;
- `mqttsuite-bridge`;
- `mqttsuite-cli`;
- virtual `mqttsuite-full` pulling those four packages.

**MQTTStore is not packaged and is not part of `mqttsuite-full`.** This is a material mismatch with the current five-application suite identity.

Therefore safe publication wording is limited to:

> Public OpenWrt packaging source exists for a four-application package set tied to the `OpenWRT` MQTTSuite tag, but it is not current-master five-application qualification.

Do **not** claim:

- current-master OpenWrt support;
- a complete five-application OpenWrt package;
- a tested architecture matrix;
- current feed availability;
- OpenWrt release parity with current master.

If OpenWrt is to become a prominent README install path, Step 5 or a dedicated qualification must update/verify the package source, include MQTTStore if intended, identify the exact OpenWrt version/target/architecture, install from a clean system and execute at least the first-success scenario.

## 15. Platform boundary

The recorded current-MQTTSuite qualification environment is:

- Debian GNU/Linux forky/sid;
- x86-64;
- GCC 16.2.0;
- CMake 4.3.4;
- Ninja 1.13.2.

All five executables compiled in that environment and the broker/CLI first-success path ran.

That is one qualified environment, not a platform support matrix. Current MQTTSuite has no application CI matrix proving compiler/distribution/architecture coverage.

OpenWrt package source exists as documented above, but current-master OpenWrt runtime is not qualified. ARM, Raspberry Pi and Android/Termux remain open as publication support claims unless separate current evidence is supplied.

## 16. Security, credential and state boundaries

| Surface | Current-head fact | Safe interpretation |
| --- | --- | --- |
| MQTTBroker MQTT credentials | username/password fields are parsed/stored, no credential-verification backend established | do not claim MQTT broker authentication |
| MQTTBroker Web API | mutating endpoints, permissive CORS, no app BasicAuth found | trusted/admin surface; TLS is not authorization |
| MQTTIntegrator admin | BasicAuth exists; defaults `admin` / `admin`; HTTP/HTTPS source listeners | authentication exists but defaults require replacement/protection |
| Mapping files/history | can contain MQTT username/password | credential-bearing filesystem state |
| MQTTBridge admin | config retrieval + live PATCH/restart/persist behavior; no app BasicAuth established | protect externally; do not expose casually |
| MQTTBridge config/logs | credentials in config; debug output can print username/password/will/address | files/logs can contain secrets |
| MQTTCli logs | debug output can print MQTT username/password/will | captures/logs can contain secrets |
| MQTTStore config | MQTT and MariaDB credentials are ordinary strings | no secret-store abstraction established |
| MQTTStore data | raw payload persisted unredacted | DB access/retention/classification operator-owned |
| MQTT/SNode.C session stores | filesystem-backed state | no encryption/managed lifecycle claim |

No `secure`, `production-ready`, remote-safe, secret-managed or zero-trust claim is justified by current evidence.

## 17. Genuine differentiators eligible for later design/writing

The strongest technically credible differentiators are:

1. **Five focused applications around one MQTT domain.** Brokerage, terminal inspection, transformation, cross-broker forwarding and persistence are separate executable responsibilities.
2. **One mapping engine in two useful forms.** The same schema/template mapper powers standalone MQTTIntegrator behavior and optional in-process MQTTBroker mapping.
3. **Concrete mapping semantics.** Static payload mapping, scalar/JSON templates, mapped topics, QoS/retain selection, delayed output and dynamically loaded template callbacks are explicit source capabilities.
4. **A bridge built from outbound MQTT clients.** Logical bridge membership, source subscriptions, prefixes, session settings and connection lifecycle are explicit rather than hidden behind another broker role.
5. **Raw-envelope-first storage.** MQTTStore preserves MQTT metadata/original payload first and only then derives optional typed JSON projections.
6. **A real broker operations UI.** The browser dashboard is backed by the live broker model/SSE/API and has genuine current-MQTTSuite-HEAD capture evidence.
7. **Broad source-level transport composition through SNode.C.** This can support the architecture story, but because most combinations are not runtime-qualified it should remain secondary to the five application/message-flow narrative.

Do not use `lightweight`, `fast`, `small footprint`, `full`, `complete`, `secure` or `production-ready` as differentiators without separate evidence.

## 18. Stale, contradictory or unsupported Landingpages claims

Later work must correct or qualify these items rather than copy existing material mechanically:

1. **Tag/release/version as current technical dependency baseline** — incorrect for this workflow. Current public MQTTSuite and SNode.C heads are the technical baseline; CMake version numbers/releases are availability metadata.
2. **“Enable MQTTSuite RFCOMM/L2CAP targets after rebuilding SNode.C with Bluetooth”** — unsupported. Bridge schema accepts `rc`/`l2`, but current executable has no corresponding MQTTSuite connection path/build target.
3. **Broker Web UI evidence contradiction** — existing Landingpages text both shows genuine current-head capture and later says evidence does not extend to Web UI. Correct boundary: dashboard load/visible synthetic state is runtime-qualified; complete mutating API behavior is not.
4. **Broker authentication wording** — do not imply a selectable built-in credential backend. Client credentials can be sent/parsed; broker credential verification was not established.
5. **All-five-app executed integration flow** — unsupported. The roles compose coherently, but mapping, bridge and database arrows remain runtime-pending.
6. **MQTTIntegrator Web UI as a shipped portable surface** — unsupported because current source points to a maintainer-local absolute build directory with no packaged UI artifact.
7. **Generic loop-prevention guarantee** — too broad. Distinguish same-connection suppression from the private SNode.C protocol-level extension; qualify topology/third-party behavior separately.
8. **Broad ARM/Raspberry Pi/Android platform support** — unsupported by current application build/test evidence.
9. **Broad current-master OpenWrt support** — unsupported. Public packaging source exists, but it targets the `OpenWRT` tag, is six commits behind current master and excludes MQTTStore from `mqttsuite-full`.
10. **`lightweight` positioning** — present in historical/source description strings but not backed by current footprint/performance measurement.
11. **`full MQTT`, MQTT 5, complete conformance, production readiness or universal transport support** — unsupported.
12. **“Credentials supported” without role qualification** — client applications can send credentials; that is different from MQTTBroker authenticating them.
13. **Bridge config/admin as harmless monitoring** — false boundary. It can return/persist credential-bearing config and modify/restart live bridge connections.
14. **MQTTStore user-guide “production pipeline” wording as maturity evidence** — unsupported; treat it as descriptive documentation only.
15. **`mqttsuite-full` as the five-application suite on OpenWrt** — false in current package source; it pulls Broker, Integrator, Bridge and CLI only.

## 19. Open facts and runtime gaps

These remain explicit after Step 3 and should be resolved only if later publication work needs the corresponding claim/visual:

- fresh broker/CLI first-success rerun against both then-current MQTTSuite and SNode.C heads;
- one deterministic MQTTIntegrator mapping run proving input → mapped output;
- two-or-more-broker MQTTBridge run proving subscriptions, exact prefix composition and restart behavior;
- third-party-broker qualification for the private loop-prevention extension;
- MQTTStore run against disposable MariaDB proving raw envelope + one typed projection;
- MQTTStore database-loss, restart, malformed-payload, migration and retention boundaries;
- per-application IPv6, Unix, TLS, WS and WSS runtime matrix;
- QoS 2, will, retained-publication, persistent-session-recovery and wildcard acceptance scenarios;
- exact bind/exposure defaults and hardened deployment guidance for broker/integrator/bridge admin listeners;
- broad compiler/distribution/architecture support matrix;
- dedicated MQTTSuite application build/test CI;
- resolution of current SNode.C external-echo CI failure before any “all current heads green” ecosystem claim;
- portable packaging/removal of the MQTTIntegrator UI route;
- correction of MQTTBridge `rc`/`l2` schema/executable mismatch;
- current-master OpenWrt package qualification, including an explicit decision about MQTTStore;
- current external opkg feed availability/target matrix;
- license prose correction described below.

## 20. License fact

Current MQTTSuite `LICENSE` starts with:

```text
SPDX-License-Identifier: MIT OR GPL-3.0-or-later
```

and the repository contains full MIT and GPL-3.0-or-later license files. However, prose in `LICENSE` incorrectly describes the second option as LGPL and refers to “GNU LGPL” while the SPDX expression/file name say GPL.

Later public copy should use **`MIT OR GPL-3.0-or-later`** as the source-of-truth expression and must not reproduce the stale LGPL prose.

The separate OpenWrt package source currently records `GPL-3.0-or-later` for its package metadata. That packaging metadata must not be used to rewrite the upstream MQTTSuite dual-license expression.

## 21. Step 4 handoff constraints

Step 4 can proceed without reopening ordinary source if it preserves these constraints:

- narrative center: five applications and their real MQTT/message/integration responsibilities;
- principal runtime proof: local MQTTBroker + MQTTCli subscriber/publisher QoS 1 path;
- strongest product visual: genuine MQTTBroker browser dashboard;
- integration figure may show Broker → Integrator / Bridge / Store relationships, but mapped/bridged/stored outputs remain architecture/source truth until runtime-qualified;
- MQTT 3.1.1 explicit near the top; no MQTT 5/full-conformance language;
- transport inventory described as source implementation, not tested support matrix;
- no Bluetooth MQTTSuite transport claim on current master;
- loop prevention described as bounded mechanisms including a private/non-standard SNode.C extension;
- raw envelope versus typed projection is the correct MQTTStore distinction;
- broker/bridge admin surfaces and credential-bearing files/logs receive explicit trust boundaries;
- MQTTIntegrator portable Web UI claim remains blocked;
- historical `v1.0.1` and OpenWrt packaging may be mentioned only with their exact staleness/completeness boundaries;
- OpenWrt `mqttsuite-full` must not be presented as the current five-application suite;
- omit rather than broaden unresolved facts.

## 22. Primary evidence index

### MQTTSuite current HEAD

- Commit: <https://github.com/SNodeC/mqttsuite/commit/52de5631245c6318bfa5b7cca700f0754014f34d>
- Top-level build/version: `CMakeLists.txt`
- Shared mapper: `lib/MqttMapper.{h,cpp}`, `lib/mapping-schema.json`
- Mapping admin: `lib/MappingAdminRouter.{h,cpp}`, `lib/ConfigApplication.{h,cpp}`, `lib/JsonMappingReader.{h,cpp}`
- MQTTBroker: `mqttbroker/CMakeLists.txt`, `mqttbroker/mqttbroker.cpp`, `mqttbroker/lib/Mqtt.cpp`, `mqttbroker/html/`
- MQTTIntegrator: `mqttintegrator/CMakeLists.txt`, `mqttintegrator/mqttintegrator.cpp`, `mqttintegrator/lib/Mqtt.cpp`
- MQTTBridge: `mqttbridge/CMakeLists.txt`, `mqttbridge/mqttbridge.cpp`, `mqttbridge/lib/{Bridge,Broker,Mqtt,BridgeStore,SSEDistributor}.*`, `mqttbridge/lib/bridge-schema.json`, `mqttbridge/html/`
- MQTTCli: `mqttcli/CMakeLists.txt`, `mqttcli/mqttcli.cpp`, `mqttcli/lib/{ConfigSections,Mqtt}.*`
- MQTTStore: `mqttstore/CMakeLists.txt`, `mqttstore/mqttstore.cpp`, `mqttstore/lib/{ConfigSections,MariaDbStorage,Mqtt,MqttMessage,StoragePlan}.*`, `mqttstore/lib/projection-schema.json`, `docs/mqttstore-user-guide.md`
- OpenWrt install helper: `misc/owrt-install`
- CI/release automation: `.github/workflows/main.yml`, `.github/workflows/release-with-submodules.yml`
- License: `LICENSE`, `LICENSE-MIT`, `LICENSE-GPL-3.0-or-later`

### SNode.C current HEAD

- Commit: <https://github.com/SNodeC/snode.c/commit/60f26d9ae54b3e9ffde954d0ca75e53f79f31d79>
- Delta from runtime baseline: <https://github.com/SNodeC/snode.c/compare/bf01683a53b48220a840522e8ccaf3b48e58c240...60f26d9ae54b3e9ffde954d0ca75e53f79f31d79>
- Current CI run: <https://github.com/SNodeC/snode.c/actions/runs/33293707417>
- MQTT client: `src/iot/mqtt/client/Mqtt.cpp`
- MQTT CONNECT packet: `src/iot/mqtt/packets/Connect.cpp`
- MQTT server CONNECT: `src/iot/mqtt/server/packets/Connect.cpp`, `src/iot/mqtt/server/Mqtt.cpp`
- Broker/session/subscription behavior: `src/iot/mqtt/server/broker/{Broker,Session,SubscriptionTree}.cpp`

### Release/package evidence

- `v1.0.1` tag: <https://github.com/SNodeC/mqttsuite/commit/0138b1c5a4bd95c5c586a6be26c18aa50b9f300e>
- Current master vs `v1.0.1`: 560 commits ahead at this review.
- `OpenWRT` MQTTSuite tag: <https://github.com/SNodeC/mqttsuite/commit/24b601818dcb650f28e35ede35a41e6cf6bc573b>
- Public package source: <https://github.com/SNodeC/OpenWRT/tree/main/net/mqttsuite>
- Package definition: `SNodeC/OpenWRT/net/mqttsuite/Makefile`
- OpenWrt package source points at tag `OpenWRT`, declares package version `1.0.0`, release `4`, and `mqttsuite-full` excludes MQTTStore.

### Landingpages qualification evidence

- `FACTS.md`
- `MQTTSuite/EVIDENCE.md`
- Existing synthetic broker/CLI terminal capture and broker-dashboard capture under `MQTTSuite/assets/`

---

**Step 3 completion verdict:** README-relevant technical truth for current MQTTSuite master is sufficiently established for Step 4. The later workflow should not reopen source for ordinary application-role, mapping, bridge, storage, Web UI, first-success, release/package or security-boundary claims. Runtime-pending items above remain intentionally open and must not be silently promoted into tested/support claims.
