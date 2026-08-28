# SNode.C evidence register

[← Shared facts](../FACTS.md) · [Proposal](PROPOSAL.md)

**Baseline:** public `master` at
[`bf01683`](https://github.com/SNodeC/snode.c/commit/bf01683a53b48220a840522e8ccaf3b48e58c240),
observed 28 August 2026.

## Claim ledger

| ID | Candidate public fact | State | Implementation/build evidence | Behavioral evidence required |
| --- | --- | --- | --- | --- |
| SN-01 | SNode.C is an event-driven C++20 networking framework | Runtime-qualified | [`CMakeLists.txt`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/CMakeLists.txt), [`src/CMakeLists.txt`](https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/CMakeLists.txt), `core::SNodeC` and multiplexer sources | Clean Release build/install and echo runs completed |
| SN-02 | Source version is `2.0.0` | Source-verified | top-level CMake project metadata | Do not translate this into stable, released, or ABI-stable |
| SN-03 | The application model uses `SocketServer`/`SocketClient`, `SocketContextFactory`, and `SocketContext` | Runtime-qualified | public headers under `src/core/socket/stream` and echo model sources under `src/apps/echo/model` | Echo binaries built; IPv4, IPv6, Unix-domain, and mutual-TLS IPv4 connections ran |
| SN-04 | IPv4, IPv6, Unix-domain, RFCOMM, and L2CAP source layers exist | Source-verified | `src/net/in`, `in6`, `un`, `rc`, and `l2`; corresponding CMake targets | Per-family/platform support matrix remains pending; do not imply all combinations |
| SN-05 | Plain stream and TLS layers exist | Runtime-qualified for echo paths | `src/core/socket/stream/legacy`, `tls`; OpenSSL is required for TLS | CA-signed client/server certificates completed a mutual-TLS IPv4 echo connection; this is not a universal TLS matrix |
| SN-06 | HTTP, WebSocket, Express-style routing, and MQTT 3.1.1 components exist | Source-verified | `src/web/http`, `src/web/websocket`, `src/express`, `src/iot/mqtt`; MQTT level constant is `0x04` | Component and unit tests exist; exact advertised matrix must be derived from passing tests |
| SN-07 | CMake can install component packages for downstream `find_package` use | Source-verified; test-defined | install/export rules and `tests/StagedInstalledConsumerTest.cmake` | Rerun staged install and downstream consumer from master |
| SN-08 | License is `MIT OR LGPL-3.0-or-later` | Source-verified | `LICENSE`, `LICENSE-MIT`, `LICENSE-LGPL-3.0-or-later` | None beyond legal review of final wording |
| SN-09 | The default configure requires OpenSSL, nlohmann/json, and pkg-config; BlueZ, libmagic, MariaDB, Curses, Doxygen, IWYU, and format tools are conditional | Source-verified; Debian package mapping verified | top-level and `src` CMake files; TLS, express, MQTT, HTTP, database, network, control-tool, documentation, IWYU, and format modules | Debian package names were checked in the qualification environment; other distributions need their own mapping |

## Test and CI evidence

The repository defines unit, component, policy, staged-install, HTTP,
WebSocket, MQTT, network, TLS, and configuration tests under `tests/`. The CI
workflow builds Debug with tests and applications enabled on `ubuntu-latest`
using `g++`. This audit records those tests as present; it does not claim the
latest CI result or broader compiler/platform coverage.

## Quick-start qualification

Current master configured, built, and installed from an isolated checkout with
GCC 16.2.0, CMake 4.3.4, and Ninja 1.13.2 on Debian forky/sid. IPv4 and IPv6
loopback, Unix-domain, and CA-signed mutual-TLS IPv4 echo pairs connected.
Passing TLS used client and server certificates signed by the same local CA;
the demo's application-specific SNI mapping was intentionally not enabled.
Screenshot capture and the complete repository CTest suite remain separate
gates.

## Open or excluded claims

- Maturity, supported distributions, compiler range, ARM/OpenWrt/Android scope,
  ABI/API policy, and performance are open.
- Existing tags stop before the source `2.0.0` baseline; do not call current
  master a `2.0 release` without release evidence.
- `single-threaded`, `single-tasking`, `lightweight`, and universal layer
  composability need precise scope and evidence before public use.
- V2 can now be captured from the qualified echo commands; the image itself is
  still pending.
