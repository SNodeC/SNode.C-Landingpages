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
AISuite, CodexUI, future landing-page subprojects, and all corresponding public-facing
text, technical figures, screenshots, runtime evidence, hero visuals, social previews,
and exported assets.

A technical figure is compliant only when its technical semantics, composition,
typography, responsive behavior, node/container grammar, connector geometry, build
output, and actual rendered appearance all pass. Compilation alone is never
sufficient.

Public landing-page text is compliant only when its technical statements, commands,
examples, capability/limitation descriptions, architecture descriptions, and
cross-project relationships are aligned with current implementation evidence. Good
prose is never a substitute for technical truth.

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
6. verified current implementation source/tests/runtime/release evidence for technical
   truth;
7. older proposals, READMEs, figures, screenshots, and historical planning only as
   research/provenance inputs.

For technical-figure presentation conflicts, the strict figure rules in this document
win over broader page-level art-direction rules.

For technical claims in text or figures, current implementation evidence wins over old
README wording, old figures, proposals, schemas, workflow notes, issues, comments, or
remembered behavior.

The earlier nine-section, fixed word-count, mandatory V1–V4, equal-visual-weight, and
other rigid README templates are no longer binding. Section count, prose length, table
count, and visual count are design outcomes, not compliance targets.

Existing proposals, READMEs, figures, screenshots, and social previews remain
research/provenance inputs until replaced or explicitly approved.

## 1.1 Hard stop for uncovered uncertainty

For both text and figure work, uncertainty must never be resolved by guessing.

First use the sources and rules already required by this contract to resolve the issue.
If a material question remains unresolved because the contract, shared TikZ system,
figure-specific contract, current source/tests/runtime/release evidence, or approved
workflow artifacts do not define or prove the required answer, **stop the current turn
immediately**.

This hard stop applies to uncertainty about, among other things:

- technical behavior, capability, limitation, ownership, ordering, optionality, or
  causality;
- wording or scope of a public technical claim;
- architecture or cross-project relationships;
- figure semantics;
- visual/layout relationships;
- spacing, typography, node/container geometry, ports, routing, or connector semantics;
- responsive behavior;
- asset dimensions or evidence provenance;
- any other decision whose resolution would require an assumption not authorized by
  this contract or proven by current evidence.

When the hard stop applies:

1. do not guess or choose the most convenient interpretation;
2. do not invent a rule, value, relationship, claim, or workaround;
3. do not make an unauthorized exception to this contract;
4. report the exact unresolved question and the evidence/rule that is missing;
5. stop the turn and wait for the user to resolve the ambiguity or authorize an
   explicit contract/system extension.

A partial result may be reported only for work already proved compliant; unresolved
material uncertainty blocks the affected text/figure refinement from continuing.

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

**Mandatory hard stop:** if any required canonical definition is missing, the current
turn must stop immediately. This includes a missing definition for a relationship,
layout relationship, size, spacing, routing shape, connector pattern, port distribution,
node/container primitive, typography treatment, semantic connector, canvas behavior,
padding rule, or any other geometry/style primitive needed to make the requested work
contract-compliant.

No unauthorized violation of this contract is permitted. Do not invent, estimate,
approximate, silently introduce a local value, introduce a local replacement constant,
copy a one-off literal from another figure, or use a workaround that bypasses the
missing canonical definition. Report exactly which canonical definition/token/style is
missing, explain why compliant work cannot continue without it, and stop the turn until
the user decides whether the shared system/contract should be extended.

Canonical physical dimensions defined later in this contract are not permission to
insert raw literal offsets into figure source. Source positioning must use the shared
system token or relationship that encodes the intended geometry. Technical-figure layout
values other than the canonical layout rhythm unit must be computed from that unit rather
than stored as independent physical constants. If no suitable derived token exists, the
hard-stop rule applies.

## 3.3 No figure-local styling inventions

Do not introduce figure-local colors, fonts, radii, line widths, fills, arrowheads,
shadows, padding systems, spacing systems, typography scales, or connector styles.
Use the shared canonical styles and constants.

Do not rescue an oversized composition by shrinking fonts, line widths, arrowheads,
padding, or spacing locally.

## 3.4 Hard layout resilience under shared-system changes

Technical figure sources must be **layout-resilient by construction**.

Canonical changes made in `landingpages-figure-system.tex` to spacing, typography,
font sizes, node dimensions, padding, radii, connector geometry, arrowheads, line
weights, canvas helpers, semantic styles, or other shared presentation parameters must
propagate through the figure family via relative geometry and shared tokens.

Figure-local code must not neutralize, cancel, pin, or compensate for a shared-system
change in order to preserve the old appearance. In particular, do not add local literal
spacing, compensating shifts, counter-scaling, local font sizes, local node dimensions,
local line widths, local arrow geometry, or one-off routing offsets to defeat the new
canonical values.

