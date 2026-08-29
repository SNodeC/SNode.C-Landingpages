# SNode.C Step 4 — README design

**Workflow stage:** Step 4 only
**Design date:** 29 August 2026
**Project:** SNode.C
**Output:** `SNode.C/workflow/04-README-DESIGN.md`

This document defines the editorial and information architecture for the new
SNode.C GitHub README. It is a design handoff, not the README itself and not a
visual-production specification.

The design is based only on repository handoff material, especially:

- `AGENTS.md`;
- `workflow/README-WORKFLOW.md`;
- `workflow/README-GOVERNANCE.md`;
- `workflow/01-REPOSITORY-AUDIT.md`;
- `workflow/02-ECOSYSTEM-POSITIONING.md`;
- `SNode.C/AGENTS.md`;
- `SNode.C/workflow/03-TECHNICAL-FACTS.md`;
- the current `SNode.C/README.md` and `SNode.C/PROPOSAL.md` as research only;
- `SNode.C/docs/architecture.md`, `SNode.C/docs/capabilities.md`, and
  `SNode.C/docs/configuration.md` as research/deeper-documentation candidates;
- the current SNode.C asset inventory as visual provenance only.

The old nine-section system, fixed word targets, mandatory V1–V4 slots,
four-visual quota, old asset filenames, and current README structure are not
design constraints.

The technical baseline inherited from Step 3 is public SNode.C `master` at
`bf01683a53b48220a840522e8ccaf3b48e58c240`, verified on 29 August 2026.
Step 5 and later stages must recheck freshness if public `master` moves.

## Design objective

Create a concise, technically authoritative GitHub landing page for experienced
C++ networking developers evaluating SNode.C.

The page should make one idea memorable:

> SNode.C gives network applications a recurring endpoint → connection →
> factory → per-connection context model, driven by an event loop.

The README should not lead with protocol inventory, project history, release
metadata, platform breadth, or ecosystem marketing. It should first make the
programming model legible, then give the reader a short verified path to a real
connection, then show what exists and where the evidence becomes narrower.

The page has six jobs:

1. identify SNode.C as a C++20 event-driven networking framework;
2. show why the object/lifecycle model matters to a C++ networking developer;
3. make `SocketServer` / `SocketClient`, `SocketConnection`,
   `SocketContextFactory`, `SocketContext`, and the surrounding event loop
   understandable without API-reference reading;
4. get the reader to the verified echo connection with minimal build
   bookkeeping;
5. summarize capability breadth without turning source presence into a support
   matrix; and
6. route evaluators to architecture, configuration, capability evidence,
   examples, issues/discussions, releases, and license information.

The design should feel like a framework README, not a launch page. It can be
visually polished, but every graphic must explain a concrete mechanism or show
real evidence.

## Audience and reader outcome

### Primary audience

**Experienced C++ networking and systems developers evaluating SNode.C as a
foundation for clients, servers, gateways, services, and protocol integrations.**

They are assumed to understand sockets, event-driven I/O, TLS, HTTP, CMake, and
basic client/server terminology. The README should not teach networking from
first principles.

Primary questions:

- What abstraction does SNode.C put around connection lifecycle?
- Where does application/protocol state live?
- How are server and client roles related?
- How is one connection associated with one application context?
- What drives callbacks?
- Can the model survive a protocol transition such as HTTP → WebSocket?
- Which paths have real tests or runtime qualification?
- How quickly can I build something that proves the framework works here?

### Secondary audiences

- C++ developers building custom application protocols.
- Systems developers comparing event-driven framework architectures.
- IoT, embedded-Linux, and OpenWrt-oriented engineers evaluating the source,
  while explicitly not inferring current platform support from that interest.
- Downstream SNode.C ecosystem contributors.
- Contributors, educators, and students studying layered event-driven network
  architecture.

### Intended reader outcome

After reading the README, a qualified visitor should be able to say:

1. “A configured `SocketServer` or `SocketClient` establishes a
   `SocketConnection`.”
2. “Its `SocketContextFactory` creates the per-connection `SocketContext` that
   owns protocol/application callbacks.”
3. “The event loop dispatches descriptor/timer-driven lifecycle and data events
   into that context.”
4. “The active context can be replaced while the underlying connection remains,
   which is used for HTTP-to-WebSocket upgrade.”
5. “IPv4, IPv6, and Unix-domain plain streams have both automated and preserved
   runtime evidence; TLS runtime evidence is currently one mutual-TLS IPv4
   echo arrangement; other capabilities have different evidence levels.”
6. “I know exactly where to run the first echo connection and where to go for
   deeper architecture, configuration, capability, source, issue, discussion,
   release, and license information.”

## Headline and value proposition

### Proposed headline

> **Event-driven network clients and servers in C++20**

Why this headline:

- it is factual at the Step 3 baseline;
- it states product category and language level immediately;
- it avoids qualitative claims;
- it avoids version/release confusion;
- it does not depend on Node.js comparison;
- it is broad enough to include raw streams and higher protocol components
  without claiming universal compatibility.

### One-sentence value proposition

> **Build C++20 network clients and servers around one recurring model: configure an endpoint, establish a connection, and attach per-connection protocol behavior while the event loop drives lifecycle and I/O.**

This is the recommended public-facing sentence. It is intentionally centered on
the programming model rather than a feature list.

### Supporting sentence, if the first viewport needs one

A second sentence may be used only if the hero otherwise feels too abstract:

> `SocketServer` and `SocketClient` establish `SocketConnection` objects; a `SocketContextFactory` then supplies the `SocketContext` that handles application-level events for each connection.

This is descriptive, not promotional, and gives the named API concepts before
the reader scrolls.

### Hero wording to avoid

Do not use “lightweight,” “fast,” “secure,” “stable,” “production-ready,”
“simple,” “highly extensible,” “complete,” “full support,” “cross-platform,” or
a current `2.0` release claim.

