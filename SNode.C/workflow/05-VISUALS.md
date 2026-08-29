# SNode.C Step 5 — validated visual specification

**Workflow stage:** Step 5b complete
**Design date:** 29 August 2026  
**Technical-validation date:** 29 August 2026
**Project:** SNode.C  
**Output:** `SNode.C/workflow/05-VISUALS.md`  
**Technical baseline inherited from Step 3:** public `SNodeC/snode.c` `master` at `bf01683a53b48220a840522e8ccaf3b48e58c240`  
**Step 5b freshness result:** public `master`, checked with `git ls-remote`, still resolves to `bf01683a53b48220a840522e8ccaf3b48e58c240`; the read-only local mirror resolves to the same commit. No source delta or Step 3 fact refresh was required.

This document preserves the Step 5a visual-design intent and adds the complete
Step 5b technical-validation and screenshot-reproduction handoff. It defines
what the SNode.C README visuals must communicate, the technically correct
relationships and labels, the evidence behind them, and the exact procedure for
future asset production. Step 5b did not create or replace final SVG/PNG assets
and did not modify the README.

The design follows the canonical workflow and governance, the SNode.C Step 3 fact base, the approved Step 4 README design, the scoped SNode.C instructions, and the shared page-system principles. The old mandatory V1–V4 system is not reused.

## Step 5b validation record

### Current source and CI

