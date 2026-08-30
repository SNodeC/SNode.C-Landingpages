# Step 5 visual storyboard — MQTTSuite

**Created:** 30 August 2026  
**Created by:** Step 4 — 1.4 MQTTSuite README + Visual Design  
**Validated:** 30 August 2026<br>
**Validated by:** Step 5A — 1.5A MQTTSuite Visual Technical Validation<br>
**Public MQTTSuite HEAD checked at execution:** `52de5631245c6318bfa5b7cca700f0754014f34d`<br>
**Public SNode.C HEAD checked at execution:** `60f26d9ae54b3e9ffde954d0ca75e53f79f31d79`<br>
**OpenWrt package-source HEAD checked at execution:** `c9378fe95f7c015752c748fc4ab012b585d294d1`<br>
**Storyboard status:** VALIDATED<br>
**Step 5A gate:** COMPLETE — Step 5B production may proceed<br>
**Human approval:** NOT YET REQUESTED

Public heads were checked directly at execution time rather than assumed from
Step 3. MQTTSuite and SNode.C remained at the SHAs above. Step 5A then built
both repositories in a new isolated qualification workspace, installed the
current SNode.C package, rebuilt all five MQTTSuite executables against it, and
reran the required broker/CLI and broker-dashboard scenarios. The read-only live
source repositories were not modified.

All three retained visuals are `VALIDATED`. Step 5B must preserve the evidence
class assigned to each visual: V1 is a current-head source-verified application
role model, V2 is a fresh runtime proof, and V3 is a freshly runtime-qualified
capture specification. `VALIDATED` authorizes production from these semantics;
it is not human approval of final visual design.

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
- V1 must carry the visible evidence label `Source-verified application role
  model · not an all-app runtime run`; arrow direction describes implemented
  message flow, not an assertion that all five applications ran together;
- V2 and V3 may use `Runtime-qualified` only for the exact scenarios recorded
  below;
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

## Validation environment

The fresh qualification used:

- Debian GNU/Linux forky/sid, x86-64;
- GCC/G++ 16.2.0;
- CMake 4.3.4;
- Ninja 1.13.2;
- OpenSSL 3.6.3, nlohmann/json 3.11.3 and MariaDB client library 3.4.9 as
  detected by CMake;
- a new local clone of each exact public head and a dedicated install prefix;
- MQTTSuite submodule `lib/json-schema-validator` at
  `f15f156c69bfea115267b189c0129462f6511913`.

Reproduction build shape:

```sh
cmake -S "$SNODEC_SOURCE" -B "$SNODEC_BUILD_DIR" -G Ninja \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_PREFIX="$QUALIFICATION_PREFIX" \
  -DSNODEC_BUILD_TESTS=OFF
cmake --build "$SNODEC_BUILD_DIR" --parallel
cmake --install "$SNODEC_BUILD_DIR"

git -C "$MQTTSUITE_SOURCE" submodule update --init
cmake -S "$MQTTSUITE_SOURCE" -B "$MQTTSUITE_BUILD_DIR" -G Ninja \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_PREFIX_PATH="$QUALIFICATION_PREFIX" \
  -DCMAKE_INSTALL_PREFIX="$QUALIFICATION_PREFIX"
cmake --build "$MQTTSUITE_BUILD_DIR" --parallel
cmake --install "$MQTTSUITE_BUILD_DIR"
```

This build establishes current-head compilation/installability in the named
environment and supplies the binaries used below. It is not a platform,
compiler, architecture or transport support matrix.

---

# V1 — One MQTT message, five focused roles

**Status:** VALIDATED<br>
**Kind:** Figma technical figure  
**README role:** narrative centerpiece  
**Priority:** mandatory<br>
**Evidence class:** current-head source-verified application architecture; not
an all-app runtime proof

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

Supporting nodes are `Publisher / device`, `Configured broker B`, and
`MariaDB`. The central MQTTBroker is representative configured broker A for the
Integrator, Bridge and Store paths.

Source-verified message relationships to depict:

1. `Publisher / device` → `MQTTBroker` — `MQTT publish`.
2. `MQTTCli` ↔ `MQTTBroker` — `publish · subscribe · inspect`.
3. `MQTTBroker` → `MQTTIntegrator` — `subscribed publication`.
4. `MQTTIntegrator` → the **same connected MQTTBroker** —
   `mapped republish on the same client connection`.
5. `MQTTBroker` → `MQTTStore` — `subscribed publication`.
6. `MQTTStore` → `MariaDB` — primary label `raw MQTT envelope first`, then
   secondary label `optional projection inserts for JSON payloads`.