A shared-system parameter change is a **global regression event** for every figure that
consumes the changed primitive. Previous visual approval of those affected figures is
invalidated by the system change.

After such a change, every affected desktop/mobile figure must:

1. rebuild from canonical source using the new shared values;
2. render fresh review PNGs;
3. undergo the complete mandatory refinement loop in this contract;
4. still satisfy every semantic, source-alignment, composition, typography, canvas,
   routing, crossing, accessibility, and human-visual-quality rule;
5. be refined through relative geometry and canonical shared primitives only where the
   new values expose a problem.

A shared-system change is not complete or acceptable while any affected figure fails.
If an affected figure cannot be made compliant using the definitions available in the
shared system, invoke the mandatory hard stop instead of violating the contract or
locally restoring the old layout.

The intended result is that the maintainer may deliberately change shared layout
parameters once in `landingpages-figure-system.tex` and have the entire affected figure
family reflow according to those values, while all figures are then re-proved correct
under the same contract.

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

## 4.1 Hard source alignment for all public text

Source alignment is mandatory for **all public landing-page text**, not only figures.

This applies to:

- prose paragraphs and headings that make technical claims;
- capability and limitation descriptions;
- architecture and ownership descriptions;
- protocol/version/platform/compatibility statements;
- security, performance, maturity, support, and availability claims;
- tables and matrices;
- quick-start commands and expected results;
- configuration snippets and code examples;
- captions and alt text when they describe technical behavior;
- cross-project relationships and dependency/runtime descriptions;
- installation/package/release wording;
- troubleshooting statements and user-visible behavior claims.

Every material technical statement must align with current public implementation truth
and the level of evidence appropriate to the claim:

- source code proves that an implementation exists;
- tests qualify behavior covered by those tests;
- reproducible runtime evidence qualifies user-visible/runtime behavior;
- release/package metadata proves availability to users;
- documentation/proposals/old READMEs may identify candidate facts but are not proof by
  themselves.

No public technical statement may rely solely on an older README, proposal, figure,
schema, issue, comment, workflow note, or remembered behavior when current source/test/
runtime/release evidence is available or required.

If source, tests, runtime behavior, maintained documentation, or release metadata
disagree, do not choose the convenient wording. Resolve the conflict where possible;
otherwise omit, neutralize, or explicitly qualify the claim until the evidence is
consistent. If the correct treatment remains uncertain after applying the contract and
available evidence, invoke the hard stop from §1.1.

A polished paragraph that is stale, broader than the evidence, or inconsistent with the
current implementation is non-compliant and blocks publication just as a semantically
wrong figure does.

Figures, captions, tables, examples, commands, and prose must not contradict one
another. The complete landing page must tell one source-aligned technical story.

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
- If the correct semantic interpretation cannot be proved from the contract and current
  evidence, invoke the hard stop from §1.1 rather than drawing an assumed relationship.

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

Canonical technical/vector layout geometry in this contract is specified in physical
units, with **millimetres as the normative layout unit**. Pixel measurements of rendered
technical figures are diagnostic only and never define source geometry, connector
lengths, spacing, box geometry, routing, or any other technical/vector relationship.
Raster pixel dimensions remain valid only for inherently raster assets and raster
capture/export specifications.

### 11.1.1 One canonical layout rhythm unit

Within the technical-figure composition system, there is exactly one independently
specified spatial layout distance:

- **canonical layout rhythm unit `R = 8.3 mm`**.

Every other recurring technical-figure layout distance must be **calculated from `R`**
inside `landingpages-figure-system.tex` as an explicit rational multiple or fraction.
It must not be stored as another independent millimetre constant. This applies to, among
other things:

- inter-node and inter-row/inter-column gaps;
- branch and lane spacing;
- node, container, group, trust-boundary, and frame padding;
- title, annotation, and edge-label spacing;
- safe-area and routing offsets;
- straight-connector primary-axis spans;
- centered-dogleg outer legs;
- canonical minimum/target node and container dimensions and text-width classes where a
  fixed layout dimension is required.

Content-driven dimensions may expand naturally to fit their content. If a minimum,
target, or class dimension is required, however, that dimension must still be produced
by a shared token derived from `R` rather than by a figure-local or independent physical
value.

The shared system may expose semantic derived tokens such as tight, normal, loose,
large, padding, label, or node-size relationships, but the underlying physical value of
each token must be computed from `R`. Figure sources consume those semantic tokens and
must never introduce their own rational multiplier or derived millimetre value.

The default recurring rhythm scale is rational and derived from `R`:

- micro / label rhythm: `R / 4`;
- compact / half rhythm: `R / 2`;
- tight rhythm: `3R / 4`;
- normal rhythm and ordinary connector span: `R`;
- loose rhythm: `4R / 3`;
- large / lane rhythm: `5R / 3`.

