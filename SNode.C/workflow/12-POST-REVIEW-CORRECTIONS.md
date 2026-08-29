# Step 12 — Post-review corrections

## Baselines

- Landingpages input baseline (`main`): `74ab8756b3c072141759773ab7bf9c745731f2a5`.
- Qualified SNode.C source baseline: `bf01683a53b48220a840522e8ccaf3b48e58c240`.
- Source-baseline freshness was rechecked before closure: upstream `SNodeC/snode.c` `master` still pointed to that exact SHA.
- The requested `SNode.C/workflow/11-INDEPENDENT-PUBLICATION-REVIEW.md` was not present in the input `main`, in the workflow directory, or in repository search. Step 12 therefore applied only the concrete Step 11 findings and Appendix-D no-change decisions repeated in the Step 12 brief; any Step 11 finding not repeated there remains unassessed.

## Step 11 disposition

### Accepted and applied

- Replaced the reintroduced three-column capability table with a vertical Markdown fit-check while preserving the available/exercised distinction and all existing evidence boundaries.
- Restored the upstream M2M/IoT design-focus context near the opening without implying platform, hardware, embedded, OpenWrt, or production qualification.
- Simplified the echo commands after confirming that information-level (`4`) text logging is already the default under an isolated configuration root.
- Explained `legacy` as the plain/non-TLS stream variant and `CHECK_INCLUDES=OFF` as excluding the optional IWYU include-analysis pass when IWYU is installed.
- Marked the echo source excerpt as abridged with `(logging omitted)`.
- Clarified that the deeper capability map also covers optional components and tooling.
- Reproduced the SVG font-fit concern in a current Linux/Chrome environment before deciding whether to modify assets.

### Rejected after qualification

- The proposed public option spelling `--log-origin-level application=trace` was not adopted: the exact echo binaries reject `application=trace` as an unexpected argument before startup.
- No SVG geometry or text-width change was made because the reported clipping/overflow was not reproduced in the representative browser/font-fallback test.

### Preserved no-change decisions

No structural rewrite, additional README figure, echo screenshot, capability expansion, removal of the image-disabled HTTP→WebSocket explanation, weakened evidence boundary, unsupported performance/platform/security claim, cosmetic Figma redesign, or live `SNodeC/snode.c` modification was made.

### Deferred

Any Step 11 finding not reproduced in the Step 12 brief is deferred because the claimed Step 11 artifact is absent from the authoritative input repository.

## README corrections

The reader journey remains unchanged: orientation/value → programming model → real code → verified echo run → capability fit-check → architecture/context replacement → next routes.

The public README now contains the restrained M2M/IoT purpose statement, the abridged-code note, the simplified default-logging echo commands, short explanations of `legacy` and `CHECK_INCLUDES`, the vertical capability fit-check, and the optional-component/tooling route to `docs/capabilities.md`.

## Echo trace qualification

Qualification used the exact source SHA, Release configuration, `CHECK_INCLUDES=OFF`, and the validated `echoserver-legacy-in` / `echoclient-legacy-in` pair on IPv4 loopback. A separate default-vs-explicit run confirmed that omitting `--log-level 4 --log-format text` retains information-level text output when `XDG_CONFIG_HOME` points to the fresh isolated configuration root. The source spelling `--monochrom` was also confirmed.

Exact scoped-trace server form tested:

```sh
XDG_CONFIG_HOME=/tmp/snodec-echo-empty-config \
  ./build/src/apps/echo/echoserver-legacy-in \
  --log-level 4 --log-format text --monochrom=true \
  --log-origin-level application=trace \
  echoserver local --host 127.0.0.1 --port 18001
```

The client was tested analogously with `echoclient-legacy-in` and `echoclient remote`.

Both exact commands terminated before endpoint startup with:

```text
The following argument was not expected: application=trace

Append -h or --help to your command line for more information.
```

Therefore payload visibility, framework-log level retention, and echo-loop trace volume are not applicable to the exact proposal: no connection is created. Scoped application trace was **not adopted**. The README retains the information-level run and one concise factual payload caveat; global trace logging was not substituted.

## SVG font-fit reproduction

Test environment: Ubuntu 24.04, Google Chrome 151.0.7922.173. `Segoe UI` and generic sans-serif resolved to DejaVu Sans in the runner, reproducing the relevant Linux fallback concern.

All flagged labels stayed inside their intended geometry:

- desktop `own SocketContextFactory`: right edge ~517/1113 px vs 525.5/1121.5 px boundaries;
- desktop long `create(this)` label: ~828 px vs 849 px boundary;
- mobile `own SocketContextFactory`: ~538 px vs 561.5 px boundary;
- mobile long `create(this)` label: ~445 px vs 585 px boundary;
- desktop `101 Switching Protocols prepared`: ~377 px vs 381 px boundary;
- mobile `101 Switching Protocols prepared`: ~431 px vs 585 px boundary.

The concern was investigated and not reproduced; **no SVG was changed**.

## Browser/mobile validation

Current GitHub rendering was reviewed in Chrome against the candidate commit:

- 390 × 844 viewport: visible README Markdown width 324 px, `scrollWidth == clientWidth`, no page-level horizontal overflow;
- 375 × 844 supplemental viewport: visible README Markdown width exactly 309 px, reproducing the previous narrow-content condition with no page-level overflow;
- responsive `<picture>` selection chose `programming-model-mobile.svg` and `http-websocket-context-switch-mobile.svg` on mobile and the desktop variants at 1440 px;
- command blocks use horizontal scrolling where needed rather than widening the page;
- the capability section renders as the intended vertical list with no reintroduced capability table;
- 1440 × 1000 desktop regression view had no README overflow;
- `docs/architecture.md` selected `layer-architecture-mobile.svg` and `http-websocket-context-switch-mobile.svg` at mobile width;
- `docs/configuration.md` selected `configuration-model-mobile.svg` at mobile width;
- full-page screenshot review found no figure clipping and no problem in first-viewport orientation, text/figure rhythm, capability readability, command-block behavior, or final routes.

## Publication dependency closure

Recursive local dependency validation closes on exactly the intended 12-file public package:

- `README.md`
- `docs/architecture.md`
- `docs/configuration.md`
- `docs/capabilities.md`
- `assets/programming-model.svg`
- `assets/programming-model-mobile.svg`
- `assets/http-websocket-context-switch.svg`
- `assets/http-websocket-context-switch-mobile.svg`
- `assets/layer-architecture.svg`
- `assets/layer-architecture-mobile.svg`
- `assets/configuration-model.svg`
- `assets/configuration-model-mobile.svg`

No workflow artifact, `EVIDENCE.md`, historical echo image, Figma metadata, or internal implementation file is a public dependency. Relative link/image resolution, Markdown heading/anchor checks, responsive references, stale/internal-link scans, and `git diff --check` passed. The final README was reread against Steps 3 and 7; no unsupported technical claim was introduced.

## Files changed

- `SNode.C/README.md`
- `SNode.C/workflow/12-POST-REVIEW-CORRECTIONS.md`

No publication SVG changed.

## Remaining concern and readiness

The publication package itself passes the targeted corrections, source freshness, dependency closure, and browser/mobile validation and is content-ready for maintainer review. The canonical review trail is incomplete because `SNode.C/workflow/11-INDEPENDENT-PUBLICATION-REVIEW.md`, which the Step 12 brief states was committed, is absent from the authoritative Landingpages baseline. Restore that artifact before final maintainer publication approval so Step 12 can be audited against the complete independent review.