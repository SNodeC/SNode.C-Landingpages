# SNode.C Step 8 — publication readiness

**Publication-readiness date:** 29 August 2026
**Validated SNode.C source baseline:** `bf01683a53b48220a840522e8ccaf3b48e58c240`
**Landingpages input revision:** `b81c8450398251a6ecc0ad586655489652e0de6f`
**Scope:** final non-human preparation before browser-based publication review and explicit maintainer approval

Step 8 preserves the Step 7c reader journey and public claim boundaries. It does
not authorize or perform publication to the live `SNodeC/snode.c` repository.

# Publication package

The publication package was derived recursively from the intended destination
entry point rather than from a hand-maintained asset list. Markdown inline
links/images, reference-style definitions, HTML `href`/`src`, and SVG
`href`/`xlink:href` references were extracted and resolved repeatedly until no
new local dependency appeared.

The fixed-point production closure contains **8 files**:

| Landingpages source path | Eventual `SNodeC/snode.c` destination | Purpose |
| --- | --- | --- |
| `SNode.C/README.md` | `README.md` | Public repository entry point |
| `SNode.C/docs/architecture.md` | `docs/architecture.md` | Deeper architecture, lifecycle, and extension-point guide |
| `SNode.C/docs/configuration.md` | `docs/configuration.md` | Named-instance and configuration guide |
| `SNode.C/docs/capabilities.md` | `docs/capabilities.md` | Scoped capability/evidence map without internal workflow dependency |
| `SNode.C/assets/programming-model.svg` | `assets/programming-model.svg` | Principal programming-model figure |
| `SNode.C/assets/http-websocket-context-switch.svg` | `assets/http-websocket-context-switch.svg` | Principal context-replacement figure, also reused by the architecture guide |
| `SNode.C/assets/layer-architecture.svg` | `assets/layer-architecture.svg` | Transitive architecture-composition figure |
| `SNode.C/assets/configuration-model.svg` | `assets/configuration-model.svg` | Transitive configuration-model figure |

Editable SVG sources, workflow records, `EVIDENCE.md`, historical assets, capture
scripts, and social-preview material are intentionally **not** part of this
production dependency closure.

The package was copied to an untracked temporary staging tree outside the
Landingpages repository, with `SNode.C/` removed so that the staging root mirrors
the eventual `SNodeC/snode.c` root. Validation was then repeated against that
staged destination layout.

# Visual status

| Visual | Final path | Editable/source path | Semantic validation | Render validation | Human approval |
| --- | --- | --- | --- | --- | --- |
| Programming model | `assets/programming-model.svg` | `SNode.C/assets/src/programming-model.svg` | PASS — all 13 Step 8 semantics | PASS — desktop/mobile, light/dark surround, grayscale, contrast, portability, privacy | **PENDING** |
| Echo connection evidence | **ABSENT** | No validated `assets/src/echo-capture/` set exists | PASS — authoritative omission decision; no synthetic/historical substitute | N/A — no publication asset | No asset to approve; overall publication approval remains **PENDING** |
| HTTP → WebSocket context replacement | `assets/http-websocket-context-switch.svg` | `SNode.C/assets/src/http-websocket-context-switch.svg` | PASS — all 13 chronological semantics, with secondary exact detail also preserved in public prose | PASS — desktop/mobile, light/dark surround, grayscale, contrast, portability, privacy | **PENDING** |
| Architecture composition | `assets/layer-architecture.svg` | Existing public SVG is its maintained source for this pass | PASS — no stale/publication-inappropriate technical claim found | PASS — responsive render and portability/privacy inspection | Covered by overall human publication review; older style is non-blocking cosmetic debt |
| Configuration model | `assets/configuration-model.svg` | Existing public SVG is its maintained source for this pass | PASS — configuration surfaces/precedence remain consistent with reviewed docs | PASS — responsive render and portability/privacy inspection | Covered by overall human publication review; older style is non-blocking cosmetic debt |

The historical `assets/protocol-upgrade.svg` was audited but is no longer a
publication dependency. Its simplified direct factory-to-attach story is less
precise than the validated staged replacement chronology. Rather than redesign
that historical asset, `docs/architecture.md` now uses the refined principal
`http-websocket-context-switch.svg`.

