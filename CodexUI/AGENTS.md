# AGENTS.md — CodexUI landing page

These instructions supplement the root [`AGENTS.md`](../AGENTS.md) for all work
under `CodexUI/`. Follow the shared [page system](../PAGE-SYSTEM.md) and this
directory's [proposal](PROPOSAL.md).

## What it solves

CodexUI gives users a visible native Qt interface for multi-client Codex
workflows. It organizes threads, turns, prompts, tool activity, connection
state, and background work so users do not need to operate the bridge or
app-server solely through raw protocol messages or terminal-oriented tooling.

## Project focus

Focus on the real user experience. Lead with the current-master native
interface, the primary thread/turn workflow, and a credible first run. Explain
state distinctions, controller behavior, reconnect handling, and privacy only
after visitors understand what the product lets them do. Browser work remains a
future route until it reaches master.

Use architecture to support the visible product story. Do not lead with reducer,
model, socketpair, or protocol implementation terminology.

## Project boundaries

- AISuite owns the typed integration, bridge, routing, and protocol generation;
  link those details rather than presenting them as CodexUI features.
- The Codex app-server owns conversation semantics and persistence.
- CodexUI owns presentation, interaction, and local UI state only where verified.
- Browser presentation and parity claims are excluded until browser code reaches
  master and receives a new evidence audit.
- Do not present workspace checkout layout, internal review inventories, or
  developer-only assumptions as installation requirements.
- Do not imply that CodexUI is an official OpenAI application.

## Reader outcome

A qualified visitor should be able to:

1. understand the product from the first viewport without architecture knowledge;
2. see how to connect, select or create a thread, submit a prompt, and observe
   work;
3. distinguish target, active turn, running background work, and inspected state;
4. understand the native presentation's verified capabilities and limitations;
5. find exact installation, compatibility, privacy, security, and support routes.

## Audience priority

1. Codex users seeking a native Linux interface.
2. Developers evaluating multi-client Codex workflows.
3. Qt, C++, and accessibility contributors.
4. Operators and security reviewers responsible for bridge exposure.

## Terminology

- **CodexUI** — product name.
- `codex-ui` — canonical native executable.
- `CodexWebUI` — browser artifact only if this remains its verified canonical
  name.
- `codex-bridge` — AISuite service; never describe it as part of CodexUI's
  semantic backend.
- Define **thread**, **turn**, **target**, **active turn**, **running**,
  **selected/inspected**, **controller**, and **observer** before relying on
  them.
- Use **native presentation** and **browser presentation** when platform
  behavior differs.

## Source and destination

- Read-only live source: `/home/voc/projects/drafts/CodexUI/codexui`.
- Working public-copy surface: `CodexUI/README.md`.
- Project specification: `CodexUI/PROPOSAL.md`.
- Eventual destination: `SNodeC/CodexUI/README.md`.
- Candidate repository URL — verify: `https://github.com/SNodeC/CodexUI`.
- Candidate detailed sources in the live repository — verify stable public
  destinations: `docs/codex-architecture.md`, `docs/ui-behavior.md`,
  `docs/web-1.0-contract.md`, `docs/web-qualification.md`, and
  `docs/web-release.md`.

## Approved decisions

- Primary CTA: see the workflow, then install CodexUI.
- V1 is a real native-product capture using synthetic, source-aligned state.
- V2 proves the native first-run workflow.
- V3 distinguishes native Qt, socketpair, AISuite, bridge, and app-server paths.
- V4 combines state distinctions and the reconnect sequence.
- Use explicit `supported`, `limited`, `not yet`, and `not applicable` states in
  the native capability matrix.
- Carry a concise independent-project notice near the hero and in project routes.
- Use the approved nine-section map and shared word target.
- A video may be linked later but does not become a fifth launch visual slot.

## Source-code alignment and proof

