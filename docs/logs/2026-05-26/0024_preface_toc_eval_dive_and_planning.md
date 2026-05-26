# Session log — 2026-05-25 → 2026-05-26 (overnight): preface TOC, AI evaluation Deep Dive, per-lecture flow plan

## Summary

Three threads of work. First, added a visual TOC to the preface (square icon tiles, one per lecture and per Deep Dive), iterated it to a denser layout, then made it collapsible with a "Lectures" subheading. Second, added a 16th Deep Dive: **AI evaluation**, slotted between Interpretability and Theory in the sidebar. Third, wrote `docs/next_session.md` — a per-lecture flow plan that documents the canonical section sequence for each of the 12 lectures, surfaces a stale-gist inconsistency (continual-learning placement), and lists concrete next-session moves per lecture.

## Tasks completed

### Preface visual TOC (4 commits)
- **5f2b66c**: Added `## Contents` with two grids of `<a class="toc-tile">` square tiles — 12 chapter tiles with numbers + icons, 15 Deep Dive tiles with icons only. CSS rules in `styles.css` (`.toc-grid`, `.toc-tile`, dark-mode aware, hover lift). Used raw HTML blocks so each tile is a direct grid child (not wrapped in a `<p>`).
- **4abe190**: Shrank tiles from 4-col / large to 6-col / small. The first cut filled too much vertical space for a 27-item grid.
- **bb00477**: Made the whole Contents block collapsible via `<details>`/`<summary>` (defaults to open, chevron rotates on toggle). Added a `### Lectures` h3 above the chapters grid, parallel to the existing `### Deep Dives` h3. Tightened the dives grid to 8 columns on desktop (6/4/3 at narrower widths) with smaller padding, icons, and labels.

### New Deep Dive: AI evaluation (commit a064085)
- New `src/deep_dives/ai_evaluation.qmd` (~80 lines), styled after `interpretability.qmd`. Sections: why it's a field now; benchmarks → elicitation; dangerous-capability evaluation (ASL / Preparedness / Frontier Safety Frameworks); sandbagging and other measurement obstacles; agentic evaluation; statistical guardrails; meta-comments; where to go next. Framing: "evaluations are experimental apparatus, not scoreboards" — pure science-of-DL pitch.
- Slotted between `interpretability` and `theory` in `_quarto.yml` (both are observational tools for studying deployed models; AI evaluation precedes the more analytical Theory dive).
- Added matching tile (`bi-clipboard-data` icon) in the preface TOC grid, in the same slot.
- Created `src/code/deep_dives/ai_evaluation/{course,homework,homework/solutions}/.gitkeep`.
- Picked over alternatives: AI safety/alignment, statistical mechanics of learning, tensor networks & quantum ML, geometric DL, self-supervised learning, adversarial robustness, causal inference. AI evaluation won because it maps cleanly onto the experimental-physicist measurement-instrument framing and has no current home in the existing 15.

### Per-lecture flow plan (`docs/next_session.md`, uncommitted)
- Wrote a ~200-line spec doc for the next authoring session. Per lecture: numbered section flow with a one-line role per section + 2–3 concrete next-session moves.
- **Discovered an inconsistency**: the gist file `docs/course_design/l11/content.md` still places continual learning in L11, but the actual chapter draft `11_scidl_concepts.qmd` only mentions continual learning in its preamble and routes the full treatment to L10 (where `10_world_models.qmd` has a substantial section on it, framed as "keeping a world model updatable"). The doc declares L10 canonical and flags l11/content.md as stale.
- Carried forward prior session's per-lecture flags: L1 reword "second half", L4 needs phenomenon hook, L6 expand inference-time compute, L10 deepen Dreamer/MuZero, L11 protect the philosophical pivot, L12 avoid grab-bag.
- Cross-cutting decisions section locks in: ICL three-treatment thread (L5 intro → L7 dissect → L11 philosophical), bitter-lesson thread (L1 → L2 → L5), 5-step methodology cross-references (L1 → L7 → L11).

### Closing tasks
- Bumped Deep Dive count in `docs/context.md` (15 → 16).
- README untouched (no setup or commands changed).

## Files modified / created

**Created:**
- `src/deep_dives/ai_evaluation.qmd`
- `src/code/deep_dives/ai_evaluation/{course,homework,homework/solutions}/.gitkeep`
- `docs/next_session.md`
- `docs/logs/2026-05-26/0024_preface_toc_eval_dive_and_planning.md` (this file)

**Modified:**
- `src/index.qmd` (preface TOC: tiles + collapsible wrapper + Lectures heading)
- `src/styles.css` (TOC grid + tile styles + collapse summary + denser dives variant)
- `src/_quarto.yml` (added `ai_evaluation.qmd` to the Deep Dives part)
- `docs/context.md` (15 → 16 Deep Dives)

## Key decisions / insights

- **Visual TOC as the preface entry point.** Replaced the implicit "scroll through prose to discover structure" with a one-look icon grid at the top. Collapsible so it doesn't dominate when readers come back to the preface looking for prose.
- **AI evaluation as a Deep Dive, not a chapter.** The author's existing post-training chapter (L6) covers evals briefly at the scoreboard level; the dive treats the methodology of measurement as its own field. Clean split: L6 = "what evals exist," dive = "what evaluation as a discipline looks like."
- **Gist files are background, not spec.** Discovered while writing the per-lecture plan that the gist files describe planning state that has been superseded by the actual chapter drafts in places (notably L10/L11 continual learning). `docs/next_session.md` now explicitly states "drafts win when they disagree with gists."

## Open questions / next steps

- **AI evaluation Deep Dive content** is in the author's voice but unverified. Likely needs a pass to rewrite passages and add the author's own opinions (especially on capability elicitation methodology and on what "an eval" should mean operationally).
- **Per-lecture work.** Execute the moves in `docs/next_session.md` — L1 reword, L4 phenomenon hook, L6 inference-time expansion, L7 voice protection, L11 pivot pacing, L12 grab-bag risk.
- **Stale gist cleanup.** Either trim `docs/course_design/l11/content.md` to remove its continual-learning section, or add a one-line "superseded by draft, see L10" note at the top of each affected gist.
- **HW pass.** Most chapters have `code/chapters/<slug>/course/` and `homework/solutions/` directories with only `.gitkeep` files. Pick a starter set of chapters (L1, L2, L7, L8 are obvious) and seed real prompts + solutions.
- **`[Plot]` callout resolution.** Chapters are full of `[Plot]` placeholders; resolve to actual rendered figures generated from `code/chapters/.../course/` scripts.
