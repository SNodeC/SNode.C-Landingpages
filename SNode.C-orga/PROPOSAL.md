# Proposal — SNode.C Organization Profile

[← Working landing page](README.md) · [Launch roadmap](../README.md)

## Purpose

Design the public SNodeC GitHub organization overview as the ecosystem’s front
door. It must explain four technically different products as one coherent
system without making visitors learn the repository history first.

The page is a decision surface, not a manual. Its job is to help visitors choose
the correct product, see credible proof, run one useful scenario, and find the
right support or contribution route.

## Audience and visitor intent

### Primary audiences

1. C++ developers seeking an asynchronous networking framework.
2. IoT and edge engineers evaluating MQTT infrastructure.
3. AI tooling developers evaluating a typed Codex integration and UI.

### Secondary audiences

- educators and students studying event-driven systems;
- Linux and OpenWrt integrators;
- potential contributors, maintainers, and research partners;
- technical evaluators arriving from articles or launch posts.

### Questions the page must answer

- What is SNode.C as an organization and ecosystem?
- Are the MQTT and AI products genuinely related?
- Which repository is the right starting point?
- What can be tried immediately?
- Which platforms and versions are supported?
- Is the work maintained, tested, licensed, and open to contributions?

## Positioning

### Working headline

> Event-driven C++ networking—from embedded MQTT systems to typed AI clients.

### Working supporting statement

> SNode.C provides the lightweight networking foundation. MQTTSuite applies it
> to broker, bridge, translation, CLI, and storage workflows. AISuite and
> CodexUI extend the same event-driven model into typed multi-client Codex
> integrations with native and browser interfaces.

### Primary call to action

**Explore the end-to-end demo**

### Secondary calls to action

- Choose a component.
- Read the architecture overview.
- Join GitHub Discussions.
- Contribute to a good first issue.

## Page architecture

### 1. Hero

Include:

- organization wordmark or compact banner;
- headline and two-line value statement;
- three restrained navigation links: `Explore projects`, `Run the demo`, and
  `Read the docs`;
- one ecosystem architecture graphic below the text.

Do not place a dense badge wall above the value statement. Organization-level
badges should show only ecosystem-wide facts that are actually shared.

### 2. What you can build

Use three outcome-oriented cards or compact subsections:

1. **Network services in modern C++** — TCP, TLS, WebSocket, HTTP, MQTT, and
   extensible protocol stacks where verified.
2. **MQTT systems at the edge** — broker, translation, bridging, CLI, storage,
   Web UI, and constrained Linux/OpenWrt scenarios.
3. **Typed multi-client AI workflows** — Codex app-server integration through
   C++/TypeScript facades, a bridge, and native/browser clients.

Each use case needs one sentence, one proof link, and one next action.

### 3. Choose your component

Present four consistent product cards:

| Product | Visitor promise | Evidence | Action |
| --- | --- | --- | --- |
| SNode.C | Build event-driven network applications in C++ | minimal running example and CI | Start with SNode.C |
| MQTTSuite | Deploy and connect practical MQTT workflows | live scenario and Web UI | Run MQTTSuite |
| AISuite | Integrate Codex with typed asynchronous clients | generated API equality tests and bridge demo | Explore AISuite |
| CodexUI | Use Codex through native and browser clients | native/web workflow demonstration | See CodexUI |

Cards must state maturity (`stable`, `preview`, or `experimental`) based on the
release policy, never based on marketing preference.

### 4. How the ecosystem fits together

Use one SVG diagram with two visual lanes:

- **Foundation and IoT lane:** application → MQTTSuite → SNode.C → operating
  system/network;
- **AI lane:** CodexUI → AISuite bridge → Codex app-server, with SNode.C as the
  transport/event foundation.

The diagram must distinguish build-time dependencies from runtime connections.
Use solid arrows for runtime traffic and dashed arrows for package dependencies.
Provide a text description below the image for accessibility.

### 5. Quick evaluation route

The organization page should not duplicate four installation manuals. Provide:

- one recommended ecosystem demo;
- expected duration and tested platform;
- exact prerequisites;
- one command block or a clear link to the maintained demo;
- expected visible outcome;
- links to component-specific alternatives.

The route must work from a clean machine and reference released versions rather
than moving `master` branches.

### 6. Credibility and proof

Use a compact evidence grid:

- current releases and compatibility matrix;
- CI platforms and compilers;
- protocol conformance scope;
- automated and integration test evidence;
- license model;
- security reporting policy;
- documentation and changelogs.

Avoid unqualified numbers. A metric must link to its methodology and date.

### 7. Community and contribution

Route different intents explicitly:

- usage questions → Discussions;
- reproducible defects → Issues;
- security reports → private security instructions;
- planned work → roadmap/project board;
- first contribution → curated issues and contribution guide.

Include a short maintainer statement that sets response expectations without
promising service-level support.

### 8. Footer

Include only essential links: documentation, releases, security, licenses,
contributing, code of conduct, and contact. Add the independent-project notice
where Codex/OpenAI naming appears.

## Visual system

### Art direction

- Technical, calm, and precise rather than futuristic or promotional.
- Neutral organization palette with a distinct accent for each product.
- Strong typographic hierarchy and generous whitespace.
- Diagrams use the same node, arrow, border, and label system everywhere.
- All assets work in GitHub light and dark themes.

### Proposed product accents

Final colors require accessibility testing; initial semantic roles:

- SNode.C: foundation blue;
- MQTTSuite: IoT green;
- AISuite: protocol violet;
- CodexUI: interface amber.

Colors must never be the only way information is distinguished.

### Required assets

- `assets/organization-hero.svg`
- `assets/ecosystem-architecture.svg`
- `assets/product-snodec.svg`
- `assets/product-mqttsuite.svg`
- `assets/product-aisuite.svg`
- `assets/product-codexui.svg`
- `assets/social-preview.png` at 1280×640

Commit editable sources beside exported assets. Optimize SVGs and PNGs, provide
alt text, and avoid externally hosted tracking images.

## Markdown and layout rules

- Prefer native Markdown; use minimal HTML only for layouts GitHub Markdown
  cannot express accessibly.
- Keep the hero below roughly one desktop viewport before project choices begin.
- Use no more than three badges in the hero.
- Keep paragraphs short and code blocks copyable.
- Use sentence-case headings and stable relative links.
- Do not use animated typing, autoplay media, or decorative GIFs.
- Ensure the profile remains useful when images fail to load.

## Search and repository discovery

Coordinate the profile with organization metadata:

- short description aligned with the headline;
- organization avatar based on the mark, not detailed text;
- website pointing to the canonical documentation or ecosystem page;
- public contact appropriate for support routing;
- pinned repositories ordered `snode.c`, `mqttsuite`, `AISuite`, `CodexUI`, then
  a demo or documentation repository if justified.

Repository cards on the organization page and GitHub’s pinned cards should use
the same names and one-line descriptions.

## Copy requirements

Prepare and review:

- headline under 80 characters;
- supporting statement under 240 characters;
- 40–60 words for each use case;
- 30–50 words for each product card;
- one paragraph explaining architecture;
- one paragraph describing project origin and maintenance;
- one concise independent-project disclaimer.

Every use of `lightweight`, `production-ready`, `secure`, `complete`, or
`supported` requires defined evidence.

## Review scenarios

Test the draft with these visitor tasks:

1. A C++ developer must find the first SNode.C example in two clicks.
2. An IoT engineer must identify all MQTTSuite applications and MQTT scope.
3. A Codex user must understand that AISuite is the integration layer and
   CodexUI is the presentation layer.
4. A security reviewer must find the reporting policy without opening every
   repository.
5. A contributor must find an approachable task and contribution instructions.

## Implementation sequence

1. Freeze naming, maturity labels, and ecosystem statement.
2. Build the verified compatibility and proof inventory.
3. Draft information architecture without visuals.
4. Produce architecture diagram and product identity assets.
5. Write product cards and quick-evaluation route.
6. Add community, trust, and contribution sections.
7. Test links, mobile layout, dark mode, and signed-out view.
8. Review with one representative from each primary audience.
9. Copy the approved file and assets to `.github/profile/README.md`.
10. Set organization metadata and pins in the same publication window.

## Acceptance criteria

- [ ] All four products are visible without excessive scrolling.
- [ ] Product roles and relationships are unambiguous.
- [ ] Every primary audience has a clear next action.
- [ ] The quick evaluation route uses released, compatible versions.
- [ ] Claims link to current evidence.
- [ ] Architecture distinguishes runtime and build-time relationships.
- [ ] Assets are accessible, optimized, and theme-safe.
- [ ] Support, security, and contribution routes are explicit.
- [ ] No important link points to a draft-only location after publication.
- [ ] Signed-out, mobile, light-mode, and dark-mode reviews pass.

## Open decisions

- Final organization headline and one-sentence description.
- Whether the primary demo covers all four products or offers separate MQTT and
  AI tracks.
- Which documentation URL is canonical across the organization.
- Exact maturity labels for AISuite and CodexUI.
- Whether a separate ecosystem demo repository is warranted.
- Final logo, palette, and product accent choices.
