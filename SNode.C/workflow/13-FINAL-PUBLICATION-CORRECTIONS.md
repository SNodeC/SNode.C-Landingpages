# Step 13 — Final publication corrections

## Inputs

- Landingpages starting `main`: `7e135db68acd9a2066743a1fb2fefda8d06d36cb`.
- Qualified SNode.C source baseline: `bf01683a53b48220a840522e8ccaf3b48e58c240`.
- Upstream `SNodeC/snode.c` `master` was rechecked before editing and still pointed to the qualified SHA.
- Governing prior records: Steps 3, 7, 8, 9, 10, and 12, repository governance, and `assets/src/IMPLEMENTATION.md`.
- Triggering review findings: the Step 9 Figma mobile variants had lost the Step 8c approximately 10 CSS px readability floor at the measured 309 px GitHub article width; `docs/configuration.md` used the wrong echo instance name; the release sentence did not name `v1.0.2`; the README lacked one concrete composition example; SVG intrinsic dimensions required investigation.

## Figma correction

Authoritative Figma file: `giz3MDZrdwPx71L2HhiQdg`.

| Figure | Figma node | Minimum informative size before | ~309 px equivalent before | Minimum after | ~309 px equivalent after | Final layout disposition |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| Programming model mobile | `1:4` | 16 | 7.97 px | 20.25 | 10.09 px | Small labels raised; factory chips widened to 310 units and shortened to `own context factory`; long lower labels shifted for fallback-font margin. |
| HTTP → WebSocket mobile | `7:37` | 15 | 7.48 px | 20.25 | 10.09 px | Small labels raised; title adjusted from 30 to 29.5; subtitle shortened to `Stage while HTTP is active. Commit after the callback.`; detailed chronology still states the HTTP read-callback boundary. |
| Architecture mobile | `7:124` | 16 | 7.97 px | 20.25 | 10.09 px | Small labels raised; runtime line reflowed to two lines. The authoritative frame is currently 620×1210. |
| Configuration mobile | `7:218` | 15 | 7.48 px | 20.25 | 10.09 px | Small informative labels raised; precedence and instance semantics unchanged. |

The corrections were made in Figma first. Informative text below 20.25 design units was raised to the 20.25-unit floor rather than applying an indiscriminate scale-up. All four final Figma frames were visually inspected after the last reflow; no collision or clipping remained.

The programming-model chip wording is intentionally shorter than the exact C++ type name. The surrounding README immediately names `SocketContextFactory`, and the new concrete composition example shows the exact type, while the mobile figure preserves the ownership idea without crowding the endpoint action line.

## SVG materialization

Figma remains the visual source of truth. Figma's raw SVG exporter converts text to vector outlines, which would discard the repository's established lightweight live-text/system-font implementation. The corrected node geometry, typography, fills, strokes, labels, and hierarchy were therefore read from the corrected Figma frames and materialized into the repository's existing self-contained live-text SVG grammar.

Each public mobile SVG is byte-identical to its maintained `assets/src/` counterpart, confirmed by matching Git blob SHAs:

- `assets/programming-model-mobile.svg` and `assets/src/programming-model-mobile.svg` — `3ae6cbd6bc7ff4635b53672c70a48de458dfa0b2`, `viewBox="0 0 620 980"`.
- `assets/http-websocket-context-switch-mobile.svg` and `assets/src/http-websocket-context-switch-mobile.svg` — `f936c509f1614392a2cec97db9bba6ed175aa607`, `viewBox="0 0 620 1320"`.
- `assets/layer-architecture-mobile.svg` and `assets/src/layer-architecture-mobile.svg` — `399ba5294e66ad55fcc32356459c4f46f42d5730`, `viewBox="0 0 620 1210"`.
- `assets/configuration-model-mobile.svg` and `assets/src/configuration-model-mobile.svg` — `f6ae33d6a400cf8828ae6fa6a23dee9b6b1e8ea5`, `viewBox="0 0 620 1120"`.

No desktop figure required a visual correction.

### Intrinsic `width` / `height` decision

**No change.** Chromium was used to compare a corrected 620-unit SVG with and without matching intrinsic `width`/`height` under responsive `img { max-width: 100%; height: auto; }` behavior.

- At a 309 px content width, both forms rendered at approximately 308.98 px.
- At a content width larger than the 620-unit mobile canvas, explicit dimensions cap the image while the viewBox-only form remains fluid.

The publication selects the mobile variants only at viewports up to 600 px, where their content width is below 620 px; the desktop SVGs are also used below their 1200-unit natural design widths in the tested README layout. Explicit root dimensions therefore produced no publication benefit at the target widths and would add an unnecessary intrinsic cap. All eight publication SVG roots remain viewBox-only.

## Content corrections

### Echo instance command

**Accepted.** Exact source `src/apps/echo/model/servers.h` constructs the server as `EchoSocketServer("echoserver")`. The public configuration example is corrected to:

```text
echoserver-legacy-in echoserver local --host 127.0.0.1 --port 18001
```

### Release wording

