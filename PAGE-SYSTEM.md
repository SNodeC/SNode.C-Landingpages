# SNode.C landing-page and figure contract

[← Workspace roadmap](README.md) · [Canonical workflow](workflow/README-WORKFLOW.md) ·
[README governance](workflow/README-GOVERNANCE.md) · [Fact register](FACTS.md)

**Status:** Repository-wide combined authority for landing-page editorial presentation,
visuals, technical figures, capture, accessibility, assets, and figure refinement.

This document completely replaces the previous contents of `PAGE-SYSTEM.md` and the
former `shared/assets/src/tikz/FIGURE-contract.md`. The former figure contract was
authoritative over the former page system in case of conflict; that precedence is
preserved here by making the stricter technical-figure rules in this document override
general visual guidance whenever both could apply.

This contract applies to the SNode.C organization profile and to SNode.C, MQTTSuite,
AISuite, CodexUI, future landing-page subprojects, and all corresponding technical
figures, screenshots, runtime evidence, hero visuals, social previews, and exported
assets.

A technical figure is compliant only when its technical semantics, composition,
typography, responsive behavior, node/container grammar, connector geometry, build
output, and actual rendered appearance all pass. Compilation alone is never
sufficient.

---

# 1. Authority and conflict resolution

Use this authority order for landing-page and visual work:

1. explicit current user instruction;
2. this combined `PAGE-SYSTEM.md` contract;
3. `shared/assets/src/tikz/landingpages-figure-system.tex` for the concrete shared
   TikZ vocabulary, constants, styles, palettes, typography, spacing, ports, canvas
   helpers, and connector definitions;
4. the canonical workflow and governance artifacts for process/presentation decisions;
5. the nearest project-specific `AGENTS.md` and accepted project workflow artifacts for
   project facts, terminology, figure-specific semantics, filenames, and placement;
6. verified current implementation source/tests/runtime evidence for technical truth;
7. older proposals, READMEs, figures, screenshots, and historical planning only as
   research/provenance inputs.

For technical-figure presentation conflicts, the strict figure rules in this document
win over broader page-level art-direction rules.

The earlier nine-section, fixed word-count, mandatory V1–V4, equal-visual-weight, and
other rigid README templates are no longer binding. Section count, prose length, table
count, and visual count are design outcomes, not compliance targets.

Existing proposals, READMEs, figures, screenshots, and social previews remain
research/provenance inputs until replaced or explicitly approved.

---

# 2. Mandatory reading before technical figure work

Before creating, reviewing, fixing, or refining any TikZ technical figure, read in
detail:

- `shared/assets/src/tikz/README.md`;
- this `PAGE-SYSTEM.md` contract;
- `shared/assets/src/tikz/landingpages-figure-system.tex`;
- the current desktop and mobile TikZ sources for the figure, where both exist;
- the figure-specific accepted contract in the relevant visual-production plan and
  accepted review register, where present;
- current implementation/source/test/runtime evidence where technical behavior is
  involved.

Do not rely on remembered style values or visual precedent instead of rereading the
current shared system.

Do not fork or restyle the shared presentation system per subproject. Project figures
may differ in semantic content and composition, but the shared presentation system is
the common style authority.

---

# 3. Hard technical-TikZ source rules

These rules are absolute.

## 3.1 Relative positioning only

Every TikZ object in a figure source must be positioned relative to another named
object, container, anchor, fit relationship, matrix relationship, or canonical shared
layout construct.

Use relative relationships such as canonical `right=... of`, `left=... of`,
`above=... of`, `below=... of`, named anchors, canonical ports, matrices, and `fit`
relationships.

Forbidden in figure sources:

- absolute `at (x,y)` placement with numeric canvas coordinates;
- arbitrary absolute coordinates;
- figure-local positioning grids based on literal coordinates;
- arbitrary `xshift` or `yshift` positioning;
- arbitrary literal coordinate offsets or manual nudges;
- positioning a group/container independently when it can be derived by `fit` or
  another relative canonical relationship.

