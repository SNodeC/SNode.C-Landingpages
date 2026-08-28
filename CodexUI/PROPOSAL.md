# Proposal — CodexUI Repository Landing Page

[← Working landing page](README.md) · [Launch roadmap](../README.md)

## Purpose

Present CodexUI as a polished, understandable product with native Qt and browser
interfaces—not merely as a thread-model implementation. The page must show the
actual user experience immediately, explain how it connects through AISuite,
offer a credible installation/evaluation path, and define parity, security,
compatibility, and project independence without ambiguity.

## Audience and jobs to be done

### Primary audiences

- Codex users seeking a native Linux or browser interface;
- developers evaluating a multi-client Codex workflow;
- Qt, C++, and frontend contributors.

### Secondary audiences

- teams evaluating local bridge deployment;
- AISuite and SNode.C developers;
- UX reviewers interested in thread/turn and multi-agent presentation;
- security reviewers assessing local/remote connection boundaries.

### Visitor questions

- What does CodexUI look like and what workflow does it support?
- Are native and browser versions equivalent?
- Is this an official OpenAI application?
- What must be installed and running?
- Where are conversations and credentials stored?
- Which Codex/AISuite versions are compatible?
- Can I install a release instead of compiling the complete stack?

## Positioning

### Working headline

> A native and browser interface for typed, multi-client Codex workflows.

### Supporting statement

> CodexUI provides a Qt 6 desktop application and browser presentation for the
> AISuite `codex-bridge`, sharing one normalized thread, turn, prompt, telemetry,
> and reconnect model while leaving semantics and persistence with the Codex
> app-server.

### Primary call to action

**See the workflow, then install CodexUI**

### Secondary calls to action

- Try the browser presentation.
- Read the native/web feature matrix.
- Understand architecture and privacy boundaries.

## Narrative principles

- Lead with the visible product and user workflow before internal thread models.
- Use real screenshots from the released build, not mockups presented as final.
- Explain dependencies progressively: CodexUI → AISuite bridge → Codex
  app-server.
- Separate application state, presentation state, and app-server persistence.
- State native/browser differences openly.
- Describe independent open-source status prominently and accurately.
- Avoid implying support for platforms that have not passed release testing.

## Page architecture

### 1. Hero

Include:

- CodexUI wordmark, stable version, and maturity;
- headline and two-line value statement;
- a native/browser composite screenshot using the released theme;
- release, CI, and dual-license badges only;
- links to `Install`, `See the workflow`, `Browser`, and `Compatibility`;
- an independent-project notice below, not hidden in the footer.

The screenshot is the dominant visual. It should show a real thread hierarchy,
conversation content, composer, status, and meaningful background activity using
synthetic data.

### 2. What you can do

Use five concise workflow outcomes:

- create, resume, and inspect Codex threads;
- submit prompts and steer or interrupt active work;
- distinguish target, active-turn, and background-running state;
- inspect shell/tool activity and connection/controller telemetry;
- reconnect without replacing the app-server’s persistence authority.

Every statement must reflect shipped behavior in both native and browser builds
or carry an explicit platform label.

### 3. Sixty-second workflow

Show a short annotated sequence:

1. connect to `codex-bridge`;
2. select or create a thread;
3. submit a prompt;
4. observe turn/tool activity;
5. inspect a background thread without changing the command target;
6. reconnect and retain app-server-owned history.

Support this section with a 10–20 second silent clip or optimized GIF plus a
60–90 second narrated demo linked externally. Provide captions/transcript.

### 4. Native and browser presentations

Use a feature matrix with explicit states: `supported`, `limited`, `not yet`,
and `not applicable`. Candidate rows:

- thread/turn navigation;
- prompt submission and interruption;
- multi-client controller/observer behavior;
- shell/tool rendering;
- Inspector and telemetry;
- reconnect behavior;
- local filesystem integration;
- desktop launch integration;
- keyboard shortcuts and accessibility;
- supported browsers/platforms.

Avoid vague “parity” language. Link to the maintained 1.0 web contract.

