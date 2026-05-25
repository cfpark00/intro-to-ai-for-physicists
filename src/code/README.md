# Chapter materials

This directory holds the code and pedagogical assets that go with each chapter. The prose lives in `src/chapters/NN_*.qmd`; everything underneath the prose, the scripts that produce figures, the interactive demos, the homework prompts, the solution code, lives here.

## High-level layout

One directory per chapter, matching the chapter slug:

```
src/code/
├── 01_intro/
├── 02_image_classification/
├── 03_sequence_modeling/
...
└── 12_intelligence/
```

How each chapter is organized inside its directory is up to whoever is building that chapter's materials. Some chapters will want a clean split between figure-generating code, interactive demos, homework prompts, and reference solutions; others will be lighter and just need a couple of scripts in a single folder. The structure is deliberately open so it can evolve.

Producing these materials is an open-ended pedagogical research process. The intent of this layout is to make per-chapter iteration cheap (each subtree is independent of the others) and to let conventions settle bottom-up as chapters mature, rather than locking everyone into a prescribed shape on day one.

When patterns crystallize across chapters, lift them into shared conventions; until then, follow what the chapter you are working on has already chosen, or pick what fits.
