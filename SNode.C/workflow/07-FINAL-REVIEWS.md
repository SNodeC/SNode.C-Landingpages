# Codex technical audit

- **Audit date:** 29 August 2026
- **Reviewed public source:** [`SNodeC/snode.c` `master` at `bf01683a53b48220a840522e8ccaf3b48e58c240`](https://github.com/SNodeC/snode.c/commit/bf01683a53b48220a840522e8ccaf3b48e58c240)
- **Baseline result:** unchanged from the Step 3/5 validated baseline

## IMPORTANT — Relative draft links do not yet have final README publication destinations

- **Severity:** **IMPORTANT**
- **Location:** draft lines 24 and 205 use
  `../assets/programming-model.svg` and
  `../assets/http-websocket-context-switch.svg`; lines 174, 221, 230, 232,
  and 234 use `../docs/capabilities.md`, `../docs/configuration.md`, and
  `../docs/architecture.md`.
- **What is wrong or unsupported:** those paths correctly resolve from the
  frozen workflow draft, but copying them unchanged to `SNode.C/README.md`
  would resolve outside the SNode.C publication root. The two assets and three
  landing-page documents also do not exist at those destination paths in the
  reviewed public `snode.c` commit, so rebasing alone is not enough unless the
  targets are co-published.
- **Authoritative evidence/source:** the relative paths are visible in the
  frozen [Step 6 draft](06-README-DRAFT.md). A recursive tree inspection of the
  reviewed commit finds none of the five destination files; the public
  [`docs` tree at the reviewed commit](https://github.com/SNodeC/snode.c/tree/bf01683a53b48220a840522e8ccaf3b48e58c240/docs)
  likewise has no `architecture.md`, `configuration.md`, or `capabilities.md`.
  Root publication rules require stable production destinations rather than
  workflow-relative links.
- **Minimum required correction:** in Step 7c, rebase the two asset links to
  `assets/...` and every document link to `docs/...`. Co-publish the final
  approved asset versions and all three documents with the README, or replace
  or omit any link whose stable public destination will not exist. This is a
  path/destination finding, not a rejection of the two technically validated
  working SVGs while their human publication approval remains pending.

## MINOR — The multiplexer row does not scope qualification to the selected default

- **Severity:** **MINOR**
- **Location:** draft line 155, capabilities table, event-runtime row:
  “`epoll` default with selectable `poll` and `select`,” followed by the generic
  exact-head CI and focused-test evidence.
- **What is wrong or unsupported:** the availability statement is true, but it
  omits that selection occurs at CMake configure time and that `core` links one
  selected multiplexer. The reviewed CI and qualification used the default
  `epoll`; they did not separately exercise `core` linked against `poll` or
  `select`. The row can therefore be read more broadly than its evidence.
- **Authoritative evidence/source:** [`src/core/CMakeLists.txt`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/CMakeLists.txt#L42-L51)
  defines the configure-time choice, and the same file
  [links `core` to one selected implementation](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/CMakeLists.txt#L149-L152).
  The exact-head [CI configure command](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/.github/workflows/ci.yml#L43-L44)
  does not override the default. Step 3 records no comparative multiplexer
  qualification.
- **Minimum required correction:** say that `epoll` is the default and that
  `poll` and `select` are configure-time alternatives; state in the evidence or
  boundary cell that current CI/runtime qualification exercised default
  `epoll` only.

## MINOR — The programming-model factory association can imply one shared factory

- **Severity:** **MINOR**
- **Location:** the programming-model figure embedded at draft line 24,
  specifically the single association rail labeled “endpoint flow retains
  factory” that joins both endpoint-role cards to one `SocketContextFactory`.
- **What is wrong or unsupported:** the surrounding draft prose correctly says
  “the endpoint flow's” retained factory, but the shared visual rail can imply
  that a server flow and a client flow retain one global factory. Each endpoint
  flow instead constructs and retains its own factory in its own shared flow
  context.
- **Authoritative evidence/source:** the server flow stores its factory in
  [`SocketServer.h`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketServer.h#L86-L100)
  and [constructs that flow with its own factory](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketServer.h#L170-L181).
  The client flow independently stores its factory in
  [`SocketClient.h`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketClient.h#L91-L105)
  and [constructs its own](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketClient.h#L205-L216).
  The validated [Step 5 semantics](05-VISUALS.md) explicitly prohibit implying
  one shared global factory.
- **Minimum required correction:** during the pending visual refinement, split
  the association by endpoint or label it unambiguously as “each endpoint flow
  retains its own factory.” Use that corrected, human-approved asset in the
  final README.

## MINOR — The upgrade figure omits explicit replacement-context creation

- **Severity:** **MINOR**
- **Location:** the HTTP-to-WebSocket figure embedded at draft line 205,
  specifically its numbered staged-switch sequence: “WebSocket factory
  selected” → “101 Switching Protocols response prepared” →
  `setSocketContext(new)` → `response->end()`.
- **What is wrong or unsupported:** draft lines 196–203 preserve the exact
  server-side order, but the figure skips the factory's creation of the
  replacement context between factory selection and `101` preparation. It also
  does not identify `response->end()` as the action taken by the upgrade-status
  callback/application path, so the compact visual can suggest more automatic
  framework behavior than the source implements.
- **Authoritative evidence/source:** server
  [`Response::upgrade()`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/web/http/server/Response.cpp#L276-L307)
  selects the factory and calls its creation surface. The WebSocket
  [`SocketContextUpgradeFactory`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/web/websocket/server/SocketContextUpgradeFactory.cpp#L66-L95)
  allocates the replacement before preparing the `101`; the tested application
  callback then calls
  [`response->end()`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/tests/component/websocket/WebSocketServerClientTextEchoTest.h#L217-L230).
  The post-callback detach → pointer change → attach order is implemented in
  [`SocketConnection.hpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketConnection.hpp#L360-L379).
- **Minimum required correction:** make the first visual stage “WebSocket
  factory selected; replacement context created,” and identify the fourth as
  the upgrade-status callback/application calling `response->end()` to queue
  the `101`. Preserve the existing staging, callback-return, context-switch,
  active-pointer, attach, and same-connection ordering.

## Audit summary

- **Current reviewed SNode.C `master` SHA:**
  `bf01683a53b48220a840522e8ccaf3b48e58c240`.
- **Step 3/5 baseline changed:** no.
- **Finding count:** **0 BLOCKER / 1 IMPORTANT / 3 MINOR**.
- **Commands technically reproducible as written:** yes. The target names,
  explicit binary paths, isolated `XDG_CONFIG_HOME`, global-option placement,
  instance/section hierarchy, loopback endpoint, client-line punctuation, and
  information-level listener/transport evidence all match the exact-revision
  qualification. The visible output does not overclaim payload proof.
- **Architecture/programming-model semantics:** correct in the draft prose and
  code excerpt. Endpoint/factory ownership, connection-driven `create(this)`,
  one active context, synchronous caller-thread `start()` dispatch, absence of
  a `tick()` claim, and the same-connection HTTP-to-WebSocket switch order are
  source-aligned. The two diagram findings above require only publication-level
  semantic clarification.
- **Release/platform/protocol evidence boundaries:** respected overall. The
  draft correctly bounds current release/package availability, Linux/GCC and
  Debian/x86-64 evidence, Bluetooth, TLS/security policy, HTTP 1.0/1.1,
  WebSocket 13, SSE, MQTT 3.1.1, MQTT over WebSocket, and downstream-project
  scope. Only the alternate-multiplexer qualification needs the minor explicit
  qualifier above.
- **Visual-status boundary:** `programming-model.svg` and
  `http-websocket-context-switch.svg` are technically validated working assets
  suitable for the draft; human publication approval and the two semantic
  refinements remain pending. `echo-connection-evidence.png` does not exist and
  is not referenced or treated as evidence by the draft.
- **Readiness for Claude Step 7b:** yes. There are no technical blockers. The
  draft may proceed to the independent editorial audit; Step 7c must resolve
  the publication links and apply the three precision corrections before the
  final README is publication-ready.
