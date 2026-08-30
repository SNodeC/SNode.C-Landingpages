# Step 15 — Post-verdict targeted publication corrections

## Scope

This is a final targeted editing pass against the independent publication review
performed on 30 August 2026. It is **not** a structural redesign and does not
reopen the approved reader journey.

Starting state:

- Landingpages `main`: `6b3a472b6cca5702c61c94d7bec20abe20101375`
- public `SNodeC/snode.c` `master`:
  `60f26d9ae54b3e9ffde954d0ca75e53f79f31d79`

The independent review evaluated an earlier Landingpages HEAD
`0d695564d978f4de54d8410d8d7cc8ae69667196`. Findings were therefore mapped
against the current post-closure package rather than applied mechanically.

## Verdict disposition

### Accepted in this pass

| Review item | Resolution |
| --- | --- |
| I1 — Express-style API not shown | Added one compact, source-verified `express::legacy::in::WebApp` health-route example linked to current `src/apps/main.cpp`. The echo remains the only quick-start path. |
| I2 — quick-start friction | Added the recorded Debian package-install command, simplified the primary server/client invocations, and moved `XDG_CONFIG_HOME` plus monochrome logging to an explicit reproducibility note. The non-system `LD_LIBRARY_PATH` requirement remains because current public CI demonstrates that the staged shared-library path matters. |
| I3 — context-switch figure after dense prose | Moved the figure before the mechanism detail and reduced README prose to the two timing/ownership facts the figure needs prose to state. Identifier-level chronology remains in `docs/architecture.md`. |
| I5 — Linux fallback-font neighbour collisions | Confirmed and corrected in Figma only; details below. |
| M1 — first-screen type-name density | Rewrote the opening model paragraph around the connection-local idea and deferred the full type inventory to the programming-model section. |
| M3 — evidence vocabulary discontinuity | Added a mapping sentence in `docs/capabilities.md` between README `Available`/`Exercised` and the deeper evidence vocabulary. |
| M4 — precedence direction | Kept the compact README order but labels it explicitly as `Highest precedence first`. |
| M5 — workflow vocabulary residue | Replaced `project-accepted C++20 compiler` with `C++20 compiler`; the older `qualified` quick-start phrasing had already disappeared in Step 14. |
| M6 — other recorded transports dead-end | Linked the IPv6/Unix/mTLS sentence directly to the capability map's network-variant evidence section. |
| M7 — architecture caption governance-speak | Caption now explains the visual convention directly: dashed RFCOMM/L2CAP entries exist in source but are not runtime-qualified here. |
| P4 — CI claim without route | Linked the exact current `gcc-debug` job for the 181/181 main CTest claim and installed-consumer evidence. |
| P6 — stale Figma architecture-mobile dimension | Re-inspection of authoritative Figma node `7:124` establishes **620×1278**. The committed SVG was already 620×1278; Step 9/14 metadata stating 620×1210 was stale and is corrected. |

### Already resolved before this pass

- I4 core issue — the README already routed directly to the generated Doxygen API reference.
- M2 — the in-tree `NET` macro caveat was superseded by the external installed-package echo example.
- P1 — meaningful figure captions and `<sub>` caption convention were already normalized.
- P2 — the historical verification stamp was superseded by current-master evidence wording.
- P3 — runtime configuration preparation was already separated from framework build setup.
- P5 — desktop architecture and configuration `assets/src/` counterparts were already restored from Figma.

This pass additionally adds the API-reference link to the top navigation of both
`docs/capabilities.md` and `docs/configuration.md`, matching
`docs/architecture.md`.

### Intentionally unchanged

The independent review's explicit no-change recommendations remain accepted:

- no terminal screenshot is added;
- the mobile-friendly capability bullets remain rather than reverting to a table;
- `Exercised` remains the README evidence word rather than being strengthened to
  `Tested`;
- no badges, benchmarks, logo, feature-count banner, competitor table, or
  star-history material is introduced;
