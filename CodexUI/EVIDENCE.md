# CodexUI evidence register

[← Shared facts](../FACTS.md) · [Proposal](PROPOSAL.md)

**Baseline:** public `master` at
[`8791923`](https://github.com/SNodeC/CodexUI/commit/8791923e5475e39222ea4fc7674ca623bc02b4de),
observed 28 August 2026.

## Claim ledger

| ID | Candidate public fact | State | Implementation/build evidence | Behavioral evidence required |
| --- | --- | --- | --- | --- |
| UI-01 | CodexUI contains native Qt 6 Widgets and browser presentations | Runtime-qualified for build/test/install/artifact and visual capture | top-level CMake, `codex-ui`, `src/codex`, `web/`, and web manifest | Native 7-test build/install and 30-test web release task passed; genuine matching synthetic screenshots captured |
| UI-02 | The native application uses AISuite and SNode.C 2.0 | Runtime-qualified for exact heads | `find_package(AISuite)` and SNode.C component requirements; links `AISuite::OpenAICodex` | Current CodexUI built against installed current AISuite and SNode.C masters |
| UI-03 | GUI and networking work are separated by a nonblocking Unix socketpair | Runtime-qualified by test | IPC sources and `SocketPairContractTest.cpp` | Test passed in the current-master stack |
| UI-04 | Presentation state covers threads, turns, prompts, activity, plans, agents, requests, and Git changes | Runtime-qualified by native tests | presentation/model/middle-region sources and seven named CTest targets | All seven tests passed; selected completed synthetic activity was captured, while authenticated workflow remains unclaimed |
| UI-05 | The application supports controller/observer and reconnect presentation without owning Codex persistence | Source-verified; test-defined | `FrontendSession`, `ClientRuntime`, architecture contract, presentation and shell tests | Authenticated live acceptance pending |
| UI-06 | Install rules provide the executable, SVG icon, and desktop entry | Runtime-qualified for install | final CMake install rules and `resources/` files | Isolated install produced all three; desktop launcher interaction remains pending |
| UI-09 | Exactly one bridge-facing CLI transport is selected from Unix, IPv4/IPv6 stream, TLS, RFCOMM, WebSocket, or WSS instances compiled into the build | Runtime-qualified for configuration plus source/test evidence | `ClientRuntime.cpp`, generated `--help=expanded`, `--command-line=standard` checks | Unix, IPv4, IPv6, and WebSocket CLI forms parsed; TLS/WSS require certificate-qualified runtime examples |
| UI-07 | Required build dependencies include Qt 6 Widgets, Threads, libgit2, AISuite, and SNode.C 2.0 | Source-verified | CMake package lookups | Minimum versions except SNode.C are not declared |
| UI-08 | License is `LGPL-3.0-or-later OR MIT` | Source-verified | license notice and full texts | None beyond final legal wording review |
| UI-10 | Debian's direct development-package mapping is `qt6-base-dev`, `libgit2-dev`, and `pkgconf`; optional TLS/RFCOMM capabilities come from the installed upstream components | Source-verified; Debian package mapping verified | top-level CMake package/component lookup and conditional target links | No `libgit3-dev`, Doxygen, or IWYU dependency is present in CodexUI CMake |
| UI-11 | Native CMake and the private CodexWebUI manifest declare `1.0.0` | Source-verified | top-level `project()` and `web/package.json` | No public tag or GitHub release exists; do not equate source version with release or maturity |
| UI-12 | CodexWebUI uses the pinned AISuite TypeScript SDK and produces a relocatable static artifact | Runtime-qualified from source | `web/AISUITE_REVISION`, package lock, release scripts, Vite config, CMake web install rule | Pinned SDK 20/20 tests and web 30/30 tests passed; artifact verification found entry page and two assets |
| UI-13 | Browser behavior has explicit parity and native-only boundaries | Runtime-qualified by web suites and visual capture | web contract, presentation/normalizer/session sources, seven web test files | Equality is behavioral rather than pixel identity; browser smoke capture and matching native Xvfb capture completed |
| UI-14 | Current web lock reports four high and one moderate full-audit findings, all omitted from the production-dependency audit | Open build-tool review | Full `npm audit --json`; `npm audit --omit=dev --json` reports zero | Review/remediate build dependencies and repeat build, tests, artifact verification, and both audits before release |

## Version and browser scope decision

Current master declares native and private web source version `1.0.0`, contains
CodexWebUI, and documents its release/equality gates. No public tag or GitHub
release exists. Public copy may identify the source version and qualified
artifact, but must not call it a released or stable `1.0`. `CodexWebUI` is now
the source-verified browser name. Native-only exceptions must remain explicit.

## Test and CI evidence

Seven CTest targets cover socketpair, presentation pipeline, conversation
projection/cards, application layout, live Git changes, and shell integration.
Native CI pins SNode.C `212bd4f` and AISuite `5aeedb2`; web CI uses Node 22 and
the same AISuite SDK pin, runs SDK tests/pack, executes the web release task, and
uploads `codexui-web`. The local all-master native stack also passed.

## Quick-start qualification

Current SNode.C, AISuite, and CodexUI masters built in dependency order and
installed to one isolated prefix. CodexUI passed 7/7 tests and installed
`codex-ui`, its SVG icon, and desktop file. Its generated CLI accepted explicit
Unix, IPv4, IPv6, and WebSocket bridge endpoints; source enforces exactly one
enabled outgoing transport. Privacy-reviewed V1/V2 scenes were captured from
the real native and browser presentations against an isolated synthetic
app-server fixture; no authenticated user workflow is claimed. Separately, the exact web
SDK pin passed 20/20 tests and CodexWebUI passed 30/30 tests, its profile task,
production build, and relocatable-artifact verification.

## Open or excluded claims

- Public release/tag status, maturity, supported distributions, architectures,
  browsers, minimum Qt/libgit2 versions, privacy policy, security route, and
  support policy remain open.
- Build-tool npm audit findings must be resolved or explicitly risk-reviewed;
  the production-dependency audit currently reports zero.
- Reconnect must not be described as CodexUI persistence.
- Native and browser screenshots are complete at 1600×900 from reproducible 2×
  sources. Interactive desktop-launcher behavior remains runtime-pending;
  build, tests, installation, and CLI transport configuration are qualified.
