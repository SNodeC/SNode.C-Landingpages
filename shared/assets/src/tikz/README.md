# Shared TikZ figure system

This directory is the shared cross-project source location for the canonical
technical-figure presentation system used by the landing-page subprojects.

The shared system is intentionally a **single-file style authority**:

- `landingpages-figure-system.tex` — complete reusable TikZ vocabulary plus the
  canonical landing-page presentation system for palette, typography, spacing,
  node/container grammar, connector semantics, responsive budgets, canvas helpers,
  and publication rules.

The repository-wide Markdown authority is the root-level `PAGE-SYSTEM.md`. It
combines and supersedes the former `PAGE-SYSTEM.md` page guidance and the former
`shared/assets/src/tikz/FIGURE-contract.md`; the stricter former figure-contract
rules win wherever the two predecessors conflicted.

New technical figures should load only:

```tex
\input{landingpages-figure-system.tex}
```

Before creating, reviewing, fixing, or refining technical figures, both of these
must be read in detail:

- root `PAGE-SYSTEM.md`;
- `landingpages-figure-system.tex`.

They are the presentation source of truth together with the figure-specific
semantic contract and current implementation evidence.

The repository-level CMake build searches a figure's own source directory first
and this shared directory second. This supports staged migration:

- **SNode.C** consumes the shared one-file system directly for migrated/new TikZ
  figures.
- **MQTTSuite** may still resolve existing local system copies while migration is
  incomplete; those copies do not authorize divergence from the repository-wide
  combined contract.
- duplicate local system files should be removed or renamed only in the dedicated
  migration pass that makes the shared system the resolved implementation.

Do not fork or restyle the shared presentation system per subproject. Project
figures may differ in semantic content and relative composition, but the shared
visual system and root combined contract are common authority.

Generated SVGs remain derived per-project build outputs and are not canonical
editable sources.
