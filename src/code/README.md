# Chapter and deep-dive materials

This directory holds the code and pedagogical assets that go with the chapters and the deep dives. The prose lives in `src/chapters/NN_*.qmd` and `src/deep_dives/<slug>.qmd`; everything underneath the prose, the scripts that produce figures, the homework prompts, the solution code, lives here.

## Layout

```
src/code/
├── chapters/
│   ├── 01_intro/
│   │   ├── course/         # code that produces course-side assets (figures, plots, ...)
│   │   └── homework/       # homework prompts and supporting code
│   │       └── solutions/  # reference solutions
│   ├── 02_image_classification/
│   │   ├── course/
│   │   └── homework/solutions/
│   ├── ...
│   └── 12_intelligence/...
└── deep_dives/
    ├── theory/
    │   ├── course/
    │   └── homework/solutions/
    ├── systems/...
    ├── ...
    └── mechanism_design/...
```

Every chapter and every deep dive gets the same two subdirectories:

- **`course/`** holds the code that produces the things the reader sees in the chapter, figures, plots, computed examples, and so on. Output assets (PNGs, etc.) land in here next to the code that produces them.
- **`homework/`** holds the homework prompts, scaffolding, and any datasets the homework needs. Reference solutions live in `homework/solutions/`.

How each chapter is organized *inside* `course/` and `homework/` is up to whoever builds the materials. Some entries will be a single script per subdir; others will grow into multiple modules. The two-bucket split (`course/` vs `homework/`) is the only thing that is consistent across entries.

## Deep dives are chapters too

The deep dives are not appendices. Each one is a chapter-shaped piece of material on a field that did not fit the main spine's scope but stands on its own. They get the same code-asset treatment as the main chapters, their own `course/`, their own `homework/`, their own solutions if and when those exist. Treat them as first-class citizens of the materials tree.

## Working in here

Producing these materials is an open-ended pedagogical research process. The intent of this layout is to make per-entry iteration cheap (each subtree is independent of the others) and to let conventions settle bottom-up as content matures, rather than locking everyone into a prescribed shape on day one.
