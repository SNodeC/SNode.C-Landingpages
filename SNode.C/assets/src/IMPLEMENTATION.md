# SNode.C visual asset implementation notes

Implementation date: 29 August 2026
Validated SNode.C source baseline: `bf01683a53b48220a840522e8ccaf3b48e58c240`

This file preserves the Step 5/6 implementation record and adds the Step 8
publication-refinement result. Human publication approval remains pending.

## Publication visual system

Visual 1 and Visual 3 now use one neutral, self-contained SVG system:

- explicit `#F8FAFC` canvas and internal surfaces so GitHub light/dark page CSS
  is irrelevant to SVG legibility;
- foundation blue `#1D4ED8` for runtime arrows/emphasis;
- explicit neutral strokes and labels so meaning survives grayscale;
- system/generic sans and monospace font stacks only;
- no `currentColor`, `prefers-color-scheme`, external CSS, external fonts,
  `<script>`, `<foreignObject>`, `<image>`, raster payloads, or linked resources;
- no fixed HTML embedding width/height; publication SVGs expose a `viewBox` and
  scale normally in GitHub Markdown.

The editable sources are already clean publication SVG. Export is therefore a
byte-preserving copy rather than a renderer-specific reserialization:

```sh
cp SNode.C/assets/src/programming-model.svg \
   SNode.C/assets/programming-model.svg
cp SNode.C/assets/src/http-websocket-context-switch.svg \
   SNode.C/assets/http-websocket-context-switch.svg
cmp -s SNode.C/assets/src/programming-model.svg \
       SNode.C/assets/programming-model.svg
cmp -s SNode.C/assets/src/http-websocket-context-switch.svg \
       SNode.C/assets/http-websocket-context-switch.svg
```

### Visual 1 — programming model

- Editable source: `SNode.C/assets/src/programming-model.svg`
- Publication export: `SNode.C/assets/programming-model.svg`
- Canvas: `1280 × 720` viewBox (`16:9`)
- Rendered export verified, not just source markup.

| Required semantic | Result | Rendered verification |
| --- | --- | --- |
| `SocketServer` endpoint flow is distinct | PASS | Separate server card and path |
| `SocketClient` endpoint flow is distinct | PASS | Separate client card and path |
| Each endpoint retains its own `SocketContextFactory` | PASS | Both endpoint cards explicitly say `retains its own factory` |
| No shared/global factory is implied | PASS | Factory target is labeled as the originating endpoint's retained factory |
| Server path is `listen → accept` | PASS | Exact label present on server card |
| Client path completes connection establishment | PASS | Exact `connect completes` label present |
| Both paths converge on an established `SocketConnection` | PASS | Both runtime arrows enter the single established connection card |
| Connection invokes retained factory with `create(this)` | PASS | Connection-to-factory runtime arrow is labeled `create(this)` |
| Factory produces per-connection `SocketContext` | PASS | `returns new` arrow enters `SocketContext` card |
| One context is active per connection | PASS | Connection and context cards explicitly state one active context |
| Event loop is driven by `start()` | PASS | Bottom rail is `Event loop — start()` |
| No operational `tick()` claim | PASS | `tick()` is absent |
| No framework worker-pool implication | PASS | No worker objects are drawn; rail explicitly says `no framework worker pool` |

Alt text remains:

> Diagram of the SNode.C programming model: a SocketServer accepts or a SocketClient completes a connection, the SocketConnection calls its endpoint flow's SocketContextFactory to create one active per-connection SocketContext, and the caller-thread event loop dispatches lifecycle and I/O callbacks.

### Visual 2 — authentic echo evidence

**Publication decision: ABSENT.**

The committed Landingpages tree has no validated
`SNode.C/assets/src/echo-capture/` raw capture set and no publication-final
`SNode.C/assets/echo-connection-evidence.png`. Step 5 contains an exact-revision
reproduction recipe and recorded output, but those text records are not a raw
terminal-capture provenance set. The current execution environment likewise has
no exact-revision SNode.C checkout or built echo binaries from which a new real
capture can be produced.

The historical `SNode.C/assets/echo-terminal.png` was not reused, relabeled,
redrawn, normalized, or copied into the publication package. No synthetic
terminal output was created.

A future pass requires a fresh exact-revision run plus the raw PNGs, verbatim
transcripts, `REPRODUCTION.md`, and deterministic composition material specified
in `SNode.C/workflow/05-VISUALS.md`, followed by the final rendered-width,
privacy, and provenance gates.

### Visual 3 — HTTP → WebSocket context replacement

- Editable source: `SNode.C/assets/src/http-websocket-context-switch.svg`
- Publication export: `SNode.C/assets/http-websocket-context-switch.svg`
- Canvas: `1440 × 900` viewBox (wider-than-tall; mobile readability prioritized over a stricter 16:9 target)
- Rendered export verified, not just source markup.

