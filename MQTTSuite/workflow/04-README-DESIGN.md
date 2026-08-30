# Step 4 — MQTTSuite README + visual design

**Design date:** 30 August 2026  
**Workflow session:** 1.4 — MQTTSuite — README + Visual Design  
**Workflow stage:** accelerated Step 4  
**Public MQTTSuite baseline:** `52de5631245c6318bfa5b7cca700f0754014f34d`  
**Current SNode.C baseline:** `60f26d9ae54b3e9ffde954d0ca75e53f79f31d79`  
**Status:** README design complete; visual semantics await Step 5A Codex validation  
**Visual semantic status:** `PENDING CODEX VALIDATION`  
**Public README modified:** no

This is the self-contained editorial and visual-design handoff for the MQTTSuite
landing page. `MQTTSuite/workflow/03-TECHNICAL-FACTS.md` is the technical
authority. SNode.C is a reference for evidence discipline, prose quality,
responsive/Figma practice, and publication polish only; its section order and
visual composition are not a template for MQTTSuite.

The page must present MQTTSuite as five independently runnable applications that
form one coherent MQTT 3.1.1 toolkit. A reader should understand immediately
which application to choose, then see how those roles relate around a real MQTT
message.

## 1. Editorial center

### Headline direction

> **Five focused MQTT 3.1.1 applications for brokerage, integration, bridging,
> inspection, and storage.**

Supporting value proposition:

> MQTTSuite separates practical MQTT work into MQTTBroker, MQTTIntegrator,
> MQTTBridge, MQTTCli, and MQTTStore. Start with a local broker and CLI message
> exchange, then add transformation, cross-broker forwarding, or persistence
> where the workflow needs it.

This is Step 4 design copy, not frozen Step 6 prose. Step 6 may tighten it while
preserving the meaning and evidence boundary.

### First-viewport requirements

The opening should contain:

- `MQTTSuite` as the product name;
- MQTT 3.1.1 visibly near the headline;
- one sentence naming all five applications;
- primary CTA: **Run the first message**;
- secondary route: **Choose an application** or equivalent;
- restrained verified metadata only;
- no broker-only hero and no decorative network illustration.

The hero is deliberately text-led. The five-application identity is reinforced
immediately by the chooser and the message-flow centerpiece rather than by a
generic hero graphic.

## 2. Audience and reader intent

### Primary audience

1. IoT and edge engineers evaluating practical MQTT infrastructure.
2. Linux operators running broker, integration, bridge, CLI, or storage
   processes.
3. Systems integrators normalizing device topics/payloads or routing selected
   traffic between brokers.
4. C++ developers evaluating or extending the focused applications.

OpenWrt is a legitimate audience context because public package source and an
install helper exist. It is **not** a primary installation claim in this README:
the reviewed OpenWrt package source targets the older `OpenWRT` MQTTSuite tag,
packages four applications, omits MQTTStore from `mqttsuite-full`, and has no
current-master runtime/feed qualification.

### Questions the page must answer quickly

- **Need a broker?** MQTTBroker.
- **Need to transform and republish MQTT messages?** MQTTIntegrator.
- **Need to forward selected traffic between brokers?** MQTTBridge.
- **Need to publish, subscribe, or inspect traffic in a terminal?** MQTTCli.
- **Need to persist MQTT messages to MariaDB?** MQTTStore.
- **Need proof before reading internals?** Run the broker/subscriber/publisher
  path and inspect the real MQTTBroker dashboard.

The page must not imply that every deployment needs all five applications or
that they are modes of one executable.

## 3. Narrative thesis and centerpiece

The README's narrative thesis is:

> **One MQTT domain, five explicit responsibilities.**

MQTTBroker provides the broker/server role. MQTTCli gives the shortest human
entry into that broker. MQTTIntegrator subscribes, maps, and republishes.
MQTTBridge groups outbound MQTT client connections into logical bridges.
MQTTStore subscribes and persists a raw MQTT envelope first, with optional typed
JSON projections to MariaDB.

The centerpiece must explain application selection and message relationships at
the same time. MQTTBroker may be visually central because the canonical local
scenario starts there, but it must not become the identity of the whole suite.

## 4. README reader journey