7. Representative message path `MQTTBroker A` → `MQTTBridge` →
   `Configured broker B` — inbound label
   `selected by A-member MQTT subscription`; outbound label
   `forward to other connected member`.

For MQTTIntegrator, do not draw an unspecified second destination broker. The
standalone process subscribes and republishes through each instance's same
outbound MQTT client connection. Optional in-process MQTTBroker mapping is a
separate source capability and must appear, if mentioned at all, only as a
small note on MQTTBroker: `optional shared mapper in process`. It must not be a
nested MQTTIntegrator box or child-process line.

For MQTTBridge, arrows show publication direction while a visible ownership
label states `MQTTBridge owns outbound MQTT clients to A and B`. The bridge must
not look like a server accepting bridge clients or like a third broker. Use the
compact selection/prefix label `configured subscriptions select · configured
prefixes applied`. The exact forwarded topic construction is:

```text
logical-bridge prefix
+ source-member prefix
+ destination-member prefix
+ original MQTT topic
```

The bridge path must also say `not sent immediately back on the source member`.
Do not add a loop-safe shield, closed-cycle graphic or generic third-party
interoperability label. The private SNode.C reflection-suppression extension is
not required in this already-dense figure; if production includes a footnote,
its only allowed wording is `optional private SNode.C origin-reflection
suppression; non-standard MQTT extension`.

## Validated technical semantics

- **MQTTBroker** is the MQTT broker/server and owns accepted client sessions,
  subscription/retained state and publication distribution.
- **MQTTCli** is an MQTT client used to publish, subscribe and inspect. The
  two-headed arrow is client interaction with MQTTBroker, not process
  ownership.
- **MQTTIntegrator** is a separate outbound MQTT client process. It derives
  subscriptions from mapping configuration, maps received publications and
  republishes immediate or delayed results over the same connection. It is not
  a broker child process. The shared mapper may instead run inside MQTTBroker,
  but that in-process option is not standalone MQTTIntegrator.
- **MQTTBridge** is a logical bridge made from outbound MQTT client connections.
  Each member's configured subscriptions select incoming traffic. One received
  PUBLISH is forwarded to every other connected member with logical-bridge,
  source-member and destination-member prefixes prepended; payload, QoS and
  retain pass through. It is not immediately forwarded back over the exact
  source connection.
- Bridge origin-reflection suppression is bounded. Same-member immediate return
  is skipped in MQTTBridge. The separate `loop_prevention` setting uses a
  private, non-standard SNode.C protocol-level mechanism. Neither establishes
  arbitrary cyclic-topology safety or interoperability of that extension with
  arbitrary third-party brokers.
- **MQTTStore** is an outbound MQTT subscriber. Every received PUBLISH creates
  the raw-envelope insert attempt with source instance, topic, original payload,
  QoS, retain, DUP and packet identifier. Projection insert attempts happen
  only when the payload parses as JSON and a configured projection matches.
  Only raw-table auto-creation exists; projection-table migration, retention,
  backup, access policy, cross-insert atomicity and retry guarantees are not
  implied.
- The protocol context is **MQTT 3.1.1**. Do not write `MQTT`, `full MQTT`, MQTT
  5 or complete-conformance language without the version/boundary.
- IPv4, IPv6, Unix-domain, TLS, WS and WSS must not appear as tested/support
  badges. They are source-implemented paths outside V1's role-model purpose.
- Bluetooth RFCOMM/L2CAP are not current MQTTSuite transports and must not
  appear.
- The canonical topic/payload are synthetic and contain no credentials. The
  figure must not imply MQTTBroker authenticates MQTT username/password fields,
  that any admin API is authorized by TLS, or that configuration/log/storage
  state is secret-managed.

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

## What it proves

V1 communicates the exact five separate application identities, their
current-head implemented responsibility and message-direction model, the
Integrator/Bridge process boundaries, the difference between mapping and
forwarding, and MQTTStore's raw-envelope-first/JSON-projection distinction.

The V1 architecture remained source-qualified deliberately. Running
Integrator, Bridge and Store would not materially improve this role-selection
figure enough to justify adding three new runtime fixtures during Step 5A. V2
owns runtime proof.

## What it does not prove

