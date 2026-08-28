# AISuite evidence register

[← Shared facts](../FACTS.md) · [Proposal](PROPOSAL.md)

**Baseline:** public `master` at
[`b6b4635`](https://github.com/SNodeC/AISuite/commit/b6b463575b0f587fe9ed97ddd8509050d05bd4ca),
observed 28 August 2026.

## Claim ledger

| ID | Candidate public fact | State | Implementation/build evidence | Behavioral evidence required |
| --- | --- | --- | --- | --- |
| AI-01 | AISuite provides a C++20 integration for the Codex app-server protocol | Runtime-qualified | CMake project, `src/ai/openai/codex`, installed `AISuite::OpenAICodex` target | Clean Release build, 26 tests, and install passed against current SNode.C master |
| AI-02 | Source version is `0.7.0` | Source-verified | top-level CMake metadata | No tag or release exists; maturity remains open |
| AI-03 | Generated C++ protocol types are tied to recorded schema/source hashes | Source-verified | `protocol/generated/ProtocolTypes.h` and `manifest.json` with schema and source SHA-256 values | Regeneration/equality procedure must be rerun before a completeness claim |
| AI-04 | Typed values retain raw JSON through `getRaw()` | Runtime-qualified by focused test | generated protocol types and `FrontendSdkTest.cpp` | Focused SDK test passed; final public consumer excerpt remains to be compiled separately |
| AI-05 | `codex-bridge` connects one provider side to multiple controller/observer frontend clients | Runtime-qualified by routing/acceptance tests | bridge/router sources, architecture contract, `BridgeRoutingTest.cpp` | Authenticated manual reference-client screenshot remains pending |
| AI-06 | `codex-bridge` and `codex-bridge-client` are installed applications | Runtime-qualified for build/install | application CMake targets and install rules | Both applications built and installed into the isolated prefix |
| AI-07 | Provider stdio/Unix/IPv4/IPv6 and frontend stream/TLS/WebSocket/WSS paths are tested | Runtime-qualified for configured matrix | `tests/codex/CMakeLists.txt` plus provider/transport acceptance sources | All 26 configured tests passed, including 9 real-app-server tests; provider TLS is not implemented |
| AI-08 | Build metadata requires SNode.C 2.0 and nlohmann/json 3.11 | Runtime-qualified for exact heads | top-level `find_package` and fallback include lookup | Current AISuite built against SNode.C `bf01683`; CI's older pin and moving heads still require maintenance |
| AI-09 | License is `MIT OR LGPL-3.0-or-later` | Source-verified | license notice and full texts | None beyond final legal wording review |

## TypeScript scope decision

Current `master` contains no `package.json`, TypeScript sources, or
`@snodec/codex-frontend` package. Version `1.0.0` occurs only on the separate
`web/typescript-frontend` development branch. Consequently:

- there is no CMake/npm version conflict inside the selected baseline;
- the public master-based landing page must not advertise a TypeScript package,
  npm installation, shared C++/TypeScript generation, or Node-free browser
  runtime yet;
- those proposal sections and figures must remain conditional until the work is
  merged to `master`, then be re-audited.

## Test and CI evidence

AISuite defines framing, frontend SDK, routing, stdio provider, stream,
WebSocket, TLS, and optional real-app-server tests. CI runs on a GCC 15.3 Debian
container and builds/tests/installs AISuite, but pins SNode.C commit `212bd4f`.
The existence of the workflow is not a claim that the current all-master stack
passes.

## Quick-start qualification

The isolated build passed 26/26 tests. Provider coverage includes owned stdio
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

## Open or excluded claims

- Exact Codex app-server revision compatibility is not identified by the
  generated manifest; it records content hashes rather than a source commit.
- Authentication ownership, remote exposure policy, support, security,
  releases, and maturity remain open.
- Claims of complete compatibility with every Codex app-server revision are
  prohibited.
- V1/V4 TypeScript content remains excluded. V2 needs a genuine sanitized
  provider/bridge/client capture even though the underlying transport tests pass.
