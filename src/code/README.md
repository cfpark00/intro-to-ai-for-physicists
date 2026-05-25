# Chapter and deep-dive materials

This directory holds the code and pedagogical assets that go with the chapters and the deep dives. The prose lives in `src/chapters/NN_*.qmd` and `src/deep_dives/<slug>.qmd`; everything underneath the prose, the scripts that produce figures, the interactive demos, the homework prompts, the solution code, lives here.

## High-level layout

```
src/code/
├── chapters/
│   ├── 01_intro/
│   ├── 02_image_classification/
│   ├── ...
│   └── 12_intelligence/
└── deep_dives/
    ├── theory/
    ├── classical_ml/
    ├── systems/
    ├── ...
    └── mechanism_design/
```

Each chapter and each deep dive gets its own subdirectory. How that subdirectory is organized internally is up to whoever builds the materials. Some entries will want a clean split between figure-generating code, interactive demos, homework, and reference solutions; others will be lighter. The structure is deliberately open so it can evolve.

## Deep dives are chapters too

The deep dives are not appendices. Each one is a chapter-shaped piece of material on a field that did not fit the main spine's scope, but stands on its own. They get the same code-asset treatment as the main chapters: their own directories, their own figure-generating code, their own homework if it ever exists. Treat them as first-class citizens of the materials tree.

## Working in here

Producing these materials is an open-ended pedagogical research process. The intent of this layout is to make per-entry iteration cheap (each subtree is independent of the others) and to let conventions settle bottom-up as content matures, rather than locking everyone into a prescribed shape on day one.

When patterns crystallize across entries, lift them into shared conventions; until then, follow what the entry you are working on has already chosen, or pick what fits.
