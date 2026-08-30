# Step 5 visual storyboard — MQTTSuite

**Created:** 30 August 2026  
**Created by:** Step 4 — 1.4 MQTTSuite README + Visual Design  
**Public MQTTSuite baseline:** `52de5631245c6318bfa5b7cca700f0754014f34d`  
**Current SNode.C baseline:** `60f26d9ae54b3e9ffde954d0ca75e53f79f31d79`  
**Storyboard status:** INITIAL  
**Step 5A gate:** required before production  
**Human approval:** NOT YET REQUESTED

Every technical visual semantic in this file is marked:

**PENDING CODEX VALIDATION**

Step 5A must validate the semantics against current public source and, where the
visual is presented as runtime proof, against a fresh deterministic run. Step 5B
must not produce final Figma/export/capture assets until the corresponding
visual is marked `VALIDATED`.

The final in-page inventory is intentionally limited to three visuals:

1. V1 — the five-application MQTT message-flow centerpiece;
2. V2 — the real broker/subscriber/publisher first-success terminal proof;
3. V3 — the real MQTTBroker Web UI.

A second mapping/bridge/storage diagram is deliberately omitted. V1 can explain
those role distinctions without adding another proof-looking visual for behavior
that was runtime-pending in Step 3. A fourth decorative hero is also omitted.

## Shared visual rules

These rules apply to V1–V3:

- use the canonical synthetic topic: `edge-lab/room-01/temperature`;
- use the canonical synthetic payload: `{"value":21.7,"unit":"C"}`;
- use synthetic client names such as `landing-subscriber` and
  `landing-publisher`;
- no real usernames, credentials, hostnames, LAN addresses, home paths,
  certificates, shell history, or unrelated desktop/browser content;
- Figma is the editable source of truth for diagrams and final composed capture
  layouts;
- real UI/terminal content may be cropped, aligned, or annotated, but never
  redrawn or replaced with simulated application output;
- desktop/mobile compositions are separate when required for GitHub-width
  legibility;
- final publication images need information-bearing alt text and concise
  captions;
- visual meaning must survive grayscale/color-blind use and image-disabled
  rendering through adjacent text;
- MQTTSuite's green accent may be used after contrast validation, but labels,
  shapes, and arrow text must carry semantics independently of color;
- test GitHub light/dark rendering, mobile width, fallback fonts, and
  label-versus-neighbour clearance;
- publication assets live under `MQTTSuite/assets/`;
- editable/capture/provenance material lives under `MQTTSuite/assets/src/`.

---

# V1 — One MQTT message, five focused roles

**Status:** PENDING CODEX VALIDATION  
**Kind:** Figma technical figure  
**README role:** narrative centerpiece  
**Priority:** mandatory

## Purpose

Make the five applications and their real relationships understandable at a
glance. The figure must answer both what each application does and how a
representative MQTT message relates to those responsibilities.

MQTTBroker is central because the primary scenario starts there, but the visual
must not present MQTTSuite as a broker-only product.

## Exact content

Show one incoming publication near MQTTBroker:

```text
Topic
edge-lab/room-01/temperature

Payload
{"value":21.7,"unit":"C"}
```

Do not invent a transformed output payload in V1.

Show all five exact application names:

- MQTTBroker;
- MQTTIntegrator;
- MQTTBridge;
- MQTTCli;
- MQTTStore.

Supporting nodes may include `Publisher / device`, `Other MQTT broker(s)`, and
`MariaDB`.

Runtime relationships to depict:

1. `Publisher / device` → `MQTTBroker` — `MQTT publish`.
2. `MQTTCli` ↔ `MQTTBroker` — `publish`, `subscribe`, `inspect`.
3. `MQTTBroker` → `MQTTIntegrator` — `subscribed publication`.
4. `MQTTIntegrator` → broker endpoint — `mapped republish`; Step 5A validates
   the final destination shown.
5. `MQTTBroker` → `MQTTStore` — `subscribed publication`.
6. `MQTTStore` → `MariaDB` — `raw envelope`, with secondary label
   `optional typed JSON projection`.
7. Representative bridge path `MQTTBroker` → `MQTTBridge` →
   `Other MQTT broker(s)` — label MQTTBridge as
   `logical bridge · outbound MQTT clients`.

The bridge geometry must not look like a server accepting arbitrary inbound
bridge connections.

