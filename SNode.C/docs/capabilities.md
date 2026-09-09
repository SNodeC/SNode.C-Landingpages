# Current-master capability map

[← SNode.C](../README.md) · [Architecture](architecture.md) ·
[Configuration](configuration.md) ·
[API reference](https://snodec.github.io/snode.c-doc/html/index.html)

This page separates what exists in the reviewed SNode.C source from what current
CI or recorded runtime qualification has actually exercised. It is deliberately
not a permanent support matrix and does not imply that every address-family ×
connection-mode × protocol combination is built, tested, or deployment-qualified.

**Reviewed source head:** public `master` at
[`1f0f728`](https://github.com/SNodeC/snode.c/commit/1f0f728fc9b3b45174f2cd790d83b2f493e58af1),
reviewed 9 September 2026.

**Current-head CI:**
[`CI` run 33489538669](https://github.com/SNodeC/snode.c/actions/runs/33489538669),
`gcc-debug` job
[`99797488461`](https://github.com/SNodeC/snode.c/actions/runs/33489538669/job/99797488461),
completed successfully. The job passed both the main repository CTest step and
the installed-package external echo CTests.

## Evidence vocabulary

- **Source-verified** — the component and build integration exist at the reviewed
  source head.
- **Test-defined** — focused automated tests exist in the repository.
- **CI-observed** — the named public workflow/job result was inspected at the
  reviewed source head.
- **Runtime-qualified** — a concrete runtime path was executed in a recorded
  qualification environment.
- **Open** — evidence is insufficient for an unqualified support, compatibility,
  performance, or deployment claim.

The README's **Available** wording corresponds to source presence. Its
**Exercised** wording may summarize test, CI, or recorded runtime evidence; this
page keeps those distinctions explicit when they matter.

## Runtime and connection foundation

- **C++20 event-driven runtime.** **Source:** source-verified. `SNodeC::start()`
  runs the event loop synchronously on its caller thread; descriptor and timer
  activity are dispatched through the event queue. **CI:** current-head build
  and main CTest step pass. **Boundary:** no throughput, latency, fairness, or
  real-time guarantee is implied.
- **Event multiplexers.** **Source:** `epoll`, `poll`, and `select`
  implementations are present; one backend is selected for a build. **Evidence:**
  current CI exercises its configured backend, not a comparative backend matrix.
- **Timers, descriptors, event queue, lifecycle dispatch.** **Source:**
  source-verified with focused tests. **Runtime:** exercised indirectly by the
  qualified client/server paths. **Boundary:** no universal event-ordering or
  workload-suitability claim.
- **Stream server/client roles.** **Source:** `SocketServer` and `SocketClient`
  flows retain their context factory and create connection-local
  `SocketConnection` / `SocketContext` state. **CI:** the installed external echo
  server/client is configured, built, and tested at the current head.
- **Connection queues/accounting.** **Source:** send queues, accounting,
  timeouts, shutdown and watermarks exist. **Boundary:** mechanism presence is
  not an automatic backpressure/resource-bound policy for every application.
- **Retry and reconnect.** **Source:** establishment retry/backoff is separate
  from client reconnect after a previously established connection is
  interrupted. **Boundary:** deployment policy still has to select bounded
  behavior appropriate to the workload.

## Configuration

SNode.C uses a typed `ConfigRoot` / `SubCommand` hierarchy shared by framework
endpoint configuration and application-owned settings.

- **Named endpoint instances** are addressable through generated CLI and
  configuration-file paths.
- **Anonymous instances** are API-configurable but do not expose a named
  CLI/config-file instance address.
- **Resolution precedence** is API/default < configuration file < command line.
- **Inspection surfaces** include `--help=expanded`, `--show-config`, and
  `--command-line=...`; `--write-config` persists configuration values rather
  than serializing arbitrary runtime state.

The exact local/remote/connection/socket/TLS section surface depends on the
concrete endpoint role, address family, and connection mode.

## Standalone installed-package example

[`examples/echo`](https://github.com/SNodeC/snode.c/tree/1f0f728fc9b3b45174f2cd790d83b2f493e58af1/examples/echo)
is a complete downstream CMake consumer. It resolves:

```cmake
find_package(snodec REQUIRED COMPONENTS net-in-stream-legacy)
```

and links the namespaced installed target `snodec::net-in-stream-legacy`.
Current-head CI installs SNode.C into a staging prefix, configures and builds the
external example against that installed package, then passes its external echo
CTest step. This supersedes the earlier recorded CI loader failure at
`60f26d9`.

## Network and connection variants

| Path | Current source | Strongest recorded evidence | Boundary |
| --- | --- | --- | --- |
| IPv4 plain stream | Source-verified | Current external echo CI + recorded loopback runtime | Concrete plain-stream path, not every higher protocol combination |
| IPv6 plain stream | Source-verified | Earlier recorded loopback runtime | Not rerun as part of this landing-page closure |
| Unix-domain plain stream | Source-verified | Earlier recorded Unix-socket runtime | Not rerun as part of this landing-page closure |
| OpenSSL-backed TLS | Source-verified | Focused TLS tests + earlier mutual-TLS IPv4 echo | No universal certificate/cipher/family matrix |
| Bluetooth RFCOMM | Conditional source/build path | Source/build evidence | No hardware runtime qualification here |
| Bluetooth L2CAP | Conditional source/build path | Source/build evidence | No hardware runtime qualification here |

The existence of compatible layer types or CMake components does not promote an
unrun composition to a supported/qualified combination.

## Application protocol components

- **HTTP.** HTTP/1.0 and HTTP/1.1 client/server contexts, parsing, transfer
  handling, and upgrade selection. **Evidence:** source and repository tests;
  coverage breadth differs by address family and connection mode. **No HTTP/2
  claim.**
- **Express-style API.** Routing, middleware and request/response conveniences
  above HTTP. “Express-style” describes the programming model, not Node.js
  Express API compatibility.
- **SSE / EventSource.** Event-stream support remains within HTTP and includes
  EventSource parsing/reconnect semantics. It does not use the WebSocket context
  replacement path.
- **WebSocket.** Version-13 client/server upgrade contexts, frame handling and
  subprotocol infrastructure. HTTP Upgrade stages a replacement context on the
  same established `SocketConnection`.
- **MQTT.** MQTT 3.1.1 client/server framework components plus
  MQTT-over-WebSocket composition. Do not infer MQTT 5 or conformance breadth
  beyond current tests/qualification.
- **MariaDB.** Optional database integration source/build components when the
  dependency is selected. Database-version and operations matrices remain
  outside this landing-page claim.
- **MIME detection.** Optional libmagic-backed content-type support when the
  dependency is available.

[MQTTSuite](https://github.com/SNodeC/mqttsuite) is the public destination for
ready-made MQTTBroker, MQTTIntegrator, MQTTBridge, MQTTCli and MQTTStore
application workflows. Those application behaviors are not attributed to the
SNode.C framework itself.

## Build and dependency surface

The documented source-build path requires a C++20 compiler, CMake 3.18+, Git,
`pkg-config`/`pkgconf`, OpenSSL development files and nlohmann/json 3.11+.
CLI11 is vendored; the documented build fetches pinned logging source as part of
its dependency graph. BlueZ, libmagic, MariaDB client development files, curses,
Doxygen/Graphviz, IWYU and formatting tools are optional according to the
selected components or maintainer tasks.

Current-head CI provides a Linux/GCC Debug lane. Earlier documentation
qualification also used a Debian/x86-64 Release build. This does **not** establish
an operating-system, distribution, compiler, architecture, ABI/API stability,
performance, footprint, or production-readiness support matrix.

## Release and package status

The reviewed source metadata declares version `2.0.0` in
[`CMakeLists.txt`](https://github.com/SNodeC/snode.c/blob/1f0f728fc9b3b45174f2cd790d83b2f493e58af1/CMakeLists.txt).
The latest public GitHub release is still
[`v1.0.2`](https://github.com/SNodeC/snode.c/releases/tag/v1.0.2), published
28 June 2026, and contains no binary release assets. Therefore source version
`2.0.0` is not presented here as proof of a tagged 2.0 release, binary package,
compatibility promise, or maturity level.

## License and public routes

The source-verified license expression is `MIT OR LGPL-3.0-or-later`.

- [Repository](https://github.com/SNodeC/snode.c)
- [API reference](https://snodec.github.io/snode.c-doc/html/index.html)
- [Issues](https://github.com/SNodeC/snode.c/issues)
- [Discussions](https://github.com/SNodeC/snode.c/discussions)
- [Releases](https://github.com/SNodeC/snode.c/releases)

Dedicated public security, support, contribution, compatibility and release
policies should be treated as separate project surfaces rather than inferred
from source presence.