The shared system implementation itself may internally use low-level TikZ mechanics;
that does not authorize figure-local absolute positioning.

Every ordinary box, peer box, group box, lane, trust boundary, note, label, and title
must be placed through relative geometry.

## 3.2 No arbitrary values and mandatory stop condition

Never invent an arbitrary geometry, spacing, routing, typography, styling, or visual
value in a figure source.

Use only constants, macros, styles, semantic node families, connector styles, ports,
canvas helpers, and layout tokens already defined by
`landingpages-figure-system.tex` or explicitly defined by this contract as review
criteria.

This prohibition includes invented values for:

- horizontal or vertical spacing;
- branch spacing;
- lane spacing;
- container or node padding;
- title or label spacing;
- box widths/heights and text widths;
- radii;
- line widths;
- arrowhead dimensions;
- font sizes;
- colors/fills;
- routing distances;
- dogleg offsets;
- connector attachment positions;
- safe areas;
- publication/canvas widths;
- one-off whitespace corrections.

**Mandatory hard stop:** if a required figure relationship, size, spacing, routing
shape, port distribution, or style cannot be expressed using an existing canonical
constant/style/primitive, stop the current turn immediately. Do not invent, estimate,
approximate, or silently introduce a local value or local constant. Report exactly
which shared token/style is missing, why the figure cannot be made compliant without
it, and wait for the user to decide whether the shared system should be extended.

The approximate millimetre values mentioned later for approval-space arrow rhythm are
review metrics, not permission to insert raw literal offsets into figure source. If no
shared source token produces the required rhythm, the hard-stop rule applies.

## 3.3 No figure-local styling inventions

Do not introduce figure-local colors, fonts, radii, line widths, fills, arrowheads,
shadows, padding systems, spacing systems, typography scales, or connector styles.
Use the shared canonical styles and constants.

Do not rescue an oversized composition by shrinking fonts, line widths, arrowheads,
padding, or spacing locally.

---

# 4. Editorial direction

Write for experienced developers and technical evaluators.

- Lead with outcomes, evidence, and the shortest useful evaluation path.
- Use concise, technically precise, GitHub-native Markdown.
- Never invent versions, compatibility, performance, security, platform, protocol,
  release, or maturity claims.
- Treat claims from existing READMEs as candidate facts until verified against current
  public `master`/`HEAD` and supporting evidence.
- Keep detailed configuration/reference material out of the landing-page narrative
  unless it is essential to first success.
- Link to qualified deeper documentation when it exists.
- Prefer omission over unsupported completeness.
- Keep all pages useful when images fail to load.
- State limitations and non-goals with the same precision as capabilities.

---

# 5. Reader journey and page structure

Each project decides its actual reader journey in
`<Project>/workflow/04-README-DESIGN.md`.

Useful building blocks include:

- an outcome-led hero;
- a concise explanation of what the project enables;
- one qualified first-success path with expected result;
- one project-specific centerpiece;
- capabilities and limitations where useful;
- architecture/workflow explanation where it improves understanding;
- installation/requirements information needed for evaluation;
- deeper documentation, support, security, contribution, roadmap, and license routes
  where those destinations exist.

These elements do not have to become separate top-level sections or appear in a fixed
order. Do not force projects to share identical section counts, prose lengths, table
counts, or visual counts.

---

# 6. Visual inventory and narrative centers

Step 4 should normally propose 2–3 meaningful in-page visuals per project. This is a
design default, not a quota. Fewer or more are acceptable when the storyboard gives a
clear reason. A social preview is separate from the in-page visual count.

Do not add a visual merely to create symmetry across projects. Every visual must
communicate something materially faster or more clearly than prose alone.

Current narrative centers are:

- **SNode.C:** programming model;
- **MQTTSuite:** MQTT applications and message flows;
- **AISuite:** typed AI middleware and bridge architecture;
- **CodexUI:** real user workflow and UI;
- **Organization:** ecosystem navigation.

