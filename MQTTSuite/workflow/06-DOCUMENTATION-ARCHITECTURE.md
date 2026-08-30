# MQTTSuite Step 6 Documentation Architecture

This handoff freezes the documentation architecture used by the Step 6 GitHub README candidate set.

Evidence baselines:

- landing/documentation repository: `SNodeC/SNode.C-Landingpages` at `ac6ae2454ed3718b4dc15d3099aac94938ed2372` before this Step 6 commit;
- MQTTSuite source: `SNodeC/mqttsuite` at `52de5631245c6318bfa5b7cca700f0754014f34d`;
- SNode.C source used for shared configuration/transport semantics: `SNodeC/snode.c` at `60f26d9ae54b3e9ffde954d0ca75e53f79f31d79`;
- earlier repository-grounded evidence: `MQTTSuite/workflow/03-TECHNICAL-FACTS.md`;
- existing visual/provenance evidence consulted only for already-demonstrated runtime paths: `MQTTSuite/workflow/05-VISUALS.md` and `MQTTSuite/assets/src/IMPLEMENTATION.md`.

The six candidates are written as their **future public README contents**. Relative links inside them are therefore publication-relative, not relative to the workflow staging directory.

## Candidate to publication mapping

| Step 6 candidate | Future publication target |
| --- | --- |
| `MQTTSuite/workflow/06-README-DRAFT.md` | `MQTTSuite/README.md` |
| `MQTTSuite/workflow/06-APP-README-DRAFTS/mqttbroker/README.md` | `MQTTSuite/mqttbroker/README.md` |
| `MQTTSuite/workflow/06-APP-README-DRAFTS/mqttintegrator/README.md` | `MQTTSuite/mqttintegrator/README.md` |
| `MQTTSuite/workflow/06-APP-README-DRAFTS/mqttbridge/README.md` | `MQTTSuite/mqttbridge/README.md` |
| `MQTTSuite/workflow/06-APP-README-DRAFTS/mqttcli/README.md` | `MQTTSuite/mqttcli/README.md` |
| `MQTTSuite/workflow/06-APP-README-DRAFTS/mqttstore/README.md` | `MQTTSuite/mqttstore/README.md` |

No public README is published by Step 6.

## Content ownership

The root README owns shared explanations only once. Application READMEs remain independently useful for a reader who lands in an application directory, but link back instead of reproducing long common sections.

| Topic | Detailed owner | Summary/routing elsewhere |
| --- | --- | --- |
| suite identity and five-application responsibility split | root | short role paragraph in every app |
| whole-suite prerequisites/build/install | root | each app states installed target/result and links root |
| first suite success | root | Broker and CLI repeat enough commands for direct landing |
| SNode.C application extension model | root | each app shows only its own factory seam |
| shared SNode.C configuration hierarchy | root | application docs explain their own subcommands/options |
| configuration persistence / `--write-config` | root | each app gives one relevant persistence example |
| transport composition concepts | root | each app documents only its own runnable/source-backed paths |
| MQTTBroker listeners, broker state, Web surface | Broker | root summarizes role |
| mapping format and mapper semantics | Integrator | root introduces mapping; Broker routes embedded-map details to Integrator |
| mapping admin draft/validate/deploy/history/rollback | Integrator | root does not duplicate API |
| bridge definition and forwarding | Bridge | root gives conceptual distinction and topology role |
| Bridge versus Integrator | Bridge | root gives short conceptual version |
| CLI command/session/pub/sub behavior | CLI | root uses CLI only for canonical first success |
| Store raw-envelope schema | Store | root summarizes raw-first principle |
| Store typed projections | Store | root gives only concept |
| practical exposure/credential boundaries | application owning the surface | root consolidates cross-suite distinctions |
| license | each README | exact expression remains `MIT OR GPL-3.0-or-later` |

## Common configuration boundary

The root README owns the distinction among four configuration layers:

1. SNode.C application/connection configuration;
2. mapping JSON;
3. bridge-definition JSON;
4. Store projection JSON.

This prevents app READMEs from accidentally describing a domain file as though it were another SNode.C config section.

## Transport evidence boundary

The candidates distinguish:

- **runtime-qualified example:** the current plain IPv4 Broker + CLI first-success path;
- **implemented/configurable source path:** endpoint families that are instantiated consistently by current source and build options;
- **declared but inconsistent path:** schema/build vocabulary that does not match runtime instantiation.