Additional layout relationships may use another rational multiple only when that
relationship is made an explicit canonical shared-system primitive. A figure source may
never invent such a multiplier locally.

The publication canvases (160 mm desktop and 100 mm mobile) are independent hard output
constraints, not derived layout rhythm distances. Optical/rendering properties such as
typography sizes, line widths, arrowhead dimensions, and corner radii are likewise
separate canonical systems and are not derived from `R` unless this contract explicitly
changes that policy later.

Changing `R` is therefore a global layout-system change: all derived spatial layout
tokens change with it, and every affected figure must undergo the full regression and
rendered-PNG refinement loop from §3.4 and §17.

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
value would be required, do not invent one; invoke the hard stop from §1.1.

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

**Connector simplicity takes precedence over mechanically enforcing an even port
formula.** When source and destination are aligned so that a single straight horizontal
or vertical border-to-border connector expresses the relationship without crossing,
overlap, or ambiguity, use that straight connector. Do not introduce a bend or dogleg
merely to reach an evenly distributed port.

When several connectors genuinely need distinct attachment positions on one border,
distribute source and destination ports evenly using canonical shared port primitives by
default rather than stacking them at one point. The canonical `i/(n+1)` distribution is
a default, not an absolute requirement when it would force an otherwise unnecessary
bend. It may be broken to preserve a cleaner straight connector, provided the attachment
still lies exactly on the border, remains orthogonal, uses a canonical center/anchor or
other canonical relative port relationship, and creates no crossing, overlap, or
ambiguous merge.

This straight-connector exception never permits a figure-local literal attachment
fraction or absolute border distance. If preserving the straight connector would require
an arbitrary `.18`, `.333`, `.50`, `.667`, `.82`, or similar literal fraction, or any
other non-canonical attachment value, invoke the mandatory hard stop instead.

**Distributed ports are relative to the current border geometry.** When the distributed
port primitive is used for `n` connectors sharing one border, canonical port `i`
(1-based, `1 <= i <= n`) is placed at the fraction `i/(n+1)` of that border's current
length. A single distributed connector therefore uses the center (`1/2`), two use `1/3`
and `2/3`, three use `1/4`, `2/4`, and `3/4`, and so on.

Figure sources using distributed ports specify only the node, border side, ordinal port
index, and total port count through canonical distributed-port primitives. Changing
canonical node width, height, padding, typography, or other shared geometry must
automatically move those distributed ports with the border while preserving the same
even relative distribution.

If neither a canonical straight center/anchor attachment nor the canonical distributed
ports can express the required relationship cleanly, that is not permission to invent a
non-even figure-local fraction. Invoke the mandatory hard stop until the required
relative attachment relationship is represented by a canonical shared primitive.

## 14.3 Routing

**Straight connectors are preferred over bent connectors whenever they can express the
same relationship cleanly.** Do not introduce a bend, dogleg, or detour when a straight
horizontal or vertical border-to-border connector can carry the same semantics without a
crossing, overlap, or ambiguous merge. Every bend must therefore have a genuine
geometric or semantic reason such as non-aligned endpoints, obstacle avoidance, branch
structure, or relationship semantics. Satisfying an even-port formula, creating visual
symmetry, or decorative routing is not by itself a valid reason to bend a connector.

Off-axis connectors that genuinely require a bend use orthogonal/Manhattan routing.
Unmotivated diagonal connectors are forbidden.

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
routing primitive, invoke the mandatory hard stop rather than inventing a workaround.

Branch/edge labels must be unambiguously attached to the correct segment and placed via
the canonical label spacing/styles.

---

# 15. Canonical connector rhythm

An ordinary straight process/data/control connector run has an edge-to-edge primary-axis
span of exactly **`1 × R`** between the connected box borders. The connector rhythm is
therefore derived from the one canonical layout rhythm unit and owns no independent
physical distance.

- Recurring ordinary straight arrows preserve this canonical run unless a genuine
  semantic/geometric constraint requires another shared `R`-derived spacing token.
- Do not shorten arrows merely to reduce figure height or width; recompose the layout.
- Desktop and mobile are independently art-directed, but preserve the same canonical
  physical connector rhythm.
- Observation/association/dependency routes may be longer when their real destination
  requires it, but still use canonical connector grammar and deliberate `R`-derived
  spacing.

The shared figure system must encode the connector span as a direct derivation from `R`.
Figure sources must not write `8.3mm`, another derived millimetre value, or a local
multiplier. Pixel measurements in review PNGs are derived diagnostics only; changing
rasterization resolution must never change the required source geometry. If no suitable
shared derived token exists, invoke the mandatory hard stop.

## 15.1 Canonical bent-arrow primary-axis span

This section applies only after §14.3 establishes that a bend is genuinely required. It
does not authorize bending a connector that can remain straight.

