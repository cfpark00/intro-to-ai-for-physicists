# Chapter 2 — Code

## What's in here

- `gabor_demo.py` — train a small CNN on CIFAR-10 for a few epochs and plot the first-layer filters. Produces `gabor_filters.png`. This is the script that backs the headline phenomenon of the chapter (Gabor-like emergence in first-layer convolutional filters of a CNN trained end-to-end on natural images).

## How to run

From the repo root:

```bash
uv sync                  # one-time, installs deps (skip if already done)
uv run python src/code/02_image_classification/gabor_demo.py
```

CPU is fine, training takes a few minutes. CIFAR-10 (~170 MB) downloads on first run to `data/cifar10/` (gitignored).
