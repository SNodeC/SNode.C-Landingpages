# Proposal — MQTTSuite Repository Landing Page

[← Working landing page](README.md) · [Launch roadmap](../README.md) ·
[Shared page system](../PAGE-SYSTEM.md)

This proposal defines MQTTSuite-specific content and visuals within the
approved shared page system. Shared editorial, accessibility, asset, capture,
and visual-placement rules are not duplicated here.

## Purpose

Present MQTTSuite as a coherent MQTT integration toolkit rather than a long list
of commands. The landing page must explain why five applications belong
together, show a realistic message flow, provide a fast first success, and make
protocol scope and operational limitations explicit.

## Audience and jobs to be done

### Primary audiences

- IoT and edge engineers deploying MQTT infrastructure;
- Linux/OpenWrt operators needing broker, bridge, translation, or storage;
- developers extending MQTT applications in modern C++.

### Secondary audiences

- home automation and self-hosting practitioners;
- students learning MQTT architecture;
- systems integrators connecting incompatible topic/payload conventions;
- evaluators comparing focused MQTT tools.

### Visitor questions

- Is this one application or a suite?
- Which component solves my problem?
- Which MQTT version and transports are supported?
- Can I run a broker and inspect it visually?
- How do mappings, bridging, loop prevention, and storage work?
- What is appropriate for production and what remains limited?

## Positioning

### Working headline

> Broker, bridge, translate, inspect, and store MQTT data at the edge.

### Supporting statement

> MQTTSuite combines five focused C++ applications built on SNode.C: an MQTT
> 3.1.1 broker, mapping-driven integrator, multi-broker bridge, command-line
> client, and MariaDB storage service—with TCP, TLS, WebSocket, IPv4/IPv6, and
> Unix-domain options where verified.

### Primary call to action

**Run the broker and publish your first message**

### Secondary calls to action

- Explore the five applications.
- Run the integration scenario.
- Open the broker Web UI.

## Page architecture

### 1. Hero

Include:

- MQTTSuite wordmark, stable version, and concise outcome statement;
- three restrained badges: release, CI, and license;
- a polished broker Web UI screenshot or five-application flow graphic;
- links to `Quick start`, `Applications`, and `Deployment`.

The first viewport must communicate that MQTTSuite is more than a broker.

### 2. Five-application suite

Use a visual flow and compact table:

| Application | Role | Typical first use |
| --- | --- | --- |
| MQTTBroker | MQTT 3.1.1 broker and optional Web UI | Accept local device connections |
| MQTTIntegrator | Topic and payload transformation | Normalize incompatible devices |
| MQTTBridge | Selective multi-broker routing | Connect sites or broker domains |
| MQTTCli | Publish/subscribe diagnostics | Test and automate message flows |
| MQTTStore | Raw-envelope and typed MariaDB persistence | Retain and query telemetry |

Every row links to a dedicated guide, not a huge anchor in the root README.

### 3. Quick start

The shortest supported path should:

1. install a released SNode.C dependency;
2. build/install a tagged MQTTSuite release;
3. start one plain local broker listener;
4. subscribe using MQTTCli;
5. publish a message in a second terminal;
6. show the expected subscriber output;
7. optionally enable/open the Web UI.

Commands must be tested verbatim on a clean supported distribution. Avoid
requiring users to understand every generated configuration option first.

### 4. A complete integration scenario

Use one scenario throughout the page and demo assets:

```text
Sensor topic/payload
        │
        ▼
MQTTBroker ── live Web UI
        │
        ▼
MQTTIntegrator ── normalize topic + JSON fields
        │
        ├────────► MQTTBridge ──► remote broker
        │
        └────────► MQTTStore ──► MariaDB
```

Provide synthetic input, mapping, output, and verification. This becomes the
shared screenshot/video scenario and the primary technical article.

### 5. Why MQTTSuite

Use evidence-backed differentiators:

- focused composable applications instead of one monolithic deployment;
- mapping-driven topic and payload translation;
- transport choices including local Unix-domain communication;
- broker Web UI and CLI diagnostics;
- C++/SNode.C extension path;
- embedded Linux/OpenWrt relevance where qualified.