No transport table is intended as a blanket certification matrix.

## Cross-document links

Future root links:

```text
mqttbroker/README.md
mqttintegrator/README.md
mqttbridge/README.md
mqttcli/README.md
mqttstore/README.md
```

Future application README links back to:

```text
../README.md
```

Significant source/schema links are publication-relative:

```text
mqttbroker -> ../lib/mapping-schema.json
mqttintegrator -> ../lib/mapping-schema.json
mqttintegrator -> ../lib/MqttMapperPlugin.h
mqttbridge -> lib/bridge-schema.json
mqttstore -> lib/projection-schema.json
mqttstore -> ../docs/mqttstore-user-guide.md
```

## Figure inventory

Step 6 plans figures only. No figure file, screenshot, Figma frame, or final asset is produced here.

| Document | Section | Working title | Reader question answered | Technical content | Likely visual type | Desktop/mobile art direction useful? | Evidence needed before production |
| --- | --- | --- | --- | --- | --- | --- | --- |
| root | opening/chooser | Five applications, five responsibilities | Which executable do I need? | five roles and message relationships | responsibility map | yes | app main/CMake/Step 3 |
| root | why five applications | Representative deployment topologies | Which apps belong in common deployments? | Broker+CLI, normalization, persistence, bridge domain | topology small multiples | yes | current app roles/runtime examples |
| root | SNode.C extension model | From SNode.C endpoint to MQTTSuite behavior | Where does app-specific behavior enter SNode.C? | endpoint, `SocketConnection`, factory, MQTT context, app behavior | architecture flow | yes | all five `SocketContextFactory.cpp`; SNode.C endpoint source |
| root | transport composition | Direct MQTT versus MQTT-over-WebSocket | What changes when WebSocket is selected? | stream vs HTTP upgrade/WS/subprotocol stack | stack comparison | yes | app mains, WebSocket factories |
| root | configuration | Configuration hierarchy and persistence | How do instance/subcommand values become reusable config? | app → instance → address/session/action → config file | hierarchy + lifecycle | yes | SNode.C `Config.cpp`; app config sections |
| root | mapping | Mapping pipeline | What happens to one mapped publish? | topic match, mapping mode, render, QoS/retain/delay, fan-out | message pipeline | yes | `MqttMapper.cpp`, schema |
| root | bridging | Logical bridge forwarding | How does a bridge member forward to peers? | source exclusion, subscriptions, prefix order | topology/message path | yes | `Bridge.cpp`, `Broker.cpp`, `BridgeStore.cpp` |
| root | storage | Raw envelope and optional projections | What is always stored versus optional? | raw row plus JSON-only projections | data flow | yes | `MariaDbStorage.cpp`, `StoragePlan.cpp` |
| Broker | assembly/listeners | Listener families around one broker core | Do listeners share broker state? | direct MQTT + HTTP/WS listener families, shared broker | hub architecture | yes | `mqttbroker.cpp`, factory, broker construction |
| Broker | Web surface | Dashboard, SSE, API, and MQTT WebSocket relationship | What is served on Broker HTTP instances? | static dashboard, SSE, mutating API, WS upgrade | router/surface map | yes | `mqttbroker.cpp`, HTML assets |
| Broker | embedded mapping | Optional embedded mapper | Is embedded mapping a second process? | Broker publish → `MqttMapper` → mapped broker publish | flow inset | yes | `mqttbroker/lib/Mqtt.cpp`, `ConfigApplication.cpp` |
| Integrator | architecture | MQTTIntegrator mapping pipeline | How does received MQTT become mapped MQTT? | subscription, match, rule, immediate/delayed publish | pipeline | yes | Integrator Mqtt + mapper |
| Integrator | topic tree | Topic-tree matching | How do literals/`+`/`#` map to subscriptions? | recursive `topic_level`, wildcard matching, QoS | tree | yes | mapping schema + mapper extraction/matching |
| Integrator | mapping modes | Static, scalar, JSON, and fan-out mapping | Which mapping form should I use? | static/value/json and arrays | comparison/fan-out | yes | schema + mapper + current `mapfile.json` |
| Integrator | admin lifecycle | Draft, validate, deploy, history, rollback | What happens after an admin edit? | active/draft, validate, deploy, hot/reconnect, history/rollback | state/lifecycle | yes | `MappingAdminRouter.cpp`, Integrator Mqtt deploy |
| Bridge | assembly | Bridge definition to runtime clients | How does JSON become running broker-member clients? | bridge/member objects, client factory/context | config-to-runtime flow | yes | `BridgeStore.cpp`, `mqttbridge.cpp`, factory |
| Bridge | definition | Bridge-definition hierarchy | Where do network/session/topic fields belong? | bridges/brokers/network/mqtt/topics/prefix/store | hierarchy | yes | bridge schema |
| Bridge | forwarding | Prefix and forwarding construction | What exact output topic is produced? | bridge + source + destination + original topic | tokenized message path | yes | `Bridge.cpp` |
| Bridge | loops | Loop boundaries | What loop protection exists and what does not? | source exclusion, topology design, private reflection mechanism | cycle diagram | yes | `Bridge.cpp`, Bridge Mqtt, SNode.C MQTT behavior |
| Bridge | admin apply | Patch, close, activate, restart, SSE | What does PATCH do to active bridge flows? | staged config, close, persist/activate, restart, SSE | lifecycle | yes | `mqttbridge.cpp`, `BridgeStore.cpp`, `SSEDistributor.cpp` |
| CLI | command anatomy | MQTTCli command hierarchy | Where do remote/session/sub/pub options go? | instance, remote/http, session, sub/pub | annotated command tree | maybe | `mqttcli.cpp`, `ConfigSections.cpp` |
| Store | raw storage | Raw-envelope-first persistence | What exactly is recorded for every publish? | raw table fields, payload classification | data-record anatomy | yes | `MariaDbStorage.cpp`, `MqttMessage.h` |
| Store | projections | JSON/topic projection extraction | How does a typed row get its columns? | JSON Pointer, topic level, literal, required semantics | extraction diagram | yes | projection schema + `StoragePlan.cpp` + storage |