V1 does not prove that all five applications ran together; that Integrator,
Bridge or MariaDB paths passed an end-to-end run; that publisher/device means a
qualified hardware device; that every source transport combination is tested or
supported; that MQTT 5/full conformance exists; that arbitrary cycles are safe;
that the private loop-prevention extension interoperates with arbitrary brokers;
that MariaDB schema lifecycle/retention/backup is managed; that Bluetooth is
available; or that MQTTSuite is production-ready, secure, lightweight, fast or
small-footprint.

## Composition and assets

Desktop target: responsive SVG around `1200 × 760–820`, finalized in Figma.
MQTTBroker near center; publisher/device upper-left/top; MQTTCli left;
MQTTIntegrator right with its mapped-republish arrow visibly returning to that
same broker; MQTTStore lower-right with MariaDB; MQTTBridge lower-left between
broker A and configured broker B; canonical message near ingress; short arrow
labels; small `MQTT 3.1.1` context label; and the visible architecture-evidence
label required above.

Mobile: separate vertical Figma composition around `620 × 1100–1350`; do not
scale down the desktop layout. Use explicit arrow labels and repeated visual
anchors for the same MQTTBroker only when needed, with a continuity label so
the repeated anchor is not mistaken for a second broker. The five roles and
architecture-evidence label must remain readable at GitHub mobile width.

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

Draft caption: Source-verified application roles around one MQTT 3.1.1 message;
the broker/CLI exchange is runtime-qualified separately in the next figure.

---

# V2 — Broker + subscriber + publisher first-success proof

**Status:** VALIDATED<br>
**Kind:** real terminal capture + Figma composition  
**README role:** primary runtime proof  
**Priority:** mandatory<br>
**Evidence class:** freshly runtime-qualified at the current public MQTTSuite
and SNode.C heads

## Purpose and exact scenario

Show that a reader can start one local MQTTBroker, subscribe with MQTTCli,
publish the canonical message with another MQTTCli process, and see the delivered
QoS 1 message.

Step 5A reran the exact Step 3 command path against MQTTSuite
`52de5631245c6318bfa5b7cca700f0754014f34d` rebuilt against SNode.C
`60f26d9ae54b3e9ffde954d0ca75e53f79f31d79`.

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

## Exact qualified commands

The commands below are the canonical Step 3 command shape. Step 5A executed the
same arguments from its isolated Release build (whose directory name was
`mqttsuite-build` rather than `cmake-build-release`). Step 5B must use the
canonical relative paths below or record an equivalently named isolated build
root; it must not substitute another broker or client.

Terminal 1 — broker:

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

Terminal 2 — subscriber:

```sh
./cmake-build-release/mqttcli/mqttcli --config-file /dev/null --log-level 4 \
  in-mqtt --disabled=false remote --host 127.0.0.1 --port 18885 \
  session --client-id landing-subscriber --qos 1 \
  sub --topic edge-lab/room-01/temperature
```

Terminal 3 — publisher:

```sh
./cmake-build-release/mqttcli/mqttcli --config-file /dev/null --log-level 4 \
  in-mqtt --disabled=false remote --host 127.0.0.1 --port 18885 \
  session --client-id landing-publisher --qos 1 \
  pub --topic edge-lab/room-01/temperature \
      --message '{"value":21.7,"unit":"C"}'
```

`ss -ltnp` during the run showed one broker listener only:

```text
LISTEN 0 5 127.0.0.1:18885 0.0.0.0:*
```

No broker HTTP/admin, TLS, IPv6 or Unix-domain listener was active.

## Current-run result and exact visible output

The broker reported `listener started`; the subscriber connected as
`landing-subscriber` and subscribed at QoS 1; the publisher connected as
`landing-publisher`; and the broker delivered the publication to the
subscriber. The stable subscriber result below is copied from the current run
with ANSI SGR color codes and the variable timestamp/log prefix removed only:

```text
MQTT Publish ┬ edge-lab/room-01/temperature │
│                                                │ QoS: 1 │ Retain: false │ Dup: false
│                                                ├ {
│                                                │   "unit": "C",
│                                                │   "value": 21.7
│                                                └ }
```

The current application pretty-prints JSON with `unit` before `value` even
though the command's compact input orders `value` first. Step 5B must capture
the real output and preserve that current order; it must not retype it in Figma.

One current behavior affects capture timing: after its publish callback closes
the connection, the publisher process reconnects and republishes roughly once
per second until stopped. The exact Step 3 command remains valid for one first
delivery, but Step 5B must press Ctrl-C in the publisher terminal immediately
after the first subscriber result and must exclude later repeated deliveries.
This is not MQTT DUP behavior: each observed delivery reported `Dup: false`.