## Technical semantics

**PENDING CODEX VALIDATION**

Step 5A must confirm:

- MQTTBroker is the MQTT server/broker role;
- MQTTCli is an MQTT client capable of publish/subscribe/inspection;
- MQTTIntegrator is an outbound MQTT client that subscribes from mapper-derived
  topics, maps received publications, and republishes immediate or delayed
  results;
- the same mapping engine can also be embedded in MQTTBroker, but V1 must not
  draw a hidden `mqttintegrator` process inside MQTTBroker;
- MQTTBridge is a group of outbound MQTT clients organized into logical bridges;
- MQTTBridge forwards to other connected members, not immediately back to the
  origin connection;
- loop prevention is not depicted as a generic guarantee; if mentioned, use
  only bounded origin-reflection wording;
- MQTTStore inserts a raw envelope for every received PUBLISH and attempts typed
  projections only for JSON payloads;
- MQTT 3.1.1 is the protocol context;
- no Bluetooth RFCOMM/L2CAP;
- no transport-support badges or support-matrix implication.

## Evidence source

Primary handoff: `MQTTSuite/workflow/03-TECHNICAL-FACTS.md`, especially the
canonical project identity, MQTTBroker, MQTTIntegrator, mapping semantics,
MQTTBridge, MQTTStore, transport inventory, and Step 4 handoff constraints.

Current-head implementation anchors recorded by Step 3 include:

- `mqttbroker/lib/Mqtt.cpp`;
- `mqttintegrator/lib/Mqtt.cpp`;
- `lib/MqttMapper.{h,cpp}`;
- `lib/mapping-schema.json`;
- `mqttbridge/lib/{Bridge,Broker,BridgeStore,Mqtt}.cpp`;
- `mqttbridge/lib/bridge-schema.json`;
- `mqttcli/lib/{ConfigSections,Mqtt}.cpp`;
- `mqttstore/lib/{Mqtt,MariaDbStorage,StoragePlan}.cpp`;
- `mqttstore/lib/projection-schema.json`.

## What V1 proves / does not prove

Once validated, V1 may communicate the exact five roles, their implemented
relationship model, the distinction between transformation, bridging, CLI
interaction and persistence, and raw-envelope versus typed-projection storage.

It must not be treated as proof that all five ran together; mapping, bridge and
MariaDB paths passed an end-to-end runtime run; every transport combination is
supported; MQTT 5/full conformance exists; arbitrary cyclic topologies are safe;
private loop prevention interoperates with arbitrary brokers; MariaDB lifecycle
is managed; Bluetooth is available; or the toolkit is production-ready, secure,
lightweight, fast or small-footprint.

## Composition and assets

Desktop target: responsive SVG around `1200 × 760–820`, finalized in Figma.
MQTTBroker near center; publisher/device upper-left/top; MQTTCli left;
MQTTIntegrator right; MQTTStore lower-right with MariaDB; MQTTBridge lower-left
or bottom toward other broker(s); canonical message near ingress; short arrow
labels; small `MQTT 3.1.1` context label.

Mobile: separate vertical Figma composition around `620 × 1100–1350`; do not
scale down the desktop layout. Use explicit arrow labels and repeated broker
anchors if needed.

Expected assets:

- `MQTTSuite/assets/application-message-flow.svg`;
- `MQTTSuite/assets/application-message-flow-mobile.svg`;
- corresponding source/export snapshots under `MQTTSuite/assets/src/`;
- canonical editable Figma frame IDs recorded during Step 5B.

Draft alt text: MQTTSuite message-flow diagram showing MQTTBroker at the center,
MQTTCli publishing/subscribing, MQTTIntegrator mapping and republishing,
MQTTBridge forwarding selected publications between configured brokers, and
MQTTStore writing raw MQTT envelopes and optional typed JSON projections to
MariaDB.

Draft caption: Five separate applications around one MQTT 3.1.1 workflow:
broker, inspect, transform, bridge, and store.

---

# V2 — Broker + subscriber + publisher first-success proof

**Status:** PENDING CODEX VALIDATION  
**Kind:** real terminal capture + Figma composition  
**README role:** primary runtime proof  
**Priority:** mandatory

## Purpose and exact scenario