Step 4 and Step 5 decide final visual inventory, purpose, filenames, and placement.

---

# 7. Organization profile

The organization profile is a scalable navigator rather than a fixed showcase. It
should let visitors understand the ecosystem, choose the right project, and reach an
evaluation route quickly.

Never describe the catalog as containing a permanent number of projects.

Use extensible categories, initially:

- **Foundations**;
- **Protocols and integrations**;
- **Applications and interfaces**;
- **Tools and examples**, when populated.

Adding a project must not require redesigning the organization profile. Architecture
graphics must not be the only navigation mechanism.

---

# 8. General visual language

## 8.1 Art direction

Visuals should be technical, calm, modern, and precise, with strong hierarchy,
generous intentional whitespace, restrained color, and real product evidence.

Avoid:

- generic AI brains;
- generic stock network imagery;
- animated typing;
- autoplay media;
- decorative GIFs;
- dense badge walls;
- fragile multi-column HTML card grids as the only navigation mechanism.

Prefer native Markdown. Minimal HTML is permitted only when it materially improves
accessibility, responsive behavior, or theme behavior.

## 8.2 Product accents

Current product accent directions are provisional until final design approval and
contrast validation:

- SNode.C — foundation blue;
- MQTTSuite — IoT green;
- AISuite — protocol violet;
- CodexUI — interface amber.

For canonical technical TikZ figures, semantic colors and styles from the shared system
win over decorative/product accent use. Color must never be the only project or
semantic distinction; labels, shapes, icons, content hierarchy, and connector grammar
must also carry meaning.

## 8.3 General diagram grammar and strict technical-TikZ override

For general noncanonical diagrams, the page-system convention is that solid arrows
represent runtime communication and dashed arrows represent package/build dependencies.
Containers show process, thread, authority, or trust boundaries and must be explicitly
labeled. Node shapes, arrowheads, border weights, typography, spacing, and captions
should be consistent across a family. Diagrams must not imply that every theoretically
composable combination is tested or supported.

For canonical technical TikZ figures, the stricter semantic connector vocabulary in
this contract and `landingpages-figure-system.tex` overrides that simplified rule.
Observation, dependency, handoff, association, containment, data flow, and control flow
must use their canonical styles and real semantics.

Editable sources belong beside or under the exported asset source tree.

---

# 9. Technical-figure semantic correctness

Every box, label, boundary, decision, branch, state, arrow, association, and containment
relationship must correspond to current implementation truth.

Current implementation behavior controls when an older brief, schema, prose
description, README, or prior figure disagrees.

- Schema admission alone is not proof of runtime support.
- Runtime order, configuration ownership, process ownership, optionality, parallelism,
  and causality must not be conflated.
- A note or qualification must never accidentally appear as a runtime/process step.
- Source-only and runtime-qualified evidence must remain distinguishable where that
  distinction affects interpretation.
- Each figure must also satisfy its figure-specific accepted contract and review
  register where such artifacts exist.
- A trust boundary must not imply application-provided protection unless the
  implementation actually enforces it; external deployment boundaries must be labeled
  as external requirements/recommendations.
- Ownership/containment is not directional runtime flow unless real flow also exists.

---

# 10. Technical-figure composition and responsive behavior

Use a clear reading order, balanced visual mass, intentional whitespace, deliberate
alignment, semantic grouping, and harmonious repeated geometry.

Use symmetry when semantics are symmetric. Asymmetry requires a semantic or genuine
geometric reason.

Peer elements must visually read as peers. Deliberately coordinate their top/bottom or
center alignment, dimensions, spacing, and overall visual mass as appropriate to their
semantics.

Human visual perception is a hard acceptance gate. A semantically correct figure that
looks visibly unbalanced, misaligned, cramped, detached, accidental, or inconsistent is
not complete.

