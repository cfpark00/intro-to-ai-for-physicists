# Project Context

## What We're Building

A short, modern web textbook: **"Intro to AI for Physicists"** — companion to a Harvard Physics grad-level AI/ML course launching early 2027.

**Genre: science of deep learning.** The book treats modern AI (transformers, scaling laws, LLM pretraining, fine-tuning, RL, reasoning, diffusion, inference) as a *scientific object* — phenomena surfaced through controlled synthetic experiments, mechanistic probing, and phenomenology. Neural networks as model organisms. The voice mirrors the lead author's own research output (ICL phase transitions, hidden-capability emergence, world representations).

**Explicitly out of scope:**
- Classical ML survey (SVM, kNN, decision trees) — other books do this well.
- ML theory (NTK, neural manifold capacity, high-dim geometry, generalization bounds) — covered by a different professor in the course.
- Software/engineering tutorials ("how to train your LLM," kubernetes, MLOps) — these are recipes, not science.

Live site: <https://scienceofdl.com>
Source: <https://github.com/cfpark00/science-of-dl>

## Target Users

Physicists (students through working researchers) who:

- Are comfortable with linear algebra, calculus, probability
- Have no required prior ML background
- Want the big picture of modern AI rather than a software tutorial or a research survey

## Tech Stack

- **Quarto** (open-source, MIT, Posit) — markdown-first scientific publishing, executable Python code blocks, KaTeX math, multi-chapter book mode.
- **GitHub Pages** — static hosting, custom domain `scienceofdl.com`.
- **GitHub Actions** — render Quarto on push, deploy to `gh-pages` branch.
- **DNS**: Cloudflare (DNS only, no proxy) → GitHub Pages IPs.

## Architecture

```
repo root
├── src/                        # Quarto book source
│   ├── _quarto.yml             # book config, sidebar, theme
│   ├── index.qmd               # preface
│   ├── chapters/               # one .qmd per chapter
│   ├── references.qmd          # bibliography page
│   ├── references.bib          # BibTeX
│   ├── styles.css              # custom CSS
│   ├── CNAME                   # custom domain marker, copied to output by Quarto
│   └── _site/                  # build output (gitignored)
├── .github/workflows/publish.yml  # CI: render + push to gh-pages
└── docs/                       # repo meta-docs (NOT the book — see CLAUDE.md)
```

Render locally: `cd src && quarto render` (output in `src/_site/`).
Preview locally: `cd src && quarto preview` (live-reload server).

## Key Decisions

- **Quarto over Jupyter Book / MkDocs / Astro** — best fit for a math-and-code textbook with multiple output formats, fully OSS, no SaaS dependency.
- **GitHub Pages over Netlify / Vercel / Cloudflare Pages** — git-native, no third-party host, matches "distributable via git" requirement.
- **`src/` holds the book**, output goes to `src/_site/` (gitignored). The `_site/` lives inside `src/` because Quarto warns if output is outside the project root.
- **Chapter scope is opinionated.** No SVMs, no kNN, no decision trees — there are good books for those. Focus is on the post-2017 paradigm.
- **Frontier model citations are illustrative, not comprehensive.** This is a textbook, not a survey.

## Constraints

- All tools must be open source (see auto-memory `feedback_open_source_only.md`).
- Site must be deployable from a clean git clone with one push.
- No proprietary or paywalled content.