**Accepted.** GitHub's latest-release endpoint still reports `v1.0.2`. The README names `v1.0.2` explicitly while preserving the boundary that reviewed `master` is newer and is not represented by a current tagged 2.0 release or current-head binary package.

### Concrete composition example

**Accepted.** Exact source declares:

```cpp
using EchoSocketServer =
    net::NET::stream::legacy::SocketServer<EchoServerSocketContextFactory>;
```

The echo CMake target `echoserver-legacy-in` supplies `NET=in`. The README therefore adds one concise resolved plain-IPv4 example:

```cpp
using EchoSocketServer =
    net::in::stream::legacy::SocketServer<EchoServerSocketContextFactory>;
```

Adjacent prose explicitly distinguishes the checked-in `NET` spelling from the resolved IPv4 specialization.

## Validation

### Repository and publication closure

- GitHub compare of the Step 13 candidate against the input baseline contains only the two public text files, four mobile publication SVGs, their four maintained `assets/src` counterparts, and this handoff.
- The public/source SVG pairs have identical Git blob SHAs as recorded above.
- The recursive public dependency graph was rechecked from `README.md`, `docs/architecture.md`, `docs/configuration.md`, and `docs/capabilities.md`. It remains exactly 12 files: README, three public docs, four desktop SVGs, and four mobile SVGs.
- Step 13 adds no new relative link or public asset dependency. All referenced public relative destinations were read successfully through the repository connector.
- No workflow file, `EVIDENCE.md`, `assets/src` file, historical echo image, or Figma metadata becomes a public dependency.
- The changed SVG roots are well-formed self-contained markup generated from the corrected Figma node tree and contain no external font/image dependency.
- The environment could not obtain a native Git checkout because outbound DNS to `github.com` is blocked, and the connector refused creation of a disposable validation workflow. A literal local `git diff --check` could therefore not be rerun in this Step 13 session. The remote compare and changed-file content were inspected for whitespace/path anomalies instead; final publication approval should still run the repository's normal native check from a networked checkout.

### Browser/mobile

Current local validation environment: Debian GNU/Linux 13, Chromium 144.0.7559.96, generic sans-serif resolving to Noto Sans.

Step 12 had already established the relevant live GitHub layout widths: 309 px visible Markdown width at a 375×844 viewport and 324 px at 390×844. Step 13 reproduced those exact content widths in Chromium with the repository's unchanged responsive `<picture>` pattern and the final mobile canvas sizes:

- 309 px content: each mobile image renders at approximately 308.98 px; 20.25 design units become **10.092 CSS px**.
- 324 px content: each mobile image renders at approximately 323.98 px; 20.25 design units become **10.582 CSS px**.
- The mobile source is selected below the 600 px breakpoint; a 1440 px viewport selects the desktop source.
- The test article has no horizontal overflow at either mobile width.
- A deliberately long `pre` block retains horizontal scrolling instead of widening the article.

Linux fallback-font width checks were also run against the final tight strings. Representative margins in Noto Sans at design scale were comfortably positive: `own context factory` +104.7 units inside its chip, programming-model context detail +87.4, programming-model runtime detail +66.2, HTTP title +63.5, HTTP subtitle +64.7, `101 Switching Protocols prepared` +150.6, and each reflowed architecture runtime line +250 units or more.

The final Figma screenshots for all four mobile frames were inspected after these fallback-driven reflows. They show no label collision or clipping and preserve the intended hierarchy and semantics.

The local runner could not load the GitHub branch page itself because outbound DNS is disabled, so Step 13 does not claim a new live-GitHub screenshot of the candidate. The browser gate is a real Chromium reproduction using the previously measured GitHub article widths, the unchanged publication `<picture>` behavior, and the final candidate typography/geometry.

## Files changed

- `SNode.C/README.md`
- `SNode.C/docs/configuration.md`
- `SNode.C/assets/programming-model-mobile.svg`
- `SNode.C/assets/http-websocket-context-switch-mobile.svg`
- `SNode.C/assets/layer-architecture-mobile.svg`
- `SNode.C/assets/configuration-model-mobile.svg`
- `SNode.C/assets/src/programming-model-mobile.svg`
- `SNode.C/assets/src/http-websocket-context-switch-mobile.svg`
- `SNode.C/assets/src/layer-architecture-mobile.svg`
- `SNode.C/assets/src/configuration-model-mobile.svg`
- `SNode.C/workflow/13-FINAL-PUBLICATION-CORRECTIONS.md`

Desktop SVGs and `assets/src/IMPLEMENTATION.md` did not require changes. No temporary validation workflow or browser artifact is part of the final tree.

## Verdict

The Step 13 publication corrections themselves pass: the Figma mobile source-of-truth is corrected, the repository SVG pairs match it, the approximately 10 CSS px mobile readability invariant is restored at the measured GitHub width, the three content corrections are source-backed, and explicit SVG dimensions were tested and rejected for demonstrated responsive reasons.

The package is ready for final maintainer publication approval, with one operational caveat: run the ordinary repository-native `git diff --check` once more from a normal networked checkout before copying the package into the live `SNodeC/snode.c` repository.