Desktop and mobile are independently art-directed, never scaled copies. They must
remain semantically equivalent: branches remain branches, siblings remain siblings,
optional paths remain optional, and error paths/qualifiers do not disappear.

Inspect actual generated renders at realistic GitHub desktop/mobile widths.

---

# 11. Canvas and dimension rules

## 11.1 Canonical technical TikZ

Canonical technical TikZ figures use fixed publication canvases:

- **desktop: 160 mm**;
- **mobile: 100 mm**.

These widths are fixed publication canvases and hard composition limits, never scale
factors and never optional targets.

There is **no dynamically sized canvas mode for canonical technical TikZ figures**.

A narrower technical composition is placed on the canonical canvas by the shared
canvas helper. An oversized technical composition remains visibly oversized and fails
review. It must be recomposed; it must not receive a wider canvas and must not be
scaled down or rescued by smaller typography.

The canonical `standalone` border/canvas behavior is defined by
`landingpages-figure-system.tex`; figure sources must use the shared presets rather
than inventing their own canvas mechanics.

## 11.2 Non-TikZ visual assets

Screenshots, genuine terminal/runtime evidence, hero composites, social previews, and
other nontechnical/non-TikZ artwork are not forced onto the 160 mm/100 mm technical
canvas.

This does **not** create permission for arbitrary or casually “dynamic” dimensions.
Their dimensions/aspect ratios must come from a prescribed asset class, approved
composition, or qualified source capture.

Practical page-system defaults remain:

- screenshots and hero composites: about 1600×900 or 1600×800 where suitable;
- social preview: 1280×640 PNG;
- general/non-TikZ wide vector artwork: a view box appropriate to its approved GitHub
  composition;
- all content images: readable at GitHub content width and on mobile.

If no prescribed dimension/aspect-ratio rule exists for an asset and a new arbitrary
value would be required, do not invent one; stop and ask for the missing rule.

SVG is preferred for diagrams. PNG is preferred for sharp UI/terminal/runtime captures
and raster-only source material. Optimize assets without making interface text or
terminal output difficult to read.

---

# 12. Technical-figure typography

Use shared typography macros and canonical presets only.

Do not rescue oversized layouts with ad-hoc font shrinking.

Code identifiers, MQTT topics, prefixes, QoS values, routes, and application names use
the shared typography hierarchy consistently.

Automatic word hyphenation is forbidden in diagram labels, notes, routes, code tokens,
and technical identifiers.

Text must not touch borders, arrowheads, connectors, or neighboring boxes and must
remain readable at final GitHub width.

Do not introduce unnecessary line wrapping when the content fits harmonically on a
single line within the canonical composition.

Labels must be placed consistently. A label must never hide a connector, bend,
arrowhead, box edge, or other graphical structure.

---

# 13. Palette, nodes, containers, and rendering

Use the canonical restrained SNode.C-compatible palette and shared node styles.

Green/success styling is reserved for a real successful outcome, never generic
emphasis, a destination, a final stage, or an action.

Meaning must survive grayscale and color-vision differences; color is never the only
semantic carrier.

Use shared node families, radii, border weights, padding, and flat rendering grammar.
Do not introduce arbitrary one-off styling or decorative elevation/shadows.

`mqtt figure frame` is a neutral enclosing surface, not a semantic boundary.

Semantic containers represent real process/runtime/configuration/lifecycle/data/control/
trust boundaries and must be labeled meaningfully.

Draw the neutral frame before semantic containers and never allow an enclosing fill to
overpaint inner semantics.

Ownership/containment uses canonical containment/association styles, never a directional
flow arrow unless real directional flow also exists.

---

# 14. Connector and arrow semantics

## 14.1 Arrowheads are part of the line

Arrow direction always represents real directional semantics, never vague association.

Every directional connector is one continuous TikZ path with its arrowhead attached to
that same path through the canonical line/connector style.

**Detached, standalone, manually positioned, or separately drawn arrowheads are hard
prohibited.** An arrow must never be constructed from a line plus an independent
arrowhead object.

