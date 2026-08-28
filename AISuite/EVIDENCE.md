# AISuite evidence register

[← Shared facts](../FACTS.md) · [Proposal](PROPOSAL.md)

**Baseline:** public `master` at
[`c3cce28`](https://github.com/SNodeC/AISuite/commit/c3cce28d813b4f48376a2a0c6ac74131bf443f65),
observed 28 August 2026.

## Claim ledger

| ID | Candidate public fact | State | Implementation/build evidence | Behavioral evidence required |
| --- | --- | --- | --- | --- |
| AI-01 | AISuite provides C++20 and TypeScript integration surfaces for the Codex app-server protocol | Runtime-qualified from source | CMake project, `src/ai/openai/codex`, installed `AISuite::OpenAICodex`, and `packages/codex-frontend` | Clean Release build, 27 C++ tests, 20 TypeScript tests, C++ install, and npm pack dry-run passed against current SNode.C master |
| AI-02 | Source version is `0.7.0` | Source-verified | top-level CMake metadata | No tag or release exists; maturity remains open |
| AI-03 | Generated C++ protocol types are tied to recorded schema/source hashes | Source-verified | `protocol/generated/ProtocolTypes.h` and `manifest.json` with schema and source SHA-256 values | Regeneration/equality procedure must be rerun before a completeness claim |
| AI-04 | Typed values retain raw JSON through `getRaw()` | Runtime-qualified by focused test | generated protocol types and `FrontendSdkTest.cpp` | Focused SDK test passed; final public consumer excerpt remains to be compiled separately |
| AI-05 | `codex-bridge` connects one provider side to multiple controller/observer frontend clients | Runtime-qualified by routing/acceptance tests | bridge/router sources, architecture contract, `BridgeRoutingTest.cpp` | Authenticated manual reference-client screenshot remains pending |
| AI-06 | `codex-bridge` and `codex-bridge-client` are installed applications | Runtime-qualified for build/install | application CMake targets and install rules | Both applications built and installed into the isolated prefix |
| AI-07 | Provider stdio/Unix/IPv4/IPv6 and frontend stream/TLS/WebSocket/WSS paths are tested | Runtime-qualified for configured matrix | `tests/codex/CMakeLists.txt` plus provider/transport acceptance sources | All 27 configured tests passed, including 9 real-app-server tests; provider TLS is not implemented |
| AI-08 | Build metadata requires SNode.C 2.0 and nlohmann/json 3.11 | Runtime-qualified for exact heads | top-level `find_package` and fallback include lookup | Current AISuite built against SNode.C `bf01683`; CI's older pin and moving heads still require maintenance |
| AI-09 | License is `MIT OR LGPL-3.0-or-later` | Source-verified | license notice and full texts | None beyond final legal wording review |
| AI-10 | OpenSSL CLI and Codex CLI are optional at configure time but gate TLS-certificate and real-app-server tests; RFCOMM depends on Bluetooth-enabled SNode.C components | Source-verified; runtime-qualified when present | top-level transport options and `tests/codex/CMakeLists.txt` program discovery | Keep build-only requirements distinct from the complete qualified test/runtime path; AISuite defines no Doxygen or IWYU target |
| AI-11 | `@snodec/codex-frontend` source declares version `1.0.0` and TypeScript `5.9.3` | Runtime-qualified from source; publication absent | package manifest/lock, exports, generated declarations, SDK and transport sources | `npm ci`, 20 tests, and package dry-run passed; npm registry lookup returned 404, so do not claim publication |
| AI-12 | `codex-bridge` can serve a prebuilt Web UI root and upgrade `/codex` WebSocket clients | Runtime-qualified for path configuration; artifact pending | bridge CMake/configuration/static routing and `CodexWebUiPathTest` | Path test passed; AISuite neither builds nor installs the CodexWebUI artifact, so genuine UI capture remains separate |

## CMake and TypeScript version decision

Current `master` contains both CMake source version `0.7.0` and the
`@snodec/codex-frontend` source-package version `1.0.0`. They version different
distribution surfaces and are not evidence of a metadata conflict. The source
package builds and its package contents qualify, but it is not present in the
public npm registry. Public copy may document repository-source use and tested
browser-facing behavior; it must not call the package published or released.

## Test and CI evidence

AISuite defines framing, frontend SDK, routing, stdio provider, stream,
WebSocket, TLS, and optional real-app-server tests. CI runs on a GCC 15.3 Debian
container and builds/tests/installs AISuite, but pins SNode.C commit `212bd4f`.
The existence of the workflow is not a claim that the current all-master stack
passes.

## Quick-start qualification

The isolated build passed 27/27 C++ tests. Provider coverage includes owned stdio
and external app-server WebSocket over Unix, IPv4, and IPv6; real app-server
acceptance passed for all applicable provider/frontend cases. Frontend coverage
includes Unix/IPv4/IPv6 stream, IPv4/IPv6 TLS, IPv4/IPv6 WebSocket, and
IPv4/IPv6 WSS. A cross-sandbox manual client connection was unsuitable for
capture because each command ran in an isolated process namespace; the public
README therefore uses the test-qualified default path and does not claim a
manual authenticated conversation capture.

Provider and frontend transports are distinct. The app-server-facing boundary
has no TLS/WSS mode. The bridge-facing frontend boundary does. Public tables
and commands must preserve that difference.

From the same checkout, `npm ci --prefix packages/codex-frontend` and
`npm test --prefix packages/codex-frontend` passed 20/20 tests with Node
24.19.0 and npm 11.16.0. The tests cover SDK behavior, generated C++/TypeScript
equality, type-checking, and browser WebSocket lifecycle parity. A package
dry-run succeeded; registry lookup for the declared package returned 404.

## Open or excluded claims

- Exact Codex app-server revision compatibility is not identified by the
  generated manifest; it records content hashes rather than a source commit.
- Authentication ownership, remote exposure policy, support, security,
  releases, and maturity remain open.
- Claims of complete compatibility with every Codex app-server revision are
  prohibited.
- V1/V4 may include source-qualified TypeScript and browser-client paths, but
  must not imply a published npm artifact or a built CodexWebUI product. V2
  still needs a genuine sanitized provider/bridge/client capture.