Teardown order is publisher, subscriber, broker, each with Ctrl-C. The current
run terminated all three processes and closed `127.0.0.1:18885`; no process or
listener remained. Do not replace Ctrl-C with a killed/crashed terminal scene.

## Logging and credential boundary

`--log-level 4` is current info-level output. No username, password, will,
certificate or real credential was supplied. Broker connection-event JSON still
contains empty `username`, `password` and will fields and becomes visually
noisy. For final composition, capture/crop the broker pane at the initial
`listener started` state and give the subscriber result the most weight. Do not
raise the client or broker to debug/trace; current MQTTCli and MQTTBridge debug
paths can print credential/will values. Inspect the raw terminal buffers before
export even when the composed crop looks clean.

Existing `MQTTSuite/assets/quick-start-terminal.png` and its capture automation
remain provenance only. V2 must be recaptured from these current-head binaries.

## What it proves

V2 proves one local plain-IPv4 MQTT 3.1.1 path using one MQTTBroker, one MQTTCli
subscriber and one MQTTCli publisher: connection, QoS 1 subscription,
publication and delivered topic/payload with `Retain: false` and `Dup: false` in
the named Debian/GCC environment.

## What it does not prove

V2 does not prove MQTTSuite CI coverage; MQTT 5 or complete MQTT conformance;
QoS 2, retained-message, will, persistent-session or recovery behavior; TLS,
WSS, IPv6 or Unix-domain runtime behavior; Integrator, Bridge or Store behavior;
broker credential authentication; performance; production readiness; or broad
platform/compiler/architecture support.

## Capture/composition and assets

Use real terminals from the exact qualified binaries and record SHAs, commands,
terminal geometry/font, publisher-stop timing and teardown in provenance. Use a
generic shell prompt and synthetic data. Application output must remain a real
terminal capture; Figma may crop, align, mask variable timestamps consistently
or add external panel labels, but may not reconstruct terminal glyphs.

Desktop preferred canvas: about `1600 × 820–900`; three readable regions with the
subscriber receiving the most weight: Broker, Subscriber, Publisher.

Mobile: mandatory art-directed stacked capture from the same run, about
`900 × 1500–1800`; order broker status, publisher command, subscriber result.
Do not shrink the desktop three-pane capture. The mobile image must use the same
first delivery, not a separately typed command/result scene.

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

**Status:** VALIDATED<br>
**Kind:** real Web UI screenshot/capture, optionally composed/cropped in Figma  
**README role:** supporting product evidence  
**Priority:** mandatory<br>
**Evidence class:** freshly runtime-qualified current-head route, shipped assets,
staged broker state and observed SSE events; final publication image still
requires a Step 5B recapture

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

## Qualified route and shipped assets

Step 5A installed the current MQTTSuite build and served the dashboard from that
qualified MQTTBroker process. The observed route and asset responses were:

```text
GET /clients                     302  Location: /clients/index.html
GET /clients/index.html          200
GET /clients/mqtt-dashboard.css  200
GET /clients/mqtt-dashboard.js   200
```

The installed dashboard contained `index.html` (416 bytes),
`mqtt-dashboard.css` (37,591 bytes) and `mqtt-dashboard.js` (701,792 bytes).
The installed-and-served JavaScript matched the current source asset at SHA-256
`3fc1421a78194e7745ad71b048832e6e42e0124028f7c0668c1a68e03f978139` and
identified the dashboard as v439. This establishes that the observed page was
the dashboard shipped by the exact qualified build, not a maintainer-local
substitute.

The current source route remains `/clients`; `/api/mqtt/events` is its SSE
stream. Current source also exposes mutating broker API routes, but Step 5A did
not exercise them and V3 must not present them as qualified behavior.

## Exact staging commands

Step 5A ran one broker with only loopback plain-IPv4 MQTT and loopback plain-HTTP
listeners. All TLS, IPv6 and Unix-domain MQTT/HTTP surfaces were disabled:

```sh
./cmake-build-release/mqttbroker/mqttbroker --config-file /dev/null --log-level 3 \
  in-mqtt local --host 127.0.0.1 --port 18885 \
  in-mqtts --disabled \
  in6-mqtt --disabled \
  in6-mqtts --disabled \
  un-mqtt --disabled \
  un-mqtts --disabled \
  in-http local --host 127.0.0.1 --port 18080 \
  in-https --disabled \
  in6-http --disabled \
  in6-https --disabled \
  un-http --disabled \
  un-https --disabled
```

Stage one persistent subscriber:

