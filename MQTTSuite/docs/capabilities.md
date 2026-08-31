# MQTTSuite capability and evidence boundaries

MQTTSuite targets MQTT 3.1.1 through five focused applications. This page separates what the reviewed source contains from what the landing-page qualification actually exercised.

**Current source baseline:** [`SNodeC/mqttsuite@6c0ff62c612694a6111ff971c446327938130cf0`](https://github.com/SNodeC/mqttsuite/tree/6c0ff62c612694a6111ff971c446327938130cf0) with shared SNode.C behavior source-reviewed at [`SNodeC/snode.c@5d6453c21df4894083b445cce00b627e7794932a`](https://github.com/SNodeC/snode.c/tree/5d6453c21df4894083b445cce00b627e7794932a). MQTTSuite `6c0ff62...` includes the narrow MQTTIntegrator wildcard fix from [PR #22](https://github.com/SNodeC/mqttsuite/pull/22) / [`d15f70a`](https://github.com/SNodeC/mqttsuite/commit/d15f70a2818d291638c50aa2e2116a9e49ebd9e1): `#` is now a true multi-level wildcard, including the zero-level `parent/#` case, while `+` remains single-level.

**Runtime qualification carried by this documentation workflow:** MQTTSuite `52de563...` rebuilt and installed against SNode.C `60f26d9...` on Debian x86-64 with GCC/G++ 16.2.0, CMake 4.3.4 and Ninja 1.13.2. PR #22 was merged after that qualification and changed only `lib/MqttMapper.cpp`; its wildcard behavior is therefore **Available/source-verified**, not newly runtime-exercised by the landing-page qualification.

## Evidence vocabulary

- **Available:** implemented or declared in the pinned source.
- **Exercised:** reproduced by the landing-page qualification for the named revisions and environment.
- **Source-only:** implementation exists, but this documentation pass did not reproduce the behavior end to end.
- **[UNVERIFIED-RUNTIME]:** a material operational consequence cannot be established safely from source inspection alone.
- **Not claimed:** deliberately outside the evidence.

## Suite-level scope

| Capability | State | Boundary |
| --- | --- | --- |
| MQTT 3.1.1 | Available; Broker+CLI path exercised | not MQTT 5; not a complete conformance claim |
| five separate executables | Available; whole suite built/installed | not one monolithic daemon |
| C++20 | Available/build requirement | compiler/platform matrix not implied |
| current whole-suite build/install | Exercised in one Debian x86-64 environment | not a distribution/platform support matrix |
| IPv4 plain MQTT | Available; Broker+CLI exercised | one local QoS 1 scenario |
| IPv6 / Unix-domain MQTT | Available in multiple application source paths | source-only here |
| TLS | Available in compiled connection families | transport protection, not an authorization claim |
| MQTT over WebSocket/WSS | Available in application source paths | source-only here |
| OpenWrt packaging sources | Available in ecosystem packaging repository | package-feed/release/runtime availability not established here |
| performance / footprint | Not claimed | no benchmark evidence in this workflow |
| production readiness | Not claimed | no production qualification asserted |

The MQTTSuite top-level CMake file declares `cmake_minimum_required(VERSION 3.14)`, while the current SNode.C dependency requires CMake 3.18. A current from-source whole-suite build therefore has a practical dependency floor of **CMake 3.18**, even though MQTTSuite's own top-level declaration still says 3.14.

## MQTT protocol behavior

Current SNode.C source contains MQTT 3.1.1 CONNECT, PUBLISH, acknowledgement, SUBSCRIBE/UNSUBSCRIBE, PING and DISCONNECT paths plus broker retained-message, session, subscription and offline queue state.

| MQTT behavior | Evidence |
| --- | --- |
| CONNECT + successful local session | Exercised in Broker+CLI path |
| subscribe + deliver a publication | Exercised |
| QoS 1 publication/delivery | Exercised |
| QoS 0 and QoS 2 implementation paths | Available/source-only |
| retained messages | Available/source-only |
| wills | Available/source-only |
| persistent sessions / offline queues | Available/source-only |
| broker subscription `+` / `#` matching | Available/source-only |
| MQTT username/password fields | Available as CONNECT fields |
| broker-side credential verification backend | Not established; do not claim authentication |

## MQTTBroker

**Available:**

- MQTT server listeners over configured SNode.C stream/TLS families;
- MQTT-over-WebSocket upgrade using the `mqtt` subprotocol;
- broker session/subscription/retained-message state;
- bundled browser dashboard;
- SSE state/events;
- HTTP operations for disconnect, subscribe, unsubscribe and retained-message release;
- optional in-process use of the shared mapper.

**Exercised:** one plain-IPv4 broker with two MQTTCli clients at QoS 1, plus the real bundled Broker dashboard from the runtime-qualified MQTTSuite head.

**Current trust limitation:** the Broker HTTP administration/event surfaces do not apply application-level authentication; `/api/mqtt` emits permissive CORS and `/api/mqtt/events` uses `Access-Control-Allow-Origin: *`. The event client representation currently includes supplied MQTT password material, and live event JSON can be logged. Treat these surfaces as trusted/protected operational interfaces; do not expose them to untrusted networks without external controls. See [Broker HTTP/event administration](broker-http-api.md).

## MQTTIntegrator

**Available:**

- outbound MQTT client connections across direct and WebSocket SNode.C client families;
- mapping-derived subscriptions;
- literal topic matching, single-level `+`, and MQTT multi-level `#` matching;
- terminal `parent/#` matching for both zero remaining levels (`parent`) and deeper descendants when the parent itself has no subscription mapping;
- static, scalar-template and JSON-template mapping;
- fan-out, output QoS, retain, delay and suppressions;
- mapper plugins exporting Inja functions;
- mapping administration API with draft, validation, deploy, history and rollback;
- hot subscription delta handling when a mapping changes without a connection change;
- reconnect when mapping connection settings change.

**Source-only:** no deterministic mapping input → output runtime fixture was executed by the landing-page qualification. The corrected `#` behavior was source-verified through merged PR #22 but was not part of the older runtime qualification.

**Current limitations that must remain visible:**

- the application seeds an inline demo mapping during startup; an explicitly parsed `--mqtt-mapping-file` can replace it, but the default effective mapping is not simply the contents of the default `mapping.json` file;
- sibling topic branches are first-match in document order, so a broad `+` or `#` fallback placed before a more specific sibling can shadow it;
- the administration router ships with Basic Authentication defaults `admin/admin` and those credentials are not wired to an application configuration surface in current main;
- `/config`/history/error paths can expose credential-bearing mapping material;
- the `/ui` static root is a maintainer-local absolute path, so a portable installed Integrator Web UI is not established.

See [Integrator mapping](integrator-mapping.md).

## MQTTBridge

**Available:**

- named logical bridges containing outbound MQTT client connections;
- member MQTT sessions, subscriptions, prefixes and session-store paths;
- forwarding to every other connected member in the same logical bridge;
- preservation of payload, QoS and retain flag on forwarding;
- immediate source-member exclusion;
- optional private SNode.C reflection-suppression extension;
- configuration staging/restart machinery and bridge operational SSE/UI source.

**Source-only:** the landing-page qualification did not execute a multi-broker bridge path.

**Current limitations:**

- the schema declares `rc` and `l2` network protocols although current bridge runtime dispatch has no corresponding branches;
- direct Unix-domain schema/runtime address handling is inconsistent; do not present it as a qualified route;
- the private `loop_prevention` mechanism is non-standard and does not prove arbitrary cyclic topologies safe;
- bridge definitions contain credentials and current debug logging prints broker username/password;
- installed Web assets do not by themselves prove a portable/default Web UI runtime path.

See [Bridge definition and forwarding](bridge-definition.md).

## MQTTCli

**Available:**

- publish and subscribe in one selected MQTT client instance;
- default QoS plus per-topic `##<qos>` override for subscriptions and publication;
- retain on outgoing publication;
- client ID, keepalive, persistent session, will and credentials;
- direct and WebSocket client families where compiled;
- pretty JSON output and wrapped plain-text output;
- retry/reconnect.

**Exercised:** a QoS 1 subscriber received the canonical `edge-lab/room-01/temperature` JSON publication from a second CLI through MQTTBroker. Verified visible fields included topic, QoS 1, `Retain: false`, `Dup: false`, and pretty-printed JSON.

**Current lifecycle limitation:** the outer client is configured to reconnect. A publish-only client disconnects after QoS completion, but reconnect can cause it to publish again; stop an interactive one-shot publisher after the first verified result when repetition is not desired.

**Current secret limitation:** debug logging prints the configured MQTT password.

## MQTTStore

**Available:**

- outbound MQTT subscription clients across direct/WebSocket families where compiled;
- raw MariaDB envelope storage;
- automatic creation of the raw table when enabled;
- JSON/text/binary payload classification while preserving original payload bytes;
- optional typed projections selected by topic filters;
- projection sources from JSON Pointer, topic level or literal values;
- source matcher with literal, `+`, and terminal multi-level `#` semantics;
- MariaDB host/port/socket/user/password/database/flags configuration.

**Source-only:** no MariaDB Store end-to-end fixture was executed by the landing-page qualification.

**Operational boundaries:**

- Store creates only the raw table; projection-table schema/migrations are operator-owned;
- raw and projection inserts are independent asynchronous database operations, not one atomic transaction;
- projection failures can coexist with a raw insert attempt and are logged independently;
- invalid projection configuration is loaded during MQTT context creation after a transport connection reaches the factory. The exact process/reconnect consequence is **[UNVERIFIED-RUNTIME]**; do not claim validation always precedes every connection attempt.

See [Store storage and projections](store-storage.md).

## Installed-tree boundary

The workflow built and installed the current suite into an isolated prefix, establishing that CMake installation completed in that qualification environment. MQTTSuite source does not define an explicit install-RPATH/RUNPATH policy, and this step did not separately prove that a clean arbitrary custom-prefix runtime is self-resolving without loader-environment assistance.

Therefore:

- **Available/Exercised:** install rules produced the five executables and documented Web assets in the qualification prefix.
- **[UNVERIFIED-RUNTIME]:** clean custom-prefix execution with no build-tree or loader-environment dependencies.

## Explicit non-claims

This documentation does **not** claim:

- MQTT 5 support;
- complete MQTT conformance;
- equal qualification for every address-family/transport/TLS/WebSocket combination;
- arbitrary cyclic Bridge topology safety;
- a portable installed MQTTIntegrator UI;
- automatic management of Store projection schemas, retention, backups or database operations policy;
- performance, memory-footprint or throughput characteristics;
- production readiness;
- a broad Linux/distribution/architecture support matrix.

## Primary source anchors

- [MQTTSuite current master after PR #22](https://github.com/SNodeC/mqttsuite/tree/6c0ff62c612694a6111ff971c446327938130cf0)
- [MQTTSuite top-level CMake](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/CMakeLists.txt)
- [SNode.C CMake minimum](https://github.com/SNodeC/snode.c/blob/5d6453c21df4894083b445cce00b627e7794932a/CMakeLists.txt)
- [MQTTBroker router](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttbroker/mqttbroker.cpp)
- [MQTTBroker event model](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttbroker/lib/MqttModel.cpp)
- [MQTTIntegrator application startup](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttintegrator/mqttintegrator.cpp)
- [Mapper implementation after PR #22](https://github.com/SNodeC/mqttsuite/blob/6c0ff62c612694a6111ff971c446327938130cf0/lib/MqttMapper.cpp)
- [PR #22 wildcard fix](https://github.com/SNodeC/mqttsuite/pull/22)
- [MQTTBridge runtime](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttbridge/mqttbridge.cpp)
- [MQTTCli behavior](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttcli/lib/Mqtt.cpp)
- [MQTTStore context creation](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttstore/SocketContextFactory.cpp)
- [MQTTStore MariaDB storage](https://github.com/SNodeC/mqttsuite/blob/52de5631245c6318bfa5b7cca700f0754014f34d/mqttstore/lib/MariaDbStorage.cpp)
