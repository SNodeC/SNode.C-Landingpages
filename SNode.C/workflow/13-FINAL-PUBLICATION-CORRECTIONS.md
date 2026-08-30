# Step 13 — Final publication corrections

## Inputs

- Landingpages starting `main`: `7e135db68acd9a2066743a1fb2fefda8d06d36cb`.
- Qualified SNode.C source baseline: `bf01683a53b48220a840522e8ccaf3b48e58c240`.
- Upstream `SNodeC/snode.c` `master` was rechecked before editing and still pointed to the qualified SHA.
- Governing prior records: Steps 3, 7, 8, 9, 10, and 12 plus repository governance and `assets/src/IMPLEMENTATION.md`.
- Triggering post-review findings: Step 9 Figma mobile exports had lost the Step 8c ~10 CSS px readability floor at the measured 309 px GitHub article width; `docs/configuration.md` used the wrong echo instance name; the release sentence did not name `v1.0.2`; the README lacked one concrete composition example; SVG intrinsic dimensions required investigation.

## Figma correction

Authoritative Figma file: `giz3MDZrdwPx71L2HhiQdg`.

| Figure | Figma node | Minimum informative size before | ~309 px equivalent before | Minimum after | ~309 px equivalent after | Layout disposition |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| Programming model mobile | `1:4` | 16 | 7.97 px | 20.25 | 10.09 px | Two `own SocketContextFactory` chips widened to 310 design units; semantics unchanged. |
| HTTP → WebSocket mobile | `7:37` | 15 | 7.48 px | 20.25 | 10.09 px | Typography only; chronology and semantics unchanged. |
| Architecture mobile | `7:124` | 16 | 7.97 px | 20.25 | 10.09 px | Typography only; current authoritative Figma frame is 620×1210; semantics unchanged. |
| Configuration mobile | `7:218` | 15 | 7.48 px | 20.25 | 10.09 px | Typography only; precedence/instance semantics unchanged. |

The correction was made in Figma first. All informative text below 20.25 design units was raised to 20.25 rather than applying a blanket font rewrite. The four frames were visually inspected after correction. The only required geometry adjustment was the pair of programming-model factory chips.

## SVG materialization

The corrected Figma frames were exported through the Figma plugin API as live-text SVG and materialized into the repository using the established system-font fallback and accessible title/description conventions. Each public mobile SVG remains byte-identical to its `assets/src/` maintained source counterpart.

Re-exported pairs:

- `assets/programming-model-mobile.svg` and `assets/src/programming-model-mobile.svg` — `viewBox="0 0 620 980"`.
- `assets/http-websocket-context-switch-mobile.svg` and `assets/src/http-websocket-context-switch-mobile.svg` — `viewBox="0 0 620 1320"`.
- `assets/layer-architecture-mobile.svg` and `assets/src/layer-architecture-mobile.svg` — `viewBox="0 0 620 1210"`.
- `assets/configuration-model-mobile.svg` and `assets/src/configuration-model-mobile.svg` — `viewBox="0 0 620 1120"`.

### Intrinsic `width` / `height` decision

**No change.** Chrome 151 on Ubuntu 24.04 was used to compare the same corrected SVG with and without explicit `width="620" height="980"` under responsive `img { max-width: 100%; height: auto; }` behavior.

- At a 309 px container, both variants rendered at ~308.98 px wide.
- At an 800 px container, the viewBox-only variant filled ~799.98 px while the explicit-dimension variant stopped at 620 px.

Explicit intrinsic dimensions therefore provide no mobile benefit and would unnecessarily constrain responsive desktop sizing. All eight publication SVG roots remain viewBox-only.

## Content corrections

### Echo instance command

**Accepted.** Exact source `src/apps/echo/model/servers.h` constructs the server as `EchoSocketServer("echoserver")`. The public configuration example is corrected from:

```text
echoserver-legacy-in echo local ...
```

to:

```text
echoserver-legacy-in echoserver local --host 127.0.0.1 --port 18001
```

### Release wording

**Accepted.** GitHub's latest-release endpoint still reports `v1.0.2`. The README now names `v1.0.2` explicitly while preserving the established boundary that reviewed `master` is newer and is not represented by a current tagged 2.0 release or current-head binary package.

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

### Repository-native

PASS:

- `git diff --check` against the Step 13 input baseline;
- recursive relative publication dependency closure;
- local Markdown link resolution;
- heading/fragment validation;
- public/internal dependency separation;
- SVG XML parsing;
- all four corrected mobile SVGs have a 20.25-unit minimum informative font size;
- each mobile publication SVG is byte-identical to its `assets/src` counterpart.

The recursive public dependency closure remains exactly **12 files**: README, three public docs, four desktop SVGs, and four mobile SVGs. No workflow record, `EVIDENCE.md`, `assets/src`, historical echo image, or Figma metadata became a public dependency.

### Browser/mobile

Environment: Ubuntu 24.04, Google Chrome 151.0.7922.173, actual GitHub rendering of the Step 13 candidate.

- 375×844 viewport: visible README article width exactly 309 px; `scrollWidth == clientWidth == 309`; no article overflow.
- Corrected mobile image width at that condition: ~308.98 px.
- Minimum informative mobile text at that condition: **10.092 CSS px** for all four corrected figures.
- 390×844 viewport: visible article width 324 px; minimum corrected text **10.582 CSS px**; no overflow.
- Responsive `<picture>` selection chose the mobile SVGs on the mobile README and deeper pages.
- 1440×1000 README view selected desktop SVGs; no mobile source was selected and no article overflow occurred.
- Mobile command blocks retain horizontal scrolling instead of widening the article.
- `docs/architecture.md` at 375 px selected the corrected architecture and HTTP→WebSocket mobile figures with no article overflow.
- `docs/configuration.md` at 375 px selected the corrected configuration mobile figure with no article overflow.
- Full-page screenshots of README, architecture, and configuration were visually inspected; no figure clipping, label collision, or responsive regression was found.

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

Desktop SVGs and `assets/src/IMPLEMENTATION.md` did not require changes. Temporary validation workflows and browser artifacts are not part of the final tree.

## Verdict

All Step 13 correction gates pass. The Figma mobile source-of-truth is corrected, the repository exports preserve that correction, the three factual/content improvements are source-backed, explicit SVG dimensions were tested and rejected for demonstrated responsive reasons, and the final public dependency closure remains atomic.

**SNode.C is ready for final maintainer publication approval.**