Total planned placeholders: **23**.

## Source map

## Whole suite

Primary:

- `CMakeLists.txt`
- `README.md` (operational topic mining only; claims revalidated)
- `lib/CMakeLists.txt`
- `lib/ConfigApplication.h`
- `lib/ConfigApplication.cpp`
- `lib/JsonMappingReader.*`
- `lib/MqttMapper.*`
- `lib/MqttMapperPlugin.h`
- `lib/MappingAdminRouter.*`
- `lib/mapping-schema.json`
- `mapfile.json`
- `mapfile-examples.json`
- `lib/plugins/`

SNode.C cross-checks:

- `src/utils/Config.cpp`
- endpoint/client/server configuration under `src/net/**/config`
- stream TLS configuration
- MQTT client/server context behavior where MQTTSuite's factory semantics require explanation.

## MQTTBroker

- `mqttbroker/CMakeLists.txt`
- `mqttbroker/mqttbroker.cpp`
- `mqttbroker/SocketContextFactory.*`
- `mqttbroker/lib/Mqtt.*`
- `mqttbroker/lib/MqttModel.*`
- broker implementation/model dependencies under SNode.C MQTT server
- `mqttbroker/websocket/SubProtocolFactory.*`
- `mqttbroker/html/`

These sources own listener creation, broker/session-store construction, Web routes, SSE, dashboard state, WebSocket upgrade, and embedded mapping.

## MQTTIntegrator

- `mqttintegrator/CMakeLists.txt`
- `mqttintegrator/mqttintegrator.cpp`
- `mqttintegrator/SocketContextFactory.*`
- `mqttintegrator/lib/Mqtt.*`
- `mqttintegrator/websocket/SubProtocolFactory.*`
- shared mapper/admin files above.

These sources own client creation, mapping attachment, session-store handling, delayed output, hot subscription changes, reconnect behavior, and the admin API.

## MQTTBridge

- `mqttbridge/CMakeLists.txt`
- `mqttbridge/mqttbridge.cpp`
- `mqttbridge/ConfigBridge.*`
- `mqttbridge/SocketContextFactory.*`
- `mqttbridge/config.json`
- `mqttbridge/config-orig.json`
- `mqttbridge/iot-config.json`
- `mqttbridge/lib/bridge-schema.json`
- `mqttbridge/lib/Bridge.*`
- `mqttbridge/lib/Broker.*`
- `mqttbridge/lib/BridgeStore.*`
- `mqttbridge/lib/Mqtt.*`
- `mqttbridge/lib/SSEDistributor.*`
- `mqttbridge/websocket/SubProtocolFactory.*`
- `mqttbridge/html/`

