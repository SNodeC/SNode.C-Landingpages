# MQTTSuite evidence register

[← Shared facts](../FACTS.md) · [Proposal](PROPOSAL.md)

**Baseline:** public `master` at
[`52de563`](https://github.com/SNodeC/mqttsuite/commit/52de5631245c6318bfa5b7cca700f0754014f34d),
observed 28 August 2026.

## Claim ledger

| ID | Candidate public fact | State | Implementation/build evidence | Behavioral evidence required |
| --- | --- | --- | --- | --- |
| MQ-01 | MQTTSuite contains five applications: MQTTBroker, MQTTIntegrator, MQTTBridge, MQTTCli, and MQTTStore | Runtime-qualified for build | top-level CMake adds five subdirectories; each defines and installs `mqttbroker`, `mqttintegrator`, `mqttbridge`, `mqttcli`, or `mqttstore` | All five linked against installed current SNode.C master |
| MQ-02 | Source version is `1.0.1` and C++20 is required | Source-verified | top-level `CMakeLists.txt` | Do not infer current-master release status from the version |
| MQ-03 | The implementation targets MQTT 3.1.1 | Source-verified at protocol level | compatible SNode.C MQTT `Connect.h` defines protocol level `0x04`; broker model exposes level 4 | Run connect/publish/subscribe cases; no MQTT conformance suite is recorded |
| MQ-04 | MQTTBroker includes a bundled Web UI | Runtime-qualified for browser capture | installed `mqttbroker/html` assets plus broker HTTP/SSE implementation | Current-master dashboard loaded from the qualified broker and displayed only synthetic client/topic state |
| MQ-05 | MQTTIntegrator reads mapping schemas and transforms MQTT inputs | Source-verified | `lib/mapping-schema.json`, `JsonMappingReader`, mapper and plugin sources | Canonical mapping scenario is runtime-pending |
| MQ-06 | MQTTBridge represents configured broker groups and forwarding behavior | Source-verified | `mqttbridge/lib/Bridge`, `Broker`, `BridgeStore`, bridge schema | Multi-broker routing, filtering, session, and loop claims need scenario evidence |
| MQ-07 | MQTTCli provides MQTT publish/subscribe client paths | Runtime-qualified | `mqttcli` executable and client implementation | Local IPv4 broker/subscriber/publisher flow delivered the canonical JSON payload at QoS 1 |
| MQ-08 | MQTTStore supports raw storage and configured projections through MariaDB | Source-verified | `MariaDbStorage`, `StoragePlan`, projection schema and user guide; SNode.C `db-mariadb` component | MariaDB versions, migration, failure, and retention behavior remain pending |
| MQ-09 | Build metadata requires SNode.C `2.0.0` and nlohmann/json `3.7.0` | Runtime-qualified for exact heads | per-application CMake `find_package` calls | Current MQTTSuite master built against installed SNode.C `bf01683`; moving heads still require requalification |
| MQ-10 | License expression is `MIT OR GPL-3.0-or-later` | Source-verified with documentation defect | SPDX line and full `LICENSE-GPL-3.0-or-later`/MIT texts | Fix or avoid the contradictory LGPL sentence inside `LICENSE` |
| MQ-11 | The complete default build needs the recursive JSON-schema-validator submodule and SNode.C components including MariaDB; documentation, include-analysis, and format tools are optional | Source-verified; Debian package mapping verified | `.gitmodules`, top-level/per-application CMake, `mqttstore/lib/CMakeLists.txt`, and `cmake/{doxygen,iwyu,format}.cmake` | Requalify after changing dependency heads or default transport options |

## Test and CI evidence

No MQTTSuite test directory or build/test job is present on current master. The
workflows maintain the README table of contents and build a release archive with
submodules. Therefore none of the operational claims above is CI-qualified by
this repository yet. SNode.C's MQTT tests cover framework protocol primitives,
not the five MQTTSuite application workflows.

## Quick-start qualification

The isolated current-master build started only MQTTBroker's IPv4 listener on
`127.0.0.1:18885`, with `/dev/null` as the configuration file so no user
configuration or credentials entered the run. An MQTTCli subscriber requested QoS 1 for
`edge-lab/room-01/temperature`; a second MQTTCli process published
`{"value":21.7,"unit":"C"}` at QoS 1, and the subscriber printed the topic,
payload, QoS, retain, and duplicate state. Ctrl-C teardown was clean. No
MQTTSuite automated tests exist on this baseline.

## Open or excluded claims

- `production-ready`, `full MQTT`, MQTT 5, low footprint, and broad embedded
  suitability are not eligible.
- Per-application TCP/TLS/WebSocket/address-family support remains a matrix to
  qualify; source target presence alone is insufficient.
- QoS, retained messages, wills, sessions, wildcard, credentials, bridge-loop,
  and persistence wording must be narrowed to executed evidence.
- Platform, compiler, ARM/OpenWrt, service-management, MariaDB-version, support,
  security, and maturity claims remain open.
- V2 is a genuine three-terminal capture of the qualified message flow and V4 is a real
  current-master broker Web UI capture using synthetic state. V3 is explanatory;
  mapping, bridge, and storage behavior remain runtime-pending and must not
  borrow proof from the basic broker/CLI run or the diagram.
