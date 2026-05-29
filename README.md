# Intro to AI for Physicists

A short, modern web textbook on the **science of deep learning** for quantitatively literate readers. Neural networks as model organisms, modern AI as a scientific object, studied via controlled synthetic experiments and phenomenology.

Live site: **<https://scienceofdl.com>**

## Setup

Install [`uv`](https://docs.astral.sh/uv/) and [Quarto](https://quarto.org/docs/get-started/), then:

```bash
git clone https://github.com/cfpark00/science-of-dl.git
cd science-of-dl
uv sync
```

## Common commands

```bash
cd src && quarto preview                       # serve the book locally with live reload
cd src && quarto render                        # build static site to src/_site/
uv run python src/code/chapters/<slug>/course/<script>.py   # run a chapter demo
```

Contributions are welcome via the [issue templates](https://github.com/cfpark00/science-of-dl/issues/new/choose) (errata, suggestions, plot-quality reports).