- the closing architecture-first/code-first choice remains.

## Figma-only figure corrections

Authoritative Figma file: `giz3MDZrdwPx71L2HhiQdg` — **SNode.C Publication Figures**.

The maintainer requirement that figure changes occur only through Figma was
preserved. No SVG was hand-edited to change visual content.

### Desktop HTTP → WebSocket

The independent review found that the transition label could collide with the
`ACTIVE AFTER` card under DejaVu Sans fallback metrics.

Figma node `7:47` was changed from:

`HTTP active → replacement staged → WebSocket active`

to:

`HTTP active → staged → WebSocket active`

The phase cards still state `Replacement context created` and
`setSocketContext(new)` / `stages replacement; HTTP stays active`, so no
technical meaning was removed. The corrected Figma render has ample separation
from the state cards.

### Programming-model mobile

The review found that `connect completes` could collide with the adjacent
factory chip under the same Linux fallback font.

Factory-chip frames `3:22` and `3:29` were moved/narrowed symmetrically in Figma
to final local geometry:

- `x = 254`
- `width = 276`
- right edge unchanged at `530`

The 20.25-unit informative-text floor is preserved. At DejaVu Sans fallback
metrics, the client action and factory chip retain positive neighbour clearance.
The server/client ownership symmetry and all programming-model semantics remain
unchanged.

Both corrected frames were re-rendered and visually inspected in Figma before
repository materialization. Repository publication/source pairs are generated
from those corrected nodes through the Figma Plugin API live-text SVG export and
remain byte-identical within each pair.

## Figma provenance correction

Direct design-context inspection of `7:124` shows:

`Architecture — Mobile · 620×1278`

This is the current Figma source of truth and matches the existing committed
`layer-architecture-mobile.svg` / `assets/src` viewBox. No architecture-mobile
figure edit was required. `09-FIGMA-RESPONSIVE-FIGURES.md` is corrected so the
current metadata now agrees with both Figma and the repository artifact.

## Technical/evidence alignment

The source baseline remains `60f26d9`. The public CI evidence used here is the
exact-head `gcc-debug` job:

`https://github.com/SNodeC/snode.c/actions/runs/33293707417/job/99209664201`

Observed status remains:

- main configure/build: pass;
- main CTest step: pass, 181/181;
- staged install: pass;
- external echo configure/build: pass;
- external echo CTests: fail because the staged shared-library directory is not
  on the runtime loader path.

The README continues to state that boundary explicitly and does not promote the
four external-example tests to passing evidence.

## Validation

Before publication of this candidate:

- Landingpages `main` and public SNode.C `master` were rechecked and frozen at
  the SHAs above;
- the remaining review findings were compared against current post-Step-14
  files rather than the older reviewed HEAD;
- current Express-style example source was verified at exact source HEAD;
- the exact CI run/job was rechecked;
- both I5 collisions were reproduced from the current Figma geometry and fixed
  in Figma only;
- corrected Figma frames were visually re-rendered;
- Linux fallback-font checks include neighbour clearance as well as box
  containment;
- authoritative architecture-mobile Figma geometry was re-read directly and
  reconciled with the existing 620×1278 repository asset;
- relative README/doc routes, new heading anchors, code fences, and figure paths
  were reviewed in the final candidate;
- public/source counterparts for each changed figure use identical Git blobs;
- the approved README section order and reader journey are unchanged.

A native checkout remains unavailable in this execution environment because
outbound DNS to GitHub is blocked. Therefore this pass validates the candidate
through GitHub Git-data/tree/compare APIs plus Figma-native inspection rather
than claiming a local `git diff --check` or repository-local render script.

## Final disposition

The independent review's remaining high-value findings are resolved without a
new design cycle. The publication structure remains approved. The only known
technical issue outside the Landingpages package remains the upstream
external-echo CI runtime-loader path; the publication already represents it
accurately.