An ordinary multi-segment bent process/data/control connector consumes the same total
primary-axis span as an ordinary straight arrow: **`1 × R`**. Bending a connector must
not increase or reduce the row/column separation between source and destination.

For a normal vertically progressing `|-|` connector, the source-border-to-destination-
border height is `1 × R`. Its two vertical outer legs are exactly equal, and **each leg
is calculated as `R / 2` from the canonical rhythm unit**.

For a normal horizontally progressing `-|-` connector, the total horizontal span is
likewise `1 × R`. Its two horizontal outer legs are exactly equal, and **each leg is
calculated as `R / 2` from the canonical rhythm unit**.

The half-span is a calculation from `R`; it must not be stored, repeated, or hard-coded
as an independent physical value in the contract, shared system, or figure sources.

The perpendicular middle segment may be as long as required by the real offset; it does
not change the canonical primary-axis span.

Do not add extra height/width merely because a connector bends. Recompose nodes instead.

A genuine semantic bypass such as a long observation/association/dependency route may
span multiple layout levels and is not forced into the adjacent-level `1 × R` span,
but every deliberate routing distance still comes from an appropriate shared
`R`-derived relationship and centered-dogleg symmetry still applies where applicable.

## 15.2 Hard centered-dogleg symmetry

For every three-segment orthogonal connector with geometric form `|-|` or `-|-`, the
two parallel outer legs **must have exactly equal length**.

- `|-|`: vertical → horizontal → vertical; first and final vertical legs are exactly
  equal, so the horizontal segment is centered between endpoint levels.
- `-|-`: horizontal → vertical → horizontal; first and final horizontal legs are
  exactly equal, so the vertical segment is centered between endpoint columns.

For ordinary adjacent-level connectors this exact symmetry rule and the canonical
`1 × R` primary-axis-span rule apply together. Each outer leg is calculated as `R / 2`;
no separate half-span constant is authoritative.

This is an exact geometry requirement, not an approximate aesthetic preference. An
off-center three-segment dogleg fails the contract even when technically connected and
otherwise readable.

---

# 16. Spacing and family consistency

Every recurring technical-figure spatial layout relationship must use a shared semantic
token calculated from the single canonical layout rhythm unit `R`. Independent
millimetre constants for layout spacing, padding, routing, or size classes are
prohibited. Derived values are formulas, not additional authorities.

Use shared spacing/rhythm tokens for every recurring layout relationship. One-off
spacing values or figure-local rational multipliers are prohibited by the
no-arbitrary-values rule.

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

If those sources leave any material semantic or presentation uncertainty unresolved,
invoke the hard stop from §1.1 before editing.

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
- layout resilience against shared-system changes;
- connector semantics;
- arrowheads attached to their paths;
- exact border attachment;
- 90-degree entry/exit;
- straight-connector preference and bend necessity;
- port distribution and any justified straight-connector exception;
- Manhattan routing;
- straight-arrow rhythm;
- centered-dogleg symmetry;
- line/box crossings;
- line/label crossings;
- labels hiding graphic structure;
- consistent label placement;
- desktop/mobile semantic equivalence;
- actual human visual quality.

If the review exposes an issue for which the contract/shared system does not define a
compliant treatment, invoke the mandatory hard stop rather than improvising one.

### 17.5 If NOT satisfied

Before editing, list **all currently identified findings in the chat**, including the
violated contract rule and whether each defect is semantic, geometric, stylistic,
responsive, or perceptual.

Then refine the canonical source, rebuild, render fresh PNGs, inspect again, and return
to **LOOP START**.

Do not merely report the next failure and stop. Do not stop because compilation passes.
Do not freeze after one refinement round while visible defects remain.

### 17.5.1 Sequential family reporting

When a requested refinement covers multiple figure concepts, process them **one concept
at a time**. Before the first edit to the current figure concept, list all currently
identified contract violations for that concept in the chat. For responsive concepts,
treat the desktop/mobile pair as that one concept.

Do **not** pre-list or batch findings for later figure concepts. Complete the current
concept's refine → build → render → inspect loop until it passes or reaches the mandatory
hard stop before moving to the next concept. If a later iteration exposes additional
violations in the current concept, report those newly identified findings before the
next edit to that same concept.

### 17.6 If satisfied

Before stopping, report every applicable style-guide/contract category and its status.
For every category state the concrete evidence for compliance or why it is genuinely not
applicable.

The final satisfaction report must explicitly include rendered desktop/mobile PNG
inspection and explain why the figure is visually harmonious, readable, balanced,
source-aligned, layout-resilient, and free from further required refinement or
unresolved material uncertainty.

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
- no material unresolved uncertainty remains;
- actual rendered PNG inspected;
- desktop/mobile variants inspected where applicable;
- fixed canvas contract satisfied;
- only relative object placement used;
- no arbitrary local geometry/style values introduced;
- layout remains driven by shared tokens and relative relationships rather than local
  compensation;
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
- straight connectors used whenever they can express the relationship cleanly;
- bends justified by actual geometry or semantics;
- ports distributed correctly, or a §14.2 straight-connector exception is justified;
- Manhattan routing used where applicable;
- centered doglegs exactly symmetric where applicable;
- alignment/visual balance satisfactory;
- desktop/mobile semantics equivalent;
- accessibility and adjacent prose requirements satisfied;
- figure fits its visual family.