## 14.2 Border attachment and ports

A connector starts exactly on the source box border and terminates exactly on the
destination box border. It must not start inside, float outside, overshoot, terminate
short, or hide beneath a node.

Connectors leave and enter box borders orthogonally at 90 degrees, using the center of
the relevant border by default.

When several connectors share one border, distribute source and destination ports
evenly using canonical shared port primitives rather than stacking them at one point.
Do not invent fractional attachment positions. If the shared system cannot express the
required distribution, invoke the hard-stop rule.

## 14.3 Routing

Off-axis connectors use orthogonal/Manhattan routing. Unmotivated diagonal connectors
are forbidden.

Parallel related connectors use harmonious repeatable geometry. Avoid tiny hooks,
accidental tangencies, arbitrary doglegs, or inconsistent bend positions.

Use the canonical semantic connector styles for data/control flow, observation,
handoff, association, containment, and dependency. Do not interchange them for
decoration.

## 14.4 Absolute crossing prohibition

**Lines/connectors must under no circumstance cross through any box, node, semantic
container content, or label.**

A connector must never run underneath an opaque label as a visual patch. A label must
never cover a line, bend, arrowhead, box border, or other graphical structure.

Unrelated line crossings and ambiguous visual merges must be eliminated through
recomposition/rerouting. If a compliant route requires a missing canonical spacing or
routing primitive, stop and report the missing primitive rather than inventing a
workaround.

Branch/edge labels must be unambiguously attached to the correct segment and placed via
the canonical label spacing/styles.

---

# 15. Canonical connector rhythm

For the canonical review raster used during figure approval, an ordinary straight
process/data/control connector run has a **75 px** edge-to-edge shaft length. At the
current desktop review scale this is approximately **8.3 mm** in source geometry.

- Recurring ordinary straight arrows preserve this canonical run unless a genuine
  semantic/geometric constraint requires another shared spacing token.
- Do not shorten arrows merely to reduce figure height or width; recompose the layout.
- Desktop and mobile are independently art-directed, but final review renders preserve
  the same canonical visual arrow rhythm.
- Observation/association/dependency routes may be longer when their real destination
  requires it, but still use canonical connector grammar and deliberate spacing.

The 8.3 mm approximation is a review metric. It is not permission to write an arbitrary
`8.3mm` figure-local offset. Source positioning must use the shared system token that
encodes the intended relationship. If no suitable token exists, stop.

## 15.1 Canonical bent-arrow primary-axis span

An ordinary multi-segment bent process/data/control connector consumes the same total
primary-axis span as an ordinary straight arrow. Bending a connector must not increase
or reduce the row/column separation between source and destination.

For a normal vertically progressing `|-|` connector, the source-border-to-destination-
border height is 75 px, approximately 8.3 mm at the current approval geometry. Its two
vertical outer legs are exactly equal: 37.5 px each, approximately 4.15 mm each.

For a normal horizontally progressing `-|-` connector, the total horizontal span is
likewise 75 px / approximately 8.3 mm and the two horizontal outer legs are exactly
equal at 37.5 px / approximately 4.15 mm each.

The perpendicular middle segment may be as long as required by the real offset; it does
not change the canonical primary-axis span.

Do not add extra height/width merely because a connector bends. Recompose nodes instead.

A genuine semantic bypass such as a long observation/association/dependency route may
span multiple layout levels and is not forced into the adjacent-level 75 px span, but it
still obeys exact centered-dogleg symmetry where applicable.

## 15.2 Hard centered-dogleg symmetry

For every three-segment orthogonal connector with geometric form `|-|` or `-|-`, the
two parallel outer legs **must have exactly equal length**.

- `|-|`: vertical → horizontal → vertical; first and final vertical legs are exactly
  equal, so the horizontal segment is centered between endpoint levels.
- `-|-`: horizontal → vertical → horizontal; first and final horizontal legs are
  exactly equal, so the vertical segment is centered between endpoint columns.