Do not use “Node.js for C++,” “C++ Express,” “Express compatible,” or any wording
that turns inspiration into compatibility.

## First viewport

The first viewport should be sparse and decisive.

### Composition

1. `# SNode.C`
2. Proposed headline.
3. One-sentence value proposition.
4. A restrained metadata line or badge row:
   - C++20;
   - current CI status if the badge is sourced from the real repository;
   - `MIT OR LGPL-3.0-or-later`.
5. Three text actions:
   - **Run the echo example** — primary action;
   - **Programming model** — direct anchor to the centerpiece;
   - **Architecture / examples** — one deeper route, not a large navigation
     bar.
6. The opening edge of the programming-model centerpiece should appear
   immediately after the hero. On a typical desktop GitHub viewport, the
   reader should see either the full first figure or enough of it to understand
   that the next section is the technical model.

### Deliberate omissions from the first viewport

- no release/version badge;
- no source version `2.0.0`;
- no platform badges;
- no protocol badge wall;
- no “supported on” list;
- no ecosystem logo strip;
- no performance claim;
- no large decorative hero illustration;
- no qualification SHA block before the reader understands the product;
- no API-reference link as a primary hero action because its freshness relative
  to the reviewed head is unresolved.

### Provenance placement

The exact reviewed SHA and verification date belong near the first-success or
capability evidence, not in the headline. A short note such as “README evidence
last verified against `bf01683` on 29 August 2026” is appropriate later in the
page. Later stages must refresh it if `master` moves.

## Reader journey

The intended reader journey is deliberately asymmetric. SNode.C is a framework,
so the page should lead with its model, not with a gallery or a broad product
catalog.

### Stage 1 — Orient

The first viewport answers:

- SNode.C is a C++20 event-driven networking framework;
- it builds clients and servers;
- its core value is the lifecycle/programming model;
- the reader can jump directly to a verified echo run.

Time target: roughly 10–20 seconds.

### Stage 2 — Understand the programming model

The first full section explains:

- server/client instance;
- connection;
- factory;
- context;
- event-loop dispatch;
- one active context per connection;
- context replacement without replacing the connection.

This is the page’s conceptual centerpiece and the main reason to continue
reading.

Time target: roughly 1–2 minutes.

### Stage 3 — Prove a real first success

The reader builds only the two relevant echo targets, starts the server and
client on loopback, and sees the verified listener/connection lines.

The section explicitly states that current default output proves listener and
transport connection, not visible application-payload reflection.

Time target: a few minutes on a prepared development system; do not advertise a
fixed “60 seconds” or similar time claim.

### Stage 4 — Understand breadth without over-reading it

A compact capability/evidence section tells the reader:

- which paths have runtime evidence;
- which higher layers are implemented and tested;
- which capabilities are source/build-only or have narrower evidence;
- what is not established as a support matrix;
- what current public release/package availability does and does not prove.

This gives enough information for a fit/no-fit decision without reproducing the
Step 3 ledger.

### Stage 5 — See the deeper architecture and extension point

A concise architecture section explains the layer responsibilities and uses the
HTTP → WebSocket context-replacement visual as the concrete example of why the
connection/context split matters.

Configuration is summarized here as an architectural consequence: named
instances expose API, file, and generated CLI surfaces with a verified
precedence. The full configuration manual stays outside the README.

### Stage 6 — Choose the next route

The final section routes the reader to:

- architecture;
- configuration;
- capability/evidence map;
- examples;
- generated API reference with an explicit freshness caveat or omission;
- Issues;
- Discussions;
- Releases;
- license;
- brief downstream ecosystem examples.

The page ends with next actions, not project history.

## Proposed README structure

The proposed public README has a hero plus five top-level sections.

This is not a template for the other ecosystem projects.

### Hero — SNode.C

**Purpose:** establish product category, language level, value proposition, and
the shortest two or three next actions.

**Content weight:** very short.

**Visual:** no separate decorative hero asset. The programming-model figure
begins immediately after the hero and supplies the first substantial visual.

---

### 1. Programming model

**Purpose:** answer “What programming model will I actually use?” before
capability breadth distracts from the framework’s identity.

**Content:**

- one introductory paragraph;
- Visual 1: programming-model lifecycle;
- a compact definition of the four public roles plus event loop;
- a small real-code excerpt showing the *feel* of a `SocketContext`, preferably
  the echo callbacks rather than template-heavy endpoint declarations;
- one precise note on single event-loop-thread dispatch;
- one sentence previewing context replacement.

**Reader takeaway:** application behavior lives in a per-connection context;
socket/event mechanics live outside it.

**Avoid:** constructor inventories, complete template type stacks, every callback,
all context methods, or a class diagram.

---

### 2. First verified connection

Recommended public heading:

> **Run the echo pair**

Alternative if a more evidence-led title reads better in Step 6:

> **First verified connection**

**Purpose:** let the reader prove a real server/client path without turning the
README into an installation manual.

**Content:**

1. one compact prerequisites statement;
2. clone/configure/build commands for only
   `echoserver-legacy-in` and `echoclient-legacy-in`;
3. server command;
4. client command;
5. expected output containing only verified default-visible lines;
6. one sentence explaining what the echo code does versus what the default log
   visibly proves;
7. Ctrl-C teardown;
8. optional short note that IPv6, Unix-domain plain, and one mutual-TLS IPv4
   echo path were separately qualified, with details linked out rather than
   reproduced inline;
9. Visual 2: real echo connection evidence.

**Reader takeaway:** the framework builds, listens, connects, and enters the same
connection/context lifecycle described above.

**Avoid:** optional dependency packages, all echo variants, certificate
generation, complete TLS commands, Debug build, full CTest, install, or
downstream-consumer instructions in this section.

---

### 3. Capabilities, evidence, and boundaries

Recommended public heading:

> **Capabilities and evidence**

