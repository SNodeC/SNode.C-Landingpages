# Step 3 — MQTTSuite technical facts

**Review date:** 30 August 2026  
**Workflow stage:** Step 3 — Technical Truth  
**Public source baseline:** `SNodeC/mqttsuite` `master`/`HEAD` at
[`52de5631245c6318bfa5b7cca700f0754014f34d`](https://github.com/SNodeC/mqttsuite/commit/52de5631245c6318bfa5b7cca700f0754014f34d)  
**Compatible foundation baseline:** `SNodeC/snode.c` `master`/`HEAD` at
[`60f26d9ae54b3e9ffde954d0ca75e53f79f31d79`](https://github.com/SNodeC/snode.c/commit/60f26d9ae54b3e9ffde954d0ca75e53f79f31d79)

This document is the self-contained technical handoff for MQTTSuite README design and writing. It verifies current public `master`/`HEAD`, not a release tag. **Current public heads are the dependency and truth baseline throughout this workflow.** Source version metadata may describe build/package expectations, but tags and historical releases are not compatibility authorities here.

Existing landing-page READMEs, proposals, figures, and screenshots are research inputs only. Where they disagree with current source or the evidence boundaries below, this document controls later MQTTSuite README work.

## Evidence vocabulary

- **Current-head source-verified** — directly established by the current MQTTSuite and/or SNode.C source at the SHAs above.
- **Runtime-qualified** — reproduced in the existing isolated landing-page qualification with recorded commands and visible output.
- **Carried forward by source-delta review** — prior runtime evidence remains relevant because the current-head changes since that run do not touch the consumed implementation surface; this is not a substitute for a fresh rerun when a final screenshot or current-head acceptance claim is required.
- **Runtime-pending** — implemented in source but not reproduced by the landing-page qualification.
- **Open** — no sufficient current-head evidence for a public claim.

## Current-head status and compatibility

MQTTSuite `master` is unchanged from the application qualification baseline at `52de563...`. Its top-level CMake build adds all five application directories and requires C++20.

SNode.C advanced after the earlier MQTTSuite runtime run from `bf01683a53b48220a840522e8ccaf3b48e58c240` to current `60f26d9...`. The exact comparison is:

<https://github.com/SNodeC/snode.c/compare/bf01683a53b48220a840522e8ccaf3b48e58c240...60f26d9ae54b3e9ffde954d0ca75e53f79f31d79>

Those five SNode.C commits add and document the external echo example, its tests, and CI wiring. They do not change the MQTTSuite-consumed MQTT, networking, HTTP/WebSocket, MariaDB, configuration, or exported component implementation. Therefore the earlier MQTTSuite broker/CLI runtime proof is carried forward by source-delta review to the current dependency surface, but **it is not a fresh current-SNode.C-HEAD rerun**.

Current SNode.C HEAD itself configures, builds, runs the pre-existing test suite, installs, configures the new external echo project, and builds that project in CI; its current CI run fails only at the final new external-echo CTest step. The current run is:

<https://github.com/SNodeC/snode.c/actions/runs/33293707417>

Do not claim that all current heads have a completely green CI state. The SNode.C failure is outside the MQTTSuite dependency surface reviewed here, but it remains a current-head fact.

MQTTSuite has no application build/test CI job and no MQTTSuite test directory on current master. Its current workflows maintain README content and packaging automation, not application acceptance. Runtime statements below therefore come from the explicit landing-page qualification, not MQTTSuite CI.

## Canonical project identity

MQTTSuite is a set of **five independently runnable MQTT applications**, not one monolithic daemon:

| Application | Executable | Exact role | Primary relationship |
| --- | --- | --- | --- |
| **MQTTBroker** | `mqttbroker` | MQTT broker/server with bundled browser dashboard and optional in-process mapping | Accepts MQTT clients and distributes publications |
| **MQTTIntegrator** | `mqttintegrator` | MQTT client integration process that subscribes, transforms, and republishes | Consumes broker traffic through configured mappings |
| **MQTTBridge** | `mqttbridge` | Group of outbound MQTT client connections that forwards selected broker traffic | Connects multiple brokers through logical bridge groups |
| **MQTTCli** | `mqttcli` | Terminal MQTT client for publishing, subscribing, and inspecting messages | Provides the shortest operator/evaluation path into a broker |
| **MQTTStore** | `mqttstore` | MQTT subscriber that persists raw message envelopes and optional typed JSON projections to MariaDB | Connects MQTT traffic to database storage |

The current top-level `CMakeLists.txt` unconditionally adds all five application directories. Later README copy should therefore present one toolkit with separate processes and responsibilities, not five modes of one executable.

A useful relationship model is:

```text
publishers / devices
        │
        ▼
   MQTTBroker  ◄──────────── MQTTCli
        │                     publish / subscribe / inspect
        ├──────────────► MQTTIntegrator ── transform + republish ──► MQTT
        │
        ├──────────────► MQTTStore ────────────────────────────────► MariaDB
        │
        └──────────────► MQTTBridge ───────────────► other brokers
```

This is a role model, not proof that all five were executed together. The basic broker/CLI path is runtime-qualified; mapping, multi-broker forwarding, and MariaDB storage remain runtime-pending in this landing-page qualification.

## MQTT protocol scope

### Safe current-head claim

MQTTSuite targets **MQTT 3.1.1** through SNode.C's MQTT implementation.

Current SNode.C defines MQTT 3.1.1 protocol level `0x04`, and its server CONNECT path requires protocol name `MQTT` and protocol level 4 after handling the private reflection bit described under loop prevention. Source paths:

- `src/iot/mqtt/packets/Connect.h`
- `src/iot/mqtt/packets/Connect.cpp`
- `src/iot/mqtt/server/packets/Connect.cpp`
- `src/iot/mqtt/server/Mqtt.cpp`

Current source implements the MQTT 3.1.1 packet paths needed for CONNECT, PUBLISH, QoS acknowledgement flows, SUBSCRIBE/UNSUBSCRIBE, PING and DISCONNECT. The broker source also contains retained-message state, subscription trees, persistent-session state and offline QoS 1/2 queues.

### Evidence boundary

The landing-page runtime proof is narrower: one plain-IPv4 broker/subscriber/publisher exchange at QoS 1. Do not broaden that run into a conformance claim for every MQTT feature.

For later public wording:

- **Runtime-qualified:** CONNECT + subscribe + publish + delivered QoS 1 message in the documented local scenario.
- **Current-head source-verified, runtime-pending here:** QoS 2 flows, retained messages, wills, persistent-session recovery, offline queues and `+`/`#` subscription matching.
- **Not eligible:** `full MQTT`, complete MQTT conformance, MQTT 5 support, or claims that every feature combination has been tested.

MQTT username/password fields are carried in CONNECT packets, but the reviewed current SNode.C broker CONNECT path validates protocol/flags and then stores the supplied username/password. No broker credential-verification backend is invoked in that path. **Do not describe MQTTBroker as authenticating MQTT usernames/passwords on the basis of these fields alone.**

## MQTTBroker

### Role

MQTTBroker is the server-side application. It accepts MQTT client connections, owns the broker/session/subscription/retained-message model through SNode.C, exposes a browser-facing broker dashboard, and can optionally run the same mapping engine used by MQTTIntegrator inside the broker process.

### Transport source scope

Current `mqttbroker/CMakeLists.txt` exposes build options for:

- IPv4 direct MQTT stream;
- IPv4 direct MQTT over TLS;
- IPv6 direct MQTT stream;
- IPv6 direct MQTT over TLS;
- Unix-domain direct MQTT stream;
- Unix-domain direct MQTT over TLS;
- MQTT over WebSocket and WSS through corresponding HTTP/HTTPS server surfaces.

The broker WebSocket upgrade requires the `mqtt` WebSocket subprotocol. Routes `/ws`, `/mqtt`, and `/` can accept that upgrade.

These are **source-implemented transport roles**, not a runtime-tested matrix. Only the plain IPv4 MQTT listener is runtime-qualified in the principal first-success scenario.

### Bundled broker Web UI

The browser dashboard is a genuine current-master product surface. Current source installs HTML/CSS/JavaScript from `mqttbroker/html/` under the MQTTSuite broker web root and routes `/clients` to the dashboard.

The broker exposes live/event and mutating HTTP endpoints including:

- `GET /api/mqtt/events` — SSE event stream;
- `GET /sse` — SSE event stream;
- `POST /api/mqtt/disconnect` — close a selected client connection;
- `POST /api/mqtt/unsubscribe` — remove a selected client subscription;
- `POST /api/mqtt/release` — release a retained topic by publishing an empty retained value;
- `POST /api/mqtt/subscribe` — add a subscription for a selected connected client.

The existing landing-page broker screenshot was captured from the real current-MQTTSuite-HEAD dashboard using synthetic clients/topic state. Because MQTTSuite HEAD has not moved, that dashboard load remains source-aligned evidence. It proves the visible dashboard state, not every mutating admin action.

### Broker security boundary

The broker `/api/mqtt` middleware sets permissive CORS, including `Access-Control-Allow-Origin: *`, and no application-level Basic Authentication middleware appears in the reviewed broker router. The API can disconnect clients and change subscription/retained state.

Therefore:

- treat the broker HTTP surface as an administrative/trusted-network surface unless separately protected;
- TLS can encrypt a listener but does not itself add authorization;
- do not call the dashboard/API secure or authenticated without additional current evidence;
- do not expose it remotely merely because HTTP/HTTPS transport exists.

### Embedded mapping

MQTTBroker constructs each MQTT connection with the shared `MqttMapper`. In `mqttbroker/lib/Mqtt.cpp`, incoming publications are sent to the broker model and then, when a mapper exists, processed into immediate and delayed mapped publications and republished through the same broker.

This is **in-process shared mapping behavior**, not a hidden `mqttintegrator` child process. It is a real architectural differentiator, but the landing-page mapping scenario remains runtime-pending.

## MQTTIntegrator

### Role

MQTTIntegrator is an outbound MQTT client application. It derives subscriptions from the mapping configuration, receives matching MQTT publications, maps them, and republishes immediate or delayed results.

`mqttintegrator/lib/Mqtt.cpp` establishes the exact lifecycle:

1. on socket connection, send MQTT CONNECT using mapper connection settings;
2. after an accepted CONNACK with no existing session, subscribe to the mapper-derived topic list;
3. on PUBLISH, obtain immediate and scheduled mapped outputs;
4. publish immediate outputs and timer-schedule delayed outputs;
5. on mapping update, reconnect when connection settings changed, otherwise compute a subscription delta and hot subscribe/unsubscribe.

Current `mqttintegrator.cpp` seeds a default/demo mapping in source after attempting to load `mapping.json`; command-line/configuration and the admin API can replace/deploy mappings. Do not imply that the executable starts in a neutral no-mapping state.

### Transport source scope

Current source instantiates client roles for:

- IPv4 / IPv6 / Unix-domain direct MQTT streams;
- plain and TLS variants;
- MQTT over WS/WSS for IPv4, IPv6 and Unix-domain HTTP clients.

Again, these are source-implemented options, not a qualified support matrix.

### Mapping administration API

MQTTIntegrator creates IPv4 HTTP and HTTPS admin servers and uses the shared mapping-admin router. The router exposes schema/config/history, PATCH/replace, validate, deploy and rollback operations.

Unlike the broker and bridge admin surfaces, this router applies SNode.C `BasicAuthentication`. However, current `AdminOptions` defaults are:

```text
user = admin
pass = admin
realm = mqttsuite-admin
```

This must be treated as a development/default credential boundary, not a security guarantee. A public deployment must replace/protect those credentials and decide its listener/TLS/exposure policy.

### Integrator UI limitation

The mapping admin router currently serves `/ui` from a **hard-coded maintainer-local absolute path**:

```text
/home/voc/tmp/integrator/mqtt-integrator-ui/dist/mqtt-integrator-ui/browser
```

No corresponding packaged MQTTIntegrator UI artifact is present in the current MQTTSuite source tree. Therefore:

- the mapping admin API is real current-head functionality;
- a portable, installed, shipped MQTTIntegrator Web UI is **not** established by current master;
- do not use an integrator UI screenshot as proof of shipped current-master functionality until this path/packaging boundary is fixed and qualified.

## Mapping semantics

The shared mapping engine is defined by `lib/mapping-schema.json`, `MqttMapper`, `JsonMappingReader`, and the mapping plugin interface. It is used by MQTTIntegrator and can also be embedded in MQTTBroker.

### Topic matching and subscriptions

The mapping schema describes a hierarchical topic tree. Current mapper source recognizes literal topic levels plus `+` and `#` level names and derives MQTT subscriptions from the configured tree. This supports MQTT-style wildcard mapping at source level, but do not claim every wildcard edge case is conformance-tested by this workflow.

### Three mapping modes

**Static mapping** compares the incoming MQTT payload string with configured `message` values. A match emits the configured `mapped_message` to `mapped_topic`.

**Value-template mapping** exposes the incoming payload as a scalar string in the template context and renders topic/message templates.

**JSON-template mapping** parses the incoming payload as JSON and exposes the parsed value in the template context. Invalid JSON does not produce a JSON-template mapping.

Mapped outputs can specify:

- `mapped_topic`;
- output QoS 0–2;
- retain flag;
- delay;
- template suppressions for template mappings.

A negative default delay takes the immediate path; non-negative delay values are placed into the scheduled-publish queue. Template rendering uses the embedded Inja implementation. Mapping plugins can be dynamically loaded and can register additional template callbacks.

### Mapping configuration and credential boundary

The mapping `connection` object contains MQTT client settings including clean session, will, username and password. The mapping admin workflow can write draft/history/current mapping files to the filesystem. These files can therefore contain credentials.

Treat mapping files and their history/drafts as credential-bearing configuration. No encrypted secret-store abstraction is established here.

### Evidence boundary

Mapping behavior is current-head source-verified. The canonical end-to-end transformation scenario has not been rerun in the landing-page qualification, so later figures must not present a mapped output as runtime proof until Step 5 validates a real scenario.

## MQTTBridge

### Role and logical bridge model

MQTTBridge is not a broker. It creates **outbound MQTT client connections** to configured brokers and groups those clients into named logical bridges.

Each configured broker member can define:

- network endpoint;
- MQTT client ID / keepalive / clean-session settings;
- will settings;
- username/password;
- session-store path;
- subscriptions with QoS;
- broker prefix;
- `loop_prevention` flag;
- disabled state.

On accepted CONNACK, a broker client joins its logical bridge and subscribes to its configured topics. Thus bridge traffic selection is primarily established by each source broker connection's MQTT subscriptions.

### Exact forwarding behavior

When one bridge member receives a publication, `Bridge::publish()` sends it to every **other connected member** of the same logical bridge. It does not send the publication directly back over the origin connection.

The forwarded topic is constructed exactly as:

```text
bridge prefix
+ origin-broker prefix
+ destination-broker prefix
+ original MQTT topic
```

The payload, QoS and retain flag are forwarded unchanged by that bridge step.

Do not describe MQTTBridge as a transformation engine; topic/payload transformation belongs to the mapper/integrator. Likewise, do not imply a separate arbitrary bridge-filter language beyond the configured MQTT subscriptions and prefixes established in source.

### Loop-prevention semantics — two bounded mechanisms

There are two different mechanisms that must not be collapsed into a generic “loops are solved” claim.

1. **Within one logical bridge**, MQTTBridge never immediately forwards a received publication back to the same bridge connection it arrived on.
2. **Per broker connection**, `loop_prevention=true` is passed into SNode.C's MQTT CONNECT path.

The second mechanism is a private extension. Current SNode.C sets the high bit of the MQTT protocol-level byte, producing `0x84` rather than ordinary MQTT 3.1.1 `0x04`. Its own server deserializer interprets that bit as “do not reflect messages to origin”, masks the bit, and then validates the remaining protocol level as MQTT 3.1.1. The broker session code suppresses delivery back to the origin client when reflection is disabled.

This mechanism is **not standard MQTT 3.1.1 behavior**. Source comments compare it with a private/`try_private` style broker mechanism. It cannot be assumed to work with arbitrary third-party brokers and does not prove every cyclic broker topology safe.

Safe wording later: MQTTSuite has explicit origin-reflection suppression mechanisms; cyclic topologies and third-party interoperability require topology-specific qualification.

### Bridge admin/API surface

Current `mqttbridge` exposes:

- `GET /api/bridge/config` — returns the active bridge JSON;
- `PATCH /api/bridge/config` — validates/stages a JSON patch, closes bridge flows, activates the new configuration, restarts connections and persists the active configuration;
- `GET /api/bridge/sse` — lifecycle/status SSE;
- `/config` — static bridge configuration UI.

Current source creates IPv4 plain/TLS admin HTTP servers. No application-level Basic Authentication middleware is present in this router.

This is a significant security boundary because the active bridge JSON contains broker username/password fields and the API can change live bridge behavior.

### Bridge credential/logging boundary

`BridgeStore::activateStaged()` writes the full active bridge JSON back to the configured definition file. Current `mqttbridge.cpp` debug logging also prints broker username, broker password, will message, address and other configuration values.

Therefore:

- the bridge definition file is credential-bearing state;
- debug logs can contain secrets;
- no real credentials may appear in screenshots or qualification captures;
- remote admin exposure requires an external/explicit trust boundary rather than being assumed safe.

### Bluetooth schema mismatch — current-head defect

The current bridge JSON schema accepts network protocols:

```text
in, in6, rc, l2, un
```

including Bluetooth RFCOMM (`rc`) and L2CAP (`l2`). However, the current `mqttbridge` executable only includes and instantiates IPv4, IPv6 and Unix-domain client paths, with their stream/TLS and corresponding WebSocket variants. `mqttbridge/CMakeLists.txt` has no MQTTSuite bridge RFCOMM/L2CAP build option; it merely lists some SNode.C Bluetooth components as optional package components.

**Conclusion:** RFCOMM/L2CAP bridge operation is not established by current MQTTSuite master. The schema is broader than the current executable implementation. A schema-valid Bluetooth bridge description is not proof that the executable can create that connection.

Any existing Landingpages claim telling users to rebuild SNode.C with Bluetooth and then enable MQTTSuite RFCOMM/L2CAP targets is stale/unsupported and must be removed or corrected before publication.

## MQTTCli

### Role

MQTTCli is the terminal evaluation/operations client. One enabled client instance can publish, subscribe, or do both. It is the correct application for the shortest visible first success because its received-message output displays the MQTT topic, payload, QoS, retain and duplicate state.

If a payload parses as JSON, current source pretty-prints it; otherwise it wraps the text for terminal width.

### Source transport scope

Current source instantiates:

- `in-mqtt`, `in-mqtts`;
- `in6-mqtt`, `in6-mqtts`;
- `un-mqtt`, `un-mqtts`;
- `in-wsmqtt`, `in-wsmqtts`;
- `in6-wsmqtt`, `in6-wsmqtts`;
- `un-wsmqtt`, `un-wsmqtts`.

WebSocket clients use the `mqtt` subprotocol and default target `/ws`.

Session configuration includes client ID, QoS 0–2, persistent-session selection, keepalive, will, username and password. Subscription topics and publication topics can carry a `##<qos>` suffix to override the default QoS; publication also supports retain.

### CLI security boundary

Current debug logging prints MQTT username, password and will message. Treat debug output as potentially secret-bearing. Public captures must use synthetic/no credentials and must be reviewed for logs as well as command lines.

## MQTTStore

### Role

MQTTStore is an outbound MQTT subscriber that writes received messages to MariaDB. Its storage model deliberately separates a **raw envelope** from optional **typed projections**.

### MQTT/client source scope

The current executable provides the same IPv4, IPv6 and Unix-domain direct/TLS plus WS/WSS client family as MQTTCli. It has configurable MQTT client ID, default subscription QoS, persistent-session choice, keepalive, will, username/password and client session-store path. Subscription strings can use `topic##qos` to override the default QoS.

### MariaDB connection configuration

Current source exposes database host, username, password, database name, TCP port, Unix socket and flags. These are ordinary configuration values, not secret-store handles.

### Raw envelope

For each received PUBLISH, MQTTStore constructs a message record containing:

- source connection name;
- MQTT topic;
- original payload bytes/string;
- QoS;
- retain flag;
- DUP flag;
- packet identifier.

It then inserts the message into the configured raw table. When auto-create is enabled, current source can create that raw table with fields for receive timestamp, source instance, topic, QoS, retain/DUP, packet identifier, raw payload, text representation, JSON representation and a `json|text|binary` payload-format marker.

Every received message takes the raw-insert path. JSON parsing only changes the derived representation and whether typed projections can be attempted.

### Typed projections

Typed projections are attempted **only when the payload parses as JSON**. `projection-schema.json` defines a target table and columns. Each column can derive from:

- an RFC 6901 JSON Pointer;
- a zero-based MQTT topic level;
- a literal string.

A projection has an MQTT topic filter. Current `StoragePlan` matching implements literal levels, `+`, and a terminal `#` wildcard. Optional missing values can be omitted; values marked required become SQL `NULL` when the configured source is unavailable.

### Storage ownership boundaries

Only the raw table has source support for automatic creation. Current MQTTSuite does **not** establish automatic creation or migration of operator-defined projection tables.

No current-head evidence establishes:

- schema migration policy for projection tables;
- retention/expiry policy;
- database backup policy;
- atomicity between the raw insert and projection inserts;
- failure/retry guarantees across database loss;
- MariaDB version support matrix.

Raw payloads are persisted unredacted. Database and MQTT credentials are ordinary configuration strings. Database schema lifecycle, retention, access control and data classification remain operator responsibilities.

## Transport matrix — source implementation, not support matrix

The following table is safe as a **source implementation inventory** only:

| Application | MQTT role | Direct MQTT source paths | MQTT-over-WebSocket source paths | HTTP/admin surface |
| --- | --- | --- | --- | --- |
| MQTTBroker | server | IPv4, IPv6, Unix; plain/TLS | WS/WSS via IPv4, IPv6 and Unix HTTP(S) servers | Broker dashboard/API/SSE |
| MQTTIntegrator | client | IPv4, IPv6, Unix; plain/TLS | WS/WSS via IPv4, IPv6 and Unix HTTP clients | Mapping admin IPv4 HTTP/HTTPS, BasicAuth |
| MQTTBridge | outbound client group | IPv4, IPv6, Unix; plain/TLS | WS/WSS via IPv4, IPv6 and Unix HTTP clients | Bridge config/status IPv4 HTTP/HTTPS; no app auth found |
| MQTTCli | client | IPv4, IPv6, Unix; plain/TLS | WS/WSS via IPv4, IPv6 and Unix HTTP clients | none |
| MQTTStore | client | IPv4, IPv6, Unix; plain/TLS | WS/WSS via IPv4, IPv6 and Unix HTTP clients | none |

Do not label these cells “supported” or “tested”. The principal runtime proof is plain IPv4 broker + MQTTCli. TLS, WSS, IPv6, Unix-domain and every per-application combination require explicit execution evidence before stronger wording.

Do not add Bluetooth to this application transport matrix. The only current MQTTSuite Bluetooth appearance found in this review is the over-broad MQTTBridge schema plus optional SNode.C package components; the executable path is absent.

## Shortest real first success

The shortest **already runtime-qualified** MQTTSuite evaluation path is one local MQTTBroker listener plus two MQTTCli processes: subscriber and publisher.

The run used MQTTSuite current HEAD `52de563...`. Its SNode.C runtime dependency was the immediately preceding head `bf01683...`; the source-delta review above establishes that the current SNode.C changes do not touch this path. A fresh current-SNode.C-HEAD rerun should still be performed when Step 5 captures new terminal evidence.

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

This deliberately disables every listener/control surface except one loopback IPv4 MQTT listener so the first-success proof has a narrow exposure and evidence boundary.

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

The subscriber printed the topic, pretty-printed JSON payload, `QoS: 1`, `Retain: false`, and duplicate state. Ctrl-C teardown was clean.

This is the public first-success candidate. Do not replace it with a shorter unexecuted command merely for presentation. Step 5 should rerun the exact path against the then-current MQTTSuite and SNode.C heads before producing final terminal imagery.

## Dependencies and build/package scope

### Current-head build requirements

Current source establishes:

- CMake minimum `3.14` for MQTTSuite;
- C++20 required;
- `nlohmann_json` package version floor `3.7.0`;
- recursive `lib/json-schema-validator` submodule;
- installed SNode.C package; application-level CMake calls request `snodec 2.0.0` as a package-version floor, not an exact SHA or release-tag dependency;
- SNode.C MQTT, HTTP/Express, networking, TLS and WebSocket components according to enabled MQTTSuite options;
- SNode.C `db-mariadb` for the MQTTStore library, so a complete default all-five-app build includes the MariaDB client development dependency through SNode.C;
- embedded Inja template implementation for mapping;
- Git for cloning/submodules, not as an application runtime dependency.

The technical dependency baseline for publication remains **the current SNode.C `master`/`HEAD`**, regardless of CMake package-version metadata.

MQTTSuite's transport build options default on for IPv4, IPv6, Unix, TLS and WebSocket families, which means a complete default build expects the corresponding SNode.C components to be present.

Doxygen/Graphviz, IWYU, clang-format, cmake-format, js-beautify and Prettier are maintainer/documentation/format tooling, not core runtime dependencies.

### Current-head packaging boundary

Current master defines normal CMake build/install rules for the five executables, internal/shared libraries, MQTTBroker Web assets and MQTTBridge Web assets. That is sufficient to claim **source build/install surfaces exist**.

This Step 3 does not establish a current-head binary distribution, distro package, container image, package-manager publication, or release-level compatibility policy. Do not use historical tags/releases to fill that gap.

### Platform boundary

The recorded MQTTSuite qualification environment was Debian GNU/Linux forky/sid on x86-64 with GCC 16.2.0, CMake 4.3.4 and Ninja 1.13.2. That proves one environment, not a support matrix.

Current MQTTSuite source contains GCC/Clang-specific compiler handling, but there is no current MQTTSuite application CI matrix proving a compiler range. No OpenWrt packaging manifest was found in the current MQTTSuite tree during this review. ARM, Raspberry Pi, Android/Termux, OpenWrt and broad distribution support are therefore open, even if comments or ecosystem history suggest relevance.

## Security, credential and state boundaries

Later README design should communicate these boundaries concisely rather than hide them in qualification prose:

| Surface | Current-head fact | Safe public interpretation |
| --- | --- | --- |
| MQTTBroker MQTT credentials | username/password fields are parsed and retained, but no broker authentication backend was established | Do not claim broker credential authentication |
| MQTTBroker Web API | mutating admin endpoints; permissive CORS; no app BasicAuth found | trusted/admin surface; TLS is not authorization |
| MQTTIntegrator admin | BasicAuth middleware; default `admin` / `admin`; HTTP and HTTPS source listeners | authentication exists, but default credentials must be changed/protected |
| Mapping files/history | can contain MQTT username/password | credential-bearing filesystem state |
| MQTTBridge admin | GET returns active config; PATCH modifies/restarts/persists; no app BasicAuth found | protect externally; do not expose casually |
| MQTTBridge config/logs | config contains username/password; debug logs print username/password and will data | credential-bearing files/logs |
| MQTTCli logs | debug logs print MQTT username/password and will data | captures/logs may contain secrets |
| MQTTStore config | MQTT and MariaDB credentials are ordinary config strings | no secret-store abstraction established |
| MQTTStore data | raw MQTT payload is stored unredacted | database access/retention/classification are operator-owned |
| Session stores | ordinary filesystem-backed state | do not imply encryption or managed lifecycle |

No `secure`, `production-ready`, remote-safe, secret-managed or zero-trust claim is justified by current evidence.

## Genuine differentiators eligible for Step 4

The strongest technically credible differentiators are these; none requires hype or unsupported performance claims:

1. **Five focused applications around one MQTT domain.** Brokerage, terminal inspection, transformation, cross-broker forwarding and persistence are separate runnable responsibilities rather than one oversized daemon.
2. **One mapping engine in two useful forms.** The same schema/template mapper powers standalone MQTTIntegrator behavior and optional in-process MQTTBroker mapping.
3. **Concrete mapping semantics.** Static payload mapping, scalar and JSON templates, topic transformation, QoS/retain selection, delayed output, suppression and dynamically loaded template callbacks are explicit source capabilities.
4. **A bridge built from outbound MQTT clients.** Logical bridges make broker membership, source subscriptions, prefixes, session settings and connection lifecycle explicit rather than pretending the bridge is another broker.
5. **Raw-envelope-first storage.** MQTTStore preserves MQTT metadata and original payload first, then optionally derives typed JSON projections. This separates evidence/data capture from application-specific relational views.
6. **A real broker operations UI.** The browser dashboard is backed by the live broker model/SSE/API and has existing genuine current-MQTTSuite-HEAD capture evidence.

Transport breadth can support the story, but because most combinations are source-verified rather than runtime-qualified it should not be the headline differentiator.

Do not use `lightweight`, `fast`, `small footprint`, `complete`, `full`, `secure` or `production-ready` as differentiators without separate current-head evidence.

## Stale, contradictory or unsupported Landingpages claims

The current working Landingpages material must not be copied mechanically. The following items need correction or qualification in later stages:

1. **Any tag/release/version as technical dependency baseline** — superseded for this workflow. Always resolve MQTTSuite and SNode.C from current public `master`/`HEAD`. CMake version numbers are package metadata/floors only.
2. **“Enable MQTTSuite RFCOMM/L2CAP targets after rebuilding SNode.C with Bluetooth”** — unsupported. The bridge schema accepts `rc`/`l2`, but current `mqttbridge` contains no corresponding executable connection path or MQTTSuite build target.
3. **Broker Web UI evidence contradiction** — existing Landingpages text both presents a genuine current-head broker UI capture and later says evidence does not extend to Web UI. Correct boundary: dashboard load/visible synthetic state is runtime-qualified; its complete mutating API behavior is not.
4. **Broker “authentication is an operator decision” wording** — can imply a built-in selectable MQTT authentication backend. Current broker accepts credential fields but no credential-verification backend was established. Say exactly that instead.
5. **Any all-five-app executed integration flow** — unsupported. The five roles compose coherently in architecture, but mapping, bridge and database arrows remain runtime-pending in this qualification.
6. **MQTTIntegrator Web UI as a shipped/portable surface** — unsupported on current master because the router points to a maintainer-local absolute build directory and no packaged UI artifact is present.
7. **Generic loop-prevention guarantee** — too broad. Distinguish same-connection origin suppression from the private protocol-level high-bit extension; qualify cyclic topologies and third-party brokers individually.
8. **Broad ARM/OpenWrt/Android/Raspberry Pi/platform support** — unsupported by current MQTTSuite build/test evidence.
9. **`lightweight` positioning** — present in historical/source description strings but not backed by current footprint or performance measurements; do not reuse as a verified differentiator.
10. **`full MQTT`, MQTT 5, complete conformance, production readiness or universal transport support** — unsupported.
11. **“Credentials supported” without role qualification** — client applications can send username/password fields; that is different from MQTTBroker authenticating them.
12. **Bridge config/admin as harmless monitoring** — false boundary. It returns/persists credential-bearing config and PATCH can restart live bridge connections.

## Open facts and runtime gaps

The following remain explicit gaps after Step 3 and should be resolved only if Step 4/5 needs the corresponding public claim or visual:

- fresh broker/CLI first-success rerun against both then-current MQTTSuite and then-current SNode.C heads;
- one deterministic MQTTIntegrator mapping run proving input → mapped output;
- a two-or-more-broker MQTTBridge run proving subscriptions, exact prefix composition and restart behavior;
- third-party-broker qualification for the private loop-prevention mechanism;
- MQTTStore run against a disposable MariaDB schema proving raw envelope + one typed projection;
- MQTTStore database-loss, restart, malformed payload and retention/migration boundaries;
- per-application IPv6, Unix, TLS, WS and WSS runtime matrix;
- MQTTSuite acceptance scenarios for QoS 2, will, retained publication, persistent-session recovery and wildcard subscriptions;
- exact bind/exposure defaults and production guidance for broker, integrator and bridge admin listeners;
- broad compiler/distribution/architecture/package support matrix;
- dedicated MQTTSuite application build/test CI;
- resolution of the current SNode.C external-echo CTest failure before any “all current heads green” ecosystem claim;
- portable packaging or removal of the MQTTIntegrator UI route;
- correction of the MQTTBridge `rc`/`l2` schema/executable mismatch;
- correction of the `LICENSE` prose defect described below.

## License fact

Current MQTTSuite `LICENSE` starts with:

```text
SPDX-License-Identifier: MIT OR GPL-3.0-or-later
```

and the repository contains full MIT and GPL-3.0-or-later license texts. However, prose in `LICENSE` incorrectly describes the second option as LGPL. Later public copy should use the SPDX expression and full license files as the source of truth and must not reproduce the stale LGPL sentence.

## Step 4 handoff

Step 4 may proceed without reopening source for ordinary MQTTSuite claims if it preserves these constraints:

- narrative center: the five applications and their real MQTT/message/integration responsibilities;
- principal proof: the local MQTTBroker + MQTTCli subscriber/publisher QoS 1 first success;
- strongest real product visual: MQTTBroker's live browser dashboard;
- centerpiece flow may show Broker → Integrator / Bridge / Store relationships, but mapping/bridge/storage arrows must be presented as verified architecture until their runtime scenarios are captured;
- MQTT 3.1.1 must remain explicit; no MQTT 5/full-conformance language;
- transport inventory is source-implemented, not a tested support matrix;
- no Bluetooth MQTTSuite transport claim on current master;
- loop prevention must be described as bounded mechanisms, including a private/non-standard SNode.C broker extension;
- raw envelope versus typed projection is the correct MQTTStore distinction;
- broker/bridge admin surfaces and credential-bearing files/logs require explicit trust boundaries;
- MQTTIntegrator's current portable UI claim is blocked;
- package/platform/maturity wording must remain current-head evidence-based and must not depend on tags/releases;
- omit rather than broaden any unresolved fact.

## Primary evidence index

### MQTTSuite current HEAD

- Commit: <https://github.com/SNodeC/mqttsuite/commit/52de5631245c6318bfa5b7cca700f0754014f34d>
- Top-level build: `CMakeLists.txt`
- Shared mapper: `lib/MqttMapper.{h,cpp}`, `lib/mapping-schema.json`
- Mapping admin: `lib/MappingAdminRouter.{h,cpp}`, `lib/ConfigApplication.cpp`
- MQTTBroker: `mqttbroker/CMakeLists.txt`, `mqttbroker/mqttbroker.cpp`, `mqttbroker/lib/Mqtt.cpp`, `mqttbroker/html/`
- MQTTIntegrator: `mqttintegrator/CMakeLists.txt`, `mqttintegrator/mqttintegrator.cpp`, `mqttintegrator/lib/Mqtt.cpp`
- MQTTBridge: `mqttbridge/CMakeLists.txt`, `mqttbridge/mqttbridge.cpp`, `mqttbridge/lib/{Bridge,Broker,BridgeStore,Mqtt}.cpp`, `mqttbridge/lib/bridge-schema.json`
- MQTTCli: `mqttcli/CMakeLists.txt`, `mqttcli/mqttcli.cpp`, `mqttcli/lib/{ConfigSections,Mqtt}.cpp`
- MQTTStore: `mqttstore/CMakeLists.txt`, `mqttstore/mqttstore.cpp`, `mqttstore/lib/{Mqtt,MariaDbStorage,StoragePlan}.cpp`, `mqttstore/lib/projection-schema.json`
- Dependencies: `.gitmodules`, `lib/CMakeLists.txt`, `mqttstore/lib/CMakeLists.txt`
- License: `LICENSE`, `LICENSE-MIT`, `LICENSE-GPL-3.0-or-later`

### SNode.C current HEAD

- Commit: <https://github.com/SNodeC/snode.c/commit/60f26d9ae54b3e9ffde954d0ca75e53f79f31d79>
- MQTT CONNECT/version/private loop bit: `src/iot/mqtt/packets/Connect.{h,cpp}` and `src/iot/mqtt/server/packets/Connect.cpp`
- Broker CONNECT/session behavior: `src/iot/mqtt/server/Mqtt.cpp`
- Subscription/wildcard behavior: `src/iot/mqtt/server/broker/SubscriptionTree.cpp`
- Persistent/offline session behavior: `src/iot/mqtt/server/broker/{Broker,Session}.cpp`
- Current-head delta from prior MQTTSuite runtime dependency: <https://github.com/SNodeC/snode.c/compare/bf01683a53b48220a840522e8ccaf3b48e58c240...60f26d9ae54b3e9ffde954d0ca75e53f79f31d79>
- Current CI run: <https://github.com/SNodeC/snode.c/actions/runs/33293707417>

## Final Step 3 status

**Technical-fact handoff: COMPLETE.**

Current-head source truth is sufficient for README design. The document intentionally leaves runtime-pending behavior and platform/package/security gaps explicit rather than converting them into public claims. No README redesign or README prose was performed in Step 3.