## Visual 2 decision

Visual 2 cannot be produced authentically in this round because the committed
Landingpages tree contains neither the required raw `assets/src/echo-capture/`
provenance set nor a publication-final `echo-connection-evidence.png`. The
available historical `echo-terminal.png` is explicitly not an approved
substitute. The execution environment for this pass also does not contain an
exact-revision SNode.C checkout and built echo pair from which a fresh genuine
capture could be produced.

No terminal output was synthesized, redrawn, normalized, relabeled, or copied
from the historical image. A future pass requires the exact-revision run, raw
server/client screenshots and verbatim transcripts, reproduction metadata, and
deterministic composition material specified in `workflow/05-VISUALS.md`, then
the documented rendered-width and privacy validation.

# Link audit

The mechanical closure/audit performed against the staged destination layout
reported:

- **8** files in the fixed-point production closure;
- **26** local dependency/link edges;
- **3** validated local Markdown fragment references;
- **38** external-link occurrences, represented by **35** distinct
  origin/target records;
- **0** missing local files;
- **0** path-casing mismatches;
- **0** broken local Markdown anchors;
- **0** staged-layout resolution errors;
- **0** SVG dependency/portability errors;
- **0** public references to `EVIDENCE.md`, workflow paths, the historical echo
  asset, or a nonexistent Visual-2 publication asset.

Local validation applies to the **destination layout**, not merely to the
Landingpages source layout. External links remain ordinary public routes or
exact-source anchors already used by the reviewed public documents; Step 8 does
not promote the generated API reference to current-fact authority.

## External links by publication file

### `README.md`

- `https://github.com/SNodeC/snode.c`
- `https://github.com/SNodeC/snode.c/blob/master/LICENSE`
- `https://github.com/SNodeC/snode.c/tree/master/src/apps`
- `https://github.com/SNodeC/snode.c/commit/bf01683a53b48220a840522e8ccaf3b48e58c240`
- `https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/apps/echo/model/EchoSocketContext.cpp`
- `https://github.com/SNodeC/snode.c/issues`
- `https://github.com/SNodeC/snode.c/discussions`
- `https://github.com/SNodeC/snode.c/releases`
- `https://github.com/SNodeC/mqttsuite`
- `https://github.com/SNodeC/AISuite`
- `https://github.com/SNodeC/CodexUI`

### `docs/architecture.md`

- `https://snodec.github.io/snode.c-doc/html/index.html`
- `https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/EventLoop.h`
- `https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/EventMultiplexer.h`
- `https://github.com/SNodeC/snode.c/tree/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/multiplexer`
- `https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketConnection.h`
- `https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketContext.h`
- `https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/net/config/ConfigConnection.h`
- `https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/core/socket/stream/SocketContextFactory.h`
- `https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/apps/echo/model/EchoSocketContext.h`
- `https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/apps/echo/model/EchoSocketContext.cpp`
- `https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/web/http/SocketContextUpgradeFactory.h`
- `https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/web/http/server/Response.cpp`
- `https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/web/websocket/SocketContextUpgrade.h`

### `docs/configuration.md`

- `https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/net/config/ConfigInstance.h`
- `https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/net/config/ConfigConnection.h`
- `https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/net/config/ConfigPhysicalSocket.h`
- `https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/net/config/ConfigTls.h`
- `https://github.com/SNodeC/snode.c/blob/bf01683a53b48220a840522e8ccaf3b48e58c240/src/utils/Config.cpp`

### `docs/capabilities.md`

- `https://github.com/SNodeC/snode.c`
- `https://github.com/SNodeC/snode.c/commit/bf01683a53b48220a840522e8ccaf3b48e58c240`
- `https://snodec.github.io/snode.c-doc/html/index.html`
- `https://github.com/SNodeC/snode.c/issues`
- `https://github.com/SNodeC/snode.c/discussions`
- `https://github.com/SNodeC/snode.c/releases`

# Evidence/publication cleanup