| Authoritative chronology | Result | Rendered verification |
| --- | --- | --- |
| Accepted HTTP Upgrade | PASS | Step 1 in active HTTP phase |
| WebSocket upgrade factory selected | PASS | Step 2 begins with factory selection |
| Replacement WebSocket context created | PASS | Step 2 explicitly completes with replacement creation |
| `101 Switching Protocols` prepared | PASS | Step 3 explicitly says `101 response prepared`; SVG description carries the full status phrase |
| `setSocketContext(new)` stages while HTTP remains active | PASS | Step 4 plus `replacement STAGED · HTTP context still ACTIVE` |
| Application/status callback calls `response->end()` and queues `101` | PASS | Step 5 explicitly identifies callback ownership and queueing |
| Current HTTP read callback returns | PASS | Step 6 explicitly states callback return |
| Old HTTP context detaches for `ContextSwitch` | PASS | First completion card says `detach` / `ContextSwitch`; public prose carries exact enum spelling |
| Old HTTP context removed | PASS | Second completion card says `old HTTP context removed` |
| Active-context pointer changes to staged replacement | PASS | Third completion card says `active pointer → staged replacement` |
| WebSocket `SocketContextUpgrade` attaches | PASS | Fourth completion card is `attach()` / `SocketContextUpgrade` |
| Same `SocketConnection` remains established | PASS | Continuous lower rail states this explicitly |
| No second transport connection is created | PASS | Lower rail states this explicitly |

The figure contains no WebSocket version number and does not imply that the
framework automatically calls `response->end()`.

Alt text remains:

> HTTP-to-WebSocket context switch in SNode.C: an accepted HTTP Upgrade stages a WebSocket context; after the current HTTP read callback, the HTTP context detaches for ContextSwitch, the new context attaches, and the same SocketConnection remains established.

## Cross-figure consistency

| Check | Result |
| --- | --- |
| Visual 1 establishes one active context per connection | PASS |
| Visual 3 shows the replacement as staged while HTTP is still the active context | PASS |
| Staging does not imply two simultaneously active contexts | PASS |
| After callback return and pointer change, the WebSocket replacement becomes the one active context | PASS |
| Both figures preserve one established `SocketConnection` as the context owner | PASS |

## Render and accessibility validation

Renderer: Inkscape `1.4 (e7c3feb100, 2024-10-09)`.
Grayscale/composite checks: Pillow `12.3.0`.

Mechanical render commands used for both principal SVGs:

```sh
inkscape SNode.C/assets/<asset>.svg --export-type=png --export-width=900 \
  --export-filename=<temporary-desktop.png>
inkscape SNode.C/assets/<asset>.svg --export-type=png --export-width=375 \
  --export-filename=<temporary-mobile.png>
```

The rendered PNGs were inspected at approximately 900 px desktop width and
375 px mobile width. Each was also composited with light (`#FFFFFF`) and dark
GitHub-like (`#0D1117`) surrounding page backgrounds, then converted to
monochrome/grayscale. Temporary validation rasters live outside the repository
and are not publication artifacts.

| Render/accessibility gate | Visual 1 | Visual 3 |
| --- | --- | --- |
| Desktop render | PASS | PASS |
| Mobile render | PASS | PASS |
| Light surrounding page | PASS | PASS |
| Dark surrounding page | PASS | PASS |
| Grayscale/monochrome | PASS | PASS |
| Clipping/overlap | PASS | PASS |
| Arrow direction unambiguous | PASS | PASS |
| Information not encoded only by color | PASS | PASS |
| Primary labels remain practically readable at mobile embedding | PASS | PASS |
| Ordinary chronology labels target approximately 10 CSS px at 375 px embedding; secondary cues defer detail to adjacent prose | PASS | PASS |
| Privacy/editor metadata | PASS | PASS |

Computed WCAG contrast ratios for ordinary text against the immediate neutral
surfaces are above 4.5:1: `#0F172A` on `#F8FAFC` = `17.06:1`, `#475569` on
`#F8FAFC` = `7.24:1`, and foundation blue `#1D4ED8` on `#F8FAFC` = `6.41:1`.
Equivalent ratios on white and `#EFF6FF` remain above 6:1 for the accent/muted
text used there.

## Existing transitive visuals

`layer-architecture.svg` and `configuration-model.svg` remain technically usable
and in the publication dependency graph. Step 8 only replaced their leading
`Inter` preference with explicit system/generic font stacks; their established
composition was not redesigned. They render without external dependencies or
privacy metadata. Their older visual language is non-blocking cosmetic debt.

The older `protocol-upgrade.svg` remains in Landingpages history but is no longer
in the publication dependency graph. Its compact direct factory-to-attach story
is less precise than the validated staged replacement chronology, so
`docs/architecture.md` now reuses the publication-final principal context-switch
SVG instead of redesigning the historical figure.

## Human workflow status

The 29 August Step 6 deviation remains historical: Visual 1 and Visual 3 were
allowed to support drafting before publication-final artwork existed. Step 8 now
completes the non-human visual refinement and validation gates, but it does not
grant human approval.

**Human approval: PENDING.**
Live `SNodeC/snode.c` publication is not authorized by this step.