Show that a reader can start one local MQTTBroker, subscribe with MQTTCli,
publish the canonical message with another MQTTCli process, and see the delivered
QoS 1 message.

Step 5A must rerun the exact Step 3 command path against the then-current public
MQTTSuite and SNode.C heads.

- Broker: only one loopback plain-IPv4 MQTT listener; Step 3 used
  `127.0.0.1:18885`.
- Subscriber client ID: `landing-subscriber`.
- Subscription: `edge-lab/room-01/temperature`, QoS 1.
- Publisher client ID: `landing-publisher`.
- Publication topic: `edge-lab/room-01/temperature`.
- Payload: `{"value":21.7,"unit":"C"}`.
- QoS: 1.

Required visible success in the real subscriber output:

- delivered topic;
- pretty-printed JSON payload;
- `QoS: 1`;
- `Retain: false`;
- duplicate state.

Do not typeset a synthetic approximation of terminal output.

## Technical semantics

**PENDING CODEX VALIDATION**

Step 5A must confirm the exact commands still work, only the intended loopback
listener is exposed, both clients are MQTTCli, the message is delivered at QoS 1,
visible fields match current behavior, teardown is clean, no secret-bearing debug
content appears, and the capture does not imply MQTTSuite CI coverage.

Evidence: Step 3 `Shortest real first success`, `MQTTCli`, `MQTT protocol scope`,
and current-head status. Existing `MQTTSuite/assets/quick-start-terminal.png` and
capture automation are provenance only until the fresh rerun.

V2 proves only that validated local plain-IPv4 broker/CLI QoS 1 scenario. It does
not prove MQTT 5/full conformance, QoS 2, retain/will/session recovery, TLS/WSS,
IPv6/Unix, Integrator, Bridge, Store, broker credential authentication,
production readiness, performance or platform breadth.

## Capture/composition and assets

Use real terminals from the exact qualified binaries and record SHAs, commands,
terminal geometry/font and teardown in provenance. Use a generic shell prompt
and synthetic data.

Desktop preferred canvas: about `1600 × 820–900`; three readable regions with the
subscriber receiving the most weight: Broker, Subscriber, Publisher.

Mobile: art-directed stacked capture from the same run, about
`900 × 1500–1800`; order broker status, publisher command, subscriber result.
Do not shrink the desktop three-pane capture.

Expected assets:

- `MQTTSuite/assets/first-success-terminal.png`;
- `MQTTSuite/assets/first-success-terminal-mobile.png`;
- capture/provenance under `MQTTSuite/assets/src/first-success/` or the canonical
  existing capture-source location;
- Figma composition frame IDs recorded during Step 5B.

Draft alt text: Three terminal views showing a local MQTTBroker, an MQTTCli
publisher sending the edge-lab temperature JSON message at QoS 1, and an MQTTCli
subscriber receiving the same topic and payload.

Draft caption: First success: one local broker, one subscriber, one publisher,
and the `edge-lab/room-01/temperature` message delivered at QoS 1.

---

# V3 — MQTTBroker live dashboard

**Status:** PENDING CODEX VALIDATION  
**Kind:** real Web UI screenshot/capture, optionally composed/cropped in Figma  
**README role:** supporting product evidence  
**Priority:** mandatory

## Purpose and exact content

Show that MQTTBroker has a genuine browser dashboard backed by the current
broker model/SSE/API without letting the UI define the whole suite.

Capture the current-head `/clients` dashboard using deterministic synthetic
state. Prefer visible connected synthetic clients, the subscription for
`edge-lab/room-01/temperature`, and other broker state only when genuinely
visible and qualified. No private network/user information or real credentials.

If retained state is staged for screenshot usefulness, record that extra action
in provenance and do not imply it was part of V2. Do not include or present an
MQTTIntegrator UI.

## Technical semantics

**PENDING CODEX VALIDATION**

Step 5A must confirm `/clients` is the current route; the dashboard comes from
the current qualified MQTTBroker build; visible state matches staged synthetic
state; live/SSE behavior is only claimed if observed; mutating actions are only
claimed if separately qualified; the image does not imply broker Web API
authentication; and no maintainer-local/private state appears.

Evidence: Step 3 MQTTBroker, bundled Web UI, broker security boundary, and stale
claim corrections; implementation anchors under `mqttbroker/html/` and broker
HTTP routing. Existing `MQTTSuite/assets/broker-web-ui.png` is provenance and
should be recaptured unless Step 5A explicitly re-approves it.