Avoid comparisons to other brokers unless a fair, reproducible comparison is
published and maintained.

### 6. Protocol and transport scope

Publish two separate matrices:

1. **MQTT behavior:** 3.1.1 features, QoS levels, retain, will, persistent
   sessions, wildcards, authentication, and known limits.
2. **Transport:** TCP, TLS, WebSocket, secure WebSocket, IPv4, IPv6, Unix-domain
   sockets, and applicable client/server roles.

State clearly that MQTT 5 is not supported if that remains true. Do not use
generic “full MQTT” language.

### 7. Mapping and transformation

Explain mappings progressively:

- subscribe and republish;
- static topic/value mapping;
- scalar template transformation;
- JSON transformation;
- wildcard behavior;
- validation against the schema;
- error behavior and observability.

Show one minimal mapping inline and link to complete schema/reference docs.

### 8. Bridge and loop safety

Explain logical bridges, multiple brokers, selective topics, direction, and loop
prevention using a diagram. Document failure/reconnect behavior and configuration
validation at a level useful for evaluation.

### 9. Storage

Explain raw MQTT envelope storage separately from optional typed projections.
State MariaDB requirements, schema ownership, migration expectations, retention
responsibility, error handling, and data/security implications.

### 10. Deployment

Offer evaluated paths:

- Debian/Ubuntu source build and install;
- system configuration and persist-once workflow;
- service management where packaged;
- OpenWrt SDK/feed process for tested releases;
- container/demo environment if maintained.

Include a concise production checklist: TLS off-host, credentials, persistent
sessions, storage, logs, limits, configuration backup, and monitoring.

### 11. Architecture and ecosystem

Explain that MQTTSuite is implemented on SNode.C and link to the internal SNode.C
draft during development. Show application boundaries and shared framework
services without duplicating SNode.C internals.

### 12. Support, contribution, security, and licenses

Route usage questions, defects, security reports, mapping examples, application
extensions, and documentation changes. Explain the MIT/GPL choice accurately
and distinguish MQTTSuite licensing from SNode.C and bundled dependencies.

## Approved final section map

The detailed requirements above consolidate into the shared nine-section
product-page system:

1. `What MQTTSuite enables`;
2. `Quick start`;
3. `Five focused applications`;
4. `A complete integration scenario`;
5. `Capabilities and limitations`;
6. `Architecture and deployment`;
7. `Installation and compatibility`;
8. `Operational and quality evidence`;
9. `Documentation and project routes`.

Mapping, bridge, storage, protocol, transport, production, support, security,
contribution, and license requirements become concise subsections within this
map. They must not expand the page beyond the shared content target.

## Visual requirements

The shared visual language, dimensions, screenshot hygiene, theme behavior, and
source-asset rules come from the [page system](../PAGE-SYSTEM.md).

### Visual inventory and placement

| Slot | Asset | Exact placement | Required content |
| --- | --- | --- | --- |
| V1 — Hero | `assets/mqttsuite-hero.svg` | Immediately below the hero links | Equal visual treatment for MQTTBroker, MQTTIntegrator, MQTTBridge, MQTTCli, and MQTTStore in one suite composition; MQTT 3.1.1 visible; no implication that the suite is only a broker |
| V2 — First success | `assets/quick-start-terminal.png` | Directly after the broker/CLI quick-start expected output | Three panes showing MQTTBroker, an MQTTCli subscriber, and an MQTTCli publisher with one successful local message flow |
| V3 — Architecture | `assets/integration-scenario.svg` | At the beginning of `A complete integration scenario` | Synthetic sensor → MQTTBroker and Web UI → MQTTIntegrator → MQTTBridge/remote broker and MQTTStore/MariaDB, with MQTTCli as the verification tool |
| V4 — Product detail | `assets/broker-web-ui.png` | Immediately after the MQTTBroker entry in `Five-application suite` or its short proof paragraph | Real released Web UI with synthetic connected clients and topics from the canonical scenario; browser and desktop chrome cropped consistently |
| Social preview | `assets/social-preview.png` | Repository metadata | Five-application motif, MQTT 3.1.1 label, approved outcome statement, and IoT-green accent |

