# SNode.C TikZ figure sources

Concrete SNode.C technical figure sources live in this directory.

Do **not** copy or fork the canonical figure-system file into this project.
SNode.C figures consume the shared cross-project system from
`shared/assets/src/tikz/` through the repository-level CMake `TEXINPUTS` search
path:

```tex
\input{landingpages-figure-system.tex}
```

Keep only figure-specific TikZ composition in this directory. Shared palette,
typography, spacing, node/container grammar, connector semantics, responsive
budgets, and publication rules belong in the shared system file.

Generated SVGs are written to `SNode.C/assets/` by the canonical CMake figure
build and remain build outputs rather than authoritative sources.
