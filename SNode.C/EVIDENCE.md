# SNode.C evidence register

[← Shared facts](../FACTS.md) · [Proposal](PROPOSAL.md)

**Current publication baseline:** public `master` at
[`60f26d9`](https://github.com/SNodeC/snode.c/commit/60f26d9ae54b3e9ffde954d0ca75e53f79f31d79),
observed 30 August 2026.

The preceding recorded runtime qualification baseline was
[`bf01683`](https://github.com/SNodeC/snode.c/commit/bf01683a53b48220a840522e8ccaf3b48e58c240).
A direct compare from `bf01683` to `60f26d9` changes CI wiring, adds the
standalone `examples/echo` consumer and its tests/documentation, and adds
semantic echo logging; it does not change the transport, HTTP, WebSocket, SSE,
MQTT, configuration, or event-runtime implementation that underpins the
existing publication claims. Earlier runtime runs therefore remain historical
evidence rather than being silently promoted to current-master reruns.

## Claim ledger

| ID | Candidate public fact | State | Implementation/build evidence | Behavioral evidence required |
| --- | --- | --- | --- | --- |
| SN-01 | SNode.C is an event-driven C++20 networking framework | Runtime-qualified; current CI observed | current top-level/source CMake; `core::SNodeC`; multiplexer sources | Earlier clean Release build/install and echo runs; current `gcc-debug` passes the main 181-test suite |
| SN-02 | Source version is `2.0.0` | Source-verified | top-level CMake project metadata at `60f26d9` | Do not translate this into stable, released, or ABI-stable; latest public release is `v1.0.2` |
| SN-03 | The application model uses `SocketServer`/`SocketClient`, `SocketContextFactory`, and `SocketContext` | Runtime-qualified | public stream headers plus current [`examples/echo`](https://github.com/SNodeC/snode.c/tree/60f26d9ae54b3e9ffde954d0ca75e53f79f31d79/examples/echo) | Recorded IPv4, IPv6, Unix-domain, and mutual-TLS IPv4 connections; current external example builds as installed-package consumer |
| SN-04 | IPv4, IPv6, Unix-domain, RFCOMM, and L2CAP source layers exist | Source-verified | `src/net/in`, `in6`, `un`, `rc`, and `l2`; corresponding CMake targets | Per-family/platform support matrix remains pending; do not imply all combinations |
| SN-05 | Plain stream and TLS layers exist | Runtime-qualified for recorded echo paths | `src/core/socket/stream/legacy`, `tls`; OpenSSL is required for TLS | Earlier mutual-TLS IPv4 echo evidence is one path, not a universal TLS matrix |
| SN-06 | HTTP, WebSocket, Express-style routing, SSE/EventSource, and MQTT 3.1.1 components exist | Source-verified; current tests observed | `src/web/http`, `src/web/websocket`, `src/express`, `src/iot/mqtt`; current CTest inventory | Exact advertised matrix remains bounded by source/test evidence; no HTTP/2 or MQTT 5 claim |
| SN-07 | CMake can install component packages for downstream `find_package` use | Source-verified; current CI observed | install/export rules; staged installed consumer; current external echo `find_package` consumer | Current CI configures and builds the installed consumer; external echo runtime tests have loader-path caveat below |
| SN-08 | License is `MIT OR LGPL-3.0-or-later` | Source-verified | `LICENSE`, `LICENSE-MIT`, `LICENSE-LGPL-3.0-or-later` | None beyond legal review of final wording |
| SN-09 | The default configure requires OpenSSL, nlohmann/json, and pkg-config; BlueZ, libmagic, MariaDB, Curses, Doxygen, IWYU, and format tools are conditional | Source-verified; Debian package mapping recorded | top-level and `src` CMake files; optional modules/tooling | Package names are environment-specific; do not imply a distribution support matrix |
| SN-10 | A connection can detach one application context and attach another; HTTP-to-WebSocket upgrade uses this mechanism | Source-verified; test-defined | `SocketConnection::setSocketContext`, `DetachReason::ContextSwitch`, HTTP upgrade selection, WebSocket upgrade contexts | Public prose describes implemented lifecycle without claiming every deployment is runtime-qualified |
| SN-11 | Named endpoint instances expose role- and layer-specific configuration through API setters, configuration files, and generated CLI sections | Source-verified; runtime-observed | `ConfigInstance`, reusable sections, `utils::Config`, generated echo help/tests | API defaults → file → command-line precedence and named/anonymous boundaries remain documented |
| SN-12 | select, poll, and epoll event multiplexer implementations exist | Source-verified; test-defined | `src/core/multiplexer/{select,poll,epoll}` | Do not infer comparative performance, broad platform coverage, or current exercise of all three |
| SN-13 | Connection configuration exposes timeouts, queue bounds/watermarks, retry/backoff, and client reconnect controls | Source-verified; test-defined | `ConfigConnection`, `ConfigPhysicalSocket`, `ConfigPhysicalSocketClient`, stream writer tests | Do not translate available controls into automatic overload safety or a universal backpressure guarantee |
| SN-14 | `examples/echo` is a standalone installed-package CMake consumer using `net-in-stream-legacy` | Source-verified; current CI build-observed | [`examples/echo/CMakeLists.txt`](https://github.com/SNodeC/snode.c/blob/60f26d9ae54b3e9ffde954d0ca75e53f79f31d79/examples/echo/CMakeLists.txt), installed headers, `snodec::net-in-stream-legacy` | Four application CTests are defined; current public CI does not pass them because the staged shared-library path is unresolved at runtime |

## Current CI evidence at `60f26d9`

The observed public `gcc-debug` job on 30 August 2026:

1. configured SNode.C with tests and applications enabled;
2. built the repository successfully;
3. ran the main CTest suite: **181/181 passed**;
4. installed SNode.C to a staging prefix;
5. configured `examples/echo` against that installed prefix;
6. built `echoserver` and `echoclient` successfully;
7. ran the four external-example CTests: **0/4 passed**.

The external failures are all downstream of one runtime-loader problem. The
first test reports that `echoserver` cannot load
`libsnodec-net-in-stream.so.2`; the remaining tests then cannot start/connect to
the built binaries. This evidence establishes installed-package configuration
and build integration, but **not** successful current-master runtime verification
of the four external-example tests.

## External echo publication facts

The current standalone example resolves SNode.C with:

```cmake
find_package(snodec REQUIRED COMPONENTS net-in-stream-legacy)
```

and links `snodec::net-in-stream-legacy`. Its executable sources use installed
public `<...>` headers such as `<core/SNodeC.h>` and
`<net/in/stream/legacy/SocketServer.h>`. The concrete server/client aliases use
`net::in::stream::legacy` directly; the external walkthrough therefore no longer
needs the in-tree `NET` build macro or the quick-start-specific IWYU switch.

Current semantic application logging includes context attach/detach, the
client's initial greeting, and each reflected payload. The README may quote the
message bodies from source without claiming a captured terminal transcript.

## Recorded runtime qualification from `bf01683`

The preceding isolated Debian qualification configured, built, and installed
SNode.C with GCC 16.2.0, CMake 4.3.4, and Ninja 1.13.2. IPv4 and IPv6 loopback,
Unix-domain, and CA-signed mutual-TLS IPv4 echo pairs connected. Passing TLS used
client and server certificates signed by the same local CA; the demo's
application-specific SNI mapping was intentionally not enabled.

Those runs remain valid evidence for those exact recorded paths. They were not
rerun against `60f26d9`, so the public presentation preserves that temporal
boundary explicitly.

## Open or excluded claims

- Maturity, supported distributions, compiler range, ARM/OpenWrt/Android scope,
  ABI/API policy, and performance remain open.
- The source CMake version is `2.0.0`, while the latest public release is
  `v1.0.2`; do not call current `master` a released 2.0 package.
- `single-threaded`, `single-tasking`, `lightweight`, and universal layer
  composability need precise scope and evidence before public use.
- The current external echo CTests are source-defined and CI-wired but must not
  be described as passing until the installed-library runtime path is fixed and
  a green exact-head run is observed.

## Publication visual status

Historical Visual-2 terminal-capture entries in earlier workflow records do
**not** describe the current canonical publication package. The current package
contains no publication-final terminal evidence image and does not substitute a
synthetic, redrawn, normalized, or historical terminal capture.

Publication figure provenance is governed by the Figma handoff and the final
closure record. The canonical editable visual source is the Figma file
`giz3MDZrdwPx71L2HhiQdg`; repository SVGs are Figma-derived publication/source
counterparts.
