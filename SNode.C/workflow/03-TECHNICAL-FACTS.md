# SNode.C Step 3 — verified technical fact base

**Workflow stage:** Step 3 only

**Verification date:** 29 August 2026

**Scope:** SNode.C facts needed by the later README design

**Public source baseline:** [`bf01683a53b48220a840522e8ccaf3b48e58c240`](https://github.com/SNodeC/snode.c/commit/bf01683a53b48220a840522e8ccaf3b48e58c240)

This file is the complete repository handoff for Step 4. It records technical
truth and evidence boundaries; it does not design the README, prescribe a
section structure, or provide launch copy.

The working [evidence register](../EVIDENCE.md), [shared facts](../../FACTS.md),
[repository audit](../../workflow/01-REPOSITORY-AUDIT.md), and
[ecosystem positioning](../../workflow/02-ECOSYSTEM-POSITIONING.md) were used as
research. Current public source, tests, CI, release metadata, and public routes
control where those artifacts disagree.

## Evidence classes used here

Every material capability is kept separate across these five classes:

| Code | Evidence class | What it proves |
| --- | --- | --- |
| **I** | Implementation | The implementation or public API exists at the reviewed commit. |
| **B** | Build/configuration | CMake exposes the target, option, dependency, or installed component; a successful build proves only the configured graph. |
| **T** | Automated test | A named unit, component, policy, or installed-consumer test exercises the stated behavior. |
| **Q** | Reproducible qualification | The named workflow was run independently of the repository test suite in a recorded environment. |
| **A** | Public availability | A tag, release asset, package, or installed distribution makes the stated revision obtainable in that form. |

Source presence is not treated as test coverage. A passing test is not treated
as a support policy. A local install is not treated as a published package.

## Verification baseline

| Item | Verified result |
| --- | --- |
| Review date | 29 August 2026 |
| Public repository | [`SNodeC/snode.c`](https://github.com/SNodeC/snode.c) |
| Branch | `master` |
| Exact observed public head | [`bf01683a53b48220a840522e8ccaf3b48e58c240`](https://github.com/SNodeC/snode.c/commit/bf01683a53b48220a840522e8ccaf3b48e58c240) |
| Head commit time | 28 August 2026, 16:16:20 UTC |
| Public-head checks | `git ls-remote` and the GitHub commit API returned the same SHA. The read-only local mirror also matched and was not modified. |
| Previous evidence baseline | The 28 August 2026 baseline in [`FACTS.md`](../../FACTS.md) and [`EVIDENCE.md`](../EVIDENCE.md) is the same exact SHA. |
| Source-change decision | **Unchanged.** No source, build, dependency, test, or example delta existed to invalidate the selected 28 August qualification. Expensive qualification was not rerun merely for ceremony. |
| Refreshed external evidence | Current public CI, release/tag metadata, documentation availability, policy-file presence, the OpenWrt feed, and downstream heads were checked on 29 August. |

The current [CI run for this exact SHA](https://github.com/SNodeC/snode.c/actions/runs/33189174904)
completed successfully. Its single `gcc-debug` job installed the declared
dependencies, configured, built, and ran CTest successfully on
`ubuntu-latest`. This upgrades the old statement “the complete repository
CTest suite remains a separate gate”: the root-configured suite did pass in
public CI at the reviewed SHA, although it was not rerun locally for this Step 3
review.

## Concise verified product definition

SNode.C at the reviewed commit is a C++20 framework for building event-driven
network clients and servers. It supplies:

- a singleton descriptor/timer event loop;
- configurable stream-server and stream-client endpoint templates;
- a connection-local application-context model;
- IPv4, IPv6, Unix domain, and conditional Bluetooth address-family layers;
- plain stream and OpenSSL-backed TLS connection layers;
- HTTP, Express-style, WebSocket, EventSource/SSE, and MQTT 3.1.1 components;
- configuration through C++ API defaults, configuration files, and generated
  command-line sections; and
- componentized shared libraries with CMake install/export metadata.

**Evidence:** **I** in the public headers and implementations under
[`src/core`](https://github.com/SNodeC/snode.c/tree/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core),
[`src/net`](https://github.com/SNodeC/snode.c/tree/bf01683a53b48220a840522e8ccaf3b48e58c240/src/net),
[`src/web`](https://github.com/SNodeC/snode.c/tree/bf01683a53b48220a840522e8ccaf3b48e58c240/src/web),
[`src/express`](https://github.com/SNodeC/snode.c/tree/bf01683a53b48220a840522e8ccaf3b48e58c240/src/express),
and [`src/iot/mqtt`](https://github.com/SNodeC/snode.c/tree/bf01683a53b48220a840522e8ccaf3b48e58c240/src/iot/mqtt);
**B** in the CMake graph; **T** in the current root test suite; **Q** for the
selected echo paths and downstream current-master builds; **A** does not exist
for current master as a tagged or binary-packaged release.

SNode.C is not an MQTT deployment toolkit, Codex integration, or user
interface. Those responsibilities belong to MQTTSuite, AISuite, and CodexUI.
It is also not Node.js, a JavaScript runtime, an npm ecosystem, or an
Express-compatible implementation.

## Verified programming model

### Public roles and relationships

| Concept | Verified role | Evidence |
| --- | --- | --- |
| `SocketServer` | A configured endpoint handle that initiates a listen/accept flow. It owns shared server flow state and a `SocketContextFactory`; each accepted physical stream becomes a `SocketConnection`. | [`SocketServer.h`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketServer.h), listener lifecycle and IPv4/IPv6/Unix component tests |
| `SocketClient` | A configured endpoint handle that initiates connections. It owns shared client flow state and a factory and implements retry and optional post-disconnect reconnect scheduling from configuration. | [`SocketClient.h`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketClient.h), connection-attempt and component tests |
| `SocketConnection` | The established connection object. It owns the descriptor-backed stream behavior, local/bind/remote addresses, connection identity, queues and counters, timeouts, and the currently active application context. | [`SocketConnection.h`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketConnection.h) and [implementation](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketConnection.cpp) |
| `SocketContextFactory` | The application-supplied creation boundary. Its public virtual `create(SocketConnection*)` returns the context for a newly established connection. | [`SocketContextFactory.h`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketContextFactory.h), echo factories, lifecycle tests |
| `SocketContext` | The per-connection protocol/application behavior. It receives connection attach/detach, readable-data, signal, and error callbacks and sends, reads, streams, times out, shuts down, or closes through its connection. | Base [socket context](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/SocketContext.h), [stream context](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketContext.h), context lifecycle test |

The precise recurring relationship is:

1. an application constructs a configured server or client instance;
2. the endpoint accepts or initiates a physical stream connection;
3. the framework creates a `SocketConnection`;
4. the instance's factory creates the connection-local `SocketContext`; and
5. the event loop dispatches connection and data events into that context.

The connection has one active context at a time. Calling
`SocketConnection::setSocketContext()` while a context is active stages a
replacement. The old context detaches with
`DetachReason::ContextSwitch`, the new one attaches, and the underlying
connection remains in place. Final connection teardown uses
`DetachReason::ConnectionClose`. The HTTP-to-WebSocket upgrade path uses this
implemented mechanism rather than creating an unrelated second connection.
This is **I** and **T**; the public WebSocket component tests exercise real
HTTP upgrade paths over the tested plain address families.

### Event loop and lifecycle

The public lifecycle surface is
`core::SNodeC::init/start/stop/tick/free/state`. The state enum contains
`LOADED`, `INITIALIZED`, `RUNNING`, and `STOPPING`.

- `init` initializes configuration and moves the singleton event loop to
  `INITIALIZED`.
- `start` bootstraps configuration, enters `RUNNING`, and repeatedly waits
  for descriptor/timer work and dispatches queued events.
- `tick` exposes one event-loop iteration for an initialized application.
- `stop` requests `STOPPING`.
- `free` begins graceful shutdown, gives pending resources up to two seconds
  to drain, terminates remaining descriptor receivers and timers, clears the
  event queue, and terminates configuration.

The reviewed framework source creates no `std::thread`, `std::jthread`,
`std::async`, or pthread worker. Event callbacks are dispatched
synchronously on the thread calling `start` or `tick`. This is the precise
supported meaning behind a scoped “single event-loop thread” statement. It is
not a prohibition on application-created threads, and it provides no
performance or memory conclusion. A blocking or long-running callback delays
other work on that loop.

The event multiplexer implementations are `epoll`, `poll`, and `select`.
The default build selects `epoll`; `SNODEC_IO_MULTIPLEXER` may select one of
the three. All three implementations are built as component libraries, but
the linked core uses the selected implementation. The preserved qualification
used the default; no comparative or cross-platform multiplexer qualification
exists.

**Primary evidence:** [`SNodeC.h`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/SNodeC.h),
[`EventLoop.cpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/EventLoop.cpp),
[`EventMultiplexer.cpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/EventMultiplexer.cpp),
and [core CMake selection](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/CMakeLists.txt).

## Verified architecture and layer model

The source supports this technical decomposition:

| Layer | Responsibility | Verified scope |
| --- | --- | --- |
| Event runtime | Descriptor readiness, timers, signals, queued event dispatch, resource shutdown | `epoll` default; selectable `poll` and `select` |
| Address/network family | Address representation and family-specific physical socket behavior | IPv4 (`in`), IPv6 (`in6`), Unix domain (`un`), conditional Bluetooth RFCOMM (`rc`) and L2CAP (`l2`) |
| Physical connection | Listen, accept, connect, read/write, lifecycle, address ownership | Connection-oriented stream endpoints; a separate lower-level Unix-domain datagram component also exists |
| Connection mode | Plain byte stream or OpenSSL TLS state and encryption | Source wrappers for each stream family; Bluetooth wrappers are conditional on BlueZ |
| Endpoint role | Configured server/listener or client/connector | `SocketServer` and `SocketClient` |
| Application context | Connection-local parsing, framing, protocol state, and callbacks | Custom contexts plus supplied HTTP, WebSocket, MQTT, and related layers |

The source term `legacy` names the unencrypted/plain stream implementation. It
does not establish a lifecycle or deprecation status.

There is no evidence for a universal Cartesian product of all rows. In
particular:

- HTTP address wrappers exist for IPv4, IPv6, Unix domain, and conditional
  RFCOMM, in plain and TLS forms; no L2CAP HTTP wrapper was found.
- WebSocket is an HTTP upgrade layer and inherits a concrete HTTP/connection
  binding chosen by the application.
- MQTT supplies generic client/server protocol contexts and MQTT-over-WebSocket
  components; its SNode.C test coverage is not a transport matrix.
- only Unix-domain datagram is exposed as a datagram component; the reviewed
  source does not provide general IPv4/IPv6 UDP endpoint counterparts.

## Verified capability inventory

### Address families, streams, and TLS

`A` is “No current-master release” for every row below. Older tags cannot be
used as proof for the current implementation.

| Capability | I — implementation | B — build/configuration | T — tests at current SHA | Q — separate qualification | A |
| --- | --- | --- | --- | --- | --- |
| IPv4 plain stream | Server/client/address layers exist | Always configured; installed `net-in-stream-legacy` component | Plain loopback composition, payload, framing, large payload, multiple-client, close, failure, and address tests passed in CI | Echo pair ran on `127.0.0.1` | No |
| IPv6 plain stream | Server/client/address layers exist | Always configured; installed `net-in6-stream-legacy` component | Corresponding plain IPv6 loopback composition, payload, framing, large payload, multiple-client, close, and failure tests passed | Echo pair ran on `::1` | No |
| Unix-domain plain stream | Server/client/address layers exist | Always configured; installed `net-un-stream-legacy` component | Composition, payload, framing, large payload, multiple-client, lifecycle, path-safety, address, and peer-credential tests passed | Echo pair ran with an isolated socket path | No |
| Bluetooth RFCOMM plain stream | Source layer exists | Built only when BlueZ is found; current CI installed BlueZ and its configured build passed | No targeted RFCOMM component or hardware test in the root suite | Not run | No |
| Bluetooth L2CAP plain stream | Source layer exists | Built only when BlueZ is found; current CI installed BlueZ and its configured build passed | No targeted L2CAP component or hardware test in the root suite | Not run | No |
| Unix-domain datagram | Lower-level `net-un-dgram` component exists | Always configured and installable | No targeted datagram component test found | Not run | No |
| Generic TLS stream layer | OpenSSL-backed handshake, read/write, shutdown, certificate/CA, cipher/options, SNI, and state-machine code exists | OpenSSL is required by the default graph; TLS wrappers exist for all five stream families, with Bluetooth conditional | TLS classification, fatal-path, ownership, state-machine, shutdown, logging, and source-compatibility unit tests passed; no certificate-bearing network component matrix exists | One mutual-TLS IPv4 echo pair connected | No |

### Exact TLS and encryption scope

- The TLS layer uses OpenSSL
  `TLS_server_method()`/`TLS_client_method()`. The source does not set a
  fixed protocol-version minimum or maximum; the negotiated range therefore
  depends on the linked OpenSSL and configured options. No README claim should
  name TLS 1.2, TLS 1.3, or a universal version range without a new
  qualification.
- Configuration exposes certificate chain, private key, key credential, CA
  file/directory/default paths, an explicit accept-unknown flag, OpenSSL cipher
  list and option values, handshake/shutdown timeouts, client SNI, and server
  SNI certificate maps.
- With no CA source enabled, the implementation sets no peer-verification mode.
  Providing a CA source or enabling the default CA path enables peer
  verification unless accept-unknown is selected. TLS availability is
  therefore not a “secure by default” claim.
- The preserved mutual-TLS run supplied separate client and server certificates
  signed by the same local CA. It proves that one IPv4 connection and
  certificate arrangement completed. It does not prove hostname verification,
  revocation policy, every address family, every application protocol, or
  production deployment policy.
- Automatic hostname verification is not enabled by the supplied echo client;
  the relevant example code is commented out.
- The TLS echo server source seeds an SNI map with developer-specific
  certificate defaults. The qualification used explicit synthetic certificate
  arguments and did not rely on that SNI mapping. Step 4 must not reproduce the
  embedded values or imply that the TLS demo is deployment-ready.

### Application protocols and higher layers

| Capability | I — implementation | B — build/configuration | T — tests at current SHA | Q — separate qualification | A |
| --- | --- | --- | --- | --- | --- |
| HTTP client/server | Parsers, request/response contexts, content decoding, limits, and client/server APIs exist for HTTP/1.0 and HTTP/1.1 | `http`, `http-server`, and `http-client` components install | Parser/formatter/policy tests plus plain IPv4 round trips, chunking, pipelining, large bodies, limits, malformed input, lifecycle and failures; smaller IPv6/Unix round-trip sets passed | No separate HTTP launch run | No |
| Express-style server API | `WebApp`, router, mounted/nested routes, middleware, static, JSON, basic-auth, and virtual-host building blocks exist | Base and family/mode wrapper components install when their dependencies exist | Plain IPv4 routing/middleware tests and IPv6/Unix transport smoke tests passed | No separate launch run | No |
| WebSocket | Version-13 HTTP handshake, client/server upgrade contexts, text/binary framing, ping/pong, close, limits, and subprotocol factories exist | `websocket-server` and `websocket-client` components install | Unit validation/limit tests; plain IPv4 text/binary/multiple/large/ping/close tests; IPv6 and Unix text-echo tests passed | No separate launch run | No |
| EventSource/SSE | HTTP EventSource client and server-side event behavior exists | Built with the HTTP components | Plain IPv4 basic, multiline, comment, default-message, retry, reconnect, close, and lifecycle component tests passed | No separate launch run | No |
| MQTT 3.1.1 | Protocol-level-4 packets, client/server contexts, broker/session/topic behavior, and QoS-related code exist | `mqtt`, `mqtt-server`, and `mqtt-client` components build when nlohmann/json is available | Two unit tests cover MQTT 3.1.1 packet validation and protocol lifecycle with test doubles; there is no SNode.C MQTT network component suite | A downstream MQTTSuite IPv4 QoS 1 broker/subscriber/publisher scenario ran; this is not a general SNode.C conformance result | No |
| MQTT over WebSocket | MQTT WebSocket subprotocol components exist for client and server | `mqtt-server-websocket` and `mqtt-client-websocket` are exported components | No targeted SNode.C network component test found | Not run in the SNode.C qualification | No |
| MariaDB integration | Optional synchronous/asynchronous MariaDB client component exists | Built only when `libmariadb` is found; current CI installed it and built successfully | No targeted database test was found in the root suite | Not run | No |

Protocol boundaries:

- The HTTP parser's version expression accepts only HTTP/1.0 and HTTP/1.1.
  Tests explicitly reject HTTP/2.0. HTTP/0.9 is not a current capability.
- WebSocket version 13 is directly selected in the client and accepted by the
  server. The evidence supports concrete implemented/tested behavior, not the
  phrase “full WebSocket support” or a conformance certification.
- The MQTT server accepts protocol level `0x04` (MQTT 3.1.1). A
  `MQTT_VERSION_5_0` constant exists, but the server rejects levels other
  than `0x04`; MQTT 5 is not a current capability.
- “Express-style” describes routing and middleware concepts. It does not mean
  Node.js Express API, package, behavioral, or runtime compatibility.
- OAuth2, calculator, echo, and WebSocket programs under `src/apps` are
  examples. Their presence is not a separate protocol-support or security
  certification.

## Verified configuration surfaces and precedence

### Surfaces

| Surface | Verified behavior | Boundary |
| --- | --- | --- |
| C++ API | Endpoint `getConfig()` objects expose typed, scope-qualified setters. Setters establish default values before bootstrap. | Available to named and anonymous instances. |
| Configuration file | The root CLI11 configuration system reads flattened hierarchical keys for configurable named instances and their sections. | Anonymous instances have no root subcommand and are API-only. |
| Command line | Named endpoint instances generate subcommands and role/family/mode-specific descendant sections. The echo shape is `echoserver local ...` or `echoclient remote ...`, with a `tls` descendant for TLS builds. | The exact option set depends on the compiled endpoint type. |
| Inspection/export | `--help=expanded`, `--show-config`, `--command-line=standard|active|complete|required`, and `--write-config` exist. | These expose configuration; they do not define a deployment policy. |

The verified effective precedence is:

1. command-line value;
2. configuration-file value, applied only when the option is still empty; and
3. API-set/default value.

This follows the reviewed CLI11 parse order and the implementation's use of
default values for API setters. The old live README's
`--command-line=full|default` modes are stale; current source uses
`active|complete`.

### Externally relevant configuration groups

- global process/logging behavior, including semantic log filters, output
  format, optional file logging, daemonization, and instance aliases;
- instance enable/disable state;
- server local/listen or client remote and optional local addresses;
- connection read/write block sizes, inactivity timeouts, shutdown timeout,
  maximum queued bytes, and high/low watermarks;
- socket listen backlog, accepts per tick, connect/accept timeout, retry,
  exponential backoff, jitter and limit, and client reconnect controls;
- family-specific address and socket options; and
- the TLS material and policy controls listed above.

The source and tests establish available controls and validation. They do not
establish automatic overload safety, universal backpressure, credential
management, or a security policy.

**Evidence:** [configuration implementation](https://github.com/SNodeC/snode.c/tree/bf01683a53b48220a840522e8ccaf3b48e58c240/src/net/config),
[`Config.cpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/utils/Config.cpp),
the vendored [CLI11 parser](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/utils/CLI11.hpp),
configuration unit tests, and the generated echo CLI observed during
qualification.

## Public extension points and composability

The following extension mechanisms are technically supportable:

1. derive a `SocketContextFactory` and `SocketContext` to supply custom
   per-connection behavior;
2. instantiate the `SocketServer`/`SocketClient` templates with concrete
   family, physical stream, connection mode, configuration, and factory types;
3. replace an active context on an established connection, as used by
   HTTP-to-WebSocket upgrade;
4. implement HTTP upgrade factories and WebSocket subprotocol factories;
5. compose Express-style routers, mounted routers, controllers, and middleware;
6. consume selected installed libraries through namespaced CMake components;
   and
7. use the API/config-file/CLI hierarchy to configure application-defined named
   endpoint instances.

Some HTTP/WebSocket extensions are dynamically loadable shared objects.
Dynamic loading is process-level code execution, not a plugin sandbox or
security boundary.

“Composable” is safe only when attached to these concrete mechanisms. It must
not be expanded into “every family, connection mode, and application protocol
combination is supported or tested.”

## Build, dependency, test, and installation facts

### Language level, compilers, and build options

| Fact | Verified result | Evidence boundary |
| --- | --- | --- |
| CMake | Minimum `3.18` | Source requirement; preserved qualification used CMake 4.3.4 |
| C++ | C++20 required; extensions disabled | Source and installed-consumer builds |
| GCC | CMake rejects GNU versions below 12.2 | Preserved qualification used GCC 16.2.0; public CI uses the unversioned `g++` from `ubuntu-latest` |
| Clang | CMake rejects Clang versions below 13.0 | Build metadata only; no current Clang CI or Step 3 runtime qualification |
| Other compilers | No equivalent explicit version rejection | No support or qualification may be inferred |
| Default multiplexer | `epoll` | Default configured path only |
| Applications | `SNODEC_BUILD_APPS=ON` by default | Echo and other example targets build when dependencies allow |
| Tests | `SNODEC_BUILD_TESTS=OFF` by default | Must be enabled for root CTest registration |
| Sanitizer | `SNODEC_ENABLE_ASAN=OFF` by default | Build option exists; no launch qualification recorded |
| Generator | No source requirement for Ninja | Ninja 1.13.2 was the preserved qualification generator |

The source sets warning-as-error and GNU/Clang-oriented linker and warning
flags. The default `epoll` path and substantial POSIX API use mean the current
evidence is Linux/POSIX-oriented; this is not evidence for Windows or a broad
portable-platform claim.

### Mandatory dependencies for the reviewed default graph

| Dependency | Verified role |
| --- | --- |
| C++20 compiler and CMake 3.18+ | Compile and configure |
| OpenSSL development library | Unconditionally required when the TLS subgraph is configured; the current default graph always adds it |
| pkg-config | Unconditionally required by current network/web/protocol discovery |
| nlohmann/json 3.11+ | Required by the always-added Express graph; also used by MQTT |
| Git/network access on a fresh default configure | CMake FetchContent clones pinned spdlog `v1.17.0`, unless the dependency is already populated or explicitly overridden |

CLI11 2.6.2 is vendored as a single header. It is not a required system
package. spdlog is fetched at the pinned tag; it is not a required system
development package in the qualified build.

### Conditional dependencies

| Dependency | Capability when present | Behavior when absent |
| --- | --- | --- |
| BlueZ | RFCOMM and L2CAP libraries, wrappers, and matching applications | Bluetooth targets are omitted with a warning |
| libmagic | More complete file MIME-type detection in HTTP | Built-in MIME knowledge remains |
| MariaDB client library | `db-mariadb` component | Database component is omitted |
| Curses | Interactive `snodec-control --ui` implementation | Other control-tool features build; UI reports unavailable |
| OpenSSL command-line tool | Certificate generation and inspection for qualification/examples | Not required merely to compile the library |
| Doxygen and Graphviz | API-documentation targets and graphs | Documentation targets are limited/omitted |
| include-what-you-use, clang-format, cmake-format | Maintainer analysis/format targets | Not runtime dependencies |

No minimum version is declared in current CMake for OpenSSL, BlueZ, libmagic,
MariaDB, or Curses. Do not invent one from the qualification host's package
versions.

### Build, tests, install, and packaging

- The preserved isolated Release qualification configured, built, and installed
  this SHA on Debian GNU/Linux forky/sid, x86-64, using GCC 16.2.0, CMake
  4.3.4, and Ninja 1.13.2.
- The exact public CI run configured Debug with applications and root tests on,
  built the full configured graph with OpenSSL, BlueZ, libmagic, MariaDB, and
  nlohmann/json present, and completed CTest successfully.
- Install rules export namespaced CMake targets and a
  `snodecConfig.cmake`/version file. The component list includes core,
  address/stream layers, HTTP, Express, WebSocket, MQTT, optional Bluetooth and
  MariaDB, and applications where built.
- `StagedInstalledConsumerTest`, part of the passing root CTest run, performs a
  staged install, verifies selected private core headers are not installed,
  compiles and runs a direct-link consumer using core/IPv4 plain/Express
  libraries, and configures, builds, and runs a `find_package` consumer using
  core and Unix-domain plain stream components.
- The previous 28 August all-master qualification also built MQTTSuite,
  AISuite, and the then-current CodexUI against the isolated SNode.C install.
  That is downstream-consumer evidence for those exact SHAs, not a release
  compatibility policy.
- CPack contains componentized Debian-package generation rules. This is build
  configuration only: no current-master CPack package was qualified or
  published in the reviewed GitHub release.

The installed version file uses CMake's `SameMinorVersion` selection rule and
shared libraries use `SOVERSION 2`. These mechanisms do not establish a
forward ABI/API stability or deprecation policy. The maintained
[`migration-2.0.md`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/docs/migration-2.0.md)
states that 2.0 starts a new API/ABI epoch, requires 1.x consumers and plugins
to rebuild, and forbids mixing 1.x and 2.0 libraries in one process. It does not
promise compatibility for future 2.x changes.

## Current tests and what they prove

### Public full-test status

| Item | Verified status |
| --- | --- |
| Workflow | [`.github/workflows/ci.yml`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/.github/workflows/ci.yml) |
| Run | [CI run 33189174904](https://github.com/SNodeC/snode.c/actions/runs/33189174904) |
| Job | [`gcc-debug` job 98909939950](https://github.com/SNodeC/snode.c/actions/runs/33189174904/job/98909939950) |
| Commit | Exact reviewed SHA |
| Result | Configure, Build, and Tests steps all completed successfully |
| Matrix | One `ubuntu-latest`/`g++` Debug job; not a compiler, OS, or architecture matrix |
| Exact test count | Not claimed; unauthenticated job logs were not available, and a static source count is not substituted for executed CTest output |

### Root-suite coverage

| Area | What passing tests establish | What they do not establish |
| --- | --- | --- |
| Core/event loop | Initialization/free, stop from callbacks, timers, descriptor failure, pipes/streaming, shutdown, endpoint and connection lifecycle | Fairness for arbitrary workloads, real-time behavior, performance |
| Stream networking | Plain IPv4, IPv6, and Unix loopback composition, payload/framing, large payload, multiple clients, failures, disconnect and close paths | TLS network matrix, Bluetooth hardware, Unix datagram, non-loopback deployment |
| TLS internals | Result classification, fatal paths, helper ownership, state machine, shutdown, logging, selected source compatibility | Certificate-bearing interoperability across families/protocols, hostname policy, security audit |
| HTTP | HTTP/1 parsing/formatting/limits/policy and plain IPv4 broad round trips; smaller IPv6/Unix round trips | HTTP/0.9, HTTP/2, TLS HTTP, RFCOMM HTTP, conformance certification |
| Express-style layer | IPv4 routing and middleware behavior; IPv6/Unix transport smoke | Node/Express compatibility, TLS/RFCOMM matrix |
| WebSocket | Frame validation/limits and plain IPv4 behavior; IPv6/Unix text echo | TLS/RFCOMM matrix, every extension/subprotocol, conformance certification |
| EventSource/SSE | Plain IPv4 event parsing, sequencing, retry/reconnect, close and lifecycle | Other families/modes |
| MQTT | MQTT 3.1.1 packet validation and protocol lifecycle through test doubles | Network broker/client integration, transport matrix, complete QoS/conformance matrix, MQTT 5 |
| Installation | Staged install, selected public/private header boundary, selected direct and CMake consumers | Every exported component and every external distribution |
| Policy tests | Selected logging API/source discipline, sensitive-log source policy, epoll/syscall and CI-path invariants | Product security certification or platform support |

The nested `snodec-control` project has a separate
`SNODEC_CONTROL_BUILD_TESTS` option that defaults off. Enabling root
`SNODEC_BUILD_TESTS` does not enable those standalone control-tool tests, so
the successful root CI result must not be described as every test source in
every nested project.

## First-success and echo facts

### Best currently verified path

The shortest independently qualified path is the supplied plain IPv4 echo
server/client pair on loopback. These are the exact reproducible source-selection
and build commands for the reviewed head:

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
export PATH="$PWD/cmake-build-release/src/apps/echo:$PATH"
```

Listener:

```sh
echoserver-legacy-in echoserver local --host 127.0.0.1 --port 18001
```

Client:

```sh
echoclient-legacy-in echoclient remote --host 127.0.0.1 --port 18001
```

The preserved real capture and runtime record establish these visible success
signals, ignoring timestamps and line wrapping:

```text
echoserver: listener started
echoserver: listening on '127.0.0.1:18001'
role=server inst=echoserver conn=1 — transport connected

echoclient: connected to '127.0.0.1:18001' (127.0.0.1)
role=client inst=echoclient conn=1 — transport connected
```

Stop both processes with Ctrl-C.

### What the echo code actually does

The client context sends `Hello peer! Nice to see you!!!` from
`onConnected()`. Both client and server contexts read available bytes in
`onReceivedFromPeer()` and send the same bytes back. Consequently the supplied
pair continues reflecting the chunk until interrupted; it is not a one-shot
terminal program that prints a single returned payload.

The default information-level capture shows listener/connection success, not
the application payload. Context-attach messages are debug-level and “Data to
reflect” is trace-level. Step 4 may use the verified connection output and the
source-defined callback behavior, but must not fabricate a terminal line that
the current default run does not print or describe the existing screenshot as
direct visible payload proof.

**Evidence:** [echo CMake targets](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/apps/echo/CMakeLists.txt),
[`echoserver.cpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/apps/echo/echoserver.cpp),
[`echoclient.cpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/apps/echo/echoclient.cpp),
and [`EchoSocketContext.cpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/apps/echo/model/EchoSocketContext.cpp).

### Other preserved echo qualifications

| Variant | Qualification result | Evidence boundary |
| --- | --- | --- |
| IPv6 plain | Server/client connected on `::1` | One loopback run |
| Unix-domain plain | Server/client connected through an isolated socket path | One local run |
| IPv4 mutual TLS | Client/server connected with separate CA-signed certificates and explicit certificate/CA options | One OpenSSL/certificate arrangement; no hostname verification or broader matrix |

The same echo model builds for additional source combinations, including
conditional Bluetooth targets, but only the rows above were run. This Step 3
did not rerun them because the exact source SHA was unchanged.

## Release, package, platform, and architecture status

### Versions and public availability

| Surface | Verified fact | Safe conclusion |
| --- | --- | --- |
| Current source | Top-level CMake project version is `2.0.0`; libraries use `SOVERSION 2` | Source metadata only |
| Runtime `--version` | Current `Config.cpp` still registers the CLI version string `1.0-rc1` | Version surfaces disagree; do not use CLI output as current release truth |
| Latest GitHub release | [`v1.0.2`](https://github.com/SNodeC/snode.c/releases/tag/v1.0.2), published 28 June 2026, points to commit `6e475262084ae2dab2daef8781ab9e4adb82d18e` | Older than current master |
| Tag/source mismatch | The `v1.0.2` tag's top-level CMake version is `1.0.1` | Release naming and source metadata disagree |
| Release assets | `v1.0.2` has no release notes and no uploaded assets | GitHub-generated source archives exist; no project-uploaded binary/current package |
| Current master release | No `2.0.0` or current-head tag/release | Do not call current master “the 2.0 release” or publicly packaged |
| Local install | `cmake --install` and selected installed consumers pass | Users can build/install from source; this is not package-manager availability |
| CPack | Debian component generation is configured | No current-master generated package was published or qualified |

### Platform evidence

| Claim area | Actual evidence | Public wording boundary |
| --- | --- | --- |
| Linux/GCC CI | One successful `ubuntu-latest`/`g++` Debug build and root CTest run | One current Linux/GCC CI lane |
| Debian/x86-64 | Clean Release build/install and selected runtime qualification on Debian forky/sid, x86-64, GCC 16.2.0 | One exact environment, not a supported-distribution range |
| Clang | CMake minimum check at 13.0 | Source requirement only; no current CI/runtime proof |
| ARM/Raspberry Pi | Old README assertions and a `-Wno-psabi` source comment | No current linked build, test, artifact, device, or reproducible qualification |
| Android/Termux | Conditional warning handling and an Android netdb workaround exist | Implementation accommodations only |
| OpenWrt | A public [SNodeC/OpenWRT feed](https://github.com/SNodeC/OpenWRT) contains package definitions | Feed head is from 9 June 2026, identifies package version 1.0.1 and the older `OpenWRT` source tag, has no Actions runs, and does not qualify current master or “all architectures” |
| Other operating systems | No current CI or qualification | Open |

No evidence supports “all Linux systems,” Raspberry Pi 3/4/5, ARM32/ARM64,
OpenWrt 23.05+ on all architectures, Android/Termux support, or a general
platform matrix for current master. The OpenWrt feed is real source
availability for users who build packages, not proof of current binary package
publication or hardware/runtime coverage.

### License

The verified source license expression is
`MIT OR LGPL-3.0-or-later`. [`LICENSE`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/LICENSE)
states the choice and both full license texts are present. GitHub's API reports
`NOASSERTION` for the repository's license field; the committed SPDX
expression, not that API classifier, is the evidence.

## Canonical public routes that exist

| Purpose | Verified route | Status/boundary |
| --- | --- | --- |
| Repository | [`github.com/SNodeC/snode.c`](https://github.com/SNodeC/snode.c) | Canonical public source |
| Exact audit snapshot | [Current reviewed commit](https://github.com/SNodeC/snode.c/commit/bf01683a53b48220a840522e8ccaf3b48e58c240) | Use for claim auditing |
| Moving source/docs | [`master`](https://github.com/SNodeC/snode.c/tree/master), [examples](https://github.com/SNodeC/snode.c/tree/master/src/apps), [2.0 migration](https://github.com/SNodeC/snode.c/blob/master/docs/migration-2.0.md), [resource policies](https://github.com/SNodeC/snode.c/blob/master/docs/resource-policy-and-streaming.md) | Visitor navigation that tracks master |
| Generated API reference | [SNode.C API documentation](https://snodec.github.io/snode.c-doc/html/index.html) | Reachable, but its publishing repository head is 16 May 2026 and its landing text retains old README claims; exact alignment with the reviewed August source is unresolved |
| Support discussion | [Issues](https://github.com/SNodeC/snode.c/issues), [Discussions](https://github.com/SNodeC/snode.c/discussions) | Both repository features are enabled |
| Releases | [GitHub Releases](https://github.com/SNodeC/snode.c/releases) | Latest release is older than current master |
| Security policy | None found | Do not fabricate a private-reporting route |
| Support policy | No `SUPPORT.md` found | Issues/Discussions are routes, not a response-time or support guarantee |
| Contribution guide | No `CONTRIBUTING.md` found | Do not promise a guide that does not exist |
| Roadmap | No canonical roadmap file found | Open |

The generated API reference may be linked as an existing reference surface, but
it must not be used as the authority for current protocol, platform, version, or
support claims until its source revision and refresh process are established.

## Exact ecosystem relationships

### MQTTSuite

- Current MQTTSuite public master remained
  [`52de5631245c6318bfa5b7cca700f0754014f34d`](https://github.com/SNodeC/mqttsuite/commit/52de5631245c6318bfa5b7cca700f0754014f34d)
  on 29 August.
- Its applications request installed SNode.C 2.0 components and link SNode.C
  MQTT, HTTP/Express, WebSocket, address-family/connection, and optional
  database components.
- The 28 August qualification built all five MQTTSuite executables against the
  reviewed SNode.C install and ran one IPv4 QoS 1
  broker/subscriber/publisher path.
- Therefore MQTTSuite is a direct downstream consumer and a real MQTT-focused
  ecosystem example. Its broker, bridge, integration, CLI, storage, and
  operational features are MQTTSuite capabilities, not SNode.C capabilities.

### AISuite

- Current AISuite public master remained
  [`c3cce28d813b4f48376a2a0c6ac74131bf443f65`](https://github.com/SNodeC/AISuite/commit/c3cce28d813b4f48376a2a0c6ac74131bf443f65)
  on 29 August.
- Its CMake graph requires `snodec 2.0`, always uses SNode.C core, and uses
  installed Unix/IPv4/IPv6 plain stream components for its Codex transports;
  TLS, RFCOMM, HTTP/Express, and WebSocket frontends are conditional on the
  matching installed SNode.C targets.
- The 28 August qualification built, installed, and tested AISuite against the
  reviewed SNode.C install.
- Therefore AISuite is a direct downstream consumer for event-loop and
  transport/web-front-end infrastructure. Codex protocol typing, controller
  semantics, bridge routing, and app-server integration belong to AISuite.

### CodexUI

- CodexUI public master moved after the shared baseline to
  [`025ac6fbc5ae7c62f44f775d45290910f50e9574`](https://github.com/SNodeC/CodexUI/commit/025ac6fbc5ae7c62f44f775d45290910f50e9574).
  The two-commit delta changed UI styling/behavior documentation and a UI test,
  not dependency manifests.
- The current native CMake graph directly requires AISuite and SNode.C 2.0
  Unix/IPv4/IPv6 stream components and conditionally links SNode.C TLS,
  RFCOMM, HTTP client, and WebSocket client targets.
- The browser UI uses the AISuite browser SDK/bridge boundary; SNode.C is not a
  JavaScript/browser runtime.
- The 28 August all-master native qualification covered the earlier CodexUI SHA
  `8791923`, not the new UI-only head. The dependency relationship remains
  source-verified; a current all-head runtime qualification is not claimed.
- Therefore CodexUI is both a native direct consumer of selected SNode.C
  transports and, at ecosystem-story level, the presentation layer above
  AISuite. UI behavior belongs to CodexUI, not SNode.C.

The two honest ecosystem paths remain:

1. SNode.C → MQTTSuite.
2. SNode.C → AISuite → CodexUI.

There is no verified all-four-product runtime scenario. MQTTSuite is not part of
the AISuite/CodexUI path.

## Technically credible differentiators

These are concrete, evidence-backed distinctions, not marketing superlatives:

1. **One connection-local context model across multiple endpoint families.**
   The same server/client → connection → factory → context relationship is
   implemented across IPv4, IPv6, Unix domain, and conditional Bluetooth
   stream layers; three plain families and one IPv4 TLS path have independent
   runtime evidence.
2. **Application-protocol replacement without replacing the connection.**
   The implemented context-switch lifecycle supports HTTP-to-WebSocket upgrade
   while preserving underlying connection state.
3. **A visible separation of address, physical stream, connection mode,
   endpoint role, and application behavior.** The source and installed
   component graph make these boundaries concrete.
4. **Configuration generated from the same typed endpoint structure.** Named
   instances expose role/family/mode-specific API, file, CLI, and inspection
   surfaces with a verified precedence rule.
5. **Componentized downstream consumption.** Installed namespaced CMake targets
   and the staged-consumer test are used by real MQTTSuite, AISuite, and
   CodexUI builds at the recorded baselines.
6. **Substantial current automated coverage for the plain core/web path.**
   The exact-head public CI passes unit, component, policy, and selected
   installed-consumer tests, with explicit gaps rather than a fabricated
   universal matrix.

Do not translate these into `lightweight`, `fast`, `complete`,
`production-ready`, `secure`, `stable`, or “supports every combination.”

## Important limitations and non-goals

- The core is stream-oriented. A Unix-domain datagram component exists, but
  there is no general IPv4/IPv6 UDP endpoint layer in the reviewed source.
- Only IPv4, IPv6, and Unix-domain **plain** network component matrices are in
  the root suite. TLS network coverage is one separate mutual-TLS IPv4 echo
  qualification plus internal unit tests. Bluetooth has build but no hardware
  runtime evidence.
- HTTP is HTTP/1.0 and HTTP/1.1 only. WebSocket is version 13. MQTT is 3.1.1.
  No “full protocol support” or conformance status is established.
- The event-loop callback model does not create worker threads. Applications
  must keep loop callbacks non-blocking or explicitly manage their own
  concurrency; no throughput, latency, fairness, real-time, or footprint
  guarantee follows.
- TLS is a mechanism and configuration surface, not an automatic security
  policy. Peer and hostname verification, certificates, trust roots, cipher
  policy, key handling, and deployment review remain application/operator
  responsibilities.
- Dynamic protocol/subprotocol loading is not isolation.
- Current master is source-buildable and locally installable but not a tagged
  2.0/current-head release or published binary package.
- No current ARM, Raspberry Pi, Android/Termux, OpenWrt-current-master, broad
  distribution, or non-Linux support matrix exists.
- No forward ABI/API stability, deprecation, supported-branch, maturity, or
  release cadence policy was found.
- No benchmark corpus was found. Performance, footprint, and “lightweight”
  wording are unsupported.
- No dedicated security, support, contribution, or roadmap document was found.
- Node.js is architectural inspiration only; there is no Node.js, JavaScript,
  npm, or Express compatibility.
- MQTTSuite, AISuite, and CodexUI features must not be attributed to the
  foundation.

## Unsupported, stale, or misleading old material

| Old material or interpretation | Current conclusion |
| --- | --- |
| “very simple,” “lightweight,” or “highly extensible” | Qualitative/unmeasured. Replace with concrete programming-model and extension facts if Step 4 chooses. |
| HTTP/0.9/1.0/1.1 | **Contradicted.** Current parser accepts 1.0 and 1.1; tests reject 2.0; 0.9 is not implemented by the current parser. |
| MQTT 5 “in preparation” as a capability | **Unsupported.** A constant exists, but the server accepts only MQTT 3.1.1 protocol level 4. |
| Node.js/Express similarity as compatibility | **Misleading.** Inspiration/style only. |
| “All five network protocols can be secured by TLS” as a tested/support statement | TLS source wrappers exist broadly, but no complete family/protocol test matrix exists; HTTP wrappers do not include L2CAP. |
| Linux everywhere; Debian stable; Raspberry Pi 3/4/5; ARM32/64; OpenWrt 23.05+ all architectures; Android/Termux | Documentation/source hints without current linked build/test/runtime/release evidence. |
| Current source version `2.0.0` means released or stable | False inference. Current head is untagged; version surfaces also disagree. |
| `v1.0.2` proves version 1.0.2 artifacts | Misleading. Tag source declares 1.0.1 and release has no uploaded assets. |
| Current CLI version identifies current source | **Contradicted.** It is hard-coded to `1.0-rc1`. |
| Old `--command-line=full|default` examples | **Stale.** Current modes are `standard`, `active`, `complete`, and `required`. |
| “single-threaded/single-tasking” without operational scope | Too broad. Only the single event-loop dispatch/thread behavior is established. |
| Existing echo screenshot visibly proves payload reflection | Too broad. It visibly proves listener/transport connection; payload behavior is source-defined but not shown at default log level. |
| Existing `EVIDENCE.md` says full CTest is still pending | Superseded for this SHA by the successful exact-head public CI run. Local Step 3 did not rerun it. |
| Generated API site as current fact authority | The route exists, but its publishing head predates the reviewed source and repeats old README claims. |
| `snodec-control` source comment says it is never added by the root build | Contradicted by current `src/tools/CMakeLists.txt`, which adds it. Its separate tests remain off by default. |

## Open and unresolved facts

Step 4 must keep these as **Open facts** or omit them:

1. a maintainer-approved maturity label, release cadence, supported branch, or
   “stable” version;
2. reconciliation of CMake `2.0.0`, CLI `1.0-rc1`, and the
   `v1.0.2`/CMake-`1.0.1` release metadata;
3. forward ABI/API compatibility and deprecation guarantees beyond the
   explicit 1.x-to-2.0 rebuild boundary;
4. a supported compiler matrix beyond the source minimum checks and one
   public GCC lane;
5. supported operating systems, distributions, architectures, ARM/Raspberry Pi
   devices, Android/Termux environments, and current OpenWrt targets;
6. a published current-master binary, Debian package, official OpenWrt package,
   or other package-manager route;
7. a complete family × plain/TLS × protocol test/support matrix;
8. exact OpenSSL/TLS version policy, hostname-verification policy, certificate
   lifecycle, security audit, and production security guidance;
9. protocol-conformance claims for HTTP, WebSocket, MQTT, or SSE;
10. benchmarked throughput, latency, memory/footprint, scaling, fairness, or
    real-time behavior;
11. exact revision alignment and refresh ownership for the generated API
    reference;
12. canonical `SECURITY.md`, `SUPPORT.md`, `CONTRIBUTING.md`, code of
    conduct, and roadmap routes;
13. a current all-head compatibility rerun after CodexUI's UI-only master
    change; and
14. any stronger default-terminal echo claim than the verified listener and
    transport-connected output.

## Evidence reference index

The following links are sufficient to retrace the main conclusions:

- baseline and metadata:
  [commit](https://github.com/SNodeC/snode.c/commit/bf01683a53b48220a840522e8ccaf3b48e58c240),
  [top-level CMake](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/CMakeLists.txt),
  [source CMake/toolchain/components](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/CMakeLists.txt);
- runtime:
  [`SNodeC.h`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/SNodeC.h),
  [`EventLoop.cpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/EventLoop.cpp),
  [`EventMultiplexer.cpp`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/EventMultiplexer.cpp);
- programming model:
  [`SocketServer.h`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketServer.h),
  [`SocketClient.h`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketClient.h),
  [`SocketConnection.h`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketConnection.h),
  [`SocketContextFactory.h`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketContextFactory.h),
  [`SocketContext.h`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketContext.h);
- family and connection layers:
  [network tree](https://github.com/SNodeC/snode.c/tree/bf01683a53b48220a840522e8ccaf3b48e58c240/src/net),
  [TLS core](https://github.com/SNodeC/snode.c/tree/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/tls),
  [TLS configuration](https://github.com/SNodeC/snode.c/tree/bf01683a53b48220a840522e8ccaf3b48e58c240/src/net/config);
- application protocols:
  [HTTP parser](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/web/http/Parser.cpp),
  [Express](https://github.com/SNodeC/snode.c/tree/bf01683a53b48220a840522e8ccaf3b48e58c240/src/express),
  [WebSocket](https://github.com/SNodeC/snode.c/tree/bf01683a53b48220a840522e8ccaf3b48e58c240/src/web/websocket),
  [MQTT](https://github.com/SNodeC/snode.c/tree/bf01683a53b48220a840522e8ccaf3b48e58c240/src/iot/mqtt);
- tests and installation:
  [test tree](https://github.com/SNodeC/snode.c/tree/bf01683a53b48220a840522e8ccaf3b48e58c240/tests),
  [staged installed-consumer test](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/tests/StagedInstalledConsumerTest.cmake),
  [successful exact-head CI](https://github.com/SNodeC/snode.c/actions/runs/33189174904);
- first success:
  [echo targets](https://github.com/SNodeC/snode.c/tree/bf01683a53b48220a840522e8ccaf3b48e58c240/src/apps/echo)
  and the preserved [evidence register](../EVIDENCE.md);
- publication:
  [releases](https://github.com/SNodeC/snode.c/releases),
  [latest tag](https://github.com/SNodeC/snode.c/tree/v1.0.2),
  [OpenWrt feed](https://github.com/SNodeC/OpenWRT),
  and [license](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/LICENSE).

Handoff to Step 4
-----------------

### 1. Verified facts Step 4 may use confidently

- SNode.C is a C++20 event-driven networking framework centered on a singleton
  descriptor/timer event loop and connection-local application contexts.
- The exact current public head is `bf01683a53b48220a840522e8ccaf3b48e58c240`;
  it is unchanged from the qualified 28 August baseline.
- The recurring model is configured `SocketServer`/`SocketClient` →
  established `SocketConnection` → `SocketContextFactory` →
  per-connection `SocketContext`.
- IPv4, IPv6, and Unix-domain plain stream paths have both passing component
  tests and preserved echo runtime evidence. One mutual-TLS IPv4 echo path also
  connected.
- RFCOMM and L2CAP source/build layers exist conditionally with BlueZ, but they
  lack hardware runtime evidence.
- HTTP/1.0 and 1.1, Express-style routing/middleware, WebSocket version 13,
  EventSource/SSE, MQTT 3.1.1, and MQTT-over-WebSocket implementations exist,
  with the exact test boundaries in this file.
- API defaults, configuration files, and generated command-line sections are
  real surfaces; precedence is command line > file > API/default.
- Current exact-head public GCC/Linux CI built and passed the root-configured
  CTest suite, including selected staged installed consumers.
- License is `MIT OR LGPL-3.0-or-later`.

### 2. Strongest technically supported differentiators

- one endpoint/connection/factory/context model reused across multiple
  address-family and connection-mode implementations;
- application-context replacement on an existing connection, concretely used
  for HTTP-to-WebSocket upgrade;
- explicit separation between event runtime, address family, physical stream,
  connection mode, endpoint role, and application protocol;
- configuration and inspection generated from the typed endpoint hierarchy;
  and
- componentized installed CMake targets consumed by real downstream projects.

### 3. Programming-model concepts that deserve editorial prominence

Step 4 should make the four public concepts and the connection between them
easy to understand:

1. server/client **instance** — the configurable endpoint and flow owner;
2. **connection** — addresses, stream mechanics, queues, timeouts, and
   connection identity;
3. **factory** — selects/creates per-connection behavior; and
4. **context** — owns protocol/application callbacks and can be replaced without
   replacing the connection.

The event loop is the execution model around those concepts. If Step 4 uses
“single-threaded,” it must say callbacks run synchronously on the event-loop
thread and that blocking callbacks delay the loop.

### 4. Best currently verified first-success/echo path

Use the two-target plain IPv4 loopback build and the exact instance/section
commands recorded above. The reliable visible result is:

- listener started and listening on `127.0.0.1:18001`;
- client connected to that endpoint; and
- server and client transport-connected records.

The source-defined client sends a greeting and both contexts reflect received
bytes, but default information-level output does not print that payload. Do not
invent a visible “Hello” result. The process runs until Ctrl-C. IPv6, Unix
domain, and mutual-TLS IPv4 are verified secondary variants, not necessary
steps in the shortest first success.

### 5. Capability or architecture facts suitable for visual explanation

- configured endpoint → connection establishment → factory → active context;
- event-loop dispatch around listener/connector, descriptor/timer events, and
  context callbacks;
- address family → physical stream → plain/TLS connection mode → application
  context, with tested/source-only distinctions made visible;
- a `SocketConnection` retaining transport/address state while an HTTP context
  detaches and a WebSocket context attaches; and
- named instance configuration expanding into local/remote, connection,
  socket, and optional TLS sections.

Any visual must avoid implying a complete all-family × TLS × protocol matrix.

### 6. Important limitations and boundaries that should remain visible

- current release/package, platform/architecture, and compatibility policy are
  narrower or unresolved compared with source breadth;
- Bluetooth is source/build-only in current evidence; TLS runtime is one IPv4
  arrangement;
- HTTP is 1.0/1.1, WebSocket is version 13, MQTT is 3.1.1;
- only Unix-domain datagram exists outside the main stream model;
- no performance, footprint, real-time, production-readiness, or security
  guarantee exists;
- TLS peer/hostname verification and deployment policy are not automatic;
- Node.js/Express are inspiration/style only; and
- downstream product behavior belongs to MQTTSuite, AISuite, or CodexUI.

### 7. Claims Step 4 must not make

Do not claim:

- “lightweight,” “fast,” “secure,” “stable,” “production-ready,” “complete,”
  or “full support”;
- a released/current `2.0.0` package or ABI/API stability policy;
- HTTP/0.9, HTTP/2, MQTT 5, Node.js compatibility, or Express compatibility;
- every address family/protocol/TLS combination is supported or tested;
- broad Linux, Debian/Ubuntu, Clang, ARM, Raspberry Pi, OpenWrt,
  Android/Termux, or other-platform support;
- automatic TLS hostname verification or production certificate policy;
- a visible echoed payload in the current default terminal capture;
- current alignment of the generated API site with the reviewed head; or
- canonical support, security, contribution, or roadmap documents that do not
  exist.

### 8. Valid detail that belongs in deeper documentation

- exhaustive constructors, factory template parameters, callback signatures,
  queue/watermark semantics, retry/backoff equations, lifecycle edge cases, and
  shutdown ordering;
- every CLI/config key, logging/daemon option, and TLS OpenSSL option;
- complete CMake component names, dependency-to-package mappings, CPack rules,
  and installed-consumer link details;
- full test inventory and per-test behavior;
- HTTP parser edge cases, WebSocket frame limits, MQTT packet types, SNI maps,
  dynamic-loader mechanics, MariaDB APIs, and Unix peer credentials;
- 1.x-to-2.0 source/ABI migration instructions; and
- qualification bookkeeping and exact audit links beyond a concise provenance
  note.

### 9. Factual choices Step 4 must resolve editorially

- how much protocol breadth to surface without obscuring the programming model;
- whether the architecture explanation names all source-only Bluetooth layers
  or keeps them in a compact availability table;
- whether the API reference is linked with a freshness caveat or omitted until
  regenerated;
- whether the source version `2.0.0` is shown at all, given the unreleased and
  contradictory version surfaces;
- how to express “single event-loop thread” compactly without implying a
  performance result or forbidding application concurrency;
- whether the first-success expected result shows only the two or three most
  diagnostic connection lines; and
- how briefly to mention the two ecosystem paths while keeping SNode.C, not the
  downstream products, as the page's subject.