The final README should use the following sequence. Step 6 may polish headings,
but it should preserve the journey and purpose.

### 4.1 Hero — what MQTTSuite is

Purpose:

- establish the five-application toolkit identity;
- make MQTT 3.1.1 explicit;
- route directly to first success and application selection;
- avoid maturity, performance, broad platform, and security claims.

Content should be compact: product name, headline, short value paragraph,
verified metadata such as C++20 and `MIT OR GPL-3.0-or-later`, and anchors to the
first message, application chooser, and source.

No in-page visual is required here.

### 4.2 Choose the application

Put application selection before architecture detail. Use a compact Markdown
table rather than five mini-manuals:

| Need | Application | Role in one line |
| --- | --- | --- |
| Accept and distribute MQTT client traffic | MQTTBroker | Broker/server with a real browser dashboard and optional in-process mapping |
| Transform topics/payloads and republish | MQTTIntegrator | Outbound MQTT client that subscribes from mapping rules, transforms, and republishes |
| Forward selected traffic between brokers | MQTTBridge | Outbound-client group connecting members of a logical bridge |
| Publish, subscribe, inspect | MQTTCli | Terminal MQTT client and fastest evaluation tool |
| Persist messages | MQTTStore | MQTT subscriber writing raw envelopes and optional typed JSON projections to MariaDB |

Keep this role-oriented. Transport matrices, schema fields, release state, and
configuration detail do not belong here.

### 4.3 One message, five roles

This is the narrative centerpiece and uses Visual V1 from `05-VISUALS.md`.

The canonical synthetic publication is:

```text
Topic:   edge-lab/room-01/temperature
Payload: {"value":21.7,"unit":"C"}
```

The figure should label behavior rather than internal implementation names:

- MQTTCli — publish / subscribe / inspect;
- MQTTIntegrator — subscribe → map → republish;
- MQTTBridge — forward selected broker traffic;
- MQTTStore — raw envelope → optional typed JSON projection → MariaDB.

Do **not** depict all five as one executed acceptance scenario. The broker/CLI
path is runtime-qualified by the existing landing-page evidence; mapping,
bridge, and storage relationships are current-head source-verified but remain
runtime-pending unless Step 5A qualifies them.

### 4.4 Run the first message

This is the fastest useful first success and the strongest direct runtime proof.
Use the already qualified Step 3 concept exactly:

1. start one MQTTBroker process with only one loopback plain-IPv4 MQTT listener
   enabled;
2. start one MQTTCli subscriber;
3. start one MQTTCli publisher;
4. subscribe/publish `edge-lab/room-01/temperature`;
5. publish `{"value":21.7,"unit":"C"}`;
6. use QoS 1;
7. show subscriber output containing the topic, pretty-printed JSON payload,
   QoS 1, retain false, and duplicate state;
8. use Ctrl-C teardown.

The public commands must preserve the Step 3 qualified command shape. Step 5A
must rerun it against the then-current MQTTSuite and SNode.C heads before the
final terminal capture is produced.

Use Visual V2 immediately after the commands or observed result. The README must
remain fully usable without the image.

Do not shorten the sequence through unexecuted defaults or a different client
merely for presentation convenience.

### 4.5 Beyond the first message — integrate, bridge, store

Once the reader has a working broker/CLI model, explain the three specialist
message-path responsibilities concisely.

#### Mapping

Keep only the landing-page semantics:

- MQTTIntegrator is an outbound MQTT client;
- subscriptions derive from mapping configuration;
- static payload mappings, scalar templates, and JSON templates are implemented;
- mapped outputs may change topic/payload and select QoS, retain, and delay;
- the same mapping engine can run in-process inside MQTTBroker.

Do not reproduce the full JSON schema, plugin API, history/draft/deploy mechanics,
or complete admin API.

#### Logical bridge

Keep these distinctions explicit:

- MQTTBridge is not a broker;
- it creates outbound MQTT client connections grouped into logical bridges;
- configured MQTT subscriptions select traffic;
- publications are forwarded to other connected bridge members, with the source
  implementation's prefix composition;
- origin-reflection suppression is bounded, and one mechanism is a private,
  non-standard SNode.C broker extension.

Do not claim generic loop safety, arbitrary third-party-broker interoperability,
a transformation engine, or a separate arbitrary filtering language.