- Public source: [`SNodeC/snode.c`](https://github.com/SNodeC/snode.c), branch
  `master`.
- Exact validated commit:
  [`bf01683a53b48220a840522e8ccaf3b48e58c240`](https://github.com/SNodeC/snode.c/commit/bf01683a53b48220a840522e8ccaf3b48e58c240),
  committed 28 August 2026 at 16:16:20 UTC.
- Freshness: public `master` and the read-only local mirror both matched the
  Step 3 baseline on 29 August 2026. The relevant source delta is empty.
- Public CI: [run 33189174904](https://github.com/SNodeC/snode.c/actions/runs/33189174904)
  is the exact-SHA `CI` run and completed successfully.

### Direct Step 5b qualification

An isolated fresh clone of the exact commit was configured and built outside
both the landing-page workspace and the read-only live source repository.

- Release configuration: Ninja, `Release`, default `epoll`,
  `SNODEC_BUILD_APPS=ON`, `SNODEC_BUILD_TESTS=OFF`, and
  `CHECK_INCLUDES=OFF`.
- Exact release targets built: `echoserver-legacy-in` and
  `echoclient-legacy-in`.
- Runtime qualification: both exact binaries completed the approved plain IPv4
  loopback listener/connection scenario on `127.0.0.1:18001` with an isolated
  configuration root and explicit information-level text logging.
- Capture-only render check: real emitted lines were rendered in temporary
  132-column × 10-row high-density terminal panes. The 2512 × 384-pixel raw
  panes showed no wrapping, and desktop-width inspection passed. These
  temporary checks remained outside the repository and are not publication
  provenance.
- Focused Debug configuration: Ninja, `Debug`, `SNODEC_BUILD_APPS=ON`,
  `SNODEC_BUILD_TESTS=ON`, and `CHECK_INCLUDES=OFF`.
- Focused tests built and run: `SocketContextLifecycleTest` and
  `InetWebSocketServerClientTextEchoTest`; both passed (`2/2`).
- Qualification host, recorded as evidence rather than a support claim: Debian
  GNU/Linux forky/sid, x86-64, GCC 16.2.0, CMake 4.3.4, and Ninja 1.13.2.

The exact-head public CI remains the broader current-suite evidence. The two
direct Step 5b tests are focused evidence for the context lifecycle and real
HTTP-to-WebSocket upgrade path; they are not substituted for a protocol or
transport conformance matrix.

## Visual strategy

SNode.C is a framework README. Its visuals should explain mechanisms or show genuine evidence; they should not decorate the page.

The final Step 5b inventory retains three in-page visuals:

1. **Programming-model lifecycle** — required principal technical figure.
2. **Echo connection evidence** — retained real terminal capture, with omission
   as the mandatory fallback if the final source-aligned asset fails the
   desktop legibility gate.
3. **HTTP → WebSocket context replacement** — required mechanism figure showing application-context replacement while retaining the same `SocketConnection`.

The implementation target is **three** in-page visuals. The README may ship
with two only if Visual 2's final authentic recapture cannot meet the
legibility and evidence requirements below; omission is the only approved
fallback.

No separate decorative hero asset is proposed. No generic stacked architecture figure is proposed. No capability matrix is converted into an image; the capability/evidence summary remains accessible Markdown.

## Shared visual language for SNode.C

### Art direction

- Technical, calm, modern, and precise.
- Use generous whitespace and a clear left-to-right or top-to-bottom reading order.
- Use a restrained **foundation-blue** accent only for emphasis; neutral text, borders, and containers carry most of the information.
- Color must never be the only carrier of meaning. Labels, shape, placement, line style, and captions must remain sufficient in monochrome.
- Use ordinary system sans-serif typography for labels and a system monospace stack only for API names, enum values, commands, or terminal text.
- Avoid gradients, shadows, pseudo-3D cards, decorative network icons, stock imagery, protocol logos, or badge-like clutter inside figures.
- Prefer one explicit neutral canvas/background that remains readable in both GitHub themes. Create separate light/dark exports only if a single neutral asset fails contrast testing.

### Diagram semantics

The shared page-system arrow grammar remains in force:

- **solid directed arrow:** a verified runtime action, dispatch, creation call, or lifecycle transition;
- **thin undirected connector / containment:** ownership, association, or persistent identity, not runtime communication;
- **dashed arrow:** reserved for package/build dependencies; none are currently needed in the two proposed SNode.C technical figures.

Every technical relationship below now carries an explicit Step 5b status. A
`VALIDATED WITH CORRECTION` result preserves the Step 5a communication goal but
replaces an imprecise ownership, call, lifecycle, logging, or arrow description
with the source-aligned form required for asset production.

### Accessibility and fallback

- Every meaningful figure needs concise information-bearing alt text.
- The surrounding README prose must restate the important mechanism; no figure may be the only explanation.
- Terminal evidence must be accompanied by a textual expected-output excerpt because screenshot text cannot remain equally legible on narrow mobile displays.
- Do not encode state solely through color.
- Ensure text and line contrast works in GitHub light and dark modes.
- Keep critical labels large enough that the figure is understandable at normal GitHub content width without opening the asset.

### Asset-source convention for Step 5 implementation

Final exported assets, if approved, should live under:

```text
SNode.C/assets/<asset-name>.svg|png
```

Editable source, composition scripts, raw qualified captures, and capture notes should live under:

```text
SNode.C/assets/src/
```

For vector figures, keep an unminified editable source under `assets/src/` and export an optimized SVG to `assets/`. For the terminal visual, preserve the raw qualified server/client captures plus a deterministic composition script or documented composition recipe under `assets/src/`.

---

# Visual 1 — Programming-model lifecycle

**Status:** **VALIDATED WITH CORRECTION — READY FOR ASSET IMPLEMENTATION**
**Human approval:** PENDING rendered-asset review
**Role:** principal technical figure; required  
**Validated export:** `SNode.C/assets/programming-model.svg`
**Editable source requirement:** unminified vector source under `SNode.C/assets/src/programming-model.*`

## Single communication goal

Make the recurring SNode.C application model understandable at a glance:

> a configured server or client endpoint establishes a `SocketConnection`; the endpoint's `SocketContextFactory` creates the per-connection `SocketContext`; the event loop drives lifecycle and I/O into the connection/context path.

## Five-second reader takeaway

A reader should be able to point at the figure and say:

> “Server or client endpoint → connection → factory-created per-connection context, all driven by the event loop.”

The figure must make clear that application/protocol behavior is attached **per connection**, rather than placing application behavior inside the endpoint object itself.

## Exact concepts to show

Show these named public concepts and no broader class inventory:

- `SocketServer` / `SocketClient` — two endpoint roles that converge on the same recurring model;
- `SocketConnection` — the established connection object;
- `SocketContextFactory` — the creation boundary associated with the endpoint flow;
- `SocketContext` — the per-connection application/protocol behavior;
- Event loop — shared runtime that drives descriptor/timer/lifecycle work.

### Technical relationships and final status

1. **VALIDATED WITH CORRECTION — endpoint to connection.** A
   `SocketServer` starts the listener flow; on a ready accept event its
   `SocketAcceptor` accepts the physical stream and constructs the
   `SocketConnection`. A `SocketClient` starts the connector flow; successful
   immediate or readiness-completed connection establishment constructs the
   `SocketConnection`. The figure must use separate labels
   `listen → accept` and `connect completes`, not one ambiguous `establish`
   label and not a claim that the endpoint handle itself is the connection.
2. **VALIDATED WITH CORRECTION — endpoint/factory ownership.** Each configured
   endpoint flow retains its factory through a shared endpoint `Context` as a
   `std::shared_ptr<SocketContextFactory>` and passes/captures that factory in
   the acceptor or connector completion path. Use a thin association labeled
   `endpoint flow retains factory`; do not show a runtime creation arrow from
   endpoint to factory and do not imply that the server and client share one
   global factory.
3. **VALIDATED WITH CORRECTION — exact creation call.** After the transport is
   connected, the connection receives the retained factory and invokes
   `SocketContextFactory::create(SocketConnection*)` with itself. A non-null
   result is installed and attached; a null result closes the connection.
   Represent this as `SocketConnection` → `SocketContextFactory` labeled
   `create(this)`, followed by the factory returning a new `SocketContext`.
   A lone factory → context arrow labeled only `create()` omits the decisive
   connection argument and caller.
4. **VALIDATED WITH CORRECTION — active and pending contexts.** A
   `SocketConnection` has one active `SocketContext`. During replacement it may
   also hold one staged `newSocketContext` until the current read dispatch
   completes. The main lifecycle visual should say `one active context` and
   omit replacement staging; Visual 3 owns that detail.
5. **VALIDATED.** The event multiplexer waits for descriptor/timer work, spans
   active events, and executes the event queue. Accept/connect readiness creates
   connections; readable events flow through `SocketReader` and
   `SocketConnection` into the active context; timers and lifecycle events use
   the same caller-driven loop.
6. **VALIDATED WITH CORRECTION — `start()` / `tick()` wording.**
   `SNodeC::start()` bootstraps the configuration, sets `RUNNING`, and calls the
   event-loop iteration synchronously in a loop on its caller's thread. No
   framework worker-thread creation was found. The public `tick()` surface is
   present, but current `EventLoop::tick()` calls `_tick()` only while state is
   `INITIALIZED`, whereas `_tick()` dispatches the multiplexer only in
   `RUNNING` or `STOPPING`; no current test establishes `tick()` as a working
   external-loop dispatcher. Therefore the figure must label the dispatch rail
   `Event loop — start()` and omit `tick()` until that operational contract is
   clarified or corrected and tested. The caption may state that callbacks
   dispatched by the framework execute synchronously on the thread running the
   loop; it must not imply worker threads or forbid application-created threads.

## Composition

Use one wide, shallow lifecycle figure rather than a class diagram.

Corrected required geometry:

```text
 ┌──────────────┐  listen → accept       ┌──────────────────┐
 │ SocketServer │ ──────────────────────►│ SocketConnection │
 └──────────────┘                        └────────┬─────────┘
                                                │ create(this)
 ┌──────────────┐  connect completes            ▼
 │ SocketClient │ ──────────────────────►┌──────────────────────┐
 └──────────────┘                        │ SocketContextFactory │
                                         └────────┬─────────────┘
                                                  │ returns new
                                                  ▼
                                         ┌──────────────────┐
                                         │  SocketContext   │
                                         │ one active /     │
                                         │ per connection   │
                                         └──────────────────┘

 endpoint flow retains factory ──────────────── association only
 SocketConnection owns active context ──────── association only

 ───────────────────────── Event loop — start() ─────────────────────────
 descriptor readiness + timers + lifecycle/data callback dispatch
```

This ASCII sketch is conceptual only; the final vector should be more compact and visually balanced.

### Hierarchy

1. **Primary emphasis:** `SocketConnection` + `SocketContext` relationship.
2. **Secondary emphasis:** `SocketServer` / `SocketClient` converge on the same connection model.
3. **Secondary emphasis:** `SocketContextFactory` is the creation boundary, not the application behavior itself.
4. **Supporting rail:** event loop underpins the model without becoming the dominant object.

The `SocketConnection` and `SocketContext` cards should be visually paired but remain separate shapes. `SocketServer` and `SocketClient` should have equal visual weight and merge into one lifecycle rather than become two duplicated diagrams.

## Labels and terminology

Use exactly:

- `SocketServer`
- `SocketClient`
- `SocketConnection`
- `SocketContextFactory`
- `SocketContext`
- `Event loop`
- `listen → accept` on the server path
- `connect completes` on the client path
- `create(this)` on the connection-to-factory runtime call
- `returns new` on the factory-to-context result arrow
- `per connection` as a small descriptive label near `SocketContext`
- `start()` only in the event-loop rail or caption, not as a large API callout

Do not add implementation namespaces unless required to disambiguate public classes.

## Arrow and lifecycle semantics

- **VALIDATED WITH CORRECTION:** use two solid runtime arrows into
  `SocketConnection`, labeled `listen → accept` and `connect completes`.
- **VALIDATED WITH CORRECTION:** use a solid call arrow from
  `SocketConnection` to `SocketContextFactory`, labeled `create(this)`, and a
  solid result/creation arrow from the factory to the new `SocketContext`.
- **VALIDATED:** show the endpoint-flow/factory relationship with an undirected
  association or labeled containment cue. It is retained ownership/use, not a
  repeated runtime message.
- **VALIDATED WITH CORRECTION:** use a restrained `Event loop — start()` rail
  with short solid dispatch arrows to endpoint readiness and connection/context
  callbacks. Do not label the rail `tick()` and do not depict a worker pool.
- **VALIDATED:** use an undirected ownership/active-context cue between
  `SocketConnection` and `SocketContext`; do not imply that every event creates
  a context or that the context owns the connection.

## Deliberate omissions

Do **not** show:

- IPv4, IPv6, Unix domain, RFCOMM, L2CAP, TLS, HTTP, MQTT, or any family/protocol list;
- template type stacks or concrete `legacy`/TLS endpoint aliases;
- CMake component names;
- configuration-file or CLI hierarchy;
- callback inventories;
- `epoll` / `poll` / `select` comparisons;
- threads, worker pools, queues, or performance claims;
- Node.js or Express references;
- context replacement details — Visual 3 owns that mechanism.

The figure must explain the programming model, not prove breadth.

## Relationship to surrounding README prose/code

Place immediately in the **Programming model** section, directly after the one-paragraph explanation and before or beside the small real `SocketContext` code excerpt.

The surrounding prose should define the five concepts in words. The code excerpt should then demonstrate the *feel* of context callbacks. The figure must not duplicate the code or become an API reference.

## Validated evidence

- Endpoint/factory ownership and flow:
  [`SocketServer.h`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketServer.h),
  [`SocketClient.h`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketClient.h),
  base [`SocketAcceptor.hpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketAcceptor.hpp),
  base [`SocketConnector.hpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketConnector.hpp),
  plain [`SocketAcceptor.hpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/legacy/SocketAcceptor.hpp),
  and plain [`SocketConnector.hpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/legacy/SocketConnector.hpp).
- Connection creation, factory call, active/pending context storage, and
  dispatch:
  [`SocketConnection.h`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketConnection.h),
  [`SocketConnection.cpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketConnection.cpp),
  and [`SocketConnection.hpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketConnection.hpp).
- Exact factory surface:
  [`SocketContextFactory.h`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketContextFactory.h).
- Context attach/detach and connection back-reference:
  [`SocketContext.h`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketContext.h)
  and [`SocketContext.cpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketContext.cpp).
- Caller-thread event dispatch and current `tick()` boundary:
  [`EventLoop.cpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/EventLoop.cpp)
  and [`EventMultiplexer.cpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/EventMultiplexer.cpp).
- Lifecycle test evidence: exact-SHA public CI plus the direct Step 5b
  `SocketContextLifecycleTest` pass. The direct test verifies the attach,
  `ContextSwitch` detach, replacement attach, and final connection-close
  detach ordering; source tracing establishes how that lifecycle is reached
  from an endpoint flow.

No runtime screenshot is required for Visual 1.

## Accessibility / alt-text target

Final alt text:

> Diagram of the SNode.C programming model: a SocketServer accepts or a SocketClient completes a connection, the SocketConnection calls its endpoint flow's SocketContextFactory to create one active per-connection SocketContext, and the caller-thread event loop dispatches lifecycle and I/O callbacks.

## GitHub-width, mobile, and theme requirements

- Prefer a wide SVG with at most five major labeled nodes plus the event-loop rail.
- At desktop GitHub width, every class name should be readable without zoom.
- On mobile, the left-to-right endpoint merge may compress; if necessary, use a responsive-friendly two-row composition where server/client sit above a centered connection/context sequence.
- Avoid tiny explanatory text. Put nuance in the caption/prose instead.
- Use explicit node outlines and labels so the figure remains understandable if the blue accent is visually muted.
- Test one neutral export in both GitHub themes before introducing light/dark variants.

---

# Visual 2 — Genuine echo connection evidence

**Status:** **VALIDATED WITH CORRECTION — RETAIN**
**Human approval:** PENDING final-capture review
**Role:** retained evidence screenshot; omission fallback defined below
**Validated export:** `SNode.C/assets/echo-connection-evidence.png`
**Editable/capture source requirement:** raw qualified captures plus deterministic composition material under `SNode.C/assets/src/echo-capture/`

## Final retention decision

**RETAIN.** Step 5b reproduced the exact current-baseline server/client run from
freshly built binaries. With an isolated configuration root and explicit
information-level, monochrome text logging, the evidence is five compact output
lines: three in the server pane and two in the client pane. The longest real
line is 125 terminal columns, so a vertically stacked 132-column capture can
preserve every selected line without wrapping or horizontal cropping. At the
specified type size and single controlled downsample, the temporary authentic
render remained readable at normal desktop content width. The result therefore
passes the Step 5b retention gate and remains subject only to inspection of the
future final-composed asset.

This retention decision does not approve the existing
`SNode.C/assets/echo-terminal.png`; that file remains historical provenance.
Asset production must create the new source-aligned capture at the filename and
from the procedure specified here. If the final rendered proof fails the stated
desktop legibility check, omit it rather than editing terminal content.

## Single communication goal

Show genuine runtime evidence for the first-success path:

> the plain IPv4 echo server reaches a listening state and the client reaches a real connection to it.

The screenshot is **not** payload proof.

## Five-second reader takeaway

A reader should immediately see two real terminal states:

- **Server:** listener is up on loopback.
- **Client:** connection to that listener succeeded.

Nothing in the visual should suggest that the terminal visibly proves an echoed payload.

## Exact concepts to show

- real `echoserver-legacy-in` run from the qualified source revision;
- real `echoclient-legacy-in` run from the same compatible build;
- loopback IPv4 first-success path only;
- only the relevant command line and verified listener/connection evidence lines;
- simple external panel labels such as `Server` and `Client` are allowed as composition labels.

### Technical/evidence relationships and final status

1. **VALIDATED.** `listener started` is emitted after the listener descriptor is
   enabled, and the application `listening on '127.0.0.1:18001'` line is emitted
   from the successful `SocketServer::listen` status callback. Together they
   visibly prove the approved plain IPv4 loopback listener reached its active
   listening state.
2. **VALIDATED.** The application client line and the client/server
   `transport connected` records were observed in the same run. The framework
   emits those records after successful connector completion and accepted
   connection construction. They prove one real loopback plain-stream
   connection, not application-payload behavior or a broader transport matrix.
3. **VALIDATED.** The client context sends
   `Hello peer! Nice to see you!!!` from `onConnected()`; both echo contexts read
   available bytes and send the same bytes back. This creates a continuing
   reflection loop. At information level the selected capture does not print
   the payload, so the screenshot is not visible echo-payload proof.
4. **VALIDATED WITH CORRECTION.** Information level is the built-in option
   default, but automatic user configuration can override it. Step 5b observed
   exactly that hazard during the first attempt. The deterministic capture must
   therefore isolate `XDG_CONFIG_HOME` and pass `--log-level 4` explicitly.
   It must not show debug context-attach lines or trace-level `Data to reflect`
   lines.

## Composition

Use a **vertically stacked two-panel terminal composite**, not two narrow
side-by-side terminals. The Step 5b line-length check fixes this choice because
the 125-column transport records need the full image width.

Recommended order:

1. **Server** panel — command plus the smallest contiguous region containing the real listening line and relevant connection evidence.
2. **Client** panel — command plus the smallest contiguous region containing the real successful connection line(s).

Use a tight crop. Preserve real terminal text. External labels may identify the
panels, but no synthetic terminal output may be inserted.

## Labels and terminology

External composition labels may use:

- `Server`
- `Client`
- optionally `plain IPv4 loopback` in the caption, not necessarily inside the image

Do not label the image `Echo succeeded`, `Payload echoed`, `Round trip`, or similar unless the visible captured output itself actually proves that claim.

## Deliberate omissions

Do **not** include:

- a fabricated payload line;
- trace/debug output solely to make the screenshot look more impressive unless the README's first-success path intentionally uses that exact validated logging configuration;
- TLS, IPv6, or Unix-domain evidence in the same visual;
- certificate commands;
- build logs;
- package installation logs;
- unrelated shell history;
- usernames, home paths, hostnames, LAN addresses, credentials, private certificates, or local repository paths;
- visual callouts claiming performance, security, or platform support.

## Relationship to surrounding README prose/code

Place after the run commands and textual expected-output excerpt in **Run the echo pair / First verified connection**.

The Markdown expected-output block remains the primary accessible proof text. The screenshot supplements it by showing that the captured output came from a real qualified run.

The adjacent prose must explicitly say that the supplied echo code reflects
bytes but the explicitly selected information-level output proves
listener/connection success rather than visibly displaying the echoed payload.

## Exact validated screenshot scenario

### Revision, build, and environment

Use a clean isolated checkout at the exact validated revision. Do not build in
the live source repository.

```sh
git clone https://github.com/SNodeC/snode.c.git
cd snode.c
git checkout bf01683a53b48220a840522e8ccaf3b48e58c240

cmake -S . -B cmake-build-release -G Ninja \
  -DCMAKE_BUILD_TYPE=Release \
  -DSNODEC_BUILD_APPS=ON \
  -DSNODEC_BUILD_TESTS=OFF \
  -DCHECK_INCLUDES=OFF
cmake --build cmake-build-release --parallel \
  --target echoserver-legacy-in echoclient-legacy-in
```

Before opening the two capture terminals, prepare a clean shell environment.
The SNode.C configuration code consults a per-user default file, so isolating
`XDG_CONFIG_HOME` is mandatory rather than cosmetic.

```sh
CAPTURE_STATE_ROOT="$(mktemp -d)"
export XDG_CONFIG_HOME="$CAPTURE_STATE_ROOT"
export PATH="$PWD/cmake-build-release/src/apps/echo:$PATH"
export LC_ALL=C.UTF-8
export TZ=UTC
export PS1='$ '
```

Assumptions: Linux with working IPv4 loopback; `127.0.0.1:18001` is unused;
the configured build dependencies are present; both terminal processes use the
same checkout, build, and isolated `XDG_CONFIG_HOME`. Check that the port is
free before capture, outside the cropped terminal region.

### Exact launch commands

Server, launched first:

```sh
echoserver-legacy-in --log-level 4 --log-format text --monochrom=true echoserver local --host 127.0.0.1 --port 18001
```

Client, launched only after both initial server information lines appear:

```sh
echoclient-legacy-in --log-level 4 --log-format text --monochrom=true echoclient remote --host 127.0.0.1 --port 18001
```

`--log-level 4` selects information level, `--log-format text` fixes the text
format, and `--monochrom=true` removes ANSI styling. These explicit options and
the isolated configuration root are part of the evidence scenario.

### Exact real Step 5b output eligible for capture

The following are the complete selected lines from the real Step 5b run. A
future asset-production run will have different real UTC timestamps; those
timestamps must be captured as emitted and must not be normalized or replaced.

Server:

```text
2026-08-29T16:18:51.190Z INF framework/instance core.socket.stream role=server inst=echoserver — listener started
2026-08-29T16:18:51.190Z INF application/application app — echoserver: listening on '127.0.0.1:18001'
2026-08-29T16:18:56.380Z INF framework/connection core.socket.stream role=server inst=echoserver conn=1 — transport connected
```

Client:

```text
2026-08-29T16:18:56.380Z INF application/application app — echoclient: connected to '127.0.0.1:18001 (127.0.0.1)'
2026-08-29T16:18:56.380Z INF framework/connection core.socket.stream role=client inst=echoclient conn=1 — transport connected
```

The quote placement in the client line is significant: the closing quote comes
after the parenthesized numeric address. Do not copy the older, differently
punctuated expected line from prior evidence.

These lines prove that this listener became active and one client/server plain
IPv4 transport connection formed on loopback. They do not visibly prove the
greeting bytes, a completed one-shot round trip, TLS, any other address family,
performance, deployment readiness, or release/package availability.

### Deterministic capture and teardown

1. Use two fresh terminal panes with a generic `$ ` prompt, **132 columns × 10
   rows**, a system monospace font at **16 CSS pixels**, device scale **2×**, a
   non-transparent dark background, and no title text containing user, host, or
   path information.
2. Perform the environment setup above before the crop begins. The visible
   server panel contains its one command plus the three selected server lines;
   the visible client panel contains its one command plus the two selected
   client lines.
3. Capture the client immediately after its two information lines appear, then
   capture the server after its `transport connected` line appears. Do not wait
   for or enable payload diagnostics; the pair continuously reflects bytes.
4. Send Ctrl-C to the client first and wait for it to exit. Then send Ctrl-C to
   the server and wait for `listener stopped`. Confirm the port is no longer
   listening. Teardown lines remain outside the final crop.
5. Preserve both complete raw captures and plain-text terminal transcripts.
   Do not edit, retype, recolor, splice, or normalize any terminal line.
6. Record the terminal emulator, terminal-emulator version, monospace font and
   version, capture utility and version, display scale, source SHA, build
   options, launch commands, UTC capture time, and teardown result in
   `REPRODUCTION.md`.

### Raw storage and composition

Future asset production must store:

```text
SNode.C/assets/src/echo-capture/REPRODUCTION.md
SNode.C/assets/src/echo-capture/server.raw.png
SNode.C/assets/src/echo-capture/client.raw.png
SNode.C/assets/src/echo-capture/server.raw.txt
SNode.C/assets/src/echo-capture/client.raw.txt
SNode.C/assets/src/echo-capture/compose.sh
```

The composition script may crop whole empty rows and terminal chrome, add the
external labels `Server` and `Client`, align the two untouched raw crops, and
downsample once to the final export. It must not crop horizontally through a
selected line or conceal timestamps/log fields. Export the vertically stacked
result to `SNode.C/assets/echo-connection-evidence.png`, targeting a 1600-pixel
width from the 2× raw sources.

Source/runtime evidence:
[`echoserver.cpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/apps/echo/echoserver.cpp),
[`echoclient.cpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/apps/echo/echoclient.cpp),
[`EchoSocketContext.cpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/apps/echo/model/EchoSocketContext.cpp),
base [`SocketAcceptor.hpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketAcceptor.hpp),
base [`SocketConnector.hpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketConnector.hpp),
the exact release target build, and the real Step 5b loopback run recorded
above.

## Legibility gate

Visual 2 is retained only if all of these pass:

1. the meaningful terminal lines are readable at normal desktop GitHub content width without opening the image;
2. the crop does not remove context needed to understand what command produced the output;
3. the screenshot remains useful when scaled on mobile, while the adjacent text carries the same essential evidence;
4. timestamps, logging prefixes, and terminal chrome do not dominate the information;
5. no synthetic terminal content is needed to make the story understandable.

The Step 5b raw-text geometry check passes these criteria. Asset production
must repeat the final rendered-width check. If the resulting PNG requires
synthetic cleanup or its selected text is not readable at normal desktop
GitHub width, change the implementation decision to
**OMIT — TEXTUAL EVIDENCE IS STRONGER**; do not manufacture a substitute.

## Accessibility / final alt text

> Two terminal captures from the verified plain IPv4 echo pair: the server is listening on loopback and the client establishes a connection. The capture does not show echoed payload text.

## GitHub-width, mobile, and theme requirements

- PNG capture with high-density source and one controlled downsample.
- Keep panel width and line count small enough that terminal text stays readable on desktop.
- Use terminal colors with strong luminance contrast and avoid relying on ANSI color to distinguish state.
- A dark terminal theme is acceptable in both GitHub themes if contrast is strong and the crop has a clear boundary.
- Because mobile downscaling inevitably reduces terminal text, key evidence must be duplicated in Markdown text immediately adjacent to the image.

---

# Visual 3 — HTTP → WebSocket context replacement

**Status:** **VALIDATED WITH CORRECTION — READY FOR ASSET IMPLEMENTATION**
**Human approval:** PENDING rendered-asset review
**Role:** required mechanism/extension-point figure  
**Validated export:** `SNode.C/assets/http-websocket-context-switch.svg`
**Editable source requirement:** unminified vector source under `SNode.C/assets/src/http-websocket-context-switch.*`

## Single communication goal

Show why the `SocketConnection` / `SocketContext` split matters:

> during an HTTP-to-WebSocket upgrade, the active application context changes while the established `SocketConnection` remains the same connection object/stream path.

The figure is about **context replacement**, not about advertising a transport matrix.

## Five-second reader takeaway

A reader should see one continuous connection underneath two application states:

> **HTTP context → context switch → WebSocket context, same `SocketConnection`.**

The persistent connection should be the strongest visual continuity cue in the figure.

## Exact concepts to show

- one existing `SocketConnection` spanning the whole figure;
- initial **HTTP `SocketContext`** attached to that connection;
- an accepted HTTP Upgrade / WebSocket handshake transition marker;
- context replacement through the connection's context-switch mechanism;
- old context detaches with `DetachReason::ContextSwitch`;
- new WebSocket **`SocketContextUpgrade`** attaches as the active context;
- the underlying connection remains in place through the transition.

### Technical relationships and final status

1. **VALIDATED WITH CORRECTION — staging versus completion.** Public
   `SocketConnection::setSocketContext(SocketContext*)` attaches immediately
   only when no active context exists. With an active context, it stores the new
   pointer as `newSocketContext`; it does not detach/attach inline. After the
   current active context's `readFromPeer()` callback returns,
   `SocketConnectionT::onReceivedFromPeer()` completes the pending switch.
2. **VALIDATED.** Switch completion first calls
   `socketContext->detach(SocketContext::DetachReason::ContextSwitch)`. The
   enum and `getDetachReason()` are protected lifecycle surfaces available to
   derived contexts. `detach()` records that reason, calls the old context's
   `onDisconnected()`, emits lifecycle logging, and destroys the old context;
   no detached old context persists. The exact source label is safe as a
   concise mechanism annotation, not as a top-level endpoint API call.
3. **VALIDATED.** The connection then assigns the staged pointer as its active
   context, clears the pending pointer, and calls `attach()` on the replacement;
   `attach()` starts the new context lifecycle and invokes its `onConnected()`.
   Both the old and replacement context were constructed with the same
   `SocketConnection*`; the connection object, descriptor-backed stream,
   addresses, connection identity, queues, and connection mode remain in place.
4. **VALIDATED.** On the server, `Response::upgrade()` selects the WebSocket
   upgrade factory, creates a WebSocket `SocketContextUpgrade` with the current
   connection, prepares the `101` Upgrade response, and calls
   `setSocketContext(new)`. In the qualified component path, the subsequent
   status callback calls `response->end()`, queuing that HTTP response through
   the still-active HTTP context before the parser/read callback returns and the
   staged switch completes. The HTTP client path performs the corresponding
   factory creation and staging after parsing `Connection: Upgrade`, selecting
   the factory named by the `Upgrade` response field, and verifying the
   WebSocket accept key. The direct Step 5b IPv4 component test completed a real
   HTTP Upgrade and WebSocket text echo.
5. **VALIDATED.** The client sends `Sec-WebSocket-Version: 13`; the server
   accepts exactly `13` and responds with `426` plus
   `Sec-WebSocket-Version: 13` for a different value. The figure itself should
   remain version-free; surrounding capability prose may say `WebSocket 13`.
6. **VALIDATED.** No family or connection-mode symbol belongs in this figure.
   The direct test is plain IPv4; other Step 3 WebSocket tests have their own
   scoped evidence. The mechanism must not be rendered as a family × TLS ×
   protocol matrix.

## Composition

Use a three-phase horizontal mechanism figure with a **continuous lower connection rail**.

Corrected required geometry:

```text
 BEFORE UPGRADE                 STAGED SWITCH                    AFTER CALLBACK

 ┌──────────────────┐    WebSocket factory selected         ┌──────────────────┐
 │ HTTP             │    new context + 101 prepared         │ WebSocket        │
 │ SocketContext    │ ──► setSocketContext(new) stages ───► │ SocketContext    │
 └────────┬─────────┘                                       │ (Upgrade)        │
          │                                                 └────────┬─────────┘
          │                                                          │
 ═════════╧════════════════ same SocketConnection ═══════════════════╧═════════
          descriptor-backed stream, addresses, identity, mode retained

 after current HTTP read callback:
 detach(DetachReason::ContextSwitch) → active-pointer swap → attach()
```

The continuous `SocketConnection` rail should visually span all three phases without breaks. The context cards above it should clearly change identity.

For the validated server-side path, preserve this order in the figure or
caption: factory selection and new-context creation; `101` response preparation;
`setSocketContext(new)` staging; application `response->end()` queuing the `101`;
current HTTP read callback returns; old-context detach, pointer swap, and
new-context attach. The client performs its corresponding staged switch after
parsing the `101` response and validating the WebSocket accept key.

Do not draw a second socket/connection on the right side. Do not use a network-family icon or TLS badge anywhere in this figure.

## Hierarchy

1. **Primary emphasis:** one continuous `SocketConnection`.
2. **Primary state change:** HTTP context becomes WebSocket context.
3. **Supporting lifecycle detail:** `ContextSwitch` detach / attach semantics.
4. **Supporting protocol marker:** an accepted HTTP Upgrade and upgrade-factory
   result initiate the staged transition.

The figure should visually answer “what stays?” and “what changes?” before the reader reads the caption.

A small textual pair such as:

- **stays:** `SocketConnection`
- **changes:** active `SocketContext`

may be used if it improves five-second comprehension without adding clutter.

## Labels and terminology

Use:

- `HTTP SocketContext`
- `WebSocket SocketContext`
- `SocketContextUpgrade` as a smaller exact-type cue beneath the WebSocket label
- `same SocketConnection`
- `WebSocket factory selected`
- `101 response prepared`
- `setSocketContext(new)`
- `DetachReason::ContextSwitch`
- `attach()`

If version labels appear at all, use `HTTP/1.0 and HTTP/1.1` only in surrounding capability prose and `WebSocket 13` only where validated and relevant. The mechanism figure itself does not need version numbers.

## Arrow / lifecycle semantics

- **VALIDATED WITH CORRECTION:** the HTTP-context arrow enters a small staged
  switch phase labeled `WebSocket factory selected`, `new context + 101
  prepared`, and `setSocketContext(new)`. Do not draw a direct old-context →
  new-context creation arrow; the old context does not create its replacement.
- **VALIDATED WITH CORRECTION:** the switch-completion annotation must say it
  occurs `after current HTTP read callback`, then show
  `detach(DetachReason::ContextSwitch) → active-pointer swap → attach()`.
- **VALIDATED:** the connection rail has no directional arrow. It represents
  persistent object/stream identity and association across the state change.
- **VALIDATED:** detach/attach remain compact lifecycle annotations, not giant
  data-flow arrows. They operate on contexts already associated with the same
  connection.

## Deliberate omissions

Do **not** show:

- IPv4, IPv6, Unix domain, RFCOMM, L2CAP;
- plain/TLS badges or a TLS lock icon;
- a matrix suggesting HTTP or WebSocket qualification across all families/modes;
- MQTT or MQTT-over-WebSocket;
- Express-style routing/middleware;
- Node.js/Express compatibility language;
- HTTP request headers or complete handshake text;
- socket file descriptors, kernel sockets, internal parser classes, or template types;
- a second connection on the WebSocket side;
- performance, security, stability, or production-readiness claims.

## Relationship to surrounding README prose/code

Place in **Architecture and extension points** after the compact textual layer decomposition and the paragraph explaining that custom factories/contexts are the application extension point.

The prose before the figure should establish that one connection has an active context. The figure then makes the replacement mechanism concrete. The prose after it can point to deeper architecture documentation rather than expanding into a WebSocket tutorial.

This visual should not appear before the main programming-model figure; it depends on the reader already understanding `SocketConnection` and `SocketContext`.

## Validated evidence

- Context replacement API, staging, completion, and retained connection:
  [`SocketConnection.h`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketConnection.h),
  [`SocketConnection.cpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketConnection.cpp),
  and [`SocketConnection.hpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketConnection.hpp).
- Detach reason and attach/detach destruction semantics:
  [`SocketContext.h`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketContext.h)
  and [`SocketContext.cpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketContext.cpp).
- Server and client HTTP upgrade paths:
  [`Response.cpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/web/http/server/Response.cpp)
  and [`Request.cpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/web/http/client/Request.cpp).
- WebSocket upgrade-context creation and version 13:
  server [`SocketContextUpgradeFactory.cpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/web/websocket/server/SocketContextUpgradeFactory.cpp),
  client [`SocketContextUpgradeFactory.cpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/web/websocket/client/SocketContextUpgradeFactory.cpp),
  and [`SocketContextUpgrade.hpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/web/websocket/SocketContextUpgrade.hpp).
- Tests: exact-SHA public CI plus direct Step 5b passes for
  [`SocketContextLifecycleTest.cpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/tests/unit/core/SocketContextLifecycleTest.cpp)
  and
  [`InetWebSocketServerClientTextEchoTest.cpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/tests/component/websocket/InetWebSocketServerClientTextEchoTest.cpp).

No screenshot is required. This is a mechanism diagram grounded in source and
focused runtime/component tests.

## Accessibility / final alt text

> HTTP-to-WebSocket context switch in SNode.C: an accepted HTTP Upgrade stages a WebSocket context; after the current HTTP read callback, the HTTP context detaches for ContextSwitch, the new context attaches, and the same SocketConnection remains established.

## GitHub-width, mobile, and theme requirements

- Use a wide but shallow SVG with three clearly labeled phases.
- Make the continuous connection rail thick enough to remain obvious after mobile scaling.
- Keep lifecycle annotations short; move detailed explanation to the caption.
- If three horizontal phases become cramped on mobile, stack the before/after context cards vertically while preserving one visually continuous connection spine.
- Use shape and labels, not color alone, to distinguish HTTP and WebSocket contexts.
- Test one neutral export against both GitHub themes before adding theme-specific variants.

---

# Cross-visual consistency

The two technical SVGs should clearly belong to one visual family:

- same node corner radius and border weight;
- same system typography and monospace treatment for API symbols;
- same foundation-blue accent role;
- same label hierarchy;
- same arrowheads and runtime-arrow style;
- same caption voice;
- similar whitespace density.

They should **not** share a mandatory canvas size. Visual 1 may be moderately wide; Visual 3 should be shallower and mechanism-focused. Visual 2 is real terminal evidence and therefore should retain authentic terminal appearance rather than imitate the SVG card language.

Do not number or publicly label the final assets as V1/V2/V3. Their identity comes from descriptive filenames and captions.

## README visual placement summary

| Candidate | README location | Final Step 5b status | Why it earns space |
| --- | --- | --- | --- |
| Programming-model lifecycle | `Programming model` | Required; **VALIDATED WITH CORRECTION** | Explains the framework's defining object/lifecycle model faster than prose alone, with the corrected connection-driven factory call and `start()` dispatch rail. |
| Echo connection evidence | `Run the echo pair` / `First verified connection` | **RETAIN; VALIDATED WITH CORRECTION** | Provides genuine, compact plain-IPv4 listener/connection proof with explicit configuration isolation and information logging. |
| HTTP → WebSocket context replacement | `Architecture and extension points` | Required; **VALIDATED WITH CORRECTION** | Demonstrates staged context replacement after the current read callback while one connection remains. |

## Evidence-boundary guardrails for implementation

The following rules apply across all three visuals:

- implementation presence is not runtime qualification;
- build availability is not runtime qualification;
- runtime qualification is not public package/release availability;
- no visual may imply a universal address-family × connection-mode × protocol support matrix;
- Bluetooth RFCOMM/L2CAP currently have source/build evidence without hardware runtime qualification;
- TLS runtime evidence is currently limited to one mutual-TLS IPv4 echo arrangement;
- the explicit information-level echo evidence proves listener/connection success, not visible payload reflection;
- protocol versions, where named in surrounding copy, remain HTTP 1.0/1.1, WebSocket 13, and MQTT 3.1.1 at the Step 3 baseline;
- Node.js/Express inspiration must not be rendered as compatibility;
- no platform, performance, security, stability, production-readiness, or current 2.0 release/package claim belongs in these visuals.

## Final Step 5 asset-production requirements

1. Produce only the three validated exports:
   - `SNode.C/assets/programming-model.svg` from an unminified editable source
     under `SNode.C/assets/src/`;
   - `SNode.C/assets/echo-connection-evidence.png` from the raw and composition
     sources under `SNode.C/assets/src/echo-capture/`; and
   - `SNode.C/assets/http-websocket-context-switch.svg` from an unminified
     editable source under `SNode.C/assets/src/`.
2. Treat existing `programming-model.svg`, `echo-terminal.png`, and
   `protocol-upgrade.svg` assets as historical provenance, not as validated
   substitutes. Do not publish an old asset under a new caption.
3. Implement Visual 1 with the corrected two endpoint arrows, connection-driven
   `create(this)` call, factory return, endpoint/factory association, active
   context ownership cue, and `Event loop — start()` rail. Do not add `tick()`.
4. Implement Visual 2 only from a new exact-revision run following the complete
   scenario above. Preserve every selected emitted line, its real timestamp,
   command, prompt, and punctuation. Do not fabricate payload proof.
5. Implement Visual 3 with a continuous non-directional connection rail, a
   staged `setSocketContext(new)` phase, and the post-callback
   `ContextSwitch` detach → pointer swap → attach ordering. Do not render a
   second socket, reconnection, TLS handshake, or transport matrix.
6. Reuse the shared restrained shape, stroke, arrowhead, type, and
   foundation-blue accent grammar, but let each figure use the dimensions its
   mechanism requires. Color may not carry meaning by itself.
7. Add the final alt text specified in each visual and a short caption that
   states the evidence boundary. Ensure the surrounding README remains complete
   with images disabled.
8. Inspect the rendered exports at normal GitHub desktop width, at approximately
   375 CSS pixels, in light and dark themes, and with images disabled. Check SVG
   labels, line directions, terminal text size, contrast, crop integrity, and
   captions. Use theme-specific variants only if a neutral export fails.
9. Record the source SHA, final capture time, terminal/tool settings, raw-file
   hashes, and composition command in the editable-source notes. No rendered
   asset may receive `Human approval: APPROVED` until this visual inspection is
   complete.

No Step 5 asset implementation may broaden the Step 3 evidence boundaries
because a relationship is visually convenient.

## Remaining open issues

1. **OPEN — REQUIRES ADDITIONAL EVIDENCE:** the public `SNodeC::tick()` API is
   present, but the reviewed state gates do not establish it as a working
   external-loop dispatcher. It is deliberately omitted from Visual 1. A source
   correction or clarifying maintainer contract plus a focused dispatch test is
   required before a future visual may add it.
2. **OPEN — REQUIRES HUMAN APPROVAL:** the final SVGs and PNG were not created
   in Step 5b, as required by this task boundary. Light/dark/mobile visual review
   and human approval remain pending after asset production.
3. **OPEN — FINAL CAPTURE PROVENANCE:** Step 5b reproduced and validated the
   scenario, line set, and geometry. The asset-production run must preserve its
   own raw screenshots/transcripts and real timestamps under the declared
   `assets/src/echo-capture/` paths.

## Step 5b completion status

- **Final visual count:** three retained candidates: two required technical
  SVGs and one real terminal-evidence PNG. Visual 2 remains subject only to the
  final rendered-width gate; failure means omission, not substitution.
- **Visual 1:** **VALIDATED WITH CORRECTION** — endpoint-specific establishment
  labels, connection-driven `create(this)`, endpoint/factory retained
  association, one active context, and caller-thread `start()` dispatch.
- **Visual 2:** **VALIDATED WITH CORRECTION — RETAIN** — clean plain-IPv4
  listener/connection run reproduced; automatic user-config influence removed;
  no payload claim.
- **Visual 3:** **VALIDATED WITH CORRECTION** — replacement is staged, then the
  old context detaches for `ContextSwitch`, the pointer swaps, and the new
  WebSocket context attaches on the same connection after the current HTTP read
  callback.
- **Major design decisions preserved:** no decorative hero, no generic
  architecture stack, no image-based capability matrix, one restrained
  technical SVG language, authentic terminal evidence, and strict separation
  between mechanism and qualification breadth.
- **Output path:** `SNode.C/workflow/05-VISUALS.md`.
- **Validation performed:** current public `master` freshness check; exact-SHA
  source/ownership/lifecycle trace; exact-SHA public CI confirmation; isolated
  Release build of both echo targets; real loopback runtime reproduction;
  isolated Debug builds and passing focused lifecycle/WebSocket tests; and
  technical review of every Step 5a label, arrow, association, protocol scope,
  and evidence boundary.