Push a compliant source change and verify the CI-generated review artifact when the
current workflow requires publication/CI verification. Freeze the figure unless a later
shared-system change requires regression inspection; such a system change invalidates
prior visual approval for every affected figure as defined in §3.4.

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

Prefer omission or qualification over an unsupported claim only where the evidence
itself clearly supports that treatment. If a material unresolved fact leaves the correct
public treatment uncertain, invoke the hard stop from §1.1.

---

# 27. Publication boundary

Workflow decisions live in canonical workflow artifacts. Working landing-page READMEs
contain public-facing presentation copy only after the corresponding writing stage.

Production publication happens through reviewed changes to canonical repositories; this
workspace must not modify live local source repositories directly.

Preserve unrelated concurrent changes. Never overwrite, revert, or squash unrelated
work while fixing documentation/figures.

A missing shared token/style/relationship/definition or any other material uncertainty
not resolved by this contract and current evidence is not permission for a local
workaround, assumption, or unauthorized contract exception. Invoke the appropriate
hard stop and notify the user.

---

# 28. Non-negotiable technical-figure checklist

For every canonical technical TikZ figure:

1. Read the shared TikZ README, this contract, the shared figure system, the current
   figure sources, its figure-specific contract, and relevant implementation evidence.
2. If any material uncertainty remains unresolved after reading the authorities and
   evidence, stop the turn and report it; never guess.
3. Build the current source before judging it.
4. Render actual desktop/mobile PNG review images and inspect them.
5. Use only relative positioning for figure objects.
6. Use only existing canonical constants/styles/primitives/relationships.
7. If any needed definition or primitive does not exist, stop the current turn and
   report the missing shared-system/contract item; no unauthorized violation or local
   workaround is allowed.
8. Keep desktop at fixed 160 mm and mobile at fixed 100 mm. Technical TikZ never uses
   dynamic canvas width.
9. Do not scale down or shrink typography to make an oversized composition fit.
10. Keep figure layout resilient: shared-system parameter changes must propagate via
    relative geometry/shared tokens; local compensation that restores old values is
    prohibited.
11. Treat each shared-system parameter change as a regression event for every affected
    figure and re-run the complete rendered-PNG refinement loop before acceptance.
12. Arrowheads must be part of their connector path; detached arrowheads are hard
    prohibited.
13. Lines/connectors must never cross boxes or labels.
14. Labels must never hide lines, bends, arrowheads, borders, or other graphic
    structures.
15. Connectors attach exactly to box borders and enter/leave orthogonally.
16. Prefer straight connectors whenever they can express the relationship cleanly; a
    bend requires a genuine geometric or semantic reason and must never be introduced
    merely to satisfy even port distribution.
17. Use canonical port distribution by default; the §14.2 straight-connector exception
    may break even `i/(n+1)` distribution only through canonical relative attachment,
    never arbitrary literal fractions or offsets.
18. Use Manhattan routing for connectors that genuinely require bends.
19. Preserve the canonical `R`-derived connector rhythm and exact centered-dogleg
    symmetry for bends that are actually required.
20. Use only shared `R`-derived spatial layout tokens; no independent or figure-local
    physical layout distances are permitted.
21. Use canonical node/container/typography/palette semantics.
22. Preserve desktop/mobile semantic equivalence.
23. Report all findings in chat before each refinement edit.
24. Refine → build → render PNG → inspect → repeat until every rule passes.
25. When satisfied, report every applicable contract category, its compliance status,
    the rendered evidence, and why the result is visually satisfactory and free of
    unresolved uncertainty.
26. Only then stop/freeze the figure.

---

# 29. Non-negotiable source-alignment checklist for public text

For every public landing-page text change or text review:

1. identify every material technical claim, command, example, capability, limitation,
   architecture statement, cross-project relationship, and availability/release claim;
2. verify each against the appropriate current source/test/runtime/release evidence;
3. do not treat an older README, proposal, diagram, schema, issue, or remembered behavior
   as sufficient proof by itself;
4. ensure prose, tables, captions, examples, commands, and figures agree with one
   another;
5. qualify claims only to the level actually proved by the evidence;
6. if evidence conflicts, resolve the conflict or keep the affected public claim out
   until its correct treatment is established;
7. if any material uncertainty remains not covered by this contract or current
   evidence, stop the turn and report it rather than guessing;