The protocol-level high-bit detail belongs in deeper technical documentation,
not in the main reader journey.

#### Storage

Keep the storage model precise:

- MQTTStore subscribes and writes to MariaDB;
- every received PUBLISH takes the raw-envelope insert path;
- the raw envelope preserves source instance, topic, payload, QoS, retain, DUP,
  and packet identifier;
- typed projections are optional and attempted only for JSON payloads;
- projection-table creation/migration, retention, backup, access, and failure
  policy remain operator-owned where Step 3 did not establish them.

Do not imply automatic projection-schema lifecycle or database reliability
semantics that are not evidenced.

### 4.6 See the broker state

Use Visual V3: a genuine current-head MQTTBroker Web UI capture staged with
synthetic `edge-lab` state.

The screenshot is supporting product evidence, not the identity of the suite.
Surrounding text should describe only the visible/validated state: connected
clients, subscriptions, retained-message state, or live updates when actually
shown and qualified.

Keep the broker trust boundary close enough that the UI does not imply a remote
safe admin product: Step 3 establishes mutating Web API operations, permissive
CORS, and no application-level Basic Authentication layer in the reviewed broker
router. HTTPS/TLS does not itself provide authorization.

Do not show MQTTIntegrator's current `/ui` route as a portable shipped UI; the
current source still points to a maintainer-local absolute build directory and
no packaged UI artifact is established.

### 4.7 Fit check — protocol, transports, trust, release/platform

This is a compact evaluator section, not a qualification report.

#### Protocol

Safe wording:

- MQTTSuite targets MQTT 3.1.1.
- The primary runtime qualification covers CONNECT + subscribe + publish +
  delivered QoS 1 behavior.
- QoS 2, retained messages, wills, persistent-session recovery, offline queues,
  and `+`/`#` matching are source-implemented but not qualified by that
  first-success run.
- No MQTT 5 or full-conformance claim.

#### Transport

Explain evidence classes rather than publishing a broad support matrix:

- current source implements IPv4, IPv6, and Unix-domain direct MQTT plain/TLS
  roles plus MQTT-over-WebSocket/WSS roles across applications as recorded by
  Step 3;
- the principal runtime proof is plain IPv4 MQTTBroker + MQTTCli;
- source inventory must not be labelled a tested/supported matrix;
- Bluetooth RFCOMM/L2CAP must not appear as current MQTTSuite transports.

The full per-application source inventory belongs in deeper technical material
unless Step 6 needs a very compact fit-check table.

#### Security and state

Only the deployment-relevant boundaries should remain:

- MQTTBroker credential fields do not establish broker-side credential
  authentication;
- MQTTBroker and MQTTBridge admin surfaces require an explicit external/trusted
  exposure boundary; TLS is not authorization;
- MQTTIntegrator admin BasicAuth exists but current defaults are
  `admin` / `admin`;
- mapping/bridge/session configuration and debug logs can contain credentials;
- MQTTStore stores raw payloads unredacted and leaves data lifecycle/access
  policy to the operator.

Do not use `secure`, `production-ready`, `secret-managed`, or remote-safe.

#### Build, release, package, and platform

Keep the availability story exact:

- current source requires C++20 and a compatible current-head SNode.C build;
- current master has CMake build/install surfaces for all five applications;
- the latest public GitHub release is historical `v1.0.1` and publishes a source
  archive; current master is far ahead of that release, so neither the tag nor
  the still-present CMake `1.0.1` version identifies the current qualified
  technical state;
- no current-head binary distribution, container image, distribution repository,
  or broad package-manager publication is established for `52de563...`;
- public OpenWrt packaging source and `misc/owrt-install` exist, but the package
  source is tied to the older MQTTSuite `OpenWRT` tag, is six commits behind
  current master, packages Broker/Integrator/Bridge/CLI only, and excludes
  MQTTStore from `mqttsuite-full`;
- therefore do not describe that OpenWrt package set as the current five-app
  suite, claim current feed availability, or make it the primary first-success
  route without later qualification;
- the recorded current-master application qualification is one Debian x86-64
  GCC environment, not a broad platform/compiler/architecture matrix;