For ordinary adjacent-level connectors this exact symmetry rule and the 75 px primary-
axis-span rule apply together.

This is an exact geometry requirement, not an approximate aesthetic preference. An
off-center three-segment dogleg fails the contract even when technically connected and
otherwise readable.

---

# 16. Spacing and family consistency

Use shared spacing/rhythm tokens for every recurring layout relationship. One-off
spacing values are prohibited by the no-arbitrary-values rule.

For the 24-figure MQTTSuite technical family, all figures must read as one family in:

- typography;
- node grammar;
- border hierarchy;
- radii;
- connector weights;
- arrowheads;
- semantic colors;
- notes;
- titles;
- spacing rhythm;
- label placement;
- responsive behavior.

MQTTSuite may use its own semantic vocabulary while presentation follows the shared
canonical system.

The same principle applies to technical-figure families in SNode.C, AISuite, CodexUI,
and future projects: semantic content may differ; presentation fundamentals do not.

---

# 17. Mandatory technical-figure refinement loop

Every technical-figure refinement uses the following loop. The loop is mandatory even
when the starting figure already looks close to correct.

## LOOP START

### 17.1 Read authority and truth

Read the shared TikZ README, this contract, `landingpages-figure-system.tex`, the
current figure sources, the figure-specific accepted contract, and relevant current
implementation evidence.

### 17.2 Build the current figure before editing

Run the canonical CMake figure build for the current source. Do not assess only an old
committed SVG when source/system files may have changed.

### 17.3 Render and inspect PNG review images

Generate actual PNG review renders from the generated technical output and inspect them.

For responsive figures inspect both:

- desktop PNG;
- mobile PNG.

Inspect at realistic GitHub display widths.

**Reviewing only TikZ code, PDF, SVG/XML, dimensions, or compile success is never
sufficient. Rendered PNG inspection is a hard requirement.**

### 17.4 Deep review

Review every applicable rule, including:

- semantic correctness and current implementation truth;
- source-only versus runtime-qualified evidence;
- reading order;
- visual balance and visual mass;
- symmetry/asymmetry justification;
- peer alignment;
- intentional whitespace;
- fixed canvas width;
- typography and readability;
- unnecessary line wrapping;
- clipping;
- canonical node/container styles;
- frame/container layering;
- color semantics;
- relative positioning only;
- absence of arbitrary source values;
- connector semantics;
- arrowheads attached to their paths;
- exact border attachment;
- 90-degree entry/exit;
- port distribution;
- Manhattan routing;
- straight-arrow rhythm;
- centered-dogleg symmetry;
- line/box crossings;
- line/label crossings;
- labels hiding graphic structure;
- consistent label placement;
- desktop/mobile semantic equivalence;
- actual human visual quality.

### 17.5 If NOT satisfied

Before editing, list **all currently identified findings in the chat**, including the
violated contract rule and whether each defect is semantic, geometric, stylistic,
responsive, or perceptual.

Then refine the canonical source, rebuild, render fresh PNGs, inspect again, and return
to **LOOP START**.

Do not merely report the next failure and stop. Do not stop because compilation passes.
Do not freeze after one refinement round while visible defects remain.

### 17.6 If satisfied

Before stopping, report every applicable style-guide/contract category and its status.
For every category state the concrete evidence for compliance or why it is genuinely not
applicable.

The final satisfaction report must explicitly include rendered desktop/mobile PNG
inspection and explain why the figure is visually harmonious, readable, balanced, and
free from further required refinement.

Only then stop.

## LOOP END

The loop continues until every applicable rule passes.

After all figures in a requested family pass individually, perform the required clean
whole-family rebuild, deterministic-output check, contact-sheet/family review,
accepted-defect-register closure, and final CI validation.

Do not declare a figure or family complete while any applicable rule remains unproved.

---

# 18. Definition of technical-figure completion

