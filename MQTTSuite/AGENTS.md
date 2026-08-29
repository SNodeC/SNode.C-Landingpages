# AGENTS.md — MQTTSuite landing page

These instructions supplement the root [`AGENTS.md`](../AGENTS.md) for all work
under `MQTTSuite/`. Follow the shared [page-system principles](../PAGE-SYSTEM.md),
the canonical [README workflow](../workflow/README-WORKFLOW.md), and the
[README governance](../workflow/README-GOVERNANCE.md). This directory's
[proposal](PROPOSAL.md) is research/design input rather than a fixed layout.

## What it solves

MQTTSuite addresses practical MQTT deployment and integration work that is
larger than a broker alone: accepting device connections, translating
incompatible topics and payloads, routing selected messages across brokers,
inspecting traffic from the command line, and persisting MQTT data for later
use.

## Project focus

Focus on the five applications as one coherent MQTT 3.1.1 toolkit and show how
an operator or integrator chooses and combines them. Lead with a visible local
message flow, then demonstrate the complete synthetic integration scenario.

Give MQTTBroker, MQTTIntegrator, MQTTBridge, MQTTCli, and MQTTStore appropriate
editorial treatment according to the reader journey. Use the Web UI as real
product evidence, not as a reason to present MQTTSuite as only a broker.

## Project boundaries

- SNode.C owns the underlying networking framework and configuration model;
  describe only the MQTTSuite-facing effect here.
- MQTTSuite is not one monolithic daemon. Preserve process and application
  boundaries.
- Do not turn the root landing page into five complete application manuals.
- Keep exhaustive connection instances, mapping schema fields, bridge JSON,
  SQL definitions, and OpenWrt SDK procedures in linked references.
- Do not present MQTT 5, universal transport combinations, production readiness,
  or small-footprint suitability without current evidence.

## Reader outcome

A qualified visitor should be able to:

1. name the five applications and choose the correct one for a task;
2. start a broker, subscribe, publish, and see a message within ten minutes;
3. understand the canonical broker/integrator/bridge/store flow;
4. identify MQTT version, tested transport scope, and important limitations;
5. find operational, security, storage, and extension documentation.

## Audience priority

1. IoT and edge engineers deploying MQTT infrastructure.
2. Linux and OpenWrt operators running broker, bridge, transformation, or
   storage services.
3. Systems integrators normalizing incompatible device topics and payloads.
4. C++ developers extending focused MQTT applications.

## Terminology

- Product: **MQTTSuite**.
- Applications: **MQTTBroker**, **MQTTIntegrator**, **MQTTBridge**,
  **MQTTCli**, and **MQTTStore**. Never change capitalization or insert spaces.
- Use **MQTT 3.1.1** with the version visible near the top.
- Distinguish **subscribe QoS** from **publish QoS**.
- Use **mapping** for topic/payload transformation, **logical bridge** for a
  configured broker group, and **raw envelope** versus **typed projection** for
  MQTTStore.
- Use exact executable names in commands: `mqttbroker`, `mqttintegrator`,
  `mqttbridge`, `mqttcli`, and `mqttstore`.

## Source and destination

- Read-only live source: `/home/voc/projects/mqttsuite/mqttsuite`.
- Working public-copy surface: `MQTTSuite/README.md`.
- Project specification: `MQTTSuite/PROPOSAL.md`.
- Eventual destination: `SNodeC/mqttsuite/README.md`.
- Candidate repository URL — verify: `https://github.com/SNodeC/mqttsuite`.
- Candidate API documentation — verify:
  `https://snodec.github.io/mqttsuite-doc/html/index.html`.

## Approved decisions

- Primary CTA: run MQTTBroker and publish the first message with MQTTCli.
- The five applications are all represented clearly, without forcing equal
  section or visual weight.
- The quick-start proof shows broker, subscriber, and publisher behavior.
- The canonical scenario uses `edge-lab/room-01/temperature` and
  `{"value":21.7,"unit":"C"}` consistently.
- The broker/integrator/bridge/store flow is the narrative centerpiece.
- Earlier hero, terminal-proof, integration-scenario, Web-UI, and bridge-topology
  concepts are candidate visuals rather than mandatory V1–V4 slots. Step 4
  chooses the visual inventory; Step 5 validates and finalizes it.

