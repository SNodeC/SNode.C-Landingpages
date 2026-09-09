# Shared TikZ figure system

This directory is the shared cross-project source location for the canonical
technical-figure presentation system used by the landing-page subprojects.

The initial shared files are copied unchanged from the currently approved
MQTTSuite TikZ system:

- `mqttsystem-figure-system.tex` — base TikZ vocabulary, helpers, node families,
  typography, ports, connector semantics, and publication rules;
- `snodec-canonical-figure-system.tex` — the canonical SNode.C presentation
  override for palette, geometry, typography, node grammar, and connectors.

New technical figures should load the shared system with the same stable input
names:

```tex
\input{mqttsystem-figure-system.tex}
\input{snodec-canonical-figure-system.tex}
```

The repository-level CMake build searches a figure's own source directory first
and this shared directory second. This intentionally supports a staged
migration:

- **SNode.C** starts consuming the shared files directly for new TikZ figures.
- **MQTTSuite** remains unchanged for now and continues to resolve its existing
  local copies under `MQTTSuite/assets/src/tikz/`.
- MQTTSuite can be migrated to the shared location in a later dedicated pass;
  only then should its duplicate local system files be removed.

Do not fork or restyle the shared presentation system per subproject. Project
figures may differ in semantic content and composition, but the shared visual
system is the common style authority.

Generated SVGs remain per-project build outputs and are not canonical sources.