A technical figure is complete only when all applicable checks are proved, including:

- canonical source/build passes;
- technical semantics verified against current implementation truth;
- actual rendered PNG inspected;
- desktop/mobile variants inspected where applicable;
- fixed canvas contract satisfied;
- only relative object placement used;
- no arbitrary local geometry/style values introduced;
- typography compliant and readable;
- no clipping;
- no unnecessary/incorrect wrapping;
- canonical node/container grammar used;
- no line crosses a box or label;
- no label hides graphics;
- arrowheads are attached to their connector paths;
- connectors attach exactly at box borders;
- 90-degree entry/exit satisfied;
- correct connector semantics used;
- ports distributed correctly;
- Manhattan routing used where applicable;
- centered doglegs exactly symmetric where applicable;
- alignment/visual balance satisfactory;
- desktop/mobile semantics equivalent;
- accessibility and adjacent prose requirements satisfied;
- figure fits its visual family.

Push a compliant source change and verify the CI-generated review artifact when the
current workflow requires publication/CI verification. Freeze the figure unless a later
shared-system change requires regression inspection.

---

# 19. Asset layout and source authority

Each presentation owns exported assets under:

```text
<presentation>/assets/<asset-name>.svg|png
<presentation>/assets/src/<editable-source>
```

Shared identity and technical presentation primitives may live under `shared/assets/`.
Production READMEs must not reference unpublished workspace-only paths after
publication.

Technical TikZ sources and the shared figure system are authoritative editable sources.
Generated SVGs are derived build outputs and must never be hand-edited. Under the
figure-contract workflow being consolidated here, generated technical SVGs are not
canonical Git sources; follow the current repository CI/publication policy for their
actual publication handling.

Runtime terminal/UI evidence remains real qualified raster capture and must not be
reconstructed as fake diagram/application output.

---

# 20. Screenshot rules

Capture real, qualified current-master builds; never present a mockup as shipped
functionality.

- Use consistent scale, crop, window treatment, and visual density within a project.
- Use synthetic repositories, topics, threads, prompts, payloads, and telemetry.
- Show a meaningful successful state, not an empty interface.
- Remove usernames, home paths, hostnames, LAN addresses, tokens, credentials,
  certificates, real/private prompts, bookmarks, unrelated applications, and shell
  history.
- Use a generic `$` prompt when terminal chrome/identity adds no value.
- State tested version/environment in surrounding text or provenance records.
- Capture from the same exact master commits used to verify README commands.

Screenshots are real evidence, not technical TikZ figures, and therefore use their
prescribed capture/composition dimensions rather than the 160 mm/100 mm technical
canvas.

---

# 21. Reproducible interactive capture

Interactive desktop evidence may be staged in an isolated Xvfb display.

- Start the qualified binary in a dedicated display; never capture the maintainer's
  live desktop or unrelated windows.
- Drive only deterministic, source-aligned synthetic scenarios.
- Record binary revisions, launch arguments, geometry, input steps, and fixture state
  for each final capture.
- Render at high density where practical, then downsample once to the approved final
  canvas.
- Preserve real application chrome and meaningful state.
- Composition may crop, label, and align qualified captures, but must not redraw
  controls, replace application content, fake functionality, or conceal relevant
  limitations.
- Overwrite the canonical approved asset after review; keep editable sources and
  capture automation under `assets/src/` rather than accumulating ambiguous alternates.

---

# 22. Synthetic data baseline

Use stable, clearly fictional data where it fits:

- scenario: `edge-lab`;
- MQTT topic: `edge-lab/room-01/temperature`;
- MQTT payload: `{"value":21.7,"unit":"C"}`;
- normalized topic: `normalized/room-01/temperature`;
- code/UI workspaces and prompts: neutral names related to qualification or
  documentation, never private project data.

The MQTT and AI demonstration tracks may share visual naming, but must not imply a
runtime integration that does not exist.

---

# 23. Accessibility and theme behavior