8. do not declare the text publication-ready while any material technical statement is
   stale, unsupported, broader than its evidence, contradictory, or unresolved.

---

# 30. Hard adversarial visual acceptance and visible-progress protocol

This section is **global and project-independent**. It applies to every canonical
technical figure, regardless of subject, topology, number of nodes, project, or
responsive composition.

This section is semantically merged with the hard rules in §§3, 9–18, and 28. Where a
circumstance is already governed elsewhere in this contract, the requirements are one
cumulative hard gate; this section strengthens the review and execution protocol and
never creates an alternative or weaker acceptance path. **No earlier instruction is
weakened, replaced, or made optional by this section.**

## 30.1 Adversarial acceptance doctrine

Technical-figure review is **disproval-driven, not confirmation-driven**.

The reviewer must actively search for reasons to reject the figure before searching for
reasons to accept it. The review question is never merely “can this be called good?” but
**“can any semantic, geometric, structural, perceptual, responsive, source, or
implementation reason be found why this figure must not pass?”**

A figure is not accepted because its implementation is correct. It is accepted only
when an adversarial, full-contract review proves that its final rendered appearance
communicates the intended semantics clearly, correctly, harmoniously, and without any
known defect.

Acceptance always has independent gates:

1. **construction/source correctness** — implementation truth, canonical primitives,
   relative positioning, shared `R`-derived geometry, connector construction, canvas
   mechanics, build, and CI;
2. **rendered human correctness** — perceived hierarchy, grouping, containment,
   relationships, sequence, balance, negative space, emphasis, typography, and
   responsive composition;
3. **reproduction/family correctness** — final clean family build, exact vector bounds,
   deterministic output, full-size regression, family/contact-sheet review, and final CI
   where applicable.

Passing any one gate provides **zero permission** to infer that another gate passes.
In particular, none of the following proves rendered visual acceptance: canonical
styles, shared tokens, absence of forbidden literals, mathematically correct border
attachments, successful compilation, green CI, generated SVGs, correct canvas numbers,
deterministic output, or technically correct semantics in source.

Human visual interpretation is a hard semantic gate. Judge what the final geometry
actually communicates to a technically competent reader, not what the author intended
or what a TikZ style happens to be named. If the render reasonably suggests a materially
different hierarchy, ownership, sequence, causality, grouping, containment, precedence,
association, flow, optionality, peer relationship, or importance than the accepted
semantic contract, the figure fails.

The reviewer who created or edited the figure must perform a stricter, not weaker,
review: discard implementation intent mentally and inspect the render as if encountering
it for the first time. Knowledge of how the source was constructed must never be used to
excuse misleading rendered geometry.

Completion requires **zero known applicable defects**, not merely zero blockers. Do not
reclassify a known contract violation as “minor”, “polish”, or “acceptable” in order to
finish the workflow.

If the user identifies one defect, that finding never narrows the review scope. After
fixing it, the entire figure is reviewed again against the complete contract, including
unrelated pre-existing and newly exposed defects.

Any later screenshot, vector-bound check, family review, user inspection, or other
current evidence that reveals a violation automatically invalidates the affected
figure's prior PASS status and every family/completion PASS that depended on it. The
full applicable refinement loop resumes; an earlier PASS verdict has no authority
against contradictory current evidence.

If a defect originates in a shared primitive, style, color rule, spacing/padding rule,
connector treatment, typography rule, or canvas helper, treat it as a shared-system
defect. Correct it centrally, identify every affected consumer, invalidate their prior
acceptance, and rerun the complete refinement loop for all affected figures. Never hide
or compensate for a shared-system defect locally.

## 30.2 Mandatory visual analysis order

Every rendered review must inspect global structure before local details, in this order:

1. whole-figure silhouette, reading order, overall balance, and visual mass;
2. major hierarchy, parent/child relationships, semantic grouping, and containment;
3. negative-space distribution and spacing rhythm;
4. peer relationships, alignment, symmetry/asymmetry, and comparative visual status;
5. connectors, branch structure, directional meaning, and perceptual dominance;
6. node/container geometry, padding, and final rendered boundaries;
7. typography, labels, color semantics, notes, and text density;
8. local details such as arrowheads, attachment points, bends, clipping, and micro
   alignment.

Perfect local details never rescue a broken global composition.

For every visible structural level, identify the parent, children, and siblings from the
render alone. Verify that containment and nesting depth are visually unambiguous, sibling
boundaries do not accidentally merge, no child appears to belong to the wrong parent,
and a neutral/decorative enclosure is not mistaken for semantic containment. If the
rendered hierarchy cannot be described unambiguously without relying on source knowledge
or surrounding prose, the figure fails.

Whitespace is an active layout element. Explicitly inspect negative space for balance,
intentionality, rhythm, and semantic justification. Reject accidental large voids,
squeezed structural gaps, unexplained empty bands, detached islands, routing-created
cavities, or whitespace that makes the wrong element appear dominant.

