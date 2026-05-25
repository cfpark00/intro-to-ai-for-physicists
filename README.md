# Intro to AI for Physicists

A short, modern web textbook on the **science of deep learning**, treating neural networks as model organisms and modern AI as a scientific object — phenomena surfaced through controlled synthetic experiments, mechanistic probing, and phenomenology.

Live site: **<https://scienceofdl.com>**

## Quick start

Install [`uv`](https://docs.astral.sh/uv/) (Python environment manager) and [Quarto](https://quarto.org/docs/get-started/), then:

```bash
git clone https://github.com/cfpark00/science-of-dl.git
cd science-of-dl
uv sync                                            # set up the Python env
uv run python src/code/02_image_classification/gabor_demo.py   # run a chapter demo
cd src && quarto preview                           # serve the book locally
```

`uv sync` reads `pyproject.toml`, creates `.venv/`, and installs everything needed to run the chapter code (numpy, scipy, scikit-learn / scikit-image, matplotlib, torch + torchvision, the Hugging Face stack).

## Structure

```
science-of-dl/
├── pyproject.toml          # single root env for all course code
├── src/
│   ├── _quarto.yml         # book config
│   ├── index.qmd           # preface
│   ├── chapters/           # one .qmd per chapter
│   ├── deep_dives/         # adjacent fields, launching-point chapters
│   ├── code/               # per-chapter materials (figures, demos, homework, solutions)
│   ├── references.qmd
│   ├── references.bib
│   ├── glossary.qmd
│   ├── styles.css
│   └── CNAME               # scienceofdl.com
└── docs/                   # design docs and session logs
```

`src/code/<chapter>/` holds the code that produces the chapter's figures, the interactive demos, the homework, and the solutions. Layout inside each chapter dir is intentionally flexible — see `src/code/README.md`.

## Deployment

Pushes to `main` trigger `.github/workflows/publish.yml`, which renders the book with Quarto and pushes the output to the `gh-pages` branch. GitHub Pages serves that branch at `scienceofdl.com`.

## Contributing

Errata, suggestions, and plot-quality reports are welcome — use the issue templates. See `docs/context.md` for the project's design rationale and `docs/repo_usage.md` for repo conventions.
