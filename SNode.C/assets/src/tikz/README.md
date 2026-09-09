# SNode.C TikZ figure sources

Concrete SNode.C technical figure sources live in this directory.

Do **not** copy or fork the canonical figure-system files into this project.
SNode.C figures consume the shared cross-project system from
`shared/assets/src/tikz/` through the repository-level CMake `TEXINPUTS` search
path:

```tex
\input{mqttsystem-figure-system.tex}
\input{snodec-canonical-figure-system.tex}
```

Keep only figure-specific TikZ composition in this directory. Shared palette,
typography, spacing, node grammar, connector semantics, and publication rules
belong in the shared system files.

Generated SVGs are written to `SNode.C/assets/` by the canonical CMake figure
build and remain build outputs rather than authoritative sources.
