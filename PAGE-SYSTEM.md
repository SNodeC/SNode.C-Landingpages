# SNode.C landing-page system

[← Workspace roadmap](README.md) · [Implementation roadmap](LAUNCH-ROADMAP.md) ·
[Fact register](FACTS.md)

**Status:** Approved planning baseline, 28 August 2026

This document is the shared source of truth for the organization profile and
four repository landing pages developed in this workspace. Product-specific
content, screenshots, and figures are specified in each presentation's
`PROPOSAL.md`. Public-facing copy belongs in the corresponding working
`README.md` only after the content plan and technical facts are approved.

The live local repositories are read-only knowledge sources. Their current
README structures and wording are not templates and do not need to be
preserved. No implementation work from this workspace may modify those live
repositories.

## Approved editorial direction

- Write for experienced developers and technical evaluators.
- Lead with outcomes, evidence, and the shortest useful evaluation path.
- Use concise, technically precise, GitHub-native Markdown.
- Never invent versions, compatibility, performance, security, platform, or
  maturity claims.
- Treat every claim from a live README as a candidate fact until it is verified
  against current public `master`/`HEAD` and supporting evidence.
- Replace the working landing-page READMEs completely after plan approval; use
  the live READMEs only as technical source material.
- Keep detailed configuration and reference material out of the landing-page
  narrative. Link to qualified documentation when it exists.
- Keep all pages useful when images fail to load.

## Shared product-page architecture

The four repository landing pages use the same nine-part system. Section names
may be adapted to the product, but their purpose and relative weight remain
consistent.

1. **Hero** — name, outcome, verified version/maturity, no more than three
   badges, primary links, and visual slot V1.
2. **What it enables** — three to five user outcomes or differentiators.
3. **Quick start** — one qualified first-success path, expected result, and
   visual slot V2.
4. **Product centerpiece** — programming model, application suite, developer
   integration, or user workflow.
5. **Capabilities and limitations** — compact verified matrix with explicit
   limits and non-goals.
6. **Architecture** — boundaries, ownership, data flow, ecosystem relationship,
   and visual slot V3.
7. **Installation and compatibility** — supported paths, exact dependencies,
   tested platforms, and version combinations.
8. **Examples, deployment, or quality evidence** — the product-specific proof
   section and visual slot V4.
9. **Documentation and project routes** — documentation, support, security,
   contribution, roadmap, and licenses.

### Content balance

Each product page targets:

- nine primary sections, with at most one additional section where clarity
  requires it;
- approximately 1,300–1,600 words of prose, excluding commands, tables, and
  captions;
- one principal quick start;
- one product-specific centerpiece;
- one capabilities/limitations table;
- one compatibility or requirements table;
- four in-page visual slots plus one social preview;
- the same compact trust and community footer structure.

Product complexity must not determine promotional weight. MQTTSuite summarizes
its five applications rather than reproducing five manuals. AISuite and CodexUI
receive sufficient workflow, integration, compatibility, and trust content to
match the depth of the more established SNode.C and MQTTSuite pages.

## Organization-profile architecture

The organization profile is a scalable navigator rather than a fixed showcase
of the current four repositories. It targets approximately 900–1,100 words and
uses this structure:

1. ecosystem hero and navigation;
2. outcome-oriented "What you can build" paths;
3. extensible project directory;
4. stable layer-based ecosystem architecture;
5. evaluation-route chooser;
6. evidence, compatibility, and trust summary;
7. community and contribution routes.

### Extensible project directory

Never describe the catalog as containing a fixed number of projects. Organize
entries under categories that can grow, initially:

- **Foundations**;
- **Protocols and integrations**;
- **Applications and interfaces**;
- **Tools and examples**, when populated.

Every project entry uses the same fields:

```text
Project name
Category · verified maturity
One-sentence outcome.
Best for: primary audience or job.
Repository · Documentation · Quick start
```

Adding a project should require one identity asset and one standard entry, not a
new layout. "Featured projects" may highlight a subset, but a complete "All
projects" directory remains available. The architecture diagram represents
stable ecosystem layers; it is not the navigation mechanism and does not encode
a permanent project count.

## Visual placement system

Every product page uses the same visual rhythm.

| Slot | Placement | Purpose | Typical format |
| --- | --- | --- | --- |
| V1 — Hero | Immediately after the headline, description, badges, and primary links | Explain the product in one glance | Full-width SVG or real UI composite |
| V2 — First success | Directly after quick-start commands and expected result | Prove the evaluation path works | Terminal or application screenshot |
| V3 — Architecture | Inside the architecture or "How it works" section | Explain components, boundaries, and data flow | Theme-aware SVG |
| V4 — Product detail | After the product-specific centerpiece or proof section | Explain the distinguishing behavior | SVG, annotated screenshot, or two-panel figure |
| Social preview | Repository metadata; not a dominant README image | Present the project consistently when shared | 1280×640 PNG |

