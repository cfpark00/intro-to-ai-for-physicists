# Next Session

The next session starts with **ZERO context** from prior conversations. This file tells you what's been done and what to do next.

## What's been done (state as of 2026-05-25)

Course design is at the **12-lecture spine + per-lecture gist** stage. We have:

1. **`docs/context.md`** — overall project context (Quarto book, scienceofdl.com, science-of-DL genre).
2. **`docs/course_design/`** *(this folder — AUTHORITATIVE for current spine)*:
   - `README.md` — course-wide context, 12-lecture spine, philosophy, audience, scope. **Read this first.**
   - `l1/content.md` through `l12/content.md` — verbose per-lecture gist files. Each is intended to be readable standalone with the README.
   - `topics_dump.md` — raw keyword brain-dump (future glossary seed).
   - `next_session.md` — this file.
3. **`resources/core_park_web_context/`** *(gitignored)* — author bio, CV, publications, GitHub repos. Local-only reference for who the author is and what voice the book should have.
4. **`src/`** — the Quarto book scaffolding. **Mostly empty** — no actual lecture content has been written yet. The book deploys to <https://scienceofdl.com> but is currently the default Quarto starter.

## What to do next

The natural next step is **content authoring** — start drafting the actual lectures.

### Recommended sequence

1. **Read `docs/course_design/README.md`** (course-wide context).
2. **Read `docs/context.md`** (project context — tech stack, deployment).
3. **Pick a starting lecture.** Strong candidates:
   - **L1 (Introduction)** — most context already captured; sets the tone for everything else. Lowest risk to start here.
   - **L7 (Science of DL 1)** — the lecture closest to the author's published research; could be drafted from existing material (Emergence of Hidden Capabilities, Competition Dynamics, etc.).
   - **L2 (Neural Networks and Image Classification)** — opens the historical thread; a natural early target.
4. **Read the chosen lecture's `lN/content.md` fully** — it captures all the implicit knowledge the author shared during planning.
5. **Discuss with the author** about depth, math vs intuition, HW, and any TBDs flagged in the content.md file before drafting.
6. **Draft into `src/chapters/lecture-N-*.qmd`** as Quarto markdown.

### Things to check with the author before drafting any lecture
Before drafting **any** lecture, confirm:
- Length / time budget per lecture (the spine assumes ~75 min Harvard grad lectures).
- Whether to include code examples inline or link to companion notebooks.
- Math notation conventions (LaTeX is supported in Quarto; check author's preference).
- HW format — written? coding? both?
- Whether the book should match the lecture flow 1:1 or have its own structure.

### Things specific to certain lectures (flagged in content.md files)
- **L1**: needs rewording away from "second half" for the standalone full-course version.
- **L4, L6**: author noted these are the most topic-bin-shaped. Consider adding a phenomenon hook at content time.
- **L6**: inference-time compute / reasoning may deserve more weight (currently a bullet).
- **L10**: now lighter (continual learning moved to L11). Could absorb Dreamer/MuZero deeper.
- **L11**: most distinctive voice in the course; pacing matters (drifts from concrete to abstract).
- **L12**: at risk of being a grab-bag; needs through-line discipline.

### Bigger-picture pending work (not for next session, but worth knowing)
- HW design for L2, L3, L4, L7, L8, L9, L10, L11, L12 (currently TBD).
- Glossary build-out — `topics_dump.md` is the seed. When lectures crystallize, convert to `src/glossary.qmd`.
- Quarto sidebar / TOC structure: 12 lecture chapters + appendix glossary + references.
- References.bib — build out as lectures cite papers.
- Slides separately, if author wants them. The book is markdown; slides could be Reveal.js via Quarto.

## Things NOT to do without checking

- Don't drop or merge lectures without confirming with the author. The 12-lecture spine has been iterated heavily (v1 → v5); current shape is a deliberate choice.
- Don't rewrite the philosophy in L1 without preserving the user's verbatim phrasing (captured in `l1/content.md`). Voice matters.
- Don't add classical-ML content (SVMs, kNN, decision trees) — explicitly out of scope.
- Don't add ML-theory content (NTK, manifold capacity, generalization bounds proofs) — the other prof's territory.
- Don't add software/MLOps tutorial content — "recipes, not science."

## File-system map (quick reference)

```
docs/
├── context.md                       # project context
├── repo_usage.md                    # conventions
├── start.md / closing_tasks.md      # session hooks
├── course_design/                   # AUTHORITATIVE for current spine
│   ├── README.md                    # READ FIRST
│   ├── next_session.md              # this file
│   ├── topics_dump.md               # glossary seed
│   └── l{1..12}/content.md
└── logs/                            # session logs

resources/                           # gitignored
└── core_park_web_context/           # author bio/CV/pubs

src/                                 # the Quarto book (mostly empty scaffold)
```