**Purpose:** answer “What can I build with it?” while preserving the Step 3
distinction among implementation, build availability, automated tests, runtime
qualification, and public availability.

**Content:**

A compact table or grouped list, not a universal matrix.

Recommended columns:

| Area | Current implementation | Strongest current evidence | Boundary |
| --- | --- | --- | --- |

Recommended groups/rows:

- event loop and stream client/server model;
- IPv4 / IPv6 / Unix-domain plain streams;
- TLS stream layer;
- Bluetooth RFCOMM / L2CAP;
- HTTP/1.0 and HTTP/1.1;
- Express-style routing/middleware;
- WebSocket version 13;
- EventSource/SSE;
- MQTT 3.1.1;
- MQTT over WebSocket;
- configuration / installed CMake components;
- optional MariaDB integration only if the table remains concise.

The table should summarize evidence in human language, for example:

- “automated component tests + preserved runtime echo”;
- “internal TLS tests + one mutual-TLS IPv4 echo”;
- “source/build present; no hardware runtime qualification”;
- “protocol tests; no SNode.C network matrix”;
- “exact-head public CI passed root CTest”.

Do **not** expose the Step 3 `I/B/T/Q/A` codes unless Step 6 finds that a tiny
legend materially improves comprehension. The distinction matters; the internal
letter codes do not.

A short visible availability note should state, if still current at publication:

- the page tracks `master`;
- current master is source-buildable and locally installable;
- current master is not represented by a current tagged 2.0/current-head binary
  package;
- the latest public release is older than the reviewed master.

This note must be refreshed before publication and should not dominate the
section.

**Reader takeaway:** SNode.C has meaningful implemented/tested breadth, but the
evidence is intentionally scoped and not a Cartesian support matrix.

---

### 4. Architecture and extension points

**Purpose:** answer “Why is the programming model architecturally useful, and
where can I extend it?”

**Content:**

A compact prose/table decomposition:

1. event runtime;
2. address/network family;
3. physical stream/connection establishment;
4. plain or TLS connection mode;
5. server/client endpoint role;
6. application context.

Then explain:

- the event loop is the shared runtime;
- concrete endpoint types assemble a valid path;
- protocol/application behavior sits in `SocketContext`;
- custom factories/contexts are the first extension point;
- a connection can replace its active context;
- Visual 3 uses HTTP → WebSocket to show the real context-switch mechanism;
- configuration follows the endpoint hierarchy;
- installed CMake components allow downstream projects to consume selected
  pieces.

The section should use prose and a compact table for the generic layer model.
Do **not** create another generic stacked architecture asset just because the old
README had one.

**Precise event-loop wording requirement:**

If “single-threaded” appears, it must be qualified as:

> framework callbacks are dispatched synchronously on the thread calling
> `start()` or `tick()`; blocking or long-running callbacks delay other work on
> that event loop.

The README must not imply that applications are forbidden from creating threads,
and must not derive a performance or memory conclusion from the event model.

**Reader takeaway:** the connection/context separation is not cosmetic; it
supports reusable endpoint composition and real protocol transitions.

---

### 5. Documentation, examples, and ecosystem routes

**Purpose:** end with clear next actions without duplicating manuals.

Recommended route groups:

**Learn**
- Architecture guide.
- Configuration guide.
- Capability/evidence map.
- Example sources.

**Reference / project**
- Repository source.
- Releases.
- Issues.
- Discussions.
- License.

**API reference**
- Either:
  - include it with a short freshness note that its exact alignment with the
    reviewed August master is unresolved; or
  - omit it from the first publication until its revision/refresh process is
    established.
- It should not be the fact authority for current version, platform, protocol,
  or support claims.

**Built around SNode.C**
- MQTTSuite — downstream MQTT applications/toolkit.
- AISuite — downstream typed Codex integration/bridge.
- CodexUI — presentation project above the AISuite path and a native consumer of
  selected SNode.C transports.

Keep this ecosystem block to roughly three bullets plus one boundary sentence.
Do not draw an all-project runtime pipeline.

No final “History” section is required.

## Programming-model centerpiece

The programming model is the README’s defining section and Visual 1 is its
defining figure.

### Concepts that must be explicit

#### `SocketServer` / `SocketClient`

Present these as **configured endpoint handles / flow owners**.

- `SocketServer` starts the listen/accept path.
- `SocketClient` starts the connect path and owns client connection-attempt /
  reconnect scheduling where configured.
- They are not themselves the per-connection application logic.

Do not collapse them into a generic “socket” box.

#### `SocketConnection`

This must be visible in both prose and the main figure.

It is the established connection object and owns the stream-side mechanics and
state: addresses, connection identity, read/write behavior, queues/counters,
timeouts, and the currently active application context.

This is the important middle object that the old simplified
`SocketServer`/`SocketClient` → `SocketContextFactory` → `SocketContext`
diagram can make too easy to miss.

#### `SocketContextFactory`

Present the factory as the application-supplied creation boundary.

Its role is not “the protocol” itself. Its role is to create/select the
connection-local context after a connection has been established.

The main figure should label the decisive operation conceptually as:

`SocketContextFactory::create(SocketConnection*)`

Exact signature typography is a Step 5 choice; the semantic relationship is not.

#### `SocketContext`

Present the context as the object that owns application/protocol behavior for
one connection.

It receives lifecycle/data/error/signal callbacks and interacts with the
connection for send/read/timeout/shutdown/close behavior.

A short callback code excerpt is the best way to show how the model feels in
C++.

#### Event loop

The event loop is not another box in the endpoint chain. It is the execution
model **around** the chain.

Visual 1 should therefore represent it as a surrounding rail, timeline, or
dispatch band that feeds:

- listen/connect readiness;
- connection establishment;
- readable-data/lifecycle events;
- timers;
- context callbacks.

This is more accurate than placing “EventLoop” above or below the object chain
as if it were just another composable layer.

### Recurring lifecycle to preserve