These sources own definition validation/defaults, member instantiation, forwarding/prefix semantics, config apply/restart, SSE, Web assets, and current protocol discrepancies.

## MQTTCli

- `mqttcli/CMakeLists.txt`
- `mqttcli/mqttcli.cpp`
- `mqttcli/SocketContextFactory.*`
- `mqttcli/lib/ConfigSections.*`
- `mqttcli/lib/Mqtt.*`
- `mqttcli/websocket/SubProtocolFactory.*`

These sources own instance enablement, session options, topic QoS suffix parsing, publish/subscribe behavior, output formatting, WebSocket target, and reconnect behavior.

## MQTTStore

- `mqttstore/CMakeLists.txt`
- `mqttstore/mqttstore.cpp`
- `mqttstore/SocketContextFactory.*`
- `mqttstore/lib/ConfigSections.*`
- `mqttstore/lib/Mqtt.*`
- `mqttstore/lib/MqttMessage.h`
- `mqttstore/lib/MariaDbStorage.*`
- `mqttstore/lib/StoragePlan.*`
- `mqttstore/lib/projection-schema.json`
- `mqttstore/websocket/SubProtocolFactory.*`
- `docs/mqttstore-user-guide.md`

These sources own database/session/subscription configuration, raw table creation/inserts, payload classification, projection validation/matching/extraction, and storage diagnostics.

## Current source/documentation discrepancies recorded by Step 6

These are intentionally reflected in the candidates instead of being smoothed into broader claims.

1. **Bridge `rc`/`l2`:** `bridge-schema.json` admits these protocol tokens and Bridge CMake requests corresponding optional SNode.C components, but `mqttbridge.cpp` has no runtime branches for either token. They are not documented as runnable network choices.
2. **Bridge direct Unix address:** the schema requires `un.path`; direct Unix stream runtime branches read `host`, while the Unix WebSocket branch reads `path`. Direct Unix Bridge deployment is not promoted as a verified usable path.
3. **Integrator `discover_prefix`:** present in the current mapping schema, but the reviewed mapper execution path does not consume it for matching/publication.
4. **Historical mapping examples:** `mapfile-examples.json` contains older shapes/names that do not match the current mapping schema. The Integrator candidate uses schema/current-source examples instead.
5. **Integrator `/ui`:** the router references a maintainer-local static build path and the Integrator target does not install UI assets. The candidate documents the API as the portable admin surface.
6. **Bridge installed HTML path:** CMake installs Bridge Web assets, but the runtime does not set that installed path as the default `--html-dir`. The candidate requires an explicit path when using shipped assets.
7. **Store user-guide instance enablement:** current Store startup creates client instances disabled; Step 6 examples add `--disabled=false` to the selected instance.
8. **Whole-suite dependency closure:** top-level CMake unconditionally builds MQTTStore, so the normal complete build requires the Store/database dependency rather than behaving as five standalone app builds.
9. **MQTTCli one-shot reconnect:** current client endpoints enable reconnect; the qualified publisher path can reconnect/republish after the first success. The candidates state the manual `Ctrl-C` boundary.
10. **License wording:** current README candidates use `MIT OR GPL-3.0-or-later`; stale comment/header wording is not copied into documentation.

## Validation expectations for the frozen candidate set

Before Step 6 closure, verify:

- exact six candidate paths plus this handoff;
- no public README changed;
- no actual figure filename or asset referenced as a Step 6 deliverable;
- every placeholder uses the prescribed `Figure placeholder` form;
- all 23 placeholders appear in the inventory above;
- relative links are correct for future publication targets;
- exact executable names;
- whole-suite build commands and recursive submodule clone;
- `C++20`, CMake, SNode.C, JSON, MariaDB dependency statements;
- canonical Broker + CLI first-success topic/payload/QoS;
- config precedence/persistence wording against SNode.C;
- current mapping field names and examples against `mapping-schema.json`;
- current Bridge definition fields against `bridge-schema.json`;
- current Store fields against `projection-schema.json`;
- Bridge-versus-Integrator distinction;
- CLI `--retain-session`, `##qos`, disabled-instance behavior;
- Store raw/projection separation and `required` semantics;
- exact license expression;
- no maturity/platform claims that exceed evidence.

This document is the internal handoff for later figure planning and independent final review. It is not a public README and does not authorize publication by itself.
