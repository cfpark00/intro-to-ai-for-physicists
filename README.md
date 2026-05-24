# Intro to AI for Physicists

A short, modern web textbook on AI/ML/DL for physicists — covering the post-2017 paradigm (transformers, scaling laws, LLM pretraining, fine-tuning, RL, reasoning, diffusion, inference) and skipping the classical ML survey material.

Live site: **<https://scienceofdl.com>**

## Local development

Install [Quarto](https://quarto.org/docs/get-started/) and a Python environment with `jupyter`, `matplotlib`, `numpy`.

```bash
cd src
quarto preview     # live-reload server at http://localhost:xxxx
quarto render      # build static site to src/_site/
```

## Structure

```
src/
├── _quarto.yml          # book config
├── index.qmd            # preface
├── chapters/            # one .qmd per chapter
├── references.qmd
├── references.bib
├── styles.css
└── CNAME                # scienceofdl.com
```

## Deployment

Pushes to `main` trigger `.github/workflows/publish.yml`, which renders the book and pushes the output to the `gh-pages` branch. GitHub Pages serves that branch at `scienceofdl.com`.

## Contributing

Issues and PRs welcome. See `docs/context.md` for the design rationale and `docs/repo_usage.md` for repo conventions.