The centerpiece must communicate this order:

1. the application constructs/configures a server or client instance;
2. the endpoint listens/accepts or connects;
3. SNode.C creates the established `SocketConnection`;
4. that endpoint’s `SocketContextFactory` creates the context for the connection;
5. the context attaches;
6. event-loop dispatch invokes lifecycle/data callbacks on the active context;
7. on final teardown, the context detaches because the connection closes; or
8. during a context switch, the old context detaches and a new one attaches while
   the connection remains.

### Server/client asymmetry

The figure should show server and client as two entry paths that **converge**
after connection establishment:

- server: listen → accept;
- client: connect;
- both: established `SocketConnection` → factory → `SocketContext`.

This avoids making the reader learn two different application models.

### What should be code rather than diagram

Use a short real echo-context excerpt to show:

- an `onConnected()` callback;
- `onReceivedFromPeer()`;
- read/reflect via the connection/context API.

Do not try to put full callback bodies inside the figure. The figure explains
ownership and lifecycle; code shows syntax and programming feel.

### Context replacement as the advanced proof

The main programming-model prose should mention, but not fully explain, context
replacement. Visual 3 later demonstrates the mechanism concretely with HTTP →
WebSocket.

This gives the README a satisfying progression:

**model → first connection → capability breadth → advanced consequence of the
model.**

## First-success presentation

### Editorial goal

The echo section is proof, not the centerpiece.

It should confirm that the reader can build and enter the model they just saw,
without forcing them through the complete framework build, install, dependency,
test, transport, and TLS story.

### Recommended evaluation path

Use the verified plain IPv4 loopback pair:

- target `echoserver-legacy-in`;
- target `echoclient-legacy-in`;
- server instance `echoserver`;
- client instance `echoclient`;
- address `127.0.0.1`;
- port `18001`.

The public README should use the current `master` checkout if that is still the
maintained landing-page policy, and should record the exact verified SHA in a
short evidence note. Do not require the reader to infer that an old tag equals
the current source.

### Build presentation

Show only the build surface needed for the two targets.

The README should not reproduce the old two-package-block prerequisite section.
For the primary audience, one short prerequisites line is enough:

- C++20 compiler meeting project metadata;
- CMake 3.18+;
- Ninja for the shown command path;
- Git/CA roots;
- pkg-config/pkgconf;
- OpenSSL development files;
- nlohmann/json 3.11+.

Step 6 may choose to provide one distro package command if it remains short and
is requalified. Optional BlueZ, libmagic, MariaDB, Curses, Doxygen, IWYU, and
formatting packages stay out of the first-success path.

### Run presentation

Use two short terminal blocks:

**Server**

`echoserver-legacy-in echoserver local --host 127.0.0.1 --port 18001`

**Client**

`echoclient-legacy-in echoclient remote --host 127.0.0.1 --port 18001`

Then show a compact expected-output block containing only the verified
default-visible signals, such as:

- `echoserver: listener started`;
- `echoserver: listening on '127.0.0.1:18001'`;
- `echoclient: connected to '127.0.0.1:18001' (127.0.0.1)`;
- one server/client `transport connected` line if the final excerpt remains
  legible.

Do not add a visible “Hello peer!” output line.

### Required honesty note

The section should say, compactly:

- source defines the client greeting and reflection behavior;
- the current default information-level terminal output does **not** print the
  echoed application payload;
- the visible result proves listener/transport connection;
- the pair continues reflecting data until interrupted;
- stop both with Ctrl-C.

This is not a weakness to hide. The README gains credibility by distinguishing
what the program does from what the default capture visibly proves.

### Secondary variants

The README may mention in one sentence that qualification also covered:

- IPv6 plain loopback;
- Unix-domain plain stream;
- one mutual-TLS IPv4 echo arrangement.

Do not reproduce all variant commands in the landing page. Link deeper evidence
or examples instead.

Bluetooth targets and broader TLS combinations must not be presented as
equivalent runtime-qualified variants.

## Capability presentation

### Principle

The README should communicate **breadth with evidence discipline**.

Do not build a support matrix whose cells imply that every address family,
plain/TLS mode, endpoint role, and application protocol combination has been
tested or is a supported product promise.

### Recommended presentation model

Use plain-language evidence levels in the table and surrounding prose:

- **implemented** — source/API exists;
- **build/configuration available** — target/option/component participates in the
  build under the documented condition;
- **automated evidence** — current tests exercise the stated behavior;
- **runtime-qualified** — a recorded independent run exists;
- **public availability** — a current release/package makes that exact revision
  available in that form.

The public table need not repeat all five labels in every row. It must simply
avoid collapsing them.

### Evidence emphasis by area

#### Strongest evidence: plain stream foundation

Surface prominently:

- IPv4 plain stream;
- IPv6 plain stream;
- Unix-domain plain stream.

These have current exact-head automated coverage and preserved echo runtime
evidence.

#### Narrower TLS evidence

State:

- generic OpenSSL-backed TLS stream implementation exists;
- TLS internal/state tests exist;
- separate runtime qualification is one mutual-TLS IPv4 echo arrangement.

Do not generalize to every family or every protocol.

#### Higher protocol layers

Safe headline-level protocol identifiers:

- HTTP/1.0 and HTTP/1.1;
- Express-style routing/middleware;
- WebSocket version 13;
- EventSource/SSE;
- MQTT 3.1.1;
- MQTT over WebSocket implementation.

The table should preserve their different evidence:

- HTTP and WebSocket have substantial plain IPv4 tests and smaller IPv6/Unix
  coverage;
- EventSource/SSE has plain IPv4 tests;
- MQTT has packet/lifecycle tests but no SNode.C network component matrix;
- MQTT-over-WebSocket has source/build presence but no targeted SNode.C network
  qualification in Step 3.

#### Conditional/source-only breadth

Keep Bluetooth RFCOMM and L2CAP visible but clearly labeled:

- source/build conditional on BlueZ;
- no targeted hardware runtime qualification.

If MariaDB is retained in the README capability table, label it optional and
build-conditional; do not make it a core networking differentiator.

#### Public availability

A visible boundary should prevent source version from becoming release
marketing:

- current source metadata says `2.0.0`;
- current master is not a tagged/current 2.0 release;
- latest GitHub release is older;
- no current-master binary/package availability was established.

The public README probably should omit the `2.0.0` number entirely unless a
later publication review resolves the metadata conflict.

### Capability information that should remain in prose

Use prose for:

- “composition is not a support matrix”;
- the exact meaning of single event-loop-thread dispatch;
- TLS security-policy responsibility;
- Node.js/Express non-compatibility;
- current release/package boundary.

Use the table for scoped factual breadth, not warnings.

## Architecture explanation strategy

The README should not recreate the old layer-architecture graphic.

The generic architecture is clearer as a compact table because the important
information is the **responsibility boundary**, not the shape of a stack.

Recommended conceptual rows:

| Layer | Question it answers |
| --- | --- |
| Event runtime | When is descriptor/timer work dispatched? |
| Address/network family | How is the local/remote endpoint represented? |
| Physical stream | How is the connection accepted/established and read/written? |
| Connection mode | Plain stream or OpenSSL-backed TLS? |
| Endpoint role | Server/listener or client/connector? |
| Application context | Which protocol/application behavior owns this connection now? |

Then use the context-upgrade visual to show one non-trivial consequence of this
architecture.

### Configuration as architecture, not as a manual

The README should make one compact point:

A named endpoint instance exposes one typed configuration hierarchy through:

1. C++ API defaults;
2. configuration file;
3. generated command-line sections;

with verified precedence:

**command line > configuration file > API/default.**

This is worth a short paragraph because it supports the idea that endpoint
policy remains outside protocol callbacks.

Do not include every configuration section, retry/backoff semantics, TLS option,
or inspection command. Link `docs/configuration.md`.

### Installed consumption

One short architecture/evaluation sentence may state that SNode.C installs
componentized CMake targets and current exact-head tests include selected staged
installed consumers.

Do not list every component name or imply every component combination was tested.

## Ecosystem references and their appropriate weight

The SNode.C README should spend very little page space on the wider ecosystem.

Recommended weight: **roughly 5–8% of total README prose**, near the end.

Use the sibling projects only as evidence that SNode.C is used beneath real
downstream software and as routes for readers with those domain needs.

### MQTTSuite

One sentence:

- downstream MQTT toolkit/application project;
- direct consumer of SNode.C networking/protocol components;
- its broker/integrator/bridge/CLI/store behavior belongs to MQTTSuite.

### AISuite

One sentence:

- downstream typed Codex integration/bridge project;
- direct consumer of SNode.C event-loop/transport/web infrastructure where
  configured;
- its protocol typing/controller/bridge semantics belong to AISuite.

### CodexUI

One sentence:

- user-facing native/browser project in the Codex path;
- its UI behavior belongs to CodexUI;
- do not imply that SNode.C is a browser runtime.

### Relationship boundary

If arrows are mentioned in prose, retain the two honest ecosystem tracks:

- SNode.C → MQTTSuite;
- SNode.C → AISuite → CodexUI.

Do not create an ecosystem visual on the SNode.C page. The organization profile
owns ecosystem navigation.

Do not imply that all four projects are one runtime, one release, or mandatory
dependencies.

## Calls to action and deeper routes

### Primary CTA

**Run the echo example**

This should link to the first-success section.

### Secondary CTA

**Understand the programming model**

This should link to the first section / Visual 1.

### Tertiary CTA

Choose one concise deeper route in the hero:

- **Browse examples**, or
- **Read the architecture**.

Prefer “Browse examples” if the README’s first section already contains enough
architecture to orient the reader.

### Deeper routes to preserve

At the end of the page, route to:

- `SNode.C/docs/architecture.md`;
- `SNode.C/docs/configuration.md`;
- `SNode.C/docs/capabilities.md`;
- current `master` example sources;
- repository source;
- Issues;
- Discussions;
- Releases;
- committed license files.

### API reference decision

The generated API reference exists, but Step 3 could not establish that its
published source revision matches the reviewed August master.

**Design decision:** do not place it in the first viewport. Include it only in
the final reference routes with a compact freshness caveat, or omit it until
alignment is established.

### Trust-route decision

There is no dedicated current `SECURITY.md`, `SUPPORT.md`, `CONTRIBUTING.md`, or
canonical roadmap.

The README may link Issues and Discussions, but it must not present them as a
support SLA or private vulnerability-reporting route.

## Visual inventory

Three in-page visuals are proposed. A social preview is outside this count and
is not designed in Step 4.

The three visuals are intentionally different:

1. a mechanism/lifecycle figure;
2. real runtime evidence;
3. a focused architecture transition.

No generic “hero architecture” or decorative layer stack is proposed.

### Visual 1 — Programming-model lifecycle

**Single communication goal**

Show how a configured server/client endpoint becomes an established
`SocketConnection`, how `SocketContextFactory` creates the per-connection
`SocketContext`, and how the event loop surrounds that lifecycle.

**What the reader should understand within about five seconds**

> Server and client differ in how they establish a connection, but once the
> connection exists they use the same connection → factory → context model, and
> the event loop drives the callbacks.

**Major elements**

- left/top split:
  - `SocketServer` → listen / accept;
  - `SocketClient` → connect;
- convergence on one clearly dominant `SocketConnection`;
- `SocketContextFactory` attached to the endpoint/flow and creating the context
  for the established connection;
- one active `SocketContext`;
- a lower or surrounding event-loop dispatch rail with descriptor/timer events
  and callback labels such as attach, readable data, error, detach;
- a small annotation that context is per connection.

**Desired hierarchy/composition**