```sh
./cmake-build-release/mqttcli/mqttcli --config-file /dev/null --log-level 3 \
  in-mqtt --disabled=false remote --host 127.0.0.1 --port 18885 \
  session --client-id landing-subscriber --qos 1 \
  sub --topic edge-lab/room-01/temperature
```

Then stage one retained publication with the canonical publisher identity and
fixture:

```sh
./cmake-build-release/mqttcli/mqttcli --config-file /dev/null --log-level 3 \
  in-mqtt --disabled=false remote --host 127.0.0.1 --port 18885 \
  session --client-id landing-publisher --qos 1 \
  pub --topic edge-lab/room-01/temperature \
      --message '{"value":21.7,"unit":"C"}' --retain=true
```

As in V2, the current publisher process reconnects and republishes until
stopped. Step 5B must press Ctrl-C immediately after the first retained event,
keep `landing-subscriber` connected, and only then open or refresh
`http://127.0.0.1:18080/clients`. That leaves deterministic dashboard state
without presenting a transient publisher as a continuously connected client.
The expected visible state is:

- connected client `landing-subscriber`;
- subscription `edge-lab/room-01/temperature` at QoS 1;
- one retained publication for that topic with the canonical JSON payload and
  QoS 1 wherever the current dashboard exposes its detail;
- activity entries for the synthetic connection, subscription and retained
  publication only.

A temporary 1600 × 900 validation capture from the live run showed the exact
current dashboard state: `Clients: 1`, `Topics: 3`, `Subscriptions: 1`,
`Retained: 1`, a green `Connected` indicator, `landing-subscriber` in the client
tree, and three activity cards. Those cards visibly reported client connected,
client subscribed to `edge-lab/room-01/temperature` at `QoS: 1`, and retained
message set for the same topic at `QoS: 1` with the unchanged compact payload
`{"value":21.7,"unit":"C"}`. This was a disposable validation frame outside the
repository, not a Step 5B publication asset.

Do not infer a topic-count meaning from slash-separated tree levels. Capture
the dashboard's real current counters and labels without explanatory rewrites.
After capture, close the browser/SSE client and terminate subscriber then broker
with Ctrl-C. Step 5A performed this teardown and left neither port listening.

## Observed live-update behavior

An SSE client attached to `/api/mqtt/events` during the run observed current-run
events equivalent to:

```text
ui-initialize
client-connected     landing-subscriber
client-subscribed    edge-lab/room-01/temperature  QoS 1
retained-message-set edge-lab/room-01/temperature  QoS 1
```

A fresh SSE connection after staging replayed that current client,
subscription, and retained state. V3 may therefore describe the dashboard as
live for those observed state changes. It must not generalize this result to
every event, reconnection edge case or mutating admin action.

## Security and capture boundary

No username, password, certificate, will or real credential was used. The
qualified Web listener was plain HTTP bound to loopback. Source inspection found
no application-level authentication layer on these MQTTBroker Web API routes;
the dashboard must not imply otherwise, and TLS/HTTPS must never be described as
authorization. Keep the screenshot at broker-overview level and exclude any
client-inspector field that could expose credential/will material, even when
empty. Use a clean browser profile and crop browser chrome so no bookmarks,
extensions, private paths or unrelated local state appear.

The existing `MQTTSuite/assets/broker-web-ui.png` is a real 1600 × 900 v439
dashboard capture aligned with the current MQTTSuite dashboard source and uses
the canonical subscriber/topic. It is approved as provenance only. Step 5B must
recapture the final desktop asset from the exact current-head installed build
and staged state above; the old image does not by itself establish the current
SNode.C build, exact retained fixture or complete capture provenance.

MQTTIntegrator's `/ui` route remains blocked as product evidence: Step 5A found
no material source change that establishes portable shipped packaging. Do not
include it or imply that MQTTSuite as a whole has one Web UI.

## What it proves

V3 proves that the current qualified MQTTBroker build ships and serves its v439
browser dashboard at `/clients`; that the dashboard receives broker state via
SSE; and that the current-run MQTT 3.1.1 synthetic connected client, QoS 1
subscription and retained-message state are available to that UI.

## What it does not prove

V3 does not prove every dashboard or admin mutation; Web API authentication;
remote deployment safety; authorization from HTTPS/TLS; MQTT credential
verification; browser compatibility breadth; a suite-wide Web UI; a portable
MQTTIntegrator UI; Integrator, Bridge or Store behavior; production readiness;
or broad platform, architecture or transport support.

## Capture/composition and assets

