# Current-master capability map

[← SNode.C](../README.md) · [Architecture](architecture.md) ·
[Configuration](configuration.md)

This page answers a narrow question: what is visible in the reviewed SNode.C
source, and what did the recorded qualification exercise?

It is not a permanent support matrix. The public presentation tracks `master`,
and the evidence below remains scoped to the reviewed revision.

**Reviewed baseline:** public `master` at
[`bf01683`](https://github.com/SNodeC/snode.c/commit/bf01683a53b48220a840522e8ccaf3b48e58c240),
observed 28 August 2026.

## Evidence vocabulary

- **Source-verified** means the component and its build integration exist at the
  reviewed commit.
- **Test-defined** means the repository contains a focused automated test; it
  does not say that this documentation pass reran every test.
- **Runtime-qualified** means the named workflow was run in the recorded
  qualification environment.
- **Open** means the landing page must not turn the subject into an unqualified
  public claim.

## Runtime and connection foundation

| Capability | Source state | Landing-page runtime evidence | Boundary |
| --- | --- | --- | --- |
| C++20 event-driven runtime | Source-verified | Clean Release configure, selected build, and echo runs completed | No performance or real-time guarantee |
| select, poll, and epoll multiplexer implementations | Source-verified | The qualified build used its configured implementation; no comparative run | Availability is not a benchmark |
| Timers, descriptor events, event queue, signals | Source-verified; repository tests exist | Used indirectly by the qualified applications | No universal ordering/fairness claim |
| Stream client and server roles | Runtime-qualified for echo | Listener and connector completed on selected paths | Other protocols need their own qualification |
| Connection read/write queues and accounting | Source-verified; tests exist | Echo exercised ordinary send/read | Queue-bound and overload policy remain application concerns |
| Retry/backoff and client reconnect configuration | Source-verified; tests exist | Not part of the launch echo evidence | Exact failure sequences remain outside this claim |

## Network and connection variants

| Variant | Source state | Runtime evidence | Required environment |
| --- | --- | --- | --- |
| IPv4 plain stream | Runtime-qualified | Echo server/client on `127.0.0.1` | Standard Linux networking |
| IPv6 plain stream | Runtime-qualified | Echo server/client on `::1` | IPv6 loopback enabled |
| Unix-domain plain stream | Runtime-qualified | Echo server/client using an isolated socket path | Unix-domain sockets |
| TLS over IPv4 | Runtime-qualified for one mutual-TLS echo path | Separate CA-signed server and client certificates connected | OpenSSL and reviewed certificate material |
| Bluetooth RFCOMM | Source-verified | Runtime pending in this documentation pass | BlueZ, adapter, peer, and protocol-specific qualification |
| Bluetooth L2CAP | Source-verified | Runtime pending in this documentation pass | BlueZ, adapter, peer, and protocol-specific qualification |

The source layout makes additional compositions expressible. This table does
not promote an unrun composition merely because its types or targets exist.

## Application protocol components

| Area | What current source contains | Evidence boundary |
| --- | --- | --- |
| HTTP | Client/server contexts, request/response parsers, connection handling, transfer decoders, upgrade selection | Source-verified with repository component tests; no universal address-family matrix |
| Express-style server API | `WebApp`, routers, route matching, middleware, request/response conveniences | Source-verified; “Express-style” describes the programming approach, not Node.js API compatibility |
| WebSocket | Client/server HTTP upgrade contexts, frame receiver/transmitter, subprotocol factories, linked and loadable extension paths | Source-verified with repository tests; plugin deployment policy is application-owned |
| MQTT | MQTT 3.1.1 protocol level, client and broker framework components, session-related source, MQTT-over-WebSocket composition | Source-verified; do not say “fully compliant” without a current conformance record |
| MariaDB | Optional database integration components | Source-verified when the MariaDB development dependency is selected; database version/operations matrix remains open |
| MIME detection | Optional content-type helper using libmagic | Source-verified when libmagic is available |

MQTTSuite is the appropriate public destination for ready-made MQTTBroker,
MQTTIntegrator, MQTTBridge, MQTTCli, and MQTTStore workflows. Their application
behavior should not be attributed to SNode.C itself.

## Build and dependency surface

The reviewed Debian qualification environment used these package names for the
base source-build path:

```sh
sudo apt install --yes \
  build-essential ca-certificates cmake git ninja-build pkgconf \
  libssl-dev nlohmann-json3-dev
```

| Dependency/tool | Role | Baseline state |
| --- | --- | --- |
| C++20 compiler | Compile SNode.C | Required |
| CMake 3.18 or newer | Configure and generate builds | Required by project metadata |
| Git and CA roots | Clone and first-configure source retrieval | Required by documented source workflow |
| `pkg-config`/`pkgconf` | Dependency discovery | Required by current graph |
| OpenSSL development files | TLS source and default graph | Required for the documented build |
| nlohmann/json 3.11 or newer | JSON/configuration-related components | Required by current graph |
| CLI11 | Command/configuration parser | Vendored single header; no system package required |
| spdlog | Logging implementation | Pinned source fetched by CMake; no system package required in the documented path |
| BlueZ | RFCOMM/L2CAP layers | Optional |
| libmagic | MIME detection | Optional |
| MariaDB client development files | Database integration | Optional |
| Curses | `snodec-control` TUI | Optional |
| Doxygen and Graphviz | Generated API documentation and diagrams | Optional maintainer tools |
| IWYU | Include analysis | Optional maintainer tool |
| clang-format and cmake-format | Formatting targets | Optional maintainer tools |

## Packaging, platforms, and release status

The selected source configured, built, and installed in an isolated Debian
GNU/Linux forky/sid x86-64 environment with GCC 16.2.0, CMake 4.3.4, and Ninja
1.13.2. Installed CMake package components and a staged downstream-consumer
test are defined in the repository.

That evidence does not establish:

- a supported distribution list;
- a general GCC or Clang version range beyond project metadata and CI shapes;
- ARM, OpenWrt, Android/Termux, or other architecture support;
- ABI or API stability;
- current binary/package availability;
- performance, footprint, or production-readiness claims.

The CMake source version at the reviewed commit is `2.0.0`, while public tags
stop earlier. Use the number to identify source metadata, not as proof that a
2.0 release, compatibility promise, or maturity level exists.

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
