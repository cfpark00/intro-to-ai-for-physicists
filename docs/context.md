# Project Context

## What We're Building

A short, modern web textbook on the **science of deep learning** for quantitatively literate readers. The companion to a Harvard Physics graduate AI/ML course launching early 2027.

**Genre: science of deep learning.** The book treats modern AI (transformers, scaling laws, LLM pretraining, fine-tuning, RL, reasoning, diffusion) as a *scientific object*: phenomena surfaced through controlled synthetic experiments, mechanistic probing, and phenomenology. Neural networks as model organisms. The voice mirrors the lead author's own research output (ICL phase transitions, hidden-capability emergence, world representations).

**Explicitly out of the main spine** (these get their own Deep Dives instead):

- Classical ML (SVM, kNN, decision trees, kernel methods).
- ML theory (NTK, neural manifold capacity, high-dim geometry, generalization bounds).
- Software / systems / infrastructure engineering.

Live site: <https://scienceofdl.com>
Source: <https://github.com/cfpark00/science-of-dl>

## Target Users

Anyone comfortable with linear algebra, calculus, probability, and a bit of statistical mechanics. No prior ML background required; the pace assumes graduate-level fluency with quantitative thinking. Physicists are the primary intended audience, hence the science-of-DL framing, but the book is no longer pinned to a specific institution or course in its prose.

## Tech Stack

- **Quarto** (open-source, MIT, Posit) for markdown-first scientific publishing: KaTeX math, multi-chapter book mode, executable Python blocks when needed.
- **uv** for the Python environment. One root `pyproject.toml` covers all chapter and Deep Dive materials; `uv sync` is the one-command onboarding.
- **GitHub Pages** for static hosting on the custom domain `scienceofdl.com`.
- **GitHub Actions** to render Quarto on push and deploy to `gh-pages`.
- **DNS**: Cloudflare (DNS only, no proxy) pointing at GitHub Pages IPs.
- **CoreWeave / `pc` cluster** for any compute-heavy chapter material (H100s, K8s, `/shared` persistent storage). Cluster-side infra files live in gitignored `scratch/cluster/` and are not part of the public repo.

## Architecture

```
repo root
├── pyproject.toml              # single root Python env (uv-managed)
├── uv.lock
├── README.md                   # short onboarding
├── .github/
│   ├── workflows/publish.yml   # render Quarto, push to gh-pages
│   └── ISSUE_TEMPLATE/         # errata / suggestion / plot_quality / other
├── src/                        # Quarto book project root
│   ├── _quarto.yml             # book config, sidebar, theme
│   ├── index.qmd               # preface (sidebar label "0  Preface")
│   ├── chapters/               # 12 numbered chapters (1..12)
│   ├── deep_dives/             # 16 adjacent-field chapters
│   ├── code/
│   │   ├── chapters/<slug>/    # per-chapter materials (course/, homework/solutions/)
│   │   └── deep_dives/<slug>/  # same layout for each Deep Dive
│   ├── references.qmd / .bib   # bibliography
│   ├── glossary.qmd            # seed glossary (term list, definitions TBD)
│   ├── assets/                 # cover art, favicon, app icons (squircle-masked)
│   ├── styles.css              # custom CSS (sidebar hline, item spacing)
│   ├── CNAME                   # custom domain marker
│   └── _site/                  # build output (gitignored)
├── data/                       # derived/precomputed data (gitignored, DVC-eligible)
├── scratch/                    # temporary work (gitignored)
│   └── cluster/                # cluster pod manifests, launch scripts (gitignored)
└── docs/                       # repo meta-docs (NOT the book itself)
    ├── context.md              # this file
    ├── repo_usage.md
    ├── course_design/          # per-lecture content gists, the v5 12-lecture spine
    └── logs/                   # session logs (YYYY-MM-DD/)
```

Render locally: `cd src && quarto render` (output in `src/_site/`).
Preview locally: `cd src && quarto preview` (live-reload server).
Run chapter code: `uv run python src/code/chapters/<slug>/course/<script>.py`.

## Key Decisions

- **Quarto over Jupyter Book / MkDocs / Astro.** Best fit for a math-and-code textbook with multiple output formats, fully OSS, no SaaS dependency.
- **GitHub Pages over Netlify / Vercel / Cloudflare Pages.** Git-native, no third-party host.
- **`src/` is the Quarto project root**, output goes to `src/_site/`. The `_site/` lives inside `src/` because Quarto warns if output is outside the project root.
- **Sidebar numbered 0..12** (preface as chapter 0). Deep Dives sit between chapter 12 and the back matter (References, Glossary), visually grouped with the main content; a horizontal rule separates back matter.
- **Deep Dives are not appendices.** Each is a chapter-shaped piece on a single adjacent field, with the same first-class materials treatment as the main chapters.
- **Single root `pyproject.toml`, uv-managed.** `uv sync` installs everything any chapter or Deep Dive code needs; future per-chapter `extras` can be added if a chapter's deps would bloat the common env.
- **Chapter materials structure**: each chapter and Deep Dive has `course/` (figure-generating and demo code) and `homework/solutions/` (with the solutions intentionally in plain sight, see the preface's "On homework and solutions" section). Internal layout below those two is open and evolves per chapter.
- **Em-dashes are dispreferred** in prose (see auto-memory). Default punctuation: commas, semicolons, periods, parentheses.
- **Cluster infra is private**, not part of the public textbook repo. `scratch/cluster/` and `.env` are gitignored.
- **Frontier model citations are illustrative, not comprehensive.** This is a textbook, not a survey.

## Constraints

- All tools must be open source (see auto-memory `feedback_open_source_only.md`).
- Site must be deployable from a clean git clone with one push.
- No proprietary or paywalled content.
- All chapter code must be runnable from `uv run python ...` after `uv sync`. No hidden environment setup.
