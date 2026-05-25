# Chapter 2 — Code

```
.
├── course/                  # code that produces course-side assets (figures, plots)
│   └── gabor_demo.py        # train a small CNN, visualize Gabor-like emergence
└── homework/                # homework prompts and supporting code
    └── solutions/           # reference solutions
```

## Course assets

- `course/gabor_demo.py` — train a small CNN on CIFAR-10 for a few epochs and plot the first-layer filters. Produces `course/gabor_filters.png`. This script backs the headline phenomenon of the chapter (Gabor-like emergence in first-layer convolutional filters of a CNN trained end-to-end on natural images).

## How to run

From the repo root:

```bash
uv sync                  # one-time, installs deps (skip if already done)
uv run python src/code/chapters/02_image_classification/course/gabor_demo.py
```

CPU is fine, training takes a few minutes. CIFAR-10 (~170 MB) downloads on first run to `data/cifar10/` (gitignored).
