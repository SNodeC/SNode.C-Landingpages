# CodexUI evidence register

[← Shared facts](../FACTS.md) · [Proposal](PROPOSAL.md)

**Baseline:** public `master` at
[`3632adc`](https://github.com/SNodeC/CodexUI/commit/3632adcf63b287aeec4bfa9da4b2f8881d526d34),
observed 28 August 2026.

## Claim ledger

| ID | Candidate public fact | State | Implementation/build evidence | Behavioral evidence required |
| --- | --- | --- | --- | --- |
| UI-01 | CodexUI is a native Qt 6 Widgets C++20 application | Runtime-qualified for build/test/install | top-level CMake, `codex-ui` target, `src/codex` | Installed first-run screenshot remains pending |
| UI-02 | The native application uses AISuite and SNode.C 2.0 | Runtime-qualified for exact heads | `find_package(AISuite)` and SNode.C component requirements; links `AISuite::OpenAICodex` | Current CodexUI built against installed current AISuite and SNode.C masters |
| UI-03 | GUI and networking work are separated by a nonblocking Unix socketpair | Runtime-qualified by test | IPC sources and `SocketPairContractTest.cpp` | Test passed in the current-master stack |
| UI-04 | Presentation state covers threads, turns, prompts, activity, plans, agents, requests, and Git changes | Runtime-qualified by native tests | presentation/model/middle-region sources and seven named CTest targets | All seven tests passed; complete visible authenticated workflow remains to be captured |
| UI-05 | The application supports controller/observer and reconnect presentation without owning Codex persistence | Source-verified; test-defined | `FrontendSession`, `ClientRuntime`, architecture contract, presentation and shell tests | Authenticated live acceptance pending |
| UI-06 | Install rules provide the executable, SVG icon, and desktop entry | Runtime-qualified for install | final CMake install rules and `resources/` files | Isolated install produced all three; desktop launcher interaction remains pending |
| UI-09 | Exactly one bridge-facing CLI transport is selected from Unix, IPv4/IPv6 stream, TLS, RFCOMM, WebSocket, or WSS instances compiled into the build | Runtime-qualified for configuration plus source/test evidence | `ClientRuntime.cpp`, generated `--help=expanded`, `--command-line=standard` checks | Unix, IPv4, IPv6, and WebSocket CLI forms parsed; TLS/WSS require certificate-qualified runtime examples |
| UI-07 | Required build dependencies include Qt 6 Widgets, Threads, libgit2, AISuite, and SNode.C 2.0 | Source-verified | CMake package lookups | Minimum versions except SNode.C are not declared |
| UI-08 | License is `LGPL-3.0-or-later OR MIT` | Source-verified | license notice and full texts | None beyond final legal wording review |

## Version and browser scope decision

Current master has no project version in CMake and no public tags. It contains
the native Qt presentation only: there is no `web/` tree, JavaScript/TypeScript
package, browser build, or browser qualification documentation. Therefore:

- `1.0` is not an approved version or maturity claim;
- browser presentation, native/browser parity, Node build/runtime behavior, and
  `CodexWebUI` naming are not eligible for current public copy;
- V1 and V2 must use genuine native-product evidence unless browser work first
  reaches master and passes a new audit.

## Test and CI evidence

Seven CTest targets cover socketpair, presentation pipeline, conversation
projection/cards, application layout, live Git changes, and shell integration.
CI builds on GCC 15.3 with Qt 6 and tests CodexUI, but it pins SNode.C
`212bd4f` and AISuite `60c81c7`. The current all-master dependency set still
needs explicit qualification.

## Quick-start qualification

Current SNode.C, AISuite, and CodexUI masters built in dependency order and
installed to one isolated prefix. CodexUI passed 7/7 tests and installed
`codex-ui`, its SVG icon, and desktop file. Its generated CLI accepted explicit
Unix, IPv4, IPv6, and WebSocket bridge endpoints; source enforces exactly one
enabled outgoing transport. A visible authenticated thread/turn workflow and
privacy-reviewed V1/V2 screenshots remain pending.

## Open or excluded claims

- Version, maturity, supported distributions/architectures, minimum Qt/libgit2
  versions, package artifacts, privacy policy, security route, and support
  policy remain open.
- Feature parity and browser claims are excluded on current master.
- Reconnect must not be described as CodexUI persistence.
- Screenshots and interactive desktop-launcher claims remain runtime-pending;
  build, tests, installation, and CLI transport configuration are qualified.
