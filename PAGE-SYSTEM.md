# SNode.C landing-page system

[← Workspace roadmap](README.md) · [Canonical workflow](workflow/README-WORKFLOW.md) ·
[README governance](workflow/README-GOVERNANCE.md) · [Fact register](FACTS.md)

**Status:** Shared design and capture principles for the canonical README redesign.

This document defines the common editorial, visual, capture, accessibility, and
asset principles for the SNode.C organization profile and the SNode.C,
MQTTSuite, AISuite, and CodexUI landing pages.

It is **not** a fixed README template. The canonical process is defined in
`workflow/README-WORKFLOW.md`, and presentation conflicts are resolved by
`workflow/README-GOVERNANCE.md`.

The earlier nine-section, fixed word-count, and mandatory V1–V4 system is no
longer binding. Git history preserves that planning baseline. Existing proposals,
READMEs, figures, screenshots, and social previews remain research/provenance
inputs until replaced or explicitly approved.

## Editorial direction

- Write for experienced developers and technical evaluators.
- Lead with outcomes, evidence, and the shortest useful evaluation path.
- Use concise, technically precise, GitHub-native Markdown.
- Never invent versions, compatibility, performance, security, platform, or
  maturity claims.
- Treat claims from existing READMEs as candidate facts until verified against
  current public `master`/`HEAD` and supporting evidence.
- Keep detailed configuration and reference material out of the landing-page
  narrative unless it is essential to first success.
- Link to qualified deeper documentation when it exists.
- Prefer omission over completeness.
- Keep all pages useful when images fail to load.

## Reader journey and page structure

Each project decides its actual reader journey in
`<Project>/workflow/04-README-DESIGN.md`.

Section count, prose length, tables, and visual count are design outcomes, not
compliance targets. Useful building blocks include:

- an outcome-led hero;
- a concise explanation of what the project enables;
- one qualified first-success path with expected result;
- one project-specific centerpiece;
- capabilities and limitations where useful;
- architecture or workflow explanation where it improves understanding;
- installation/requirements information needed for evaluation;
- deeper documentation, support, security, contribution, roadmap, and license
  routes where those destinations exist.

These elements do not have to become separate top-level sections or appear in a
fixed order.

## Visual inventory

Step 4 should normally propose **2–3 meaningful in-page visuals** per project.
This is a design default, not a quota. Fewer or more are acceptable when the
storyboard gives a clear reason. A social preview is separate from the in-page
visual count.

Do not add a visual merely to create symmetry across projects. Every visual must
communicate something that is materially faster or clearer than prose alone.

The four projects share a visual language but have different narrative centers:

- **SNode.C:** programming model;
- **MQTTSuite:** MQTT applications and message flows;
- **AISuite:** typed AI middleware and bridge architecture;
- **CodexUI:** real user workflow and UI;
- **Organization:** ecosystem navigation.

## Organization profile

The organization profile is a scalable navigator rather than a fixed showcase.
It should let visitors understand the ecosystem, choose the right project, and
reach an evaluation route quickly.

Never describe the catalog as containing a permanent number of projects.
Organize entries under extensible categories, initially:

- **Foundations**;
- **Protocols and integrations**;
- **Applications and interfaces**;
- **Tools and examples**, when populated.

Adding a project should not require redesigning the organization profile.
Architecture graphics must not be the only navigation mechanism.

## Visual language

### Art direction

- Technical, calm, modern, and precise.
- Strong hierarchy, generous whitespace, restrained color, and real product
  evidence.
- No generic AI brains, stock network imagery, animated typing, autoplay media,
  decorative GIFs, or dense badge walls.
- No fragile multi-column HTML card grid as the only navigation mechanism.
- Native Markdown is preferred; minimal HTML is permitted when it materially
  improves accessibility or theme behavior.

### Product accents

Current semantic roles are provisional until final design approval and contrast
validation:

- SNode.C — foundation blue;
- MQTTSuite — IoT green;
- AISuite — protocol violet;
- CodexUI — interface amber.

Color must never be the only project distinction; labels, icons, shapes, and
content hierarchy also carry meaning.

### Diagram grammar

- Solid arrows mean runtime communication.
- Dashed arrows mean package or build dependencies.
- Containers show process, thread, authority, or trust boundaries and must be
  labeled explicitly.
- Node shapes, arrowheads, border weights, typography, spacing, and captions
  should be consistent across the family.
- Diagrams must not imply that every theoretically composable combination is
  tested or supported.
- Editable sources are committed beside or under the exported asset tree.

## Asset and capture specification

### Dimensions

Use dimensions appropriate to the final composition rather than forcing every
visual into the same canvas. Practical defaults are:

- screenshots and hero composites: about 1600×900 or 1600×800;
- architecture/wide SVGs: view boxes sized for GitHub content width;
- social preview: 1280×640 PNG;
- all content images: readable at GitHub content width and on mobile.

SVG is preferred for diagrams. PNG is preferred for sharp UI and terminal
captures. Optimize assets without making interface text or terminal output hard
to read.

### Asset layout

Each presentation owns its exported assets:

```text
<presentation>/assets/<asset-name>.svg|png
<presentation>/assets/src/<editable-source>
```

Shared identity primitives may live under `shared/assets/` when introduced.
Production READMEs must not reference unpublished workspace-only paths after
publication.

### Screenshot rules

- Capture real, qualified current-master builds; never present a mockup as
  shipped functionality.
- Use consistent scale, crop, window treatment, and visual density within a
  project.
- Use synthetic repositories, topics, threads, prompts, payloads, and telemetry.
- Show a meaningful successful state, not an empty interface.
- Remove usernames, home paths, hostnames, LAN addresses, tokens, credentials,
  certificates, real prompts, bookmarks, unrelated applications, and shell
  history.
- Use a generic `$` prompt when terminal chrome or identity adds no value.
- State tested version/environment in surrounding text or provenance records.
- Capture from the same exact master commits used to verify README commands.

### Reproducible interactive capture

Interactive desktop evidence may be staged in an isolated Xvfb display.

- Start the qualified binary in a dedicated display; never capture the
  maintainer's live desktop or unrelated windows.
- Drive only deterministic, source-aligned synthetic scenarios.
- Record binary revisions, launch arguments, geometry, input steps, and fixture
  state for each final capture.
- Render at high density where practical, then downsample once to the final
  canvas.
- Preserve real application chrome and meaningful state. Composition may crop,
  label, and align qualified captures, but must not redraw controls, replace
  application content, or conceal relevant limitations.
- Overwrite the canonical approved asset after review; keep editable sources and
  capture automation under `assets/src/` rather than accumulating ambiguous
  alternates.

### Synthetic data baseline

Use a stable, clearly fictional data set where it fits:

- scenario: `edge-lab`;
- MQTT topic: `edge-lab/room-01/temperature`;
- MQTT payload: `{"value":21.7,"unit":"C"}`;
- normalized topic: `normalized/room-01/temperature`;
- code/UI workspaces and prompts: neutral names related to qualification or
  documentation, never private project data.

The MQTT and AI demonstration tracks may share visual naming, but must not imply
a runtime integration that does not exist.

## Accessibility and theme behavior

- Every meaningful image receives concise, information-bearing alt text.
- Every meaningful figure receives a short useful caption when the surrounding
  prose does not already provide that context.
- Important information is repeated in text; screenshots are never the only
  instructions or proof.
- Test SVGs and screenshots in GitHub light and dark modes.
- Use light/dark variants through minimal HTML only when one neutral asset cannot
  maintain contrast.
- Avoid embedded text sizes that become unreadable on mobile.
- Ensure pages remain navigable with images disabled.

## Product-specific visual direction

These are starting points, not mandatory asset lists:

- **SNode.C:** code-to-result/programming-model communication and real echo proof
  where useful.
- **MQTTSuite:** the five applications and a representative MQTT message flow,
  supported by real broker/CLI/UI evidence where useful.
- **AISuite:** client types converging on the bridge/app-server boundary,
  authority separation, and typed-generation flow where useful.
- **CodexUI:** real native/browser UI and a representative workflow; architecture
  should support rather than dominate the visible product story.
- **Organization:** ecosystem navigation and stable layer relationships without a
  fixed project count.

Step 4 and Step 5 decide the final visual inventory and filenames.

## Ecosystem evaluation strategy

The organization uses one `Run a demo` entry point with two honest tracks:

1. **Networking and MQTT:** SNode.C → MQTTSuite.
2. **Typed Codex client:** SNode.C → AISuite → CodexUI.

Do not force an all-four-product scenario unless a real, qualified user outcome
later justifies it.

## Facts that remain unresolved

Approval of this page system does not approve technical release claims. Before
publication, the workflow still requires verified or owner-approved:

- versions and maturity labels;
- canonical repository and documentation URLs;
- compatibility matrices;
- supported platforms and dependencies;
- release artifacts and tested commands;
- protocol, security, performance, and parity claims;
- final visual identity and freshness against the publication candidate.

## Publication boundary

Workflow decisions live in the canonical workflow artifacts. The working
landing-page READMEs contain only public-facing presentation copy after the
corresponding writing stage. Production publication happens through reviewed
changes to canonical repositories later; this workspace must never modify the
live local source repositories directly.
