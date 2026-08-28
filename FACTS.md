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
| AISuite | `master`/`HEAD` | [`b6b4635`](https://github.com/SNodeC/AISuite/commit/b6b463575b0f587fe9ed97ddd8509050d05bd4ca) | 2026-08-25 | `0.7.0` in CMake |
| CodexUI | `master`/`HEAD` | [`3632adc`](https://github.com/SNodeC/CodexUI/commit/3632adcf63b287aeec4bfa9da4b2f8881d526d34) | 2026-08-28 | No project version declared |

These SHAs identify what was reviewed. Public copy continues to follow
`master`/`HEAD`; refresh this table whenever a remote head changes.

## Version and maturity facts

| Project | Source evidence | Release evidence | Public maturity wording |
| --- | --- | --- | --- |
| SNode.C | CMake `2.0.0` | Public tags stop at `v1.0.2`; current master is not tagged | Open; do not infer stability from `2.0.0` |
| MQTTSuite | CMake `1.0.1` | Tag `v1.0.1` exists, while current master is newer | Open; distinguish source version from released tag |
| AISuite | CMake `0.7.0` | No public tags found | Pre-1.0 source version is factual; maturity label remains open |
| CodexUI | No version in CMake | No public tags found | Version and maturity both open; `1.0` is not eligible |

AISuite's development branch `web/typescript-frontend` contains
`@snodec/codex-frontend` version `1.0.0`, but that package is absent from
`master`. This is a branch-scope difference, not a version conflict within the
selected baseline.

## Cross-project compatibility

| Consumer | Declared dependency | What is proved | Gap before public compatibility wording |
| --- | --- | --- | --- |
| MQTTSuite | `find_package(snodec 2.0.0 ...)` | Current MQTTSuite master configured and built all five executables against installed current SNode.C master | Repository CI still has no equivalent application build/test job |
| AISuite | `find_package(snodec 2.0 ...)` | Current AISuite master built and installed against current SNode.C master; all 26 configured tests passed | Public release compatibility and future moving-head drift remain open |
| CodexUI | unversioned `find_package(AISuite ...)`; `find_package(snodec 2.0 ...)` | Current CodexUI master built and installed against the qualified AISuite/SNode.C prefix; all 7 tests passed | Public release compatibility, distribution range, and moving-head drift remain open |

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
| CodexUI CI | Ubuntu 24.04 host, `gcc:15.3.0-trixie`, Qt 6, Debug/Ninja, CTest | Native Linux/GCC/Qt CI shape is defined |
| MQTTSuite CI | README maintenance and release-archive workflows only | No build/test platform may be inferred from CI |

ARM, OpenWrt, Android/Termux, distribution, browser, and compiler-range claims
remain project-level open facts until qualification evidence is recorded.

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
- AISuite TypeScript and CodexUI browser presentations are not on `master`.
- CodexUI has no source version and cannot carry a `1.0` claim.
- Security, support, contribution, and roadmap destinations need owner-approved
  canonical files or links.
- Screenshots must come from the same commits that pass qualification.