Use a lifecycle/timeline composition rather than a conventional stacked boxes
diagram.

The `SocketConnection` should be the visual pivot. Server and client paths
converge into it. Factory/context sit immediately downstream. The event loop is
a supporting rail around the lifecycle, not another stack layer.

The figure should work at GitHub width without fine-print annotations.

**Why visual is better than prose**

The key insight is relational: two endpoint roles converge on one recurring
connection/context lifecycle while the event loop drives both. A diagram can
show convergence and surrounding dispatch simultaneously; prose explains these
one sentence at a time.

**Technical concepts the visual must preserve**

- endpoint exists before the established connection;
- `SocketConnection` is not skipped;
- factory creates the context for the connection;
- context is connection-local;
- event loop dispatch surrounds the lifecycle;
- server accepts while client initiates;
- no universal transport/protocol combination is implied.

**Must not imply**

- one global `SocketContext`;
- the factory creates the physical connection;
- the context owns the event loop;
- server and client are the same runtime object;
- every connection mode/address family is tested;
- worker-thread execution;
- Node.js/Express compatibility.

---

### Visual 2 — Real echo connection proof

**Single communication goal**

Show that the exact qualified IPv4 echo server and client were actually run and
reached listener/transport connection success.

**What the reader should understand within about five seconds**

> The server is listening on loopback and the client connects successfully;
> this is real terminal evidence from the qualified path.

**Major elements**

- two real terminal panes or one carefully composed two-role capture;
- generic `$` prompts;
- exact server command;
- exact client command;
- server listening line;
- client connected line;
- one or two transport-connected records if legible;
- no unrelated logs, home paths, hostname, username, shell history, or personal
  data.

**Desired hierarchy/composition**

The commands and the two success lines are the largest/clearest elements.
Crop aggressively. Avoid a 1600×900 canvas containing mostly empty terminal.

Step 5 may use a wide two-pane crop rather than the existing screenshot
composition if that improves GitHub-width readability.

**Why visual is better than prose**

The text block already tells the reader what to expect; the capture adds a
different kind of evidence: a genuine run of both processes. It should remain
only if the recapture is legible enough to add credibility rather than noise.

**Technical concepts the visual must preserve**

- IPv4 loopback;
- server and client roles;
- listener success;
- transport connection success;
- current default log level.

**Must not imply**

- visible echoed payload;
- one-shot request/response behavior;
- TLS;
- IPv6/Unix/Bluetooth qualification;
- throughput/performance;
- deployment readiness.

**Screenshot/evidence requirement**

Recapture from the exact Step 5 qualification revision, using the same real
targets and synthetic loopback settings. If `master` moves, requalify before
capture.

---

### Visual 3 — Context replacement on one connection

**Single communication goal**

Show that SNode.C can replace the active application context while retaining the
underlying `SocketConnection`, using HTTP → WebSocket upgrade as the concrete
implemented example.

**What the reader should understand within about five seconds**

> The connection stays; protocol ownership changes from an HTTP context to a
> WebSocket context.

**Major elements**

- one stable horizontal `SocketConnection` rail;
- persistent address / stream / optional connection-mode state indicated as
  staying in place;
- initial HTTP `SocketContext`;
- upgrade decision/factory;
- detach with `ContextSwitch`;
- WebSocket `SocketContext` attaching to the same connection;
- event-loop dispatch continues to the new active context.

**Desired hierarchy/composition**

Make the connection a continuous visual anchor across the whole figure. The
protocol contexts should look like replaceable layers attached above the same
connection, with the transition between them as the only directional emphasis.

Avoid a generic HTTP-box → WebSocket-box arrow that could look like a second
network connection.

**Why visual is better than prose**

The differentiator is identity continuity across a state transition. A visual
can make “same connection, different active context” immediately obvious in a
way a paragraph cannot.

**Technical concepts the visual must preserve**

- one active context at a time;
- old context detaches with context-switch semantics;
- new context attaches;
- underlying connection remains;
- HTTP-to-WebSocket is the concrete implemented use;
- event loop remains the dispatcher.

**Must not imply**

- transport reconnection;
- a second TLS handshake;
- a new socket;
- universal arbitrary hot-swapping with no application constraints;
- all HTTP/WebSocket family/TLS combinations are tested;
- plugin loading is a security boundary.

## What should be communicated visually versus in prose/code

| Information | Best medium | Reason |
| --- | --- | --- |
| Server/client → connection → factory → context lifecycle | Visual 1 | Relationship and convergence are faster to grasp spatially. |
| Event loop surrounding the lifecycle | Visual 1 + one prose sentence | Visual shows execution context; prose supplies the precise single-thread wording. |
| What a `SocketContext` feels like in C++ | Short code excerpt | Syntax/callback feel is better shown in real code than in labels. |
| First successful listener/client connection | Command/output text + Visual 2 | Text is copyable; real capture adds evidence. |
| Echo payload visibility boundary | Prose | A caveat must be explicit and searchable; do not hide it in a caption. |
| Capability/evidence distinctions | Markdown table | Tables are accessible, searchable, and easier to keep current than a graphic matrix. |
| Generic architecture layers | Compact Markdown table/prose | A separate stacked diagram would be generic and imply more combinability than needed. |
| HTTP → WebSocket context replacement | Visual 3 | Connection identity across transition is inherently spatial. |
| Configuration precedence | One prose line / tiny list | `CLI > file > API/default` does not justify another figure. |
| Ecosystem relationships | Brief prose links | The organization profile, not SNode.C, owns ecosystem navigation. |
| Release/platform/security limitations | Prose | They must remain explicit, precise, and easy to update. |

## Content deliberately kept out of README

The README should link out or omit the following.

### Detailed API and lifecycle mechanics

- exhaustive constructors and template parameters;
- callback signature catalog;
- every `SocketConnection` method;
- queue/high-low watermark semantics;
- timer and graceful-shutdown ordering;
- retry/backoff equations;
- all lifecycle edge cases;
- detailed `DetachReason` behavior beyond the context-switch distinction.