### 5. Installation and first run

Offer paths in user-friendly order:

1. downloadable release artifacts/packages, if qualified;
2. source build using tagged CodexUI, AISuite, and SNode.C releases;
3. browser build and deployment;
4. developer setup.

The quick start must specify:

- supported OS and architecture;
- Qt, libgit2, Node, and build-tool requirements where applicable;
- exact compatible AISuite and SNode.C versions;
- bridge and Codex app-server prerequisites;
- start commands;
- expected first screen;
- shutdown and troubleshooting.

Do not expose workspace-layout assumptions such as sibling extraction directory
names in end-user installation instructions.

### 6. Architecture

Show separate native and browser paths converging at AISuite:

```text
Qt GUI thread                       Browser UI
      │ bounded presentation JSONL       │ TypeScript proxy/WebSocket
      ▼                                  ▼
SNode.C client thread              codex-bridge
      └──────────────► AISuite ◄─────────┘
                          │
                          ▼
                  Codex app-server
```

Refine the diagram so it accurately distinguishes in-process native components,
socketpair communication, bridge connections, and browser WebSocket transport.
Explain ownership in one short section and link to full architecture docs.

### 7. State and interaction model

Explain the distinctions users see:

- **Target** receives commands;
- **Active turn** identifies current work for the target;
- **Running** shows background activity;
- **Selection/inspection** controls what the user is viewing.

State that background updates should not unexpectedly change expansion,
selection, scroll position, or inspected content. Demonstrate this visually only
if the released behavior is fully qualified.

### 8. Connection, controller, and reconnect behavior

Explain:

- connection states and visible errors;
- controller versus observer roles;
- what happens when the bridge or provider disappears;
- pending-prompt acknowledgement;
- reconnect and resynchronization expectations;
- which state is restored by Codex app-server versus locally remembered UI.

Link guarantees to tests or maintained behavior documentation.

### 9. Browser deployment

Describe the production artifact and same-origin bridge deployment:

- static routes and `/codex` WebSocket route;
- required subprotocol;
- supported browser baseline;
- Node as build-time only where applicable;
- bind address, TLS/reverse proxy, authentication, and exposure guidance;
- cache and asset-version behavior;
- exact AISuite revision/package relationship.

### 10. Compatibility and releases

Publish a table:

| CodexUI | AISuite | SNode.C | Codex schema/revision | Native | Browser | Status |
| --- | --- | --- | --- | --- | --- | --- |

The 1.0 claim requires native/browser release qualification, clean installation,
web asset reproducibility, acceptance tests, and release artifacts. Historical
0.x Codex UI packages must be clearly distinguished from canonical CodexUI 1.x.

### 11. Security, privacy, and trust boundaries

Explain in plain language:

- CodexUI is independent open source and not an official OpenAI product;
- where OpenAI/Codex authentication is handled;
- where prompts, responses, and thread history persist;
- what presentation state is local;
- what the bridge can observe or route;
- safe bind-address defaults and remote exposure requirements;
- logging/telemetry content and secret-handling guidance;
- private vulnerability reporting.

### 12. Performance and quality

Link release qualification evidence for:

- UI responsiveness and bounded cross-thread communication;
- model/reducer and presentation protocol tests;
- native/browser behavioral equality boundaries;
- reconnect and scrolling acceptance scenarios;
- web bundle build and size;
- accessibility and keyboard review;
- installation/desktop integration.

Use measured results only, with environment and date.

### 13. Ecosystem, support, and contribution

Explain AISuite as the typed integration/bridge and SNode.C as its networking
foundation. Link internal working presentations during drafting. Route UI bugs,
protocol/bridge issues, security reports, ideas, and usage questions to the
correct repository and template.

Highlight contribution lanes: Qt widgets/presentation, browser UI, protocol
normalization, accessibility, tests, documentation, and packaging.

## Visual requirements

### Required assets

- `assets/codexui-hero.png`
- `assets/native-workflow.png`
- `assets/browser-workflow.png`
- `assets/native-browser-architecture.svg`
- `assets/state-model.svg`
- `assets/reconnect-sequence.svg`
- `assets/demo-short.gif` or `.webm` where GitHub rendering permits
- `assets/social-preview.png`