- ARM, Raspberry Pi, Android/Termux, and current-master OpenWrt runtime support
  remain open as publication claims.

Avoid version badges or platform badges that visually overstate maturity or
availability.

### 4.8 Choose the next route

End with task-based routing, not a generic ecosystem paragraph:

| If you want to… | Next route |
| --- | --- |
| Prove the toolkit locally | MQTTBroker + MQTTCli first-success path |
| Operate a broker | MQTTBroker source/configuration reference |
| Transform MQTT traffic | MQTTIntegrator mapping reference |
| Connect brokers | MQTTBridge configuration/reference |
| Inspect or script MQTT interactions | MQTTCli source/usage |
| Persist MQTT messages | MQTTStore storage/projection reference |
| Inspect implementation and current development | `SNodeC/mqttsuite` source and issues |
| Understand the networking foundation | SNode.C |

Only publish routes verified at finalization. Do not invent `SECURITY.md`,
`SUPPORT.md`, `CONTRIBUTING.md`, package, or release destinations. OpenWrt may be
linked later only with its explicit four-application/stale-package boundary or
after dedicated qualification upgrades it.

Closing direction:

> Start with MQTTBroker + MQTTCli; add MQTTIntegrator, MQTTBridge, or MQTTStore
> only for the transformation, routing, or persistence responsibility you need.

Step 6 may rewrite this while preserving the routing intent.

## 5. Product surface priority

The README should show product surfaces in this order:

1. five-application message-flow centerpiece;
2. broker/subscriber/publisher terminal proof;
3. genuine MQTTBroker Web UI.

No C++ code/API excerpt outranks these for an application toolkit. The strongest
MQTTSuite demonstration is operational behavior and role selection, not an API
listing.

## 6. README proof versus deeper documentation

### Keep in the README

- exact five-application identity and selection;
- MQTT 3.1.1 near the top;
- one representative application/message-flow figure;
- exact canonical topic/payload and the qualified broker/CLI path;
- concise mapping, logical-bridge, bounded loop-prevention, and
  raw-envelope-versus-projection distinctions;
- one evidence-bounded transport explanation;
- the important trust/credential/data boundaries;
- one real broker dashboard capture;
- source-build/release/package/platform limitations needed for fit evaluation;
- the narrow OpenWrt packaging fact only if it helps the evaluator and is kept
  clearly subordinate to current-master qualification.

### Keep out of the README

- exhaustive mapping schema fields and admin API endpoints;
- mapping history/draft/deploy internals;
- complete MQTT packet implementation paths;
- identifier-level bridge prefix formula unless a validated example needs it;
- the private loop-prevention bit encoding (`0x84`);
- complete session-store structures;
- full raw/projection SQL schemas;
- database retry/migration/retention analysis;
- per-option CMake inventories;
- full transport × application matrices;
- OpenWrt package Makefile/init-script detail and feed mechanics;
- CI forensic detail unless publication status requires one concise caveat;
- workflow evidence vocabulary.

The README should communicate evidence boundaries in natural product language,
not read like Step 3.

## 7. Visual inventory and rhythm

Use exactly three initial in-page visuals because each has a distinct job:

1. **V1 — application message flow:** comprehension and selection.
2. **V2 — first-success terminal proof:** direct runtime evidence.
3. **V3 — MQTTBroker dashboard:** genuine supporting product surface.

A second mapping/bridge/storage figure is intentionally omitted. V1 can carry the
semantic distinction, and Step 3 has not yet runtime-qualified the full mapping,
bridge, or MariaDB paths. A fourth decorative hero is also omitted.

Recommended text/visual rhythm:

1. short text-led hero;
2. compact application chooser;
3. wide responsive V1 centerpiece;
4. first-success explanation and commands;
5. compact V2 terminal proof;
6. concise mapping/bridge/store semantics;
7. V3 real broker dashboard;
8. compact fit-check and task routes.

Every visual must have an adjacent textual equivalent so image-disabled reading
remains complete.

## 8. Responsive and Figma direction

Reuse SNode.C's publication discipline, not its graphic composition:

- Figma is the editable source of truth for diagrams and composed captures;
- desktop and mobile are separately art-directed when scaling harms legibility;
- use GitHub `<picture>` with a mobile source around 600 CSS px and desktop
  fallback where responsive variants are needed;
