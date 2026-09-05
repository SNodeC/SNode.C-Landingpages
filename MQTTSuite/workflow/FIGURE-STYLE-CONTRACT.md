# MQTTSuite canonical figure style contract

**Status:** normative figure-refinement contract  
**Applies to:** all canonical MQTTSuite technical TikZ figures, desktop and mobile  
**Related authority:** `10-VISUAL-PRODUCTION-PLAN.md`, `MQTTSuite/assets/src/tikz/mqttsystem-figure-system.tex`, and `MQTTSuite/assets/src/tikz/snodec-canonical-figure-system.tex`

This contract makes the visual acceptance rules used during the current 24-figure refinement pass explicit. It supplements the shared visual grammar in `10-VISUAL-PRODUCTION-PLAN.md`. Where this file is stricter about concrete geometry, the stricter rule is the acceptance rule for the refinement pass.

A figure is compliant only when its technical semantics, composition, typography, responsive behavior, node/container grammar, connector geometry, build output, and actual rendered appearance all pass. Compilation alone is never sufficient.

## Semantic correctness

- Every box, label, boundary, decision, branch, state, arrow, association, and containment relationship must correspond to current implementation truth.
- Current MQTTSuite/SNode.C implementation behavior controls when an older brief, schema, prose description, or prior figure disagrees.
- Schema admission alone is not proof of runtime support.
- Runtime order, configuration ownership, process ownership, optionality, parallelism, and causality must not be conflated.
- A note or qualification must never accidentally appear as a runtime/process step.
- Source-only and runtime-qualified evidence must remain distinguishable where that distinction affects interpretation.
- Each figure must also satisfy its figure-specific contract in `10-VISUAL-PRODUCTION-PLAN.md` and the accepted review register.

## Composition and responsive behavior

- Use a clear reading order, balanced visual mass, intentional whitespace, deliberate alignment, and semantic grouping.
- Use symmetry when the semantics are symmetric; asymmetry requires a semantic or geometric reason.
- Desktop and mobile are independently art-directed, never a scaled copy.
- Desktop/mobile must remain semantically equivalent: branches remain branches, siblings remain siblings, optional paths remain optional, and error paths/qualifiers must not disappear.
- Respect the shared width/legibility budgets. Recompose oversized figures rather than shrinking typography.
- Inspect the actual generated render at realistic GitHub desktop/mobile widths.

## Typography

- Use the shared typography macros and canonical SNode.C adapter; do not rescue oversized layouts with ad-hoc font shrinking.
- Code identifiers, MQTT topics, prefixes, QoS values, routes, and application names use the shared typography hierarchy consistently.
- Automatic word hyphenation is forbidden in diagram labels, notes, routes, and technical identifiers.
- Text must not touch borders, arrowheads, connectors, or neighboring boxes and must remain readable at final GitHub width.

## Palette, nodes, and containers

- Use the canonical restrained SNode.C-compatible palette and node styles.
- Green/success styling is reserved for an actual successful outcome, never generic emphasis, a destination, a final stage, or an action.
- Meaning must survive grayscale/color-vision differences; color is never the only semantic carrier.
- Use the shared node families, radii, border weights, padding, and flat rendering grammar; avoid arbitrary one-off styling.
- `mqtt figure frame` is a neutral enclosing surface, not a semantic boundary.
- Semantic containers represent real process/runtime/configuration/lifecycle/data/control/trust boundaries and must be labeled meaningfully.
- Draw the neutral frame before semantic containers and never allow an enclosing fill to overpaint inner semantics.
- Ownership/containment uses `mqtt contains` or `mqtt association`, not a directional flow arrow unless real directional flow also exists.
- A trust boundary must not imply application-provided protection unless the implementation actually enforces it; external deployment boundaries must be labeled as external requirements/recommendations.

## Connector and arrow semantics

- Arrow direction always represents real directional semantics, never vague association.
- Every directional connector is one continuous TikZ path with its arrowhead attached to that same path. Detached/separately placed arrowheads are forbidden.
- A connector starts on the source box border and terminates on the destination box border; it must not start inside, float outside, overshoot, terminate short, or hide beneath a node.
- Connectors leave and enter box borders orthogonally at 90 degrees, using the center of the relevant border by default.
- When several connectors share one border, distribute source and destination ports evenly rather than stacking them at one point.
- Off-axis connectors use orthogonal/Manhattan routing. Unmotivated diagonal connectors are forbidden.
- Crossing through nodes is forbidden; unrelated line crossings and ambiguous visual merges must be avoided.
- Parallel related connectors should use harmonious, repeatable geometry. Avoid tiny hooks, accidental tangencies, arbitrary doglegs, or inconsistent bend positions.
- Use the canonical semantic connector styles: data/control flow, observation, handoff, association, containment, dependency. Do not interchange them for decoration.
- Branch/edge labels must be unambiguously attached to the correct segment and must not obscure a line, bend, box, or arrowhead.

### Hard centered-dogleg symmetry rule

For every three-segment orthogonal connector whose geometric shape is `|-|` or `-|-`, the two parallel outer legs **MUST have exactly equal length**.

- `|-|` means vertical → horizontal → vertical. The first and final vertical legs must be exactly equal in length. Therefore the horizontal middle segment is exactly centered between the endpoint levels.
- `-|-` means horizontal → vertical → horizontal. The first and final horizontal legs must be exactly equal in length. Therefore the vertical middle segment is exactly centered between the endpoint columns.

This is an exact geometry rule, not an approximate visual preference. An off-center three-segment dogleg fails the figure contract even when it is technically connected and otherwise readable.

## Spacing and family consistency

- Use shared spacing/rhythm tokens for recurring layout relationships; one-off offsets require a genuine geometric reason.
- All 24 figures must read as one family: typography, node grammar, border hierarchy, radii, connector weights, arrowheads, semantic colors, notes, titles, spacing rhythm, and responsive behavior must be consistent.
- MQTTSuite uses its own semantic vocabulary while presentation follows the SNode.C canonical adapter.

## Accessibility and evidence

- Final meaningful figures require information-bearing alt text and adjacent prose that preserves essential meaning when images are unavailable.
- Runtime terminal/UI evidence must remain real qualified raster capture and must not be reconstructed as fake diagram/application output.
- Technical TikZ sources are authoritative; generated SVGs are build outputs and are not committed to Git in the current workflow.

## Mandatory refinement loop

For every figure:

1. read its accepted contract;
2. verify implementation truth where technical behavior is involved;
3. inspect the current desktop/mobile render;
4. identify semantic and visual violations against this complete contract;
5. edit the canonical TikZ source only as required;
6. run the canonical CMake figure build;
7. inspect the actual generated desktop/mobile render at realistic GitHub widths;
8. inspect typography, clipping, composition, container layering, connector attachment, arrowheads, 90-degree entry/exit, port distribution, Manhattan routing, centered-dogleg symmetry, spacing, and desktop/mobile semantic equivalence;
9. repair, rebuild, and inspect again until every applicable rule passes;
10. push the compliant source change and verify its CI-generated review artifact;
11. freeze the figure unless a later shared-system change requires regression inspection.

After all figures pass individually, perform a clean whole-family rebuild, deterministic-output check, contact-sheet/family review, accepted-defect-register closure, and final CI validation.

Do not declare a figure or the family complete while any applicable rule above remains unproved.
