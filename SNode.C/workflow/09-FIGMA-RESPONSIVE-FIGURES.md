# SNode.C responsive Figma figure integration

**Integration date:** 29 August 2026  
**Closure refresh:** 30 August 2026  
**Original Landingpages baseline:** `915901ab85805ea31ff9aa210ace28fd8136d0ac`  
**Current closure source baseline:** `60f26d9ae54b3e9ffde954d0ca75e53f79f31d79`  
**Figma design source:** [SNode.C Publication Figures](https://www.figma.com/design/giz3MDZrdwPx71L2HhiQdg)

This handoff records the Figma source-of-truth for the responsive publication
figures. It supersedes older source/layout dimensions in the Step 8/8c records,
but does not rewrite their historical technical validation or publication
decisions. Final closure details, including the two minimal clearance corrections,
are recorded in `14-FINAL-CLOSURE.md`.

## Design source

The Figma file is the editable visual design source for the four publication
figures. Each figure has a separately composed desktop and mobile frame; mobile
is not a scaled desktop layout.

| Figure | Desktop Figma node | Mobile Figma node |
| --- | --- | --- |
| Programming model | `1:3` — 1200×720 | `1:4` — 620×980 |
| HTTP → WebSocket context replacement | `7:36` — 1200×820 | `7:37` — 620×1320 |
| Architecture by composition | `7:123` — 1200×760 | `7:124` — 620×1210 |
| Configuration model | `7:217` — 1200×700 | `7:218` — 620×1120 |

The architecture-mobile height above corrects the stale 620×1180 value in the
original Step 9 table; Step 13 already recorded the authoritative 620×1210
frame after its readability correction.

Repository SVGs are Figma-derived, self-contained reproductions/exports of the
current node geometry, typography, fills, strokes, labels, and hierarchy. The
repository retains source counterparts under `assets/src/` for all eight
responsive figure variants; Figma remains the canonical editable source.

## Responsive publication strategy

GitHub supports the HTML `<picture>` element in Markdown. The publication uses
art-directed responsive image selection:

```html
<picture>
  <source media="(max-width: 600px)" srcset="assets/<figure>-mobile.svg">
  <img src="assets/<figure>.svg" alt="...">
</picture>
```

The desktop SVG is the fallback/default. At viewport widths up to 600 CSS px the
dedicated mobile composition is selected. No JavaScript, repository CSS, theme
CSS, external font, or external image dependency is required.

## Publication assets

| Figure | Desktop publication path | Mobile publication path |
| --- | --- | --- |
| Programming model | `assets/programming-model.svg` | `assets/programming-model-mobile.svg` |
| HTTP → WebSocket context replacement | `assets/http-websocket-context-switch.svg` | `assets/http-websocket-context-switch-mobile.svg` |
| Architecture by composition | `assets/layer-architecture.svg` | `assets/layer-architecture-mobile.svg` |
| Configuration model | `assets/configuration-model.svg` | `assets/configuration-model-mobile.svg` |

Visual 2 remains **ABSENT**. No terminal evidence image was synthesized or
reused.

## Repository source counterparts

The responsive figure source/export snapshots are retained at:

- `assets/src/programming-model.svg`
- `assets/src/programming-model-mobile.svg`
- `assets/src/http-websocket-context-switch.svg`
- `assets/src/http-websocket-context-switch-mobile.svg`
- `assets/src/layer-architecture.svg`
- `assets/src/layer-architecture-mobile.svg`
- `assets/src/configuration-model.svg`
- `assets/src/configuration-model-mobile.svg`

The desktop architecture and configuration counterparts were missing before the
30 August closure pass and are restored from their current Figma nodes. These
repository files are provenance/export counterparts; visual editing belongs in
Figma.

## Public dependency closure

The responsive publication closure contains **12 files**:

1. `README.md`
2. `docs/architecture.md`
3. `docs/configuration.md`
4. `docs/capabilities.md`
5. `assets/programming-model.svg`
6. `assets/programming-model-mobile.svg`
7. `assets/http-websocket-context-switch.svg`
8. `assets/http-websocket-context-switch-mobile.svg`
9. `assets/layer-architecture.svg`
10. `assets/layer-architecture-mobile.svg`
11. `assets/configuration-model.svg`
12. `assets/configuration-model-mobile.svg`

The repository paths above are relative to the eventual `SNodeC/snode.c`
publication root. Workflow files, Figma metadata, source counterparts,
`EVIDENCE.md`, historical terminal imagery, and browser-review archives are not
part of the production closure.

## Integration validation

- Current Figma desktop and mobile frames were visually inspected before the
  final closure materialization.
- All publication figures use explicit self-contained surfaces and portable
  system/generic font stacks in the repository materialization.
- SVGs contain no `<script>`, `<foreignObject>`, external images, external fonts,
  raster payloads, credentials, private paths, or editor metadata.
- README and linked documentation preserve explicit source/runtime evidence
  boundaries.
- Final closure status and exact SHAs are recorded in
  `SNode.C/workflow/14-FINAL-CLOSURE.md`.
