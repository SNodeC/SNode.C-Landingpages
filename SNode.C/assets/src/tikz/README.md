# SNode.C TikZ figure sources

Concrete SNode.C technical figure sources live in this directory.

Do **not** copy or fork the canonical figure system into this project. Every
figure consumes the shared cross-project system from
`shared/assets/src/tikz/` through the repository-level CMake `TEXINPUTS` path:

```tex
\input{landingpages-figure-system.tex}
```

Hard source rules for every SNode.C technical figure:

- use only canonical node/container/connector styles from
  `landingpages-figure-system.tex`;
- do not introduce figure-local colors, fonts, radii, line widths, fills,
  arrowheads, shadows, or other visual styling;
- place every element relative to other elements; absolute `at (x,y)` placement,
  absolute numeric canvas coordinates, and `xshift`/`yshift` positioning are
  forbidden;
- use canonical border ports/anchors and orthogonal routing for connectors;
- desktop and mobile sources may use different relative compositions but must
  remain semantically equivalent.

Generated SVGs are **derived publication outputs**. CI regenerates the 16 SNode.C
technical SVGs from these TikZ sources and commits the resulting publication assets
when the sources change. The TikZ sources and shared figure system remain the only
authoritative editable sources; generated SVG geometry is never hand-edited.