`docs/capabilities.md` is now self-contained for publication and no longer links
to `../EVIDENCE.md`. Its public factual content remains within the established
Step 3/7 evidence boundaries; the edit removes internal workflow vocabulary and
the publication dependency rather than adding a new capability claim.

`EVIDENCE.md` remains an internal historical record and is not copied to the
production package. Its old Visual-2 statements were not deleted or rewritten.
A dated 29 August 2026 correction/status section was appended to make the
canonical state explicit: no publication-final Visual 2 exists in this Step 8
state, the historical terminal image is not a substitute, and current status is
governed by `05-VISUALS.md`, `assets/src/IMPLEMENTATION.md`,
`07-FINAL-REVIEWS.md`, and this file.

No public document in the staged dependency closure requires `workflow/`,
`EVIDENCE.md`, internal review terminology, the historical echo image, or the
historical protocol-upgrade figure.

# Non-human gate checklist

| Gate | Result | Evidence/result |
| --- | --- | --- |
| Destination-layout dependency closure | PASS | Fixed point is the 8-file staged package above |
| Local file resolution | PASS | 0 missing local targets in source and staged layout |
| Local anchor resolution | PASS | 3/3 local Markdown fragments resolved |
| Path casing | PASS | Exact component-by-component casing check; 0 mismatches |
| SVG dependency closure | PASS | 4 public SVGs are self-contained; no external/embedded SVG dependencies |
| Public/internal dependency separation | PASS | No `EVIDENCE.md`, `workflow/`, historical echo, or nonexistent Visual-2 dependency in public closure |
| Visual 1 semantics | PASS | 13/13 required semantics; rendered final export checked |
| Visual 3 semantics | PASS | 13/13 authoritative chronology semantics; rendered final export and adjacent public prose checked |
| Visual 1/3 cross-consistency | PASS | One active context in Visual 1; staged-not-active replacement then pointer switch in Visual 3 |
| Light rendering | PASS | Opaque neutral SVG canvases inspected on light surrounding page |
| Dark rendering | PASS | Same SVGs inspected on GitHub-like dark surrounding page; no theme dependency |
| Desktop rendering | PASS | Principal SVGs mechanically rendered at approximately 900 px width |
| Mobile rendering | PASS | Principal SVGs mechanically rendered at approximately 375 px; Visual 3 geometry was made less wide and type enlarged to keep core chronology readable |
| Monochrome/grayscale | PASS | Direction, grouping, labels, and state remain understandable without color |
| Contrast | PASS | Ordinary-text combinations meet at least 4.5:1; recorded ratios are in `assets/src/IMPLEMENTATION.md` |
| Privacy/editor metadata | PASS | No usernames, hostnames, machine/local paths, credentials, certificates, raster payloads, or editor-private metadata in public SVG/package audit |
| Visual 2 status | PASS | Authoritative decision is ABSENT; missing provenance identified; no synthetic/historical substitute used |
| README/document consistency | PASS | Step 7c structure preserved; only context-switch precision and publication/internal dependency cleanup changed public prose |
| Production source→destination mapping | PASS | Every file in the 8-file closure has an explicit Landingpages→`snode.c` mapping above |

Additional final checks completed before commit:

- whitespace/diff validation equivalent to `git diff --check`: PASS;
- principal editable SVG and publication export byte identity: PASS;
- XML parsing and SVG portability constraints: PASS;
- public-package stale Visual-2/internal-link scan: PASS;
- temporary staging/raster files remain outside the repository and are not part
  of the commit;
- intended changes contain no new binary file;
- the live `SNodeC/snode.c` repository was not modified.

# Human approval gate

**PENDING**

Step 8 does not grant maintainer visual approval and does not authorize a live
production publication. The next workflow action is the separate browser-based
publication validation using Chromium/Playwright, followed by explicit
maintainer visual/publication approval.

# Production publication status

**READY FOR HUMAN PUBLICATION REVIEW**

Every applicable non-human Step 8 gate is PASS. The remaining mandatory gate is
explicit maintainer approval after the browser-based publication review. No
files have been published to the live `SNodeC/snode.c` repository in this round.