The desktop asset is a fresh high-density browser capture around `1600 × 900`.
Preserve enough application/browser context to establish a real UI while
excluding bookmarks, extensions, private URLs and unrelated desktop state.
Never redraw application controls or data in Figma.

A dedicated mobile asset is required because the full desktop dashboard becomes
unreadable at GitHub mobile width. Step 5A ran the same real state at a
620-pixel CSS viewport and observed the current responsive `Explorer`/`Activity`
tab layout with the same connected counters, synthetic client, topic and
retained-message branches. Step 5B must recapture that actual responsive product
state, preferably with `Activity` selected so the canonical subscription and
retained payload remain readable. It must not simulate the responsive UI, and
Figma must not invent tabs, controls, counters or data.

Expected assets:

- `MQTTSuite/assets/broker-web-ui.png`;
- `MQTTSuite/assets/broker-web-ui-mobile.png`;
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

# OpenWrt boundary retained

Public OpenWrt package source and MQTTSuite's `misc/owrt-install` helper exist.
The reviewed package source targets MQTTSuite tag `OpenWRT` at
`24b601818dcb650f28e35ede35a41e6cf6bc573b`, which is behind current master
`52de5631245c6318bfa5b7cca700f0754014f34d`. Its package set covers MQTTBroker,
MQTTIntegrator, MQTTBridge and MQTTCli. MQTTStore is not part of
`mqttsuite-full`. Current-master OpenWrt runtime, feed compatibility and target
architecture qualification remain unestablished. Step 5A adds no OpenWrt visual
or primary installation CTA.

# Step 5A validation checklist

Before changing any status to `VALIDATED`, Codex must confirm:

## V1

- [x] all five exact application names and roles;
- [x] every arrow direction;
- [x] MQTTIntegrator subscribe/map/republish semantics;
- [x] optional in-broker mapping is not confused with a child process;
- [x] MQTTBridge outbound-client/logical-bridge ownership;
- [x] forwarding to other members, not immediate origin connection;
- [x] prefix/subscription wording;
- [x] bounded/private loop-prevention language;
- [x] MQTTStore raw-envelope-first and JSON-only typed projection;
- [x] no Bluetooth;
- [x] no transport-support overclaim;
- [x] MQTT 3.1.1 wording;
- [x] desktop/mobile filenames and responsive intent.

## V2

- [x] fresh current-head MQTTSuite + SNode.C rerun;
- [x] exact broker command/exposure boundary;
- [x] subscriber and publisher commands;
- [x] canonical topic/payload;
- [x] QoS 1 delivery;
- [x] current real subscriber output fields;
- [x] clean teardown;
- [x] no secret-bearing debug/log content;
- [x] desktop/mobile capture plan.

## V3

- [x] current-head dashboard route and build;
- [x] synthetic state matches visible dashboard fields;
- [x] no private data;
- [x] current dashboard capture is fresh or explicitly re-approved;
- [x] screenshot proof boundary;
- [x] broker Web API security wording;
- [x] no MQTTIntegrator UI claim;
- [x] desktop/mobile crop strategy.

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

No final visual asset was produced in Step 5A.

# Raw capture handoff repair — Step 5B source material

The missing real-pixel handoff for V2 and V3 was materialized from the existing
Step 5A qualification build after confirming that public `master` remained at
MQTTSuite `52de5631245c6318bfa5b7cca700f0754014f34d` and SNode.C
`60f26d9ae54b3e9ffde954d0ca75e53f79f31d79`.

V2 raw terminal sources:

- `MQTTSuite/assets/src/first-success/broker-raw.png`;
- `MQTTSuite/assets/src/first-success/subscriber-raw.png`;
- `MQTTSuite/assets/src/first-success/publisher-raw.png`;
- provenance: `MQTTSuite/assets/src/first-success/README.md`.

V3 raw dashboard sources:

- `MQTTSuite/assets/src/broker-web-ui/dashboard-desktop-raw.png`;
- `MQTTSuite/assets/src/broker-web-ui/dashboard-620-raw.png`;
- provenance: `MQTTSuite/assets/src/broker-web-ui/README.md`.

These are raw source captures for Step 5B, not final publication assets. Step
5B must import/crop/compose and export them through the approved Figma workflow
without redrawing, retyping, or otherwise reconstructing terminal or product
content. The 620px dashboard source is a genuine responsive render at a 620 CSS-
pixel viewport, not a crop of the desktop capture. This repair does not change
the existing `VALIDATED` V1/V2/V3 semantics and does not grant human approval.
