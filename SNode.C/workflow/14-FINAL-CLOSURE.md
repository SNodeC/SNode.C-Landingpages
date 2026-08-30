# Step 14 — Final closure and publication consistency

## Scope

This is a closure pass only. It does not redesign the approved SNode.C README,
reopen its information architecture, or broaden the publication workflow.

Starting repository state:

- `SNodeC/SNode.C-Landingpages` `main`:
  `0d695564d978f4de54d8410d8d7cc8ae69667196`
- public `SNodeC/snode.c` `master`:
  `60f26d9ae54b3e9ffde954d0ca75e53f79f31d79`

Both heads were rechecked immediately before the final closure materialization
and were unchanged.

## Echo walkthrough synchronization

The README quick start now follows current public `examples/echo/`, which is a
complete standalone CMake consumer of an installed SNode.C package.

The publication now shows the actual downstream contract:

```cmake
find_package(snodec REQUIRED COMPONENTS net-in-stream-legacy)
```

with `snodec::net-in-stream-legacy`, concrete
`net::in::stream::legacy::{SocketServer,SocketClient}` use, installed public
`<...>` includes, the external build/run paths, semantic application log output,
and the example's CTest entry point.

The previous quick-start-specific in-tree `NET` macro explanation and
`CHECK_INCLUDES=OFF`/IWYU detail are removed because they are superseded by the
external installed-package example.

### Current CI evidence boundary

At exact public `master` `60f26d9`, the observed `gcc-debug` job:

- builds SNode.C successfully;
- passes the main repository CTest suite: **181/181**;
- installs SNode.C to a staging prefix;
- configures and builds the standalone `examples/echo` project against that
  installed package;
- then fails the four external-example CTests because the built executables
  cannot locate `libsnodec-net-in-stream.so.2` from the staging prefix at
  runtime.

The README and capability/evidence records therefore distinguish **CTest
integration and invocation** from **a passing exact-head external-example test
run**. No passing claim is made for those four tests.

The earlier IPv6, Unix-domain, and mutual-TLS IPv4 runtime runs remain recorded
against the preceding qualified source baseline. A compare from that baseline
(`bf01683`) to current `60f26d9` changes CI, the external echo example and its
documentation/tests, and semantic echo logging; it does not change the transport,
HTTP, WebSocket, SSE, MQTT, configuration, or event-runtime implementations that
support the existing publication claims. Those earlier runs are preserved as
historical qualification, not presented as current-master reruns.

## Navigation and captions

The README's `Choose your next step` table now includes a direct generated
Doxygen/API-reference route:

`https://snodec.github.io/snode.c-doc/html/index.html`

The programming-model figure now has a meaningful caption, and the
HTTP→WebSocket figure caption uses the same `<sub>` caption convention as the
architecture/configuration documentation.

## Figma-only figure corrections

The maintainer required all figure updates to occur through Figma. No repository
SVG was hand-edited to implement a visual correction.

Authoritative Figma file:

`giz3MDZrdwPx71L2HhiQdg` — **SNode.C Publication Figures**

Claude's two clearance reports were reproduced directly against the Figma
frames and both were confirmed:

1. **HTTP → WebSocket desktop** (`7:36`): `SocketContextUpgrade` (`7:46`) used a
   22 px bold label only 6 px from the right edge of its state card. Minimal
   correction in Figma: 22 px → 21 px, increasing right clearance to 17 px.
2. **Programming model mobile** (`1:4`): the event-loop detail (`3:42`) used a
   12 px local left inset while the rail title and established figure spacing
   use 20 px. Minimal correction in Figma: local x 12 → 20.

Both corrected Figma frames were re-rendered and visually inspected. No redesign,
content change, or unrelated geometry change was made.

Repository materialization was generated from the corrected/current Figma nodes
through the Figma Plugin API's live-text SVG export, with only publication
portability normalization performed in that Figma export pipeline: root intrinsic
width/height are omitted, accessibility title/description are inserted, and the
existing portable system/generic font stack is used. The corrected publication
SVG and its `assets/src/` counterpart share the same Git blob.

## Figma provenance and dimensions

Current source-of-truth frames are:

| Figure | Desktop | Mobile |
| --- | --- | --- |
| Programming model | `1:3` — 1200×720 | `1:4` — 620×980 |
| HTTP → WebSocket | `7:36` — 1200×820 | `7:37` — 620×1320 |
| Architecture | `7:123` — 1200×760 | `7:124` — 620×1210 |
| Configuration | `7:217` — 1200×700 | `7:218` — 620×1120 |

`09-FIGMA-RESPONSIVE-FIGURES.md` is refreshed to these current dimensions. In
particular, the stale architecture-mobile 620×1180 entry is corrected to
620×1210. Older dimensions in historical Step 8/8c prose remain historical
records rather than current source-of-truth metadata.

The previously missing desktop repository-side source/export counterparts are
restored from Figma:

- `SNode.C/assets/src/layer-architecture.svg`
- `SNode.C/assets/src/configuration-model.svg`

Figma remains the editable source. Repository `assets/src/` files are provenance
and export counterparts, not an authorization to edit figures outside Figma.

## Validation

Closure validation performed:

- verified Landingpages `main` and public SNode.C `master` before materialization;
- compared public SNode.C `bf01683..60f26d9` and reviewed every changed path;
- inspected exact current external echo CMake, installed includes, server/client
  aliases, semantic logging, README, tests, and public CI logs;
- confirmed main exact-head CTest result 181/181 and preserved the separate
  external-example 0/4 loader-path failure boundary;
- visually reproduced both reported figure-clearance issues in Figma before
  changing anything;
- made and visually rechecked only the two minimal Figma spacing corrections;
- re-established the eight Figma source-of-truth dimensions;
- restored desktop architecture/configuration source counterparts from Figma;
- retained the 12-file public dependency closure; source counterparts and
  workflow/evidence files remain non-public support artifacts;
- checked that the new API route resolves to the existing SNode.C Doxygen site;
- retained self-contained SVG requirements: no script, foreign object, external
  image/font resource, raster payload, private path, credential, or editor
  metadata is introduced by the Figma materialization;
- reviewed Markdown/code-fence/table structure and all newly introduced relative
  paths against the repository tree.

A native checkout could not be obtained in this execution environment because
outbound DNS to GitHub is blocked. Therefore a literal local `git diff --check`
and repository-local rendering script invocation cannot be claimed from this
session. The final candidate is instead validated through the GitHub Git-data
compare/tree APIs plus Figma-native visual inspection. This is an operational
validation limitation, not an omitted publication issue.

## Closure verdict

The SNode.C Landingpages publication is closed with the requested consistency
corrections. No README redesign or structural reopening was performed.

One upstream issue remains outside the Landingpages publication package: current
public SNode.C CI does not yet provide a green runtime result for the four new
external echo CTests because of the staged shared-library loader path. The
publication records that boundary explicitly and makes no stronger claim.
