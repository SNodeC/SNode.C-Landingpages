# Proposal — CodexUI Repository Landing Page

[← Working landing page](README.md) · [Launch roadmap](../README.md) ·
[Shared page system](../PAGE-SYSTEM.md)

This proposal defines CodexUI-specific content and visuals within the approved
shared page system. Shared editorial, accessibility, asset, capture, and
visual-placement rules are not duplicated here.

## Current-master scope decision

The public page tracks CodexUI `master`/`HEAD`. At the 28 August 2026 evidence
baseline, master contains the native Qt application and CodexWebUI, with both
source manifests declaring `1.0.0`. Native and web qualification pass, but no
public tag or GitHub release exists and full-audit build-tool findings remain
for review; the production-dependency audit is clear. See
[`EVIDENCE.md`](EVIDENCE.md).

## Purpose

Present CodexUI as one polished product with native Qt and browser
presentations—not merely as a thread-model implementation. Show both real user
experiences, their shared behavior and honest exceptions, how they connect
through AISuite, and their release, security, and compatibility boundaries.

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
- Which native/browser workflows and limitations are qualified?
- Is this an official OpenAI application?
- What must be installed and running?
- Where are conversations and credentials stored?
- Which Codex/AISuite versions are compatible?
- Can I install a release instead of compiling the complete stack?

## Positioning

### Working headline

> Native and browser interfaces for typed, multi-client Codex workflows.

### Supporting statement

> CodexUI provides Qt 6 and browser presentations for the AISuite
> `codex-bridge`, sharing a normalized thread, turn, prompt, telemetry, and
> reconnect model while leaving semantics and persistence with the app-server.

### Primary call to action

**See the workflow, then install CodexUI**

### Secondary calls to action

- Review the native/browser capability and limitation matrix.
- Understand architecture and privacy boundaries.

## Narrative principles

- Lead with the visible product and user workflow before internal thread models.
- Use real screenshots from the qualified current-master build, not mockups presented as final.
- Explain dependencies progressively: CodexUI → AISuite bridge → Codex
  app-server.
- Separate application state, presentation state, and app-server persistence.
- Label behavioral equality, browser-specific representations, and native-only
  capabilities exactly as the current web contract defines them.
- Describe independent open-source status prominently and accurately.
- Avoid implying support for platforms that have not passed release testing.

## Page architecture

### 1. Hero

Include:

- CodexUI wordmark, stable version, and maturity;
- headline and two-line value statement;
- a real native/browser product pair using qualified matching state;
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

Every statement must reflect current-master behavior in the native build
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

### 4. Native presentation

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
- supported native platforms.

Avoid vague “parity” language. Link to the maintained 1.0 web contract.

### 5. Installation and first run

Offer paths in user-friendly order:

1. downloadable release artifacts/packages, if qualified;
2. source build using current CodexUI, AISuite, and SNode.C master heads with
   exact tested SHAs;
3. qualified static browser artifact when a release destination exists;
4. developer setup.

The quick start must specify:

- supported OS and architecture;
- Qt, libgit2, and build-tool requirements;
- exact compatible AISuite and SNode.C versions;
- bridge and Codex app-server prerequisites;
- start commands;
- expected first screen;
- shutdown and troubleshooting.

Do not expose workspace-layout assumptions such as sibling extraction directory
names in end-user installation instructions.

### 6. Architecture

Show both paths through AISuite:

```text
Qt GUI ─ bounded JSONL ─ SNode.C/AISuite client ─┐
                                                 ├─ codex-bridge
Browser UI ─ AISuite TypeScript SDK/WebSocket ───┘
      │
      ▼
Codex app-server
```

Refine the diagram so it accurately distinguishes in-process native components,
socketpair communication, bridge connections, and app-server authority.
Explain ownership in one short section and link to full architecture docs.

### 7. State and interaction model

Explain the distinctions users see:

- **Target** receives commands;
- **Active turn** identifies current work for the target;
- **Running** shows background activity;
- **Selection/inspection** controls what the user is viewing.

State that background updates should not unexpectedly change expansion,
selection, scroll position, or inspected content. Demonstrate this visually only
if the current-master behavior is fully qualified.

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
- exact current browser baseline and pinned AISuite SDK revision;
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

Highlight current contribution lanes: Qt widgets/presentation, protocol
normalization, accessibility, tests, documentation, and packaging.

## Approved final section map

The detailed requirements above consolidate into the shared nine-section
product-page system:

1. `What you can do`;
2. `First-run workflow`;
3. `Native presentation`;
4. `State and interaction model`;
5. `Connection and reconnect behavior`;
6. `Architecture`;
7. `Installation and compatibility`;
8. `Privacy, security, and quality evidence`;
9. `Documentation and project routes`.

The hero precedes these sections. Browser deployment, ecosystem relationships,
support, contribution, and license requirements become concise subsections in
the appropriate final section so CodexUI does not receive more page weight than
the other products.

## Visual requirements