Every meaningful image receives concise information-bearing alt text.

Every meaningful figure receives a short useful caption when surrounding prose does not
already provide that context.

Important information is repeated in text; screenshots and figures are never the only
instructions or proof.

Test SVGs and screenshots in GitHub light and dark modes.

Use light/dark variants through minimal HTML only when one neutral asset cannot maintain
contrast.

Avoid embedded text sizes that become unreadable on mobile.

Ensure pages remain navigable and understandable with images disabled.

---

# 24. Product-specific visual direction

These are starting points, not mandatory asset lists:

- **SNode.C:** code-to-result/programming-model communication and real echo proof where
  useful;
- **MQTTSuite:** the five applications and a representative MQTT message flow,
  supported by real broker/CLI/UI evidence where useful;
- **AISuite:** client types converging on bridge/app-server boundaries, authority
  separation, and typed-generation flow where useful;
- **CodexUI:** real native/browser UI and representative workflow; architecture should
  support rather than dominate the visible product story;
- **Organization:** ecosystem navigation and stable layer relationships without a fixed
  project count.

---

# 25. Ecosystem evaluation strategy

The organization uses one `Run a demo` entry point with two honest tracks:

1. **Networking and MQTT:** SNode.C → MQTTSuite.
2. **Typed Codex client:** SNode.C → AISuite → CodexUI.

Do not force an all-four-product scenario unless a real, qualified user outcome later
justifies it.

---

# 26. Facts that remain unresolved

Approval of presentation does not approve technical/release claims.

Before publication, verify or obtain owner approval for:

- versions and maturity labels;
- canonical repository and documentation URLs;
- compatibility matrices;
- supported platforms and dependencies;
- release artifacts and tested commands;
- protocol claims;
- security claims;
- performance claims;
- parity claims;
- final visual identity and freshness against the publication candidate.

Prefer omission or qualification over an unsupported claim.

---

# 27. Publication boundary

Workflow decisions live in canonical workflow artifacts. Working landing-page READMEs
contain public-facing presentation copy only after the corresponding writing stage.

Production publication happens through reviewed changes to canonical repositories; this
workspace must not modify live local source repositories directly.

Preserve unrelated concurrent changes. Never overwrite, revert, or squash unrelated
work while fixing documentation/figures.

A missing shared token/style is a contract/system issue, not permission for a local
workaround: invoke the hard-stop rule and notify the user.

---

# 28. Non-negotiable technical-figure checklist

For every canonical technical TikZ figure:

1. Read the shared TikZ README, this contract, the shared figure system, the current
   figure sources, its figure-specific contract, and relevant implementation evidence.
2. Build the current source before judging it.
3. Render actual desktop/mobile PNG review images and inspect them.
4. Use only relative positioning for figure objects.
5. Use only existing canonical constants/styles/primitives.
6. If a needed constant/style/primitive does not exist, stop the current turn and
   report the missing shared-system item; do not invent a value.
7. Keep desktop at fixed 160 mm and mobile at fixed 100 mm. Technical TikZ never uses
   dynamic canvas width.
8. Do not scale down or shrink typography to make an oversized composition fit.
9. Arrowheads must be part of their connector path; detached arrowheads are hard
   prohibited.
10. Lines/connectors must never cross boxes or labels.
11. Labels must never hide lines, bends, arrowheads, borders, or other graphic
    structures.
12. Connectors attach exactly to box borders and enter/leave orthogonally.
13. Use canonical port distribution and Manhattan routing.
14. Preserve canonical connector rhythm and exact centered-dogleg symmetry.
15. Use canonical node/container/typography/palette semantics.
16. Preserve desktop/mobile semantic equivalence.
17. Report all findings in chat before each refinement edit.
18. Refine → build → render PNG → inspect → repeat until every rule passes.
19. When satisfied, report every applicable contract category, its compliance status,
    the rendered evidence, and why the result is visually satisfactory.
20. Only then stop/freeze the figure.
