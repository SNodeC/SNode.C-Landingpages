# Current-master capability map

[← SNode.C](../README.md) · [Architecture](architecture.md) ·
[Configuration](configuration.md) ·
[API reference](https://snodec.github.io/snode.c-doc/html/index.html)

This page answers a narrow question: what is visible in the reviewed SNode.C
source, and what did the recorded qualification or current public CI exercise?

It is not a permanent support matrix. The public presentation tracks `master`,
and the evidence below remains scoped to the reviewed revision and explicitly
identified earlier qualification runs.

**Reviewed baseline:** public `master` at
[`60f26d9`](https://github.com/SNodeC/snode.c/commit/60f26d9ae54b3e9ffde954d0ca75e53f79f31d79),
observed 30 August 2026.

Compared with the preceding qualified baseline `bf01683`, the current revision
adds the standalone `examples/echo` consumer, its CTests and CI wiring, an
annotated application walkthrough, and semantic echo logging. It does not change
the transport, HTTP, WebSocket, SSE, MQTT, configuration, or event-runtime
implementation used by the existing publication claims.

## Evidence vocabulary

- **Source-verified** means the component and its build integration exist at the
  reviewed commit.
- **Test-defined** means the repository contains a focused automated test; it
  does not say that every invocation passed in this documentation pass.
- **CI-observed** means the named public workflow/job result was inspected at the
  reviewed commit.
- **Runtime-qualified** means the named workflow was run in the recorded
  qualification environment.
- **Open** means the landing page must not turn the subject into an unqualified
  public claim.

The README's simpler **Available** label corresponds to source-verified
availability. Its **Exercised** label can summarize test-defined, CI-observed,
or runtime-qualified evidence; this page separates those states when the
distinction matters.

## Runtime and connection foundation

- **C++20 event-driven runtime.** **Source:** source-verified. **Runtime
  evidence:** the earlier clean Release configure/build/install and echo runs
  remain recorded; the current public
  [`gcc-debug` job](https://github.com/SNodeC/snode.c/actions/runs/33293707417/job/99209664201)
  also builds the tree and passes the main 181-test CTest suite. **Boundary:** no
  performance or real-time guarantee.
- **select, poll, and epoll multiplexer implementations.** **Source:**
  source-verified. **Runtime evidence:** the documented qualification and current
  CI use the configured/default implementation; no comparative run. **Boundary:**
  availability is not a benchmark.
- **Timers, descriptor events, event queue, signals.** **Source:**
  source-verified; repository tests exist. **Runtime evidence:** used indirectly
  by qualified applications and current tests. **Boundary:** no universal
  ordering/fairness claim.
- **Hierarchical application configuration.** **Source:** `ConfigRoot` and
  `SubCommand` provide a typed command tree that applications can extend with
  their own options and nested subcommands while sharing generated help,
  configuration-file, command-line, and inspection surfaces. **Runtime
  evidence:** the external echo example tests this surface; downstream MQTTSuite
  uses application-owned `SubCommand` types. **Boundary:** applications still own
  their configuration structure, defaults, validation, and secret-management
  policy.
- **Stream client and server roles.** **Source:** runtime-qualified for echo.
  **Runtime evidence:** listener and connector completed on recorded paths;
  current `examples/echo` builds as an installed-package consumer. **Boundary:**
  other protocols need their own qualification.
- **Connection read/write queues and accounting.** **Source:** source-verified;
  tests exist. **Runtime evidence:** echo exercised ordinary send/read.
  **Boundary:** queue-bound and overload policy remain application concerns.
- **Retry/backoff and client reconnect configuration.** **Source:**
  source-verified; tests exist. **Runtime evidence:** not part of the launch echo
  evidence. **Boundary:** exact failure sequences remain outside this claim.

## Standalone installed-package example

`examples/echo` is a complete external CMake project. It resolves:

```cmake
find_package(snodec REQUIRED COMPONENTS net-in-stream-legacy)
```

and links `snodec::net-in-stream-legacy`. Its source uses installed public
`<...>` headers and builds `echoserver` plus `echoclient`. Four application-level
CTest cases cover the generated configuration surface, real server versus an
external peer, real client versus an external peer, and a bounded real-pair
smoke run.

At `60f26d9`, the public
[`gcc-debug` job](https://github.com/SNodeC/snode.c/actions/runs/33293707417/job/99209664201)
successfully configured and built the main repository, passed **181/181** main
CTests, installed SNode.C to a staging prefix, then configured and built
`examples/echo` against that installed package. The subsequent external-example
CTest invocation failed **0/4 passed** because the example executables could not
locate `libsnodec-net-in-stream.so.2` from the staged install prefix at runtime.
That is recorded as an unresolved CI/runtime-loader integration issue; it is not
evidence that the four application tests passed, and this publication does not
describe them as passing.

## Network and connection variants

- **IPv4 plain stream.** **State:** runtime-qualified. **Runtime evidence:** echo
  server/client on `127.0.0.1`; current external example is the concrete
  installed-package IPv4/plain-stream composition.
- **IPv6 plain stream.** **State:** runtime-qualified on the preceding source
  baseline. **Runtime evidence:** echo server/client on `::1`. **Boundary:** not
  rerun in this closure pass.
- **Unix-domain plain stream.** **State:** runtime-qualified on the preceding
  source baseline. **Runtime evidence:** echo server/client using an isolated
  socket path. **Boundary:** not rerun in this closure pass.
- **TLS over IPv4.** **State:** runtime-qualified for one mutual-TLS echo path on
  the preceding source baseline. **Runtime evidence:** separate CA-signed server
  and client certificates connected. **Boundary:** not rerun in this closure
  pass; no universal TLS matrix.
- **Bluetooth RFCOMM.** **State:** source-verified. **Runtime evidence:** pending
  in this documentation pass. **Required environment for qualification:** BlueZ,
  adapter, peer, and protocol-specific qualification.
- **Bluetooth L2CAP.** **State:** source-verified. **Runtime evidence:** pending in
  this documentation pass. **Required environment for qualification:** BlueZ,
  adapter, peer, and protocol-specific qualification.

The source layout makes additional compositions expressible. These entries do
not promote an unrun composition merely because its types or targets exist.

## Application protocol components

- **HTTP.** Client/server contexts, request/response parsers, connection handling,
  transfer decoders, and upgrade selection. **Evidence boundary:** source-verified
  with repository component tests; no universal address-family matrix.
- **Express-style server API.** `WebApp`, routers, route matching, middleware,
  and request/response conveniences. **Evidence boundary:** source-verified;
  “Express-style” describes the programming approach, not Node.js API
  compatibility.
- **SSE/EventSource.** Server-sent-event streaming over HTTP and EventSource
  client support, including event parsing, event IDs, and reconnect handling.
  **Evidence boundary:** source-verified with plain-IPv4 SSE tests; no universal
  transport/address-family matrix.
- **WebSocket.** Client/server HTTP upgrade contexts, frame receiver/transmitter,
  subprotocol factories, and linked/loadable extension paths. **Evidence
  boundary:** source-verified with repository tests; plugin deployment policy is
  application-owned.
- **MQTT.** MQTT 3.1.1 protocol level, client and broker framework components,
  session-related source, and MQTT-over-WebSocket composition. **Evidence
  boundary:** source-verified; do not say “fully compliant” without a current
  conformance record.
- **MariaDB.** Optional database integration components. **Evidence boundary:**
  source-verified when the MariaDB development dependency is selected; database
  version/operations matrix remains open.
- **MIME detection.** Optional content-type helper using libmagic. **Evidence
  boundary:** source-verified when libmagic is available.

MQTTSuite is the appropriate public destination for ready-made MQTTBroker,
MQTTIntegrator, MQTTBridge, MQTTCli, and MQTTStore workflows. Their application
behavior should not be attributed to SNode.C itself.

## Build and dependency surface

The recorded Debian qualification environment used these package names for the
base source-build path:

```sh
sudo apt install --yes \
  build-essential ca-certificates cmake git ninja-build pkgconf \
  libssl-dev nlohmann-json3-dev
```

- **C++20 compiler — required.** Compiles SNode.C.
- **CMake 3.18 or newer — required.** Configures and generates builds; the
  minimum comes from project metadata.
- **Git and CA roots — required for the documented source workflow.** Used for
  clone and first-configure source retrieval.
- **`pkg-config`/`pkgconf` — required by the current graph.** Dependency
  discovery.
- **OpenSSL development files — required for the documented build.** TLS source
  and default graph.
- **nlohmann/json 3.11 or newer — required by the current graph.**
  JSON/configuration-related components.
- **CLI11 — vendored.** Command/configuration parser; no system package required.
- **spdlog — fetched as pinned source in the documented path.** Logging
  implementation; no system package required there.
- **BlueZ — optional.** RFCOMM/L2CAP layers.
- **libmagic — optional.** MIME detection.
- **MariaDB client development files — optional.** Database integration.
- **Curses — optional.** `snodec-control` TUI.
- **Doxygen and Graphviz — optional maintainer tools.** Generated API
  documentation and diagrams.
- **IWYU — optional maintainer tool.** Include analysis.
- **clang-format and cmake-format — optional maintainer tools.** Formatting
  targets.

## Packaging, platforms, and release status

The preceding source qualification configured, built, and installed SNode.C in
an isolated Debian GNU/Linux forky/sid x86-64 environment with GCC 16.2.0,
CMake 4.3.4, and Ninja 1.13.2. Current public CI at `60f26d9` provides a separate
Ubuntu/GCC Debug lane and validates the installed CMake consumer through
configuration and build, with the external example runtime-loader caveat above.

That evidence does not establish:

- a supported distribution list;
- a general GCC or Clang version range beyond project metadata and CI shapes;
- ARM, OpenWrt, Android/Termux, or other architecture support;
- ABI or API stability;
- current binary/package availability;
- performance, footprint, or production-readiness claims.

The CMake source version at the reviewed commit is `2.0.0`, while the latest
public GitHub release remains `v1.0.2`. Use the source number to identify project
metadata, not as proof that a 2.0 release, compatibility promise, or maturity
level exists.

## License and public routes

The source-verified license expression is `MIT OR LGPL-3.0-or-later`; the
repository contains both license texts. Canonical routes currently available
are:

- [repository](https://github.com/SNodeC/snode.c)
- [API reference](https://snodec.github.io/snode.c-doc/html/index.html)
- [Issues](https://github.com/SNodeC/snode.c/issues)
- [Discussions](https://github.com/SNodeC/snode.c/discussions)
- [Releases](https://github.com/SNodeC/snode.c/releases)

Dedicated public security, support, contribution, and compatibility policies
remain launch gaps.
