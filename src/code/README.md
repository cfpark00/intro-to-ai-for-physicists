# Chapter materials

This directory holds the code and pedagogical assets that go with each chapter of the book. The prose lives in `src/chapters/NN_*.qmd`; everything *underneath* the prose — the scripts that produce figures, the interactive demos, the homework prompts, the solution code — lives here.

## Layout

```
src/code/
└── NN_slug/                # one directory per chapter (matches the qmd filename)
    ├── figures/            # code that produces figures embedded in the chapter
    ├── interactive/        # interactive demos (notebooks, small webapps, widgets)
    ├── homework/           # homework prompts, datasets, scaffolding
    └── solutions/          # reference solutions to the homework
```

The four subdirectories are the same for every chapter so contributors know where to look. Empty subdirectories are kept in git via `.gitkeep` files.

## Working in here

Producing these materials is itself an open-ended pedagogical research process. The structure is designed to support that: each chapter's subtree is independent of the others, so experimental work on one chapter's figures or interactives does not block work on any other chapter. Use git branches freely for in-progress experiments; merge to main when something settles.

A few conventions worth following:

- **Keep scripts self-contained.** A figure-generating script should run end-to-end without needing global state or imports from other chapters. Cross-chapter shared utilities go in a separate location once they crystallize.
- **Cache slow outputs.** If a figure script takes more than a few seconds to run, save the output (image file, computed array, etc.) somewhere git or DVC can track it, and have the script load the cache if available.
- **Pin your environment.** Each chapter's `interactive/` may end up with its own `requirements.txt` or `pyproject.toml` if it has unusual dependencies. The book's top-level build does not need to install these.
- **Solutions are not gated.** See the preface — solutions live in plain sight on purpose.

## How materials get into the book

When a figure is ready to ship in the rendered book, two options:

- **Static embed**: render the figure once, save the image, embed it from the qmd with a relative path (e.g. `![](code/NN_slug/figures/foo.png)`).
- **Executable embed**: include a code cell in the qmd that runs the figure script at render time. This is reproducible but slower to build; usually only worth it when the output may change.

Interactive demos can be linked from the chapter via a sidebar link or an iframe — exact mechanics will settle once the first few interactives exist.