Use the shared `edge-lab/room-01/temperature` topic and
`{"value":21.7,"unit":"C"}` payload across commands, terminal captures, the
integration figure, Web UI, and later video. Use loopback endpoints in the
quick-start proof. Screenshots must contain no LAN addresses, usernames, tokens,
certificates, private device data, or unrelated browser content. A bridge-only
topology may be documented later, but it is not an additional launch-page visual
slot.

## Copy and format rules

- Spell application names exactly: MQTTBroker, MQTTIntegrator, MQTTBridge,
  MQTTCli, and MQTTStore.
- Keep MQTT 3.1.1 visible near the top.
- Use diagrams for flows and tables for capability comparisons.
- Keep the root page outcome-oriented; move exhaustive flags into reference docs.
- Use code fences with language hints and copyable commands.
- No more than three hero badges and no vanity counters.
- Avoid “production-ready” until the operational qualification is linked.

## Use of existing documentation

1. Treat the current live README as a read-only source of candidate facts,
   examples, commands, terminology, and documentation links.
2. Verify selected behavior against the recorded current-master SHA and supporting tests.
3. Rewrite all landing-page copy independently in this workspace; do not carry
   over the manual's structure or wording.
4. Link application, mapping, bridge, storage, transport, and deployment
   references rather than reproducing them in the landing page.
5. Do not modify the live local repository during this workflow.
6. Reject stale moving-branch, OpenWrt release-candidate, or unqualified
   production claims.

## Evidence checklist

- Current version and release notes.
- Clean install and runtime smoke tests.
- MQTT 3.1.1 conformance scope.
- QoS/session/retain/will integration tests.
- TLS and WebSocket test coverage.
- Loop-prevention tests and limitations.
- Mapping schema validation and canonical fixtures.
- MariaDB compatibility and migration behavior.
- ARM/OpenWrt tested versions.
- Security reporting and license analysis.

## Review scenarios

1. A new user starts broker, subscriber, and publisher without reading reference
   documentation.
2. An integrator chooses the correct application for payload transformation.
3. An operator finds TLS, persistence, and failure-behavior guidance.
4. An evaluator identifies MQTT 5 as unsupported without ambiguity.
5. A developer locates extension and contribution documentation.

## Implementation sequence

1. Freeze release, protocol scope, and tested transport matrix.
2. Qualify the minimal broker/CLI quick start.
3. Build and test the canonical integration scenario.
4. Capture final Web UI and terminal evidence.
5. Draft hero and five-application section.
6. Create protocol, transport, mapping, bridge, and storage summaries.
7. Migrate long reference content to structured documentation.
8. Add deployment, production, security, support, and license sections.
9. Run clean-machine, ARM/OpenWrt, link, and visual reviews.
10. Publish only after commands and claims match the recorded current-master SHAs.

## Acceptance criteria

- [ ] Visitors understand all five applications from the first two sections.
- [ ] The quick start produces a visible MQTT message in ten minutes or less.
- [ ] MQTT version and unsupported scope are explicit.
- [ ] Protocol and transport claims are tied to tests.
- [ ] The integration scenario works with released versions.
- [ ] Web UI screenshots match the shipped UI.
- [ ] Production checklist addresses TLS, persistence, storage, and monitoring.
- [ ] Long reference material remains discoverable outside the root narrative.
- [ ] Support, security, contribution, and licensing are clear.
- [ ] All links, commands, images, and dark/light rendering pass review.
- [ ] V1–V4 and the social preview match the approved inventory and placement.
- [ ] The final section count and prose weight meet the shared product-page target.

## Open decisions

- Stable release and exact SNode.C compatibility.
- MQTT conformance evidence suitable for publication.
- Supported OpenWrt versions and packaging ownership.
- Whether containerized evaluation belongs in the initial launch.