The shared visual language, dimensions, screenshot hygiene, theme behavior, and
source-asset rules come from the [page system](../PAGE-SYSTEM.md).

### Visual inventory and placement

| Slot | Asset | Exact placement | Required content |
| --- | --- | --- | --- |
| V1 — Hero | `assets/codexui-hero.png` | Immediately below the hero links and independent-project notice | Real native/browser diptych with matching synthetic thread, conversation, composer, connection, and activity state; platform labels remain visible |
| V2 — First success | `assets/first-workflow.png` | Directly after the first-run workflow and expected screen | Shared connect → select/create → prompt → activity → inspect → return workflow, using the clearest qualified presentation and labeling platform-specific controls |
| V3 — Architecture | `assets/presentation-architecture.svg` | At the beginning of `Architecture` | Native Qt/socketpair/SNode.C path and browser/TypeScript/WebSocket path converging at the bridge, with process, runtime, and persistence boundaries distinguished |
| V4 — Product detail | `assets/state-and-reconnect.svg` | Between `State and interaction model` and `Connection, controller, and reconnect behavior` | Two coordinated panels: target/active/running/inspected state distinctions and connected → provider loss → visible error → reconnect → resynchronize sequence |
| Social preview | `assets/social-preview.png` | Repository metadata | Native/browser product pairing, approved outcome statement, and interface-amber accent |

### Capture specification

- Use the exact qualified current-master native and browser builds for screenshots.
- Use the same synthetic repository/thread data and matching theme.
- Capture at a consistent scale with readable text at GitHub width.
- Remove usernames, paths, tokens, real prompts, and unrelated applications.
- Show meaningful states without visual overload.
- Provide alt text and a text workflow for every important image.
- Crop browser bookmarks, extensions, personal profiles, desktop panels, and
  unrelated window chrome.
- Do not add a GIF or video as a fifth visual slot. A later qualified demo may
  be linked as an optional secondary action with captions or transcript.

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

## Use of existing documentation

Treat the live README and linked architecture and behavior documents as
read-only knowledge sources. Browser, qualification, and release documents are
current source inputs but do not prove public release. Verify selected behavior
against the recorded current-master SHA, then rewrite the landing page independently in this
workspace without preserving the live README's structure or wording.

The current page links a user-facing documentation index covering first-run
troubleshooting, native architecture and presentation protocol, UI behavior,
compatibility, qualification evidence, contributor
setup, tests, and releases. Internal review inventories stay outside the primary
visitor path. Do not modify the live local repository during this workflow.

## Evidence checklist

- Explicit `1.0.0` source-version wording separated from release and maturity.
- Tested current-master AISuite and SNode.C SHAs.
- Native clean build/install/runtime test.
- Native/browser behavior, equality, and limitation matrix.
- Connection/controller/reconnect tests.
- Interaction-state regression tests.
- Desktop file/icon/application-ID qualification.
- Accessibility, keyboard, and responsive layout review.
- License and independent-project wording review.

## Review scenarios

1. A potential user understands the product from the hero without reading code.
2. A native user finds an installable path and first-run instructions.
3. A reviewer distinguishes target, running, active, and inspected state.
4. A security reviewer understands where credentials and history live.
5. A contributor identifies whether a UI issue belongs in CodexUI or AISuite.

## Implementation sequence

1. Confirm canonical product names, source version/maturity, and compatibility matrix.
2. Qualify the native current-master build from clean checkouts.
3. Build a synthetic demonstration workspace and shot list.
4. Capture hero, workflow, state, and reconnect visuals.
5. Draft hero, outcomes, workflow, and native capability matrix.
6. Publish installation, architecture, compatibility, and deployment sections.
7. Add security, privacy, quality, support, and contribution routes.
8. Connect user guides and contributor documentation.
9. Run command, link, visual, mobile, dark-mode, and accessibility reviews.
10. Copy the approved draft/assets to the production repository only after the
    recorded master build, assets, and publication routes pass final review.

## Acceptance criteria

- [ ] The first viewport shows the real native and browser product clearly.
- [ ] A new user understands the primary workflow without architecture knowledge.
- [ ] Install paths use tested compatible master heads.
- [ ] Native/browser capabilities and limitations are explicit.
- [ ] State labels and reconnect behavior match the released application.
- [ ] Architecture and persistence ownership are accurate.
- [ ] Security, privacy, listener exposure, and independence are clear.
- [ ] Screenshots contain no sensitive or developer-specific data.
- [ ] Support and contribution routing separates UI from bridge issues.
- [ ] All commands, links, assets, and light/dark rendering pass review.
- [ ] V1–V4 and the social preview match the approved inventory and placement.
- [ ] The final section count and prose weight meet the shared product-page target.

## Open decisions

- Initial release artifact/package formats and supported Linux distributions.
- Final browser distribution route, supported-browser matrix, and dependency
  audit remediation.
- Whether a hosted demo is feasible without creating security or cost concerns.
- Final wording and placement of the independent-project notice.