## Source-code alignment and proof

Every statement about an application, MQTT behavior, transport, mapping,
bridging, loop prevention, persistence, Web UI, or MariaDB storage must be traced
to the exact selected MQTTSuite and compatible SNode.C revisions. Record the
executable target, implementation or schema, configuration surface, and the
integration or runtime test that proves the stated behavior.

Configuration options or schema fields alone do not prove operational behavior.
Verify broker/client message flows, mappings, forwarding, session recovery, and
storage with reproducible scenarios. Verify transport and platform cells per
application role, and prove release availability with tagged artifacts.

## Candidate facts — verify

The live source currently suggests the following; verify all against the chosen
release, configuration, tests, and documentation:

- MQTT 3.1.1 broker and client behavior, including QoS, retain, will, sessions,
  wildcards, credentials, and related limits.
- TCP/TLS, IPv4/IPv6, Unix domain sockets, WebSocket/WSS, and Unix-domain
  WebSocket roles for the five applications.
- MQTTBroker Web UI and optional embedded integrator behavior.
- Static, scalar-template, and JSON-template mapping behavior.
- Multi-broker forwarding, prefixing, filtering, session stores, and loop
  prevention.
- Raw MQTT envelope storage and optional typed MariaDB projections.
- Linux, x86-64, ARM, OpenWrt, and Android/Termux claims.
- C++20 compiler minimums and exact SNode.C dependency.
- `MIT OR GPL-3.0-or-later` licensing.

## Commands and examples

Use this only as the build shape to qualify, not approved public copy:

- Reuse the isolated checkout's `cmake-build-release` directory for Release
  qualification and `cmake-build-debug` for Debug work while the SHA,
  compiler, generator, SNode.C prefix, submodule SHA, and CMake options remain
  unchanged.
- Keep the SNode.C install prefix and MQTTSuite build outside both live local
  repositories; never trade source isolation for incremental-build speed.

```sh
git submodule update --init --recursive
cmake -S . -B "$BUILD_DIR" -DCMAKE_BUILD_TYPE=Release
cmake --build "$BUILD_DIR" --parallel
ctest --test-dir "$BUILD_DIR" --output-on-failure
cmake --install "$BUILD_DIR" --prefix "$INSTALL_PREFIX"
```

The public quick start must use current compatible SNode.C and MQTTSuite master
heads and record their exact tested SHAs, start only the required local listener,
show an MQTTCli subscriber and publisher, include expected output, and explain
teardown. Do not copy the live README's long all-instances configuration
sequence without qualification.

## Common misconceptions

- MQTTSuite is more than MQTTBroker, but it is not one executable.
- MQTTIntegrator transforms and republishes; it is not a general-purpose stream
  processing platform.
- MQTTBridge uses outbound client connections; it is not another broker.
- MQTTStore does not make operator-defined schema migration or retention policy
  disappear.
- Loop-prevention options do not prove that every cyclic topology is safe.
- MQTT 3.1.1 support must not be described as generic `full MQTT` support.

## Open facts

- Exact release, maturity, release date, and version source.
- Exact compatible SNode.C release.
- MQTT conformance scope and tested QoS/session/retain/will behavior.
- Tested transport matrix for each application role.
- Current Web UI behavior and final screenshot state.
- ARM/OpenWrt targets, packaging owner, and service-management status.
- MariaDB versions, migration behavior, retention ownership, and failure modes.
- Canonical docs, support, security, roadmap, contribution, and release links.

## Validation

- Complete the broker/subscriber/publisher quick start from clean current-master
  checkouts and compare any approved terminal proof with actual output.
- Run the canonical `edge-lab` scenario and verify every runtime arrow used in
  approved Step 5 visuals.
- Confirm all five applications are represented clearly enough for project
  selection without forcing equal page-space quotas.
- Check MQTT 5 status and every protocol/transport claim explicitly.
- Review TLS, credentials, persistence, loop, storage, and monitoring language
  with the relevant evidence.
- Verify approved Step 4/Step 5 visuals, social preview if used, captions, alt
  text, links, and exact names.