- SVG for V1, PNG for real terminal/UI captures;
- mobile capture variants may crop/recompose the same qualified real run but may
  not redraw application or terminal content;
- use a restrained MQTTSuite green accent only after contrast validation;
- labels, shapes, and arrow text—not color alone—carry meaning;
- solid arrows mean real runtime communication relationships;
- no SNode.C dependency arrow is needed in the MQTTSuite centerpiece;
- provide information-bearing alt text and short captions;
- test GitHub light/dark rendering, mobile width, fallback-font containment and
  neighbour clearance, and image-disabled comprehension;
- keep editable/capture sources under `MQTTSuite/assets/src/`;
- do not hand-edit SVG geometry after Figma export.

Exact visual specifications and filenames live in
`MQTTSuite/workflow/05-VISUALS.md`.

## 9. Step 3 constraints that materially shaped the design

1. MQTTSuite is five separate runnable applications, not MQTTBroker plus helpers
   and not one daemon.
2. MQTT 3.1.1 is explicit; MQTT 5, `full MQTT`, and complete conformance are
   excluded.
3. The principal runtime-qualified flow is plain-IPv4 MQTTBroker + MQTTCli
   subscriber + publisher at QoS 1.
4. Mapping, bridge forwarding, and MariaDB storage are current-head
   source-verified but runtime-pending in the Step 3 qualification.
5. The same mapper powers standalone MQTTIntegrator behavior and optional
   in-process MQTTBroker mapping.
6. MQTTBridge is an outbound-client logical bridge, not a broker or mapping
   engine.
7. Loop prevention is bounded: immediate origin-connection suppression plus a
   private/non-standard SNode.C broker extension, not a generic cyclic-topology
   guarantee.
8. MQTTStore is raw-envelope-first; typed projections are optional and
   JSON-dependent.
9. IPv4/IPv6/Unix/TLS/WS/WSS breadth is a source implementation inventory, not
   a runtime-tested support matrix.
10. Bluetooth RFCOMM/L2CAP must not appear as a current MQTTSuite transport.
11. MQTTBroker's Web UI is genuine current-head evidence, but it proves the
   visible staged dashboard state rather than every mutating admin operation.
12. MQTTIntegrator's `/ui` route is not a portable shipped UI surface.
13. Broker/bridge admin exposure, default integrator credentials,
   credential-bearing files/logs, and raw stored payloads require explicit
   trust/data boundaries.
14. Current application runtime/platform qualification is one Debian x86-64 GCC
   environment; it does not establish broad Linux/ARM/Android/OpenWrt support.
15. Historical `v1.0.1` and CMake version metadata do not represent current
   master.
16. Public OpenWrt package source exists, but it targets the older `OpenWRT` tag,
   packages four applications, omits MQTTStore, and is not current-master runtime
   qualification or proof of current feed availability.
17. Upstream license wording must use `MIT OR GPL-3.0-or-later`; the separate
   OpenWrt package metadata must not overwrite the upstream dual-license fact.
18. No performance, footprint, small-device, security, production-readiness, or
   maturity claim is established.

## 10. Step 5A handoff

Step 5A validates visuals once; it does not redesign the README.

Required outcomes:

- validate V1/V2/V3 semantics in `05-VISUALS.md`;
- rerun the current-head broker/CLI first-success path before terminal capture;
- confirm the current MQTTBroker dashboard state and exact visible fields before
  screenshot production;
- decide whether mapping/bridge/store relationships remain source-only in V1 or
  gain deterministic runtime qualification;
- validate every arrow, ownership boundary, loop-prevention label, and
  raw-versus-projection label;
- validate responsive variants and filenames;
- mark each retained visual `VALIDATED` before Step 5B production.

OpenWrt does not need visual qualification for the current three-visual plan. If
later work promotes OpenWrt to a visible install/CTA path, that is a separate
qualification requirement: package-currentness, MQTTStore inclusion decision,
OpenWrt version/target/architecture, clean installation, feed availability, and
first-success execution must be established first.

## Final Step 4 status

**README design: COMPLETE.**  
**Initial visual storyboard: COMPLETE, pending Codex technical validation.**  
**MQTTSuite/README.md: intentionally unchanged.**
