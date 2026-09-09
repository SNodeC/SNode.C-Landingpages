# Shared TikZ figure system

This directory is the shared cross-project source location for the canonical
technical-figure presentation system used by the landing-page subprojects.

The shared system is intentionally a **single-file style authority**:

- `landingpages-figure-system.tex` — complete reusable TikZ vocabulary plus the
  canonical landing-page presentation contract for palette, typography, spacing,
  node/container grammar, connector semantics, responsive budgets, and
  publication rules.

New technical figures should load only:

```tex
\input{landingpages-figure-system.tex}
```

The repository-level CMake build searches a figure's own source directory first
and this shared directory second. This supports a staged migration:

- **SNode.C** starts consuming the shared one-file system directly for new TikZ
  figures.
- **MQTTSuite** remains unchanged for now and continues to resolve its existing
  local `mqttsystem-figure-system.tex` and
  `snodec-canonical-figure-system.tex` copies under
  `MQTTSuite/assets/src/tikz/`.
- MQTTSuite can be migrated to this shared one-file system in a later dedicated
  pass; only then should its duplicate local system files be removed or renamed.

Do not fork or restyle the shared presentation system per subproject. Project
figures may differ in semantic content and composition, but the shared visual
system is the common style authority.

Generated SVGs remain per-project build outputs and are not canonical sources.
