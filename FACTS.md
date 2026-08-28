# SNode.C ecosystem fact register

[← Implementation roadmap](LAUNCH-ROADMAP.md)

**Audit date:** 28 August 2026

**Baseline:** current public `master` at the exact observed commit below

**Scope:** source/repository audit plus clean current-master build, install,
test, and selected quick-start qualification; visual capture remains pending

This register owns facts shared across landing pages. Project-level claim
evidence lives in each directory's `EVIDENCE.md`.

## Evidence states

- **Source-verified** — present in committed source or build metadata at the
  recorded SHA.
- **Test-defined** — an automated test exists, but this landing-page audit has
  not rerun it unless runtime evidence says otherwise.
- **CI-defined** — a workflow declares a build or test environment; this does
  not by itself assert that the latest run passed.
- **Runtime-pending** — implementation exists but the public workflow has not
  been reproduced during landing-page qualification.
- **Runtime-qualified** — the stated workflow passed in the recorded isolated
  environment at the exact baseline SHAs.
- **Not on master** — found only outside the selected public baseline.
- **Open** — no authoritative value or policy was found.

## Current source baseline

| Project | Public baseline | Observed commit | Commit date | Source version |
| --- | --- | --- | --- | --- |
| SNode.C | `master`/`HEAD` | [`bf01683`](https://github.com/SNodeC/snode.c/commit/bf01683a53b48220a840522e8ccaf3b48e58c240) | 2026-08-28 | `2.0.0` in CMake |
| MQTTSuite | `master`/`HEAD` | [`52de563`](https://github.com/SNodeC/mqttsuite/commit/52de5631245c6318bfa5b7cca700f0754014f34d) | 2026-08-28 | `1.0.1` in CMake |
| AISuite | `master`/`HEAD` | [`c3cce28`](https://github.com/SNodeC/AISuite/commit/c3cce28d813b4f48376a2a0c6ac74131bf443f65) | 2026-08-28 | `0.7.0` in CMake; TypeScript package source `1.0.0` |
| CodexUI | `master`/`HEAD` | [`8791923`](https://github.com/SNodeC/CodexUI/commit/8791923e5475e39222ea4fc7674ca623bc02b4de) | 2026-08-28 | Native CMake and private web manifest `1.0.0` |

These SHAs identify what was reviewed. Public copy continues to follow
`master`/`HEAD`; refresh this table whenever a remote head changes.

## Version and maturity facts

| Project | Source evidence | Release evidence | Public maturity wording |
| --- | --- | --- | --- |
| SNode.C | CMake `2.0.0` | Public tags stop at `v1.0.2`; current master is not tagged | Open; do not infer stability from `2.0.0` |
| MQTTSuite | CMake `1.0.1` | Tag `v1.0.1` exists, while current master is newer | Open; distinguish source version from released tag |
| AISuite | CMake `0.7.0`; TypeScript package manifest `1.0.0` | No public tags; npm registry lookup returned 404 | Independent source surfaces are factual; release and maturity labels remain open |
| CodexUI | Native CMake and private CodexWebUI manifest `1.0.0` | No public tags or GitHub release found | Source version is factual; release and maturity remain open |

AISuite master contains `@snodec/codex-frontend` version `1.0.0` beside the
CMake project version `0.7.0`. They describe different distribution surfaces,
not conflicting metadata for one artifact. Source build, tests, and package
contents qualify; public npm publication does not.

## Cross-project compatibility

| Consumer | Declared dependency | What is proved | Gap before public compatibility wording |
| --- | --- | --- | --- |
| MQTTSuite | `find_package(snodec 2.0.0 ...)` | Current MQTTSuite master configured and built all five executables against installed current SNode.C master | Repository CI still has no equivalent application build/test job |
| AISuite | `find_package(snodec 2.0 ...)` | Current AISuite master built and installed against current SNode.C master; all 27 C++ tests and 20 TypeScript tests passed | Public release compatibility, npm publication, and future moving-head drift remain open |
| CodexUI | unversioned native `find_package(AISuite ...)`; SNode.C 2.0; web pins AISuite SDK `5aeedb2` | Current native master built/installed against all-master dependencies with 7/7 tests; pinned SDK passed 20/20 and web passed 30/30 plus artifact verification | Public release compatibility, browser/distribution range, build-tool audit review, and moving-head drift remain open |

The all-current-master stack is the editorial baseline and passed one recorded
qualification build on Debian GNU/Linux forky/sid, x86-64, GCC 16.2.0, CMake
4.3.4, and Ninja 1.13.2. This proves those exact SHAs in that environment; it
does not establish a general support matrix or release compatibility policy.

## Shared platform and toolchain evidence

| Fact | Evidence | Safe interpretation |
| --- | --- | --- |
| C++ language level | All four CMake builds request C++20 | `C++20` is source-verified |
| SNode.C CI | `ubuntu-latest`, default `g++`, Debug build and CTest | One Linux/GCC CI shape is defined; exact compiler and broad platform support remain open |
| AISuite CI | Ubuntu 24.04 host, `gcc:15.3.0-trixie` container, Debug/Ninja, CTest | GCC 15.3/Linux CI shape is defined |
| CodexUI CI | Native GCC 15.3/Qt 6 CTest plus Node 22 web SDK/test/profile/build/artifact job | Native and web CI shapes are defined; passing state must still be checked at release time |
| MQTTSuite CI | README maintenance and release-archive workflows only | No build/test platform may be inferred from CI |

ARM, OpenWrt, Android/Termux, distribution, supported-browser, and compiler-range claims
remain project-level open facts until qualification evidence is recorded.

## Current-master dependency audit

The public Debian/Ubuntu commands map the logical dependencies in the selected
CMake graphs to package names available in the qualified Debian environment.
They list top-level packages; `apt` resolves their transitive package
dependencies. Other distributions require an equivalent mapping.

| Project | Required for the documented build | Optional, with scope |
| --- | --- | --- |
| SNode.C | C++20 toolchain; CMake ≥ 3.18; Ninja; Git and CA roots for clone/FetchContent; pkg-config; OpenSSL development files; nlohmann/json ≥ 3.11 | BlueZ for L2CAP/RFCOMM; libmagic for MIME detection; MariaDB client development files; Curses for the control TUI; OpenSSL CLI for certificate work; Doxygen + Graphviz, IWYU, clang-format, and cmake-format for maintainer targets |
| MQTTSuite | C++20 toolchain; CMake ≥ 3.14; Ninja; Git and recursive submodule; nlohmann/json ≥ 3.7; installed SNode.C 2.0 components including `db-mariadb`; MariaDB client development files | SNode.C Bluetooth components, libmagic MIME detection, and OpenSSL CLI for corresponding paths; Doxygen + Graphviz, IWYU, clang-format, cmake-format, js-beautify, and Prettier for maintainer targets |
| AISuite | C++20 toolchain; CMake ≥ 3.18; Ninja; Git; nlohmann/json ≥ 3.11; installed SNode.C 2.0 base components | OpenSSL CLI enables TLS test certificates; Bluetooth-enabled SNode.C enables RFCOMM; Codex CLI enables real-app-server tests/runtime; Node/npm builds/tests the optional TypeScript source package and installs its locked TypeScript 5.9.3. AISuite defines no Doxygen, IWYU, or format-tool discovery |
| CodexUI | Native: C++20, CMake ≥ 3.20, Ninja, Git, pkg-config, Qt 6 Widgets, libgit2, Threads, AISuite, and SNode.C 2.0. Web: Node ≥ 20, npm lockfiles, exact AISuite SDK pin | Bluetooth/TLS tooling applies through upstream transports; Codex CLI is behind the bridge; Node is build-time only for the static web artifact. CodexUI defines no Doxygen or IWYU discovery |

For Debian/Ubuntu, the potentially ambiguous mappings are `pkgconf` for
`pkg-config`, `libgit2-dev` for CMake's `libgit2` module, and `qt6-base-dev` for
Qt 6 Widgets and its matching base development tools. There is no
`libgit3-dev` dependency. SNode.C vendors CLI11 and fetches pinned spdlog source
through CMake, so neither is a required system development package.

## Licensing

| Project | Source-verified SPDX expression | Evidence note |
| --- | --- | --- |
| SNode.C | `MIT OR LGPL-3.0-or-later` | `LICENSE` and both full license texts are present |
| MQTTSuite | `MIT OR GPL-3.0-or-later` | SPDX line and full GPL/MIT texts agree; the prose inside `LICENSE` incorrectly says LGPL and must not be copied |
| AISuite | `MIT OR LGPL-3.0-or-later` | `LICENSE` and both full license texts are present |
| CodexUI | `LGPL-3.0-or-later OR MIT` | `LICENSE` and both full license texts are present |

## Canonical public routes

| Project | Repository | Documentation | Support | Security policy | Releases |
| --- | --- | --- | --- | --- | --- |
| SNode.C | [repository](https://github.com/SNodeC/snode.c) | [API documentation](https://snodec.github.io/snode.c-doc/html/index.html) | [Issues](https://github.com/SNodeC/snode.c/issues), [Discussions](https://github.com/SNodeC/snode.c/discussions) | Missing | [Releases](https://github.com/SNodeC/snode.c/releases) |
| MQTTSuite | [repository](https://github.com/SNodeC/mqttsuite) | [API documentation](https://snodec.github.io/mqttsuite-doc/html/index.html) | [Issues](https://github.com/SNodeC/mqttsuite/issues) | Missing | [Releases](https://github.com/SNodeC/mqttsuite/releases) |
| AISuite | [repository](https://github.com/SNodeC/AISuite) | [Architecture on master](https://github.com/SNodeC/AISuite/blob/master/src/ai/openai/codex/docs/architecture.md) | [Issues](https://github.com/SNodeC/AISuite/issues) | Missing | [Releases](https://github.com/SNodeC/AISuite/releases) |
| CodexUI | [repository](https://github.com/SNodeC/CodexUI) | [Architecture](https://github.com/SNodeC/CodexUI/blob/master/docs/codex-architecture.md), [UI behavior](https://github.com/SNodeC/CodexUI/blob/master/docs/ui-behavior.md) | [Issues](https://github.com/SNodeC/CodexUI/issues) | Missing | [Releases](https://github.com/SNodeC/CodexUI/releases) |

No project-level or organization-level `SECURITY.md`, `SUPPORT.md`, or
`CONTRIBUTING.md` was found through the public repository API on the audit date.
Do not fabricate those destinations; create and review them before the final
landing-page route block promises them.

## Shared launch gaps

- The principal SNode.C echo and MQTTSuite broker/subscriber/publisher paths are
  runtime-qualified. AISuite's full transport acceptance matrix and CodexUI's
  native tests pass; authenticated visible UI capture remains pending.
- Current-master cross-project compilation is qualified for the exact recorded
  Debian/GCC environment; release-level compatibility remains open.
- Maturity and support policies are not established by source version numbers.
- AISuite's TypeScript browser-facing SDK and CodexWebUI are on `master` and
  qualified from source. AISuite is not publicly published on npm; CodexUI has
  no public tag/release; its full audit has build-tool findings while the
  production-dependency audit reports zero.
- CodexUI source version `1.0.0` must not be presented as release or maturity.
- Security, support, contribution, and roadmap destinations need owner-approved
  canonical files or links.
- Screenshots must come from the same commits that pass qualification.
