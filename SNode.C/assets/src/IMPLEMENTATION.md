# SNode.C visual asset implementation notes

Implementation date: 29 August 2026
Validated SNode.C source baseline: `bf01683a53b48220a840522e8ccaf3b48e58c240`

## Visual 1 — Programming-model lifecycle

- Export: `../programming-model.svg`
- Editable source: `programming-model.svg`
- Canvas: 920 × 940 SVG viewBox
- Neutral canvas: `#F8FAFC`
- Foundation-blue accent: `#1D4ED8`
- Runtime arrows use the accent; association/identity connectors remain neutral and undirected.
- The server path is labeled `listen → accept`; the client path is labeled `connect completes`.
- `SocketConnection` calls the retained factory with `create(this)` and the factory returns the new context.
- The figure shows one active context per connection and uses `Event loop — start()`; `tick()` is deliberately absent.
- No raster image is embedded.

Alt text recommendation:

> Diagram of the SNode.C programming model: a SocketServer accepts or a SocketClient completes a connection, the SocketConnection calls its endpoint flow's SocketContextFactory to create one active per-connection SocketContext, and the caller-thread event loop dispatches lifecycle and I/O callbacks.

Caption recommendation:

> Server and client establishment paths converge on the same connection-local context model; the event loop is driven by `start()` and the connection calls the retained factory with `create(this)`.

## Visual 2 — Echo connection evidence

No final PNG was produced in this implementation run. The repository contains no validated `assets/src/echo-capture/` raw capture set, and the available execution environment does not contain an exact-revision SNode.C checkout or built echo binaries from which a new authentic terminal capture can be made. The historical `echo-terminal.png` was not reused, redrawn, normalized, or relabeled.

The deterministic capture stage in `SNode.C/workflow/05-VISUALS.md` remains required before `echo-connection-evidence.png` can exist.

## Visual 3 — HTTP → WebSocket context replacement

- Export: `../http-websocket-context-switch.svg`
- Editable source: `http-websocket-context-switch.svg`
- Canvas: 920 × 720 SVG viewBox
- Neutral canvas: `#F8FAFC`
- Foundation-blue accent: `#1D4ED8`
- The connection rail is continuous and undirected.
- The staging box preserves factory selection → `101 Switching Protocols` preparation → `setSocketContext(new)` staging → `response->end()` queueing.
- The completion sequence is explicitly post-callback and preserves detach/removal → active-pointer change → attach ordering.
- The `attach()` transition leads to the WebSocket context; there is no direct old-context → new-context creation arrow.
- No WebSocket version is printed inside the mechanism figure; the validated specification keeps version 13 in surrounding capability scope rather than implying a transport matrix here.
- No raster image is embedded.

Alt text recommendation:

> HTTP-to-WebSocket context switch in SNode.C: an accepted HTTP Upgrade stages a WebSocket context; after the current HTTP read callback, the HTTP context detaches for ContextSwitch, the new context attaches, and the same SocketConnection remains established.

Caption recommendation:

> An HTTP Upgrade stages the replacement context and queues the `101 Switching Protocols` response; after the current read callback, the old context is removed, the active pointer changes, and the WebSocket context attaches to the same connection.

## Render and accessibility checks

The exported SVGs were rendered from their actual SVG markup, not inferred from source text. Checks performed on the generated assets:

- desktop-width raster inspection at the 920-pixel native content width;
- mobile-width raster inspection at 375 CSS pixels;
- GitHub-light and GitHub-dark page-background composites;
- grayscale/monochrome inspection;
- text, arrow direction, alignment, and clipping inspection;
- SVG parse validation;
- text/accent contrast checks on the neutral canvas (`17.06:1` primary text, `7.24:1` secondary text, `6.41:1` foundation blue);
- no `<image>` elements or raster data URLs;
- no credentials, usernames, hostnames, local paths, LAN addresses, certificates, or unrelated data in exported assets.

Result: both SVGs pass the implementation-stage light, dark, desktop, mobile, monochrome, and privacy checks. Human visual approval remains pending.

## Human workflow decision — proceed to Step 6 with deferred visual refinement

Human maintainer decision recorded on 29 August 2026:

- the implemented Visual 1 and Visual 3 are **sufficient for README drafting and layout work**;
- they are **not yet accepted as publication-final visual design**;
- publication-level visual refinement is intentionally deferred until after the Step 6 README draft exists;
- `Human approval: APPROVED` is **not** granted at this stage and remains pending;
- Visual 2 remains absent/pending authentic deterministic capture and must not be replaced by synthetic evidence;
- Step 6 may reference the current Visual 1 and Visual 3 as working assets and must remain structurally valid if Visual 2 is absent;
- later visual refinement may change composition, typography, spacing, hierarchy, and aesthetic treatment without reopening Step 4 or Step 5b, provided the validated technical semantics and evidence boundaries in `SNode.C/workflow/05-VISUALS.md` are preserved;
- final publication still requires human visual approval of the refined assets.

This is an explicit maintainer-authorized workflow deviation from the normal human-approval gate between Step 5 and Step 6. It authorizes README drafting only; it does not approve the current visuals for publication.
