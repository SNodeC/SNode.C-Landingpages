# SNode.C KTikZ handover

This directory is a convenience view of the current SNode.C technical figures for direct editing in KTikZ.

- The 16 `*.tex` files contain only the current `\begin{tikzpicture} ... \end{tikzpicture}` bodies.
- `landingpages-figure-system.tex` is a repository symlink to the canonical shared style at `shared/assets/src/tikz/landingpages-figure-system.tex`; there is no duplicated style copy.
- `ktikz-template.pgs` is the KTikZ template. Set it once in KTikZ's Template field, then open any figure file in this directory.

No CMake or command-line setup is required for editing/previewing these handover files in KTikZ.

The canonical publication sources remain `SNode.C/assets/src/tikz/*.tex`; after editing, transfer the changed TikZ picture body back to the corresponding canonical source.