Every statement about native or browser behavior, state ownership, target/turn/
running distinctions, prompt handling, tool rendering, reconnect, parity,
privacy, desktop integration, or deployment must be traced to the exact selected
CodexUI, AISuite, and SNode.C revisions. Record the relevant UI/model/protocol
implementation, package manifests, build/install rules, and behavior,
acceptance, equality, or qualification tests.

A documented contract or visible widget alone does not prove released behavior.
Verify user workflows in real qualified builds, record genuine native/browser
differences, and prove installability with release artifacts. Screenshots must
show the same source-aligned builds used for the documentation claims.

## Candidate facts — verify

The live source currently suggests the following; verify all against the chosen
release candidates, tests, qualification documents, and installed artifacts:

- Native Qt 6 Widgets application for AISuite `codex-bridge`.
- A Qt GUI thread communicating with a SNode.C client thread through bounded,
  nonblocking Unix socketpair JSONL.
- Shared normalized thread, turn, prompt, telemetry, and reconnect behavior.
- Installation of executable, desktop entry, icon, application ID, and launcher
  integration.
- Qt, Threads, libgit2, SNode.C, AISuite, Node, and browser requirements.
- Browser and Node runtime claims are not on master.
- `MIT OR LGPL-3.0-or-later` licensing.

## Commands and examples

Use these only as qualification shapes, not approved public copy:

- Reuse the isolated checkout's `cmake-build-release` directory for Release
  qualification and `cmake-build-debug` for Debug/test work while the SHA,
  compiler, generator, SNode.C/AISuite prefixes, Qt installation, and CMake
  options remain unchanged.
- Keep every dependency prefix and the CodexUI build outside all live local
  repositories. Current-master qualification covers the native Qt application
  only.

```sh
cmake -S . -B "$BUILD_DIR" -G Ninja \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_PREFIX_PATH="$AISUITE_PREFIX;$SNODEC_PREFIX"
cmake --build "$BUILD_DIR" --parallel
ctest --test-dir "$BUILD_DIR" --output-on-failure
cmake --install "$BUILD_DIR" --prefix "$INSTALL_PREFIX"
```

Public native commands must use current compatible CodexUI, AISuite, and SNode.C
master heads, record their exact tested SHAs, avoid sibling-checkout assumptions,
and test the installed first run.

Show how the native executable selects its bridge-facing transport with real
SNode.C command-line sections. Include the default Unix-domain path plus
concise IPv4, IPv6, and WebSocket alternatives, explicitly disabling the
default Unix instance and enabling exactly one alternative. TLS/WSS examples
must include the corresponding certificate prerequisites rather than implying
that encryption is automatic.

## Common misconceptions

- CodexUI is not the bridge, provider, or persistence authority.
- Selection/inspection is not necessarily the command target.
- A running background thread is not necessarily the active turn for the target.
- Native and browser sharing a protocol model does not prove complete feature or
  platform parity.
- Reconnection does not mean CodexUI independently persisted conversation
  history.
- `1.0` in source material is not an approved launch version until all release
  gates pass.
- CodexUI is independent open source, not an official OpenAI product.

## Open facts

- Qualified release version, maturity, release date, and supported branch.
- Native packages/artifacts and supported Linux distributions/architectures.
- Exact browser baseline and canonical browser artifact/product naming.
- AISuite, SNode.C, Codex schema/revision, and frontend-package compatibility.
- Row-by-row native/browser feature and limitation matrix.
- Authentication, credential, prompt/history, local-state, logging, and telemetry
  boundaries in user-facing language.
- Hosted-demo feasibility and exposure/cost constraints.
- Canonical installation, user guide, support, security, roadmap, contribution,
  and release URLs.

## Validation

- Qualify the native build from clean current-master checkouts and its installed
  artifact.
- Verify target, active, running, inspected, pending-prompt, reconnect, and
  scrolling behavior against tests and qualification documents.
- Confirm the hero and workflow captures show real matching release state and no
  private data.
- Review privacy, authentication, listener exposure, and independent-project
  wording with the relevant evidence.
- Verify exact names, V1–V4 assets, social preview, alt text, captions, and links.