V3 proves only that the dashboard is a genuine current-head product surface and
that the visible synthetic state exists. It does not prove all admin mutations,
remote safety, authentication, authorization from TLS, MQTT credential
verification, a suite-wide Web UI, a portable Integrator UI, mapping/bridge/store
behavior, platform breadth or production readiness.

## Capture/composition and assets

Desktop source: high-density browser capture around `1600 × 900`; preserve enough
application/browser context to establish a real UI while excluding bookmarks,
extensions, private URLs and unrelated desktop state. Never redraw application
controls or data in Figma.

For mobile README treatment, prefer `broker-web-ui-mobile.png` as an art-directed
crop/composition of the same qualified state, not a simulated responsive mobile
UI. Step 5A/5B may omit the mobile asset if the full screenshot remains legible;
record that decision.

Expected assets:

- `MQTTSuite/assets/broker-web-ui.png`;
- preferred `MQTTSuite/assets/broker-web-ui-mobile.png`;
- capture/provenance under `MQTTSuite/assets/src/broker-web-ui/` or the canonical
  existing source location;
- optional Figma crop/composition frame IDs recorded during Step 5B.

Draft alt text: MQTTBroker browser dashboard showing synthetic MQTT client and
subscription state for the edge-lab temperature topic.

Draft caption: MQTTBroker's real browser dashboard provides operational
visibility into the broker state shown here; it is supporting evidence for the
broker, not the identity of the whole suite.

---

# Explicitly omitted visual — second semantic diagram

**Decision:** OMIT

V1 already distinguishes map + republish, forwarding, and raw envelope + typed
projection. Step 3 did not runtime-qualify the mapping, bridge or MariaDB
scenarios, so another polished diagram risks looking like end-to-end proof. Add
one only if Step 5A establishes that V1 cannot preserve the required distinctions
at GitHub/mobile width, with an explicit reason and validated semantics.

# Step 5A validation checklist

Before changing any status to `VALIDATED`, Codex must confirm:

## V1

- [ ] all five exact application names and roles;
- [ ] every arrow direction;
- [ ] MQTTIntegrator subscribe/map/republish semantics;
- [ ] optional in-broker mapping is not confused with a child process;
- [ ] MQTTBridge outbound-client/logical-bridge ownership;
- [ ] forwarding to other members, not immediate origin connection;
- [ ] prefix/subscription wording;
- [ ] bounded/private loop-prevention language;
- [ ] MQTTStore raw-envelope-first and JSON-only typed projection;
- [ ] no Bluetooth;
- [ ] no transport-support overclaim;
- [ ] MQTT 3.1.1 wording;
- [ ] desktop/mobile filenames and responsive intent.

## V2

- [ ] fresh current-head MQTTSuite + SNode.C rerun;
- [ ] exact broker command/exposure boundary;
- [ ] subscriber and publisher commands;
- [ ] canonical topic/payload;
- [ ] QoS 1 delivery;
- [ ] current real subscriber output fields;
- [ ] clean teardown;
- [ ] no secret-bearing debug/log content;
- [ ] desktop/mobile capture plan.

## V3

- [ ] current-head dashboard route and build;
- [ ] synthetic state matches visible dashboard fields;
- [ ] no private data;
- [ ] current dashboard capture is fresh or explicitly re-approved;
- [ ] screenshot proof boundary;
- [ ] broker Web API security wording;
- [ ] no MQTTIntegrator UI claim;
- [ ] desktop/mobile crop strategy.

# Step 5B production handoff

After all retained visuals are `VALIDATED`:

1. create V1 in Figma with separate desktop/mobile frames;
2. rerun/capture V2 and compose real terminal regions in Figma;
3. capture V3 from the real qualified dashboard and create only honest
   crops/compositions;
4. export publication assets to `MQTTSuite/assets/`;
5. retain Figma node IDs, capture scripts/fixtures, exact SHAs, commands and
   provenance under this file and/or `MQTTSuite/assets/src/`;
6. validate fallback fonts, label clearance, light/dark GitHub rendering, mobile
   width, alt text, captions and image-independent comprehension;
7. record `Human approval: APPROVED` only after the user accepts the final
   visuals.

No final visual asset is produced in Step 4.