Destination: architecture/API documentation.

### Full configuration reference

- every instance/section key;
- all socket options;
- complete timeout/retry/reconnect options;
- logging/daemon controls;
- every TLS OpenSSL option;
- config-writing details;
- deployment checklist.

Destination: `SNode.C/docs/configuration.md` or maintained canonical replacement.

### Full build/dependency inventory

- all optional dependency package names;
- Doxygen/Graphviz/IWYU/formatting tools;
- complete CMake option list;
- every exported CMake component;
- CPack internals;
- detailed package generation rules.

Keep only what the first echo build needs and one short installed-consumer note.

### Qualification bookkeeping

- full Step 3 evidence ledger;
- all test names;
- exact CI job internals;
- every audit link;
- detailed host package versions;
- complete downstream all-master build history.

Destination: capability/evidence documentation.

### Complete protocol implementation detail

- HTTP parser edge cases;
- all WebSocket frame limits/extensions;
- MQTT packet/state details;
- SNI maps;
- dynamic loader symbol/path mechanics;
- MariaDB API details;
- Unix peer credential details.

### Migration and compatibility internals

- full 1.x → 2.0 migration instructions;
- ABI/SOVERSION discussion;
- package compatibility rules.

Link the migration document if needed from a dedicated migration/reference route,
not the main narrative.

### Unsupported publication material

Keep entirely out until resolved:

- benchmarks;
- memory/footprint comparisons;
- broad platform matrices;
- support-policy promises;
- security-policy promises;
- maturity labels;
- current 2.0 release/package instructions.

## Required limitations and claim boundaries

These boundaries are part of the README design, not footnotes to be removed for
tone.

### Visible limitations the README should retain

1. **Composition is not a support matrix.**
   Source breadth does not prove every family × connection mode × protocol
   combination.
2. **Current strongest runtime evidence is scoped.**
   IPv4, IPv6, and Unix-domain plain echo paths were qualified; TLS runtime
   evidence is one mutual-TLS IPv4 arrangement; Bluetooth has no hardware
   runtime qualification.
3. **Protocol versions are bounded.**
   HTTP is 1.0/1.1; WebSocket is version 13; MQTT is 3.1.1.
4. **Single event-loop-thread dispatch has an operational consequence.**
   Framework callbacks run synchronously on the loop thread; blocking callbacks
   delay other loop work.
5. **TLS is a mechanism, not a deployment security policy.**
   Peer/hostname verification and certificate/trust/key/cipher policy remain
   application/operator responsibilities.
6. **Current master availability is not a current 2.0 release/package claim.**
   Source version/release metadata are unresolved and must not be collapsed.
7. **Platform breadth is unresolved.**
   One current public Linux/GCC CI lane and one Debian/x86-64 Release
   qualification do not establish broad Linux, ARM, OpenWrt, Android, or other
   platform support.
8. **No performance/footprint conclusion is available.**
9. **Node.js/Express are inspiration/style boundaries only.**
10. **Downstream application behavior belongs to the downstream project.**

### Claims or wording explicitly forbidden by Step 3

The README and visuals must not claim or imply:

- lightweight;
- fast;
- secure;
- stable;
- production-ready;
- complete;
- full support;
- “supports every combination”;
- current/released `2.0.0`;
- a current-head binary/package;
- ABI/API stability or a forward compatibility policy;
- HTTP/0.9;
- HTTP/2;
- MQTT 5;
- Node.js compatibility;
- JavaScript or npm compatibility;
- Express compatibility;
- universal address-family × TLS × protocol compatibility;
- automatic TLS hostname verification;
- automatic production certificate policy;
- broad Linux support;
- Debian/Ubuntu support as a distribution range;
- current Clang support beyond the source minimum check;
- ARM/Raspberry Pi support;
- current OpenWrt target support;
- Android/Termux support;
- other-platform support;
- a visible echoed application payload in the current default terminal capture;
- current API-site alignment with the reviewed master;
- a canonical security policy that does not exist;
- a support policy/SLA that does not exist;
- a contribution guide that does not exist;
- a roadmap route that does not exist;
- downstream MQTTSuite, AISuite, or CodexUI behavior as SNode.C capability.

### Wording that requires precision rather than prohibition

**Single-threaded:** only use with the exact event-loop-thread meaning described
above.

**Composable:** attach only to concrete source mechanisms and immediately avoid
a universal-matrix implication.

**Express-style:** always make clear that this describes routing/middleware
concepts, not compatibility.

**TLS:** describe as an OpenSSL-backed connection mode with scoped evidence, not
as a security adjective.

**Supported:** prefer `implemented`, `tested`, `qualified`, or `available` with
scope. If `supported` is ever used later, it requires an explicit maintainer
support policy that Step 3 did not find.

## Decisions deferred to Step 5

Step 4 fixes the communication goals and semantics. Step 5 decides the final
visual implementation.

### Shared visual-system choices

Step 5 must resolve:

- exact SVG/PNG dimensions;
- typography and label scale at GitHub width;
- final foundation-blue accent value after light/dark contrast testing;
- neutral stroke/background treatment that works in GitHub light and dark mode;
- whether one neutral SVG works in both themes or theme-specific variants are
  required;
- final border/arrow/shape grammar;
- exact asset filenames;
- alt text and captions;
- editable-source format under `SNode.C/assets/src/`;
- whether any figure needs a separate mobile simplification.

### Visual 1 choices

Step 5 must decide:

- horizontal lifecycle versus shallow left-to-right timeline;
- exact way to show the event loop as a surrounding rail without visual clutter;
- whether callback labels are textual or icon-assisted;
- whether `SocketContextFactory::create(SocketConnection*)` appears in full or
  as `create(context)`;