Do not stack all visuals at the top. A page should alternate concise text,
commands or tables, and meaningful visuals so it remains scannable without
becoming a promotional microsite.

## Visual language

### Art direction

- Technical, calm, modern, and precise.
- Strong hierarchy, generous whitespace, restrained color, and real product
  evidence.
- No generic AI brains, stock network imagery, animated typing, autoplay media,
  decorative GIFs, or dense badge walls.
- No fragile multi-column HTML card grid as the only navigation mechanism.
- Native Markdown is preferred; minimal HTML is permitted for theme-aware
  images when it improves accessibility.

### Product accents

Final colors require contrast testing. Their approved semantic roles are:

- SNode.C — foundation blue;
- MQTTSuite — IoT green;
- AISuite — protocol violet;
- CodexUI — interface amber.

The neutral organization palette anchors the system. Product identity must also
use labels, icons, and shapes so color is never the only distinction.

### Diagram grammar

- Solid arrows mean runtime communication.
- Dashed arrows mean package or build dependencies.
- Containers show process, thread, authority, or trust boundaries and must be
  labeled explicitly.
- Node shapes, arrowheads, border weights, typography, spacing, and captions are
  shared across every figure.
- Diagrams must not imply that every theoretically composable combination is
  tested or supported.
- Editable sources are committed beside the exported assets.

## Asset and capture specification

### Standard dimensions

- hero and screenshot canvas: approximately 1600×900 or 1600×800;
- architecture SVG `viewBox`: approximately `0 0 1200 675`;
- wide hero SVG `viewBox`: approximately `0 0 1600 900`;
- social preview: exactly 1280×640 PNG;
- all content images: readable when rendered at GitHub content width.

SVG is preferred for diagrams. PNG is preferred for sharp UI and terminal
captures. Assets must be optimized without making interface text or terminal
output difficult to read.

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

- Capture real, qualified current-master builds; never present a mockup as shipped
  functionality.
- Use consistent scale, theme, crop, window treatment, and visual density.
- Use synthetic repositories, topics, threads, prompts, payloads, and telemetry.
- Show a meaningful successful state, not an empty interface.
- Remove usernames, home paths, hostnames, LAN addresses, tokens, credentials,
  certificates, real prompts, bookmarks, unrelated applications, and shell
  history.
- Use a generic `$` prompt when terminal chrome or identity adds no value.
- State the tested version and environment in the surrounding text or caption.
- Capture from the same exact master commits used to verify the README commands.

### Synthetic data baseline

Use a stable, clearly fictional data set where it fits the product:

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
- Every figure receives a short caption immediately below it.
- Important information is repeated in text; screenshots are never the only
  instructions or proof.
- Test SVGs and screenshots in GitHub light and dark modes.
- Use light/dark variants through a minimal `<picture>` element when one neutral
  asset cannot maintain contrast.
- Avoid text embedded at sizes that become unreadable on mobile.
- Ensure pages remain navigable with images disabled.

## Approved product visual decisions

- **SNode.C:** compact echo example; code-to-result hero; echo terminal proof;
  programming-model and layer-architecture figures.
- **MQTTSuite:** five-application hero; broker/subscriber/publisher terminal
  proof; canonical `edge-lab` integration scenario; real broker Web UI evidence.
- **AISuite:** current-master C++/TypeScript multi-client bridge hero;
  bridge/client terminal proof; authority boundaries; shared typed-generation
  flow. Do not imply npm publication or a built CodexWebUI artifact.
- **CodexUI:** real native/browser product hero; shared first-workflow proof;
  native Qt/socketpair and browser/TypeScript paths converging at AISuite;
  combined state-and-reconnect figure with platform differences labeled.
- **Organization:** brand-level hero without a fixed project count; reusable
  project identities; layer-based architecture; extensible evaluation routes.

## Approved evaluation strategy

The organization uses one `Run a demo` entry point with two honest tracks:

1. **Networking and MQTT:** SNode.C → MQTTSuite.
2. **Typed Codex client:** SNode.C → AISuite → CodexUI.

Do not force an all-four-product scenario unless a real, qualified user outcome
later justifies it.

## Facts that remain unresolved

Approval of this page system does not approve technical release claims. Before
public copy is written, the project proposals still require verified:

- versions and maturity labels;
- canonical repository and documentation URLs;
- compatibility matrices;
- supported platforms and dependencies;
- release artifacts and tested commands;
- protocol, security, performance, and parity claims;
- final logos, exact colors, screenshots, and release-candidate evidence.

## Publication boundary

Planning decisions live in this document and the five proposals. The working
landing-page READMEs contain only public-facing presentation copy after approval.
Production publication happens through reviewed changes to canonical
repositories at a later stage; this workspace must never modify the live local
repositories directly.
