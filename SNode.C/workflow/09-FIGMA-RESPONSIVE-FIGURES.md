# SNode.C responsive Figma figure integration

**Integration date:** 29 August 2026  
**Landingpages baseline:** `915901ab85805ea31ff9aa210ace28fd8136d0ac`  
**Validated SNode.C source baseline:** `bf01683a53b48220a840522e8ccaf3b48e58c240`  
**Figma design source:** [SNode.C Publication Figures](https://www.figma.com/design/giz3MDZrdwPx71L2HhiQdg)

This handoff records the maintainer-requested integration of the current Figma
figure designs without an additional refinement pass. It supersedes the visual
asset source/layout portions of the Step 8/8c records, but does not rewrite their
historical technical validation or publication decisions.

## Design source

The Figma file is the visual design source for the four publication figures.
Each figure has a separately composed desktop and mobile frame; mobile is not a
scaled desktop layout.

| Figure | Desktop Figma node | Mobile Figma node |
| --- | --- | --- |
| Programming model | `1:3` — 1200×720 | `1:4` — 620×980 |
| HTTP → WebSocket context replacement | `7:36` — 1200×820 | `7:37` — 620×1320 |
| Architecture by composition | `7:123` — 1200×760 | `7:124` — 620×1180 |
| Configuration model | `7:217` — 1200×700 | `7:218` — 620×1120 |

Repository SVGs are lightweight, self-contained reproductions of the current
Figma node geometry, typography, fills, strokes, labels, and hierarchy. The
principal desktop/mobile SVGs are also retained under `assets/src/` as editable
repository-side source counterparts.

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

## Public dependency closure

The responsive publication closure now contains **12 files**:

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
publication root. Workflow files, Figma metadata, editable source counterparts,
`EVIDENCE.md`, historical terminal imagery, and browser-review archives are not
part of the production closure.

## Integration validation

- Current Figma desktop and mobile frames were visually inspected before export.
- All eight repository SVG variants were mechanically rendered with Inkscape
  from their final markup and inspected together.
- Desktop/mobile variants preserve the validated technical semantics recorded in
  Steps 5, 7, 8, and 8c.
- SVGs use explicit self-contained surfaces and system/generic font stacks.
- SVGs contain no `<script>`, `<foreignObject>`, external images, external fonts,
  raster payloads, credentials, private paths, or editor metadata.
- README and linked documentation retain their existing prose and claim
  boundaries; only figure embedding changes to responsive `<picture>` markup.
- The live `SNodeC/snode.c` repository is not modified by this integration.

## Human approval

**PENDING**

This integration intentionally preserves the current Figma designs as requested.
It does not assert final aesthetic approval and does not authorize publication to
the live `SNodeC/snode.c` repository.