- how to show per-connection multiplicity without drawing several dense copies;
- whether the small real C++ code excerpt remains separate from the figure or is
  visually paired with it in README layout.

Step 5 must **not** change the semantic order
endpoint → connection → factory → context.

### Visual 2 choices

Step 5 must decide:

- whether a recaptured two-pane terminal is sufficiently informative at GitHub
  width;
- exact crop and terminal geometry;
- whether to show transport-connected lines in both panes or only the clearest
  diagnostic lines;
- whether the command line appears in the image when the same command is already
  visible as copyable Markdown;
- the exact provenance note.

If the real capture remains too sparse or log-dense after recapture, Step 5 may
recommend dropping Visual 2 and using only the copyable expected-output block.
That would reduce the page to two in-page visuals and still satisfy the design
goal. It must not replace the missing evidence with a fabricated “successful
echo payload” graphic.

### Visual 3 choices

Step 5 must decide:

- exact representation of stable connection state;
- whether optional TLS is shown at all; if shown, it must be labeled as optional
  connection state, not a universal WebSocket requirement;
- how to label the upgrade decision/factory;
- how to show `DetachReason::ContextSwitch` without requiring tiny type labels;
- whether the event-loop rail from Visual 1 is reused for visual-language
  continuity.

The visual must preserve “same `SocketConnection`, new active context.”

### Social preview

A social preview may later be designed as a separate artifact, but Step 4 does
not require or specify one beyond these constraints:

- no version number;
- no unsupported adjectives;
- emphasize C++20 event-driven networking / programming model;
- use SNode.C foundation identity, not generic network imagery.

## Handoff to Step 5

### 1. Approved intended reader journey

1. **Orient:** SNode.C is a C++20 event-driven networking framework for clients
   and servers.
2. **Understand the model:** server/client endpoint → established
   `SocketConnection` → `SocketContextFactory` → per-connection
   `SocketContext`, with the event loop dispatching lifecycle/data work around
   the chain.
3. **Run a real path:** build only the IPv4 echo pair and observe verified
   listener/transport connection output.
4. **Assess breadth:** read a compact capability/evidence table that distinguishes
   implementation, build availability, automated tests, runtime qualification,
   and public availability.
5. **See the deeper consequence:** understand layer responsibilities and the
   HTTP-to-WebSocket context replacement on one continuing connection.
6. **Choose next action:** architecture, configuration, capability/evidence map,
   examples, source, issues/discussions, releases, license, and brief ecosystem
   routes.

### 2. Proposed visuals and communication goals

**Visual 1 — Programming-model lifecycle**

Goal: show server/client convergence on the same
`SocketConnection` → factory → per-connection context lifecycle, with the event
loop surrounding and dispatching the flow.

**Visual 2 — Real echo connection proof**

Goal: show genuine qualified terminal evidence that the IPv4 server listened and
the client/transport connected.

**Visual 3 — Context replacement on one connection**

Goal: show that HTTP protocol ownership can transition to a WebSocket context
while the underlying `SocketConnection` remains established.

Proposed count: **three in-page visuals**, with Visual 2 permitted to be removed
after real recapture only if it does not add legible information. No replacement
decorative visual is required in that case.

### 3. Technical concepts each visual must preserve

**Visual 1**

- `SocketServer` listens/accepts;
- `SocketClient` connects;
- both lead to an established `SocketConnection`;
- the endpoint’s `SocketContextFactory` creates the connection-local context;
- one active `SocketContext` receives callbacks;
- event-loop descriptor/timer dispatch surrounds the lifecycle;
- no worker-thread or support-matrix implication.

**Visual 2**

- exact real IPv4 loopback roles/commands;
- listening/connected success;
- current default information-level output;
- no visible payload claim.

**Visual 3**

- one persistent `SocketConnection`;
- old context detaches for a context switch;
- new context attaches;
- HTTP → WebSocket is the concrete implemented example;
- no new socket/connection/TLS handshake is implied;
- no universal family/TLS matrix is implied.

### 4. Screenshot/evidence needs

**Visual 1:** no screenshot required. Validate every label/arrow against Step 3
and current public source before export.

**Visual 2:** requires a fresh real capture from the exact Step 5-qualified
revision using the actual
`echoserver-legacy-in` / `echoclient-legacy-in` targets, `127.0.0.1:18001`,
generic prompts, and privacy-clean terminal state. Capture only real
default-visible output.

**Visual 3:** no product screenshot required. Validate context-switch semantics
against `SocketConnection::setSocketContext()`, detach reasons, HTTP server
upgrade implementation, WebSocket context implementation, and the relevant
current tests.

If public `master` changes before Step 5 validation, refresh the technical
baseline before reusing these semantics or captures.

### 5. Claims/relationships the visuals must not imply

No visual may imply:

- universal address-family × TLS × protocol support;
- Bluetooth runtime qualification;
- visible echo payload proof;
- a current 2.0 release/package;
- performance, memory, security, stability, or production-readiness claims;
- Node.js/Express compatibility;
- worker-thread execution;
- TLS being automatic or universally enabled;
- context replacement creating a new physical connection;
- all ecosystem projects forming one runtime pipeline.

### 6. Open visual/editorial choices Step 5 must resolve

- final art direction details, dimensions, filenames, palette, typography,
  theme strategy, alt text, and captions;
- exact Visual 1 lifecycle layout and event-loop rail;
- whether the small real code excerpt is visually paired with Visual 1 or remains
  normal Markdown;
- whether Visual 2 survives the real recapture readability test;
- exact Visual 2 crop and provenance;
- exact Visual 3 transition labels and whether optional TLS state appears;
- whether the API-reference route should be visually de-emphasized or omitted
  until freshness is established;
- whether the final README needs two or three in-page visuals after real capture
  review.

Step 5 must preserve these communication goals and evidence boundaries while
designing the actual assets. It must not reintroduce the old V1–V4 quota or old
asset compositions merely for continuity.