For every major element or group, inspect visual weight from area, border strength,
color/fill, text density, connector density, position, and surrounding whitespace. The
most visually dominant elements must deserve that dominance semantically.

Whenever elements are semantic peers, compare them directly for dimensions, alignment,
spacing, border/color treatment, typography, whitespace, connector density, and
perceived importance. Any asymmetry requires a real semantic or unavoidable geometric
reason; symmetric semantics must not be rendered with accidental hierarchy.

## 30.3 Mandatory perceptual tests

Every connector receives two independent reviews:

- **geometric review:** semantic style, correct source/destination, border attachment,
  direction, orthogonal entry/exit, whether a straight connector was used whenever
  possible, whether every bend is genuinely necessary, routing, crossings, port
  distribution or justified §14.2 exception, rhythm, and dogleg symmetry;
- **perceptual review:** what relationship the line actually looks like, whether it
  resembles an unintended bypass or alternate path, whether association looks like flow,
  whether it creates a false stack/layer interpretation, whether it merges with another
  path, and whether its length/placement makes it more important than intended.

A connector passes only when both reviews pass. A technically correct style name is not
sufficient if the rendered line communicates the wrong thing.

Long connectors are reviewed for perceptual dominance. A long route fails when it
becomes one of the strongest visual elements without semantic justification, creates a
false stack or hierarchy, makes a peer path look secondary without reason, or creates a
large empty region merely to accommodate routing.

Every visible enclosure must pass a **container-legitimacy test**: identify the real
semantic boundary it communicates. A semantic container may represent only a proven
process/runtime/configuration/lifecycle/data/control/trust or other explicitly accepted
semantic boundary. If its only purpose is presentation grouping, alignment, or layout,
use an approved non-semantic grouping treatment instead; if none exists, invoke the hard
stop.

Enclosing geometry is judged from the **final padded/styled rendered boundary**, not
from an internal content-fit/helper node. A parent frame or container must actually
contain its final child containers with deliberate clearance, must not touch or visually
merge with them or with siblings, and must remain correct when shared padding changes.
Helper geometry is never sufficient proof of final containment.

Every colored node, border, connector, or fill passes a **color-semantics test**:
identify the canonical semantic meaning of the color and the semantic meaning of the
object, then verify that they agree. Style names grant no exemption. If a shared style
assigns a semantic color incorrectly, the shared system is defective and affected
figures cannot pass until it is corrected centrally.

Text is reviewed for visual mass as well as legibility. Notes, qualifications, and prose
must remain subordinate to the technical structure and must not dominate the figure,
repeat most relationships already encoded graphically, or turn the figure into a text
panel with decorative graphics.

Every figure receives an explicit **ambiguity test**: ask whether a technically
competent reader could reasonably infer a materially different relationship from the
render. Deliberately test, where applicable, parent vs peer, containment vs flow,
sequence vs ownership, association vs causality, optional branch vs normal progression,
shared resource vs independent resource, grouping vs boundary, and precedence vs
ordinary input flow. Any materially different reasonable interpretation fails the
figure.

Figure-specific semantics must be visually encoded, not merely written somewhere. Text,
style names, source comments, captions, or surrounding prose may clarify an already
correct render but must never repair a misleading visual structure.

## 30.4 Responsive, vector, and family review

Desktop approval provides zero evidence for mobile approval, and mobile approval
provides zero evidence for desktop approval. Each variant independently passes the full
semantic, structural, perceptual, typography, color, connector, negative-space, canvas,
and visual-balance review. Responsive review asks whether the variant is itself a good
composition, not merely whether all content survived.

PNG inspection and vector-bound inspection are independent hard gates. For every
technical figure inspect the actual generated vector bounds/viewBox and prove the exact
canonical physical canvas. A PNG that looks as if it fits does not prove canvas
compliance, and content must not silently enlarge the vector output.

Review order is mandatory:

1. full-size desktop render;
2. full-size mobile render;
3. individual figure acceptance;
4. only then family/contact-sheet review.

A contact sheet is a secondary family-consistency gate and never substitutes for
full-size individual review. At family level actively search for inconsistent visual
density, hierarchy, border treatment, whitespace rhythm, title treatment, color
semantics, visual weight, connector language, and responsive behavior.

After the last concept in a family is refined, rebuild the final family and reinspect
all earlier accepted figures from that final build before family acceptance. Earlier
individual acceptance remains provisional until this final-family regression passes.

## 30.5 Mandatory second-pass review

The first apparently successful render is **not sufficient to freeze a figure**.

When an analysis first appears to produce all-pass results, perform one additional
full review from scratch before satisfaction. Do not rely on previous findings or on the
fact that the requested defects were fixed. Reassess the complete render and complete
contract as though it had not been reviewed before.

Immediately before any PASS, ask:

> **What could still be wrong with this figure even though the source, build, and
> previous fixes look correct?**

Perform a fresh inspection specifically to answer that question. Only when no concrete
applicable defect remains may PASS be issued.

## 30.6 Progress must be visual — mandatory visible state machine

**Progress must be visual. This workflow is a hard must and is not optional.**

For every figure concept, execute and visibly report this state machine in the chat:

1. **Switch to Figure X.** Explicitly state which figure concept is now current. For a
   responsive concept, desktop and mobile are one concept but both variants are reviewed.
2. **Start the analysis of Figure X.** Analyze the current generated render(s), source,
   semantic contract, implementation evidence, and **every applicable PAGE-SYSTEM.md
   styling/technical-figure item**, including the adversarial protocol in this section.
3. **Produce a conformance report as a table.** The table must contain the applicable
   checks/categories with explicit **✓ / ✗** status and concrete evidence/findings. Do
   not replace this table with prose or a vague “looks good” statement.

**Hard write barrier before any figure-source edit:** the complete visible conformance
table for the exact current rendered desktop/mobile figure pair is a precondition for
any source-changing tool call that edits the current figure or a shared figure-system
primitive affecting it. If that table is absent, incomplete, refers to a stale render or
source state, or omits any applicable `PAGE-SYSTEM.md` category, **do not edit or write
the figure source**.

4. **Satisfied?** Satisfaction means every applicable check is ✓, there is no unresolved
   uncertainty, exact vector/canvas checks pass, and the mandatory second-pass review in
   §30.5 has also passed.
   - **YES:** report the **final conformance report as a ✓ / ✗ table** with concrete
     evidence. All applicable rows must be ✓. Stop/freeze this figure concept only then.
   - **NO:** report **all currently identified findings** in the conformance table; every
     failed row is ✗ and states the concrete violation. Then fix the canonical source.
5. **After every fix, build and render fresh preview PNG(s), and SHOW those preview
   PNG(s) visibly in the chat.** For responsive concepts show both desktop and mobile
   previews. Merely saying that an artifact exists, giving a path, or reporting CI is
   not sufficient visual progress.

**Hard write barrier after any figure-source edit:** after a source-changing tool call,
no second source-changing tool call for that figure is permitted until the edited source
has been canonically built, fresh desktop/mobile PNGs have been shown visibly in chat,
and the complete analysis has restarted from step 2 for those exact fresh renders. The
previous defect list, successful compilation/CI, source inspection, or evidence that the
requested defect was fixed cannot satisfy this barrier.

6. **Go back to “Start the analysis of Figure X”.** Re-analyze the complete figure from
   scratch against all applicable rules, not only the defect just fixed. Repeat the
   conformance-table → fix → visible-preview loop until satisfaction.

The loop is therefore exactly:

```text
Switch to Figure X
        ↓
Start full analysis using every applicable contract item
        ↓
Conformance table with ✓ / ✗ and concrete evidence
        ↓
Satisfied? ── YES ──→ final ✓ / ✗ conformance table → freeze/stop figure
    │
    NO
    ↓
Report all findings in the table
    ↓
Fix canonical source
    ↓
Build + render fresh PNG(s)
    ↓
SHOW preview PNG(s) in chat
    ↓
return to Start full analysis
```

No hidden multi-round refinement is permitted. The visible chat progression must make
clear which concept is active, what currently fails, what was changed, what the actual
new render looks like, and why the next analysis passes or fails.

When multiple figure concepts are requested, complete this visible state machine for
one concept before switching to the next. Do not batch later-figure findings in advance.

## 30.7 Concrete acceptance evidence and prohibition on premature completion

PASS evidence must be concrete. Statements such as “looks clean”, “looks balanced”,
“visually harmonious”, “no obvious issue”, “CI is green”, “the contact sheet looks
coherent”, “source rules pass”, “all arrows are connected”, or “canvas dimensions pass”
are insufficient by themselves.

A final conformance report must state concrete evidence for applicable categories such
as hierarchy/nesting, negative space, peer balance, visual weight, connector meaning,
container legitimacy and final padded extents, color semantics, text-to-diagram balance,
typography, crossings, border attachment, routing/doglegs, responsive equivalence,
vector bounds, source alignment, layout resilience, and actual rendered inspection.

The assistant must never declare a figure or family complete merely because the
requested edit is finished, CI became green, no source violation is obvious, the latest
PNG looks better, every previously listed defect was addressed, or the user has not
identified another problem. Completion is based exclusively on a fresh full-contract
acceptance review with zero known applicable defects.

Every figure checklist in §28 is incomplete unless this section also passes. Every
family completion in §17/§18 is incomplete unless the three independent proof classes in
§30.1, the full-size/family regression in §30.4, the second-pass review in §30.5, and the
visible-progress protocol in §30.6 have all been satisfied.