### Capture specification

- Use exact release candidates for both native and browser screenshots.
- Use the same synthetic repository/thread data and matching theme.
- Capture at a consistent scale with readable text at GitHub width.
- Remove usernames, paths, tokens, real prompts, and unrelated applications.
- Show meaningful states without visual overload.
- Provide alt text and a text workflow for every important image.

## Copy and format rules

- Use `CodexUI` for the product, `codex-ui` for the executable, `CodexWebUI` only
  where it is the canonical browser artifact name, and `codex-bridge` for the
  AISuite service.
- Define `thread`, `turn`, `target`, `controller`, and `observer` before relying
  on them.
- Avoid internal reducer/object terminology in the first two sections.
- Use at most three hero badges and no vanity counters.
- Keep architecture code blocks secondary to the visual product story.
- All install commands must be tested from a clean environment.
- Use a clear independent-project notice without defensive or legalistic prose.

## Documentation migration and organization

Keep detailed material but give it a user-facing index:

- user guide and first-run troubleshooting;
- native architecture and presentation protocol;
- browser contract and deployment;
- UI behavior and interaction contract;
- compatibility and migration guides;
- performance/qualification evidence;
- contributor setup and test strategy;
- release process.

Move internal review inventories out of the primary visitor path while retaining
them for contributors.

## Evidence checklist

- Unified `1.0.0` version across CMake, web package, UI, docs, and release.
- Tagged compatible AISuite and SNode.C versions.
- Native clean build/install/runtime test.
- Browser clean build/reproducible artifact test.
- Native/web behavior and limitation matrix.
- Connection/controller/reconnect tests.
- Interaction-state regression tests.
- Desktop file/icon/application-ID qualification.
- Browser security/deployment review.
- Accessibility, keyboard, and responsive layout review.
- License and independent-project wording review.

## Review scenarios

1. A potential user understands the product from the hero without reading code.
2. A native user finds an installable path and first-run instructions.
3. A browser operator finds WebSocket, TLS, and exposure requirements.
4. A reviewer distinguishes target, running, active, and inspected state.
5. A security reviewer understands where credentials and history live.
6. A contributor identifies whether a UI issue belongs in CodexUI or AISuite.

## Implementation sequence

1. Freeze canonical product names, version, and compatibility matrix.
2. Qualify native and browser release candidates from clean checkouts.
3. Build a synthetic demonstration workspace and shot list.
4. Capture hero, workflow, state, and reconnect visuals.
5. Draft hero, outcomes, workflow, and native/browser matrix.
6. Publish installation, architecture, compatibility, and deployment sections.
7. Add security, privacy, quality, support, and contribution routes.
8. Connect user guides and contributor documentation.
9. Run command, link, visual, mobile, dark-mode, and accessibility reviews.
10. Copy the approved draft/assets to the production repository and release
    them together with the tagged artifacts.

## Acceptance criteria

- [ ] The first viewport shows the real native and browser product clearly.
- [ ] A new user understands the primary workflow without architecture knowledge.
- [ ] Install paths use released, compatible dependencies.
- [ ] Native/browser parity and limitations are explicit.
- [ ] State labels and reconnect behavior match the released application.
- [ ] Architecture and persistence ownership are accurate.
- [ ] Security, privacy, listener exposure, and independence are clear.
- [ ] Screenshots contain no sensitive or developer-specific data.
- [ ] Support and contribution routing separates UI from bridge issues.
- [ ] All commands, links, assets, and light/dark rendering pass review.

## Open decisions

- Whether the hero uses a composite image or native-first image plus browser tab.
- Initial release artifact/package formats and supported Linux distributions.
- Exact browser support baseline.
- Canonical names for the browser artifact and public-facing product labels.
- Which features qualify as native/browser parity at 1.0.
- Whether a hosted demo is feasible without creating security or cost concerns.
- Final wording and placement of the independent-project notice.
