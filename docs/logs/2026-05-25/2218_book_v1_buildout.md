# Session log — 2026-05-25 (evening): book v1 build-out

## Summary

Large evening session that took the project from "scaffolded book with placeholder chapters" to a full v1 of the textbook: cover art and favicon, all 12 chapters drafted from the course-design gists, 15 Deep Dives added, glossary seeded, sidebar polished, per-chapter materials structure set up, Python env wired via `uv`, and a first cluster run executed on the `pc` cluster (though the demo was ultimately scrapped, see below).

## Tasks completed

### Cover art and favicon
- Picked `cand2.png` (cosmic-aurora gradient) over `cand1.png` (generic NN diagram). Moved to `src/assets/cover.png`.
- Generated favicon.ico (multi-res 16/32/48/64) plus apple-touch-icon and 192/512 app icons. All squircle-masked with an antialiased superellipse (n=5) for iOS-style corners.
- Wired `book.favicon: assets/favicon.ico` in `_quarto.yml`, registered `assets/**` as a project resource.

### Course-design docs consolidation
- Merged `docs/layout/` (which had the up-to-date v5 spine content) into `docs/course_design/`.
- Deleted the now-stale `lecture_outline.md`. README and next_session.md updated for the new paths.

### Book v1 content
- **Issue templates** at `.github/ISSUE_TEMPLATE/`: errata, suggestion, plot_quality, other; `blank_issues_enabled: false`. Removed "edit this page" repo-action.
- **Wrote all 12 chapter v1 drafts** sequentially from each `docs/course_design/lN/content.md` (had to give up on 12 parallel subagents after they all failed with API 529 Overloaded). Each chapter ~2000–3000 words, with plot-placeholder callouts. Voice and topics match the per-lecture gist.
- **Preface rewritten** to the science-of-DL framing, then later depersonalized (removed the Harvard-physics-grad-course framing per user feedback; framed around two aims, "quantitatively literate reader" not "physicist").
- **Chapter 1 "theory has been wrong" softened** to "or so I read the history," explicit acknowledgment that this is one reading and theorists may reasonably disagree.
- **Chapter 2 Gabor section dropped** entirely (was a forced fit in an otherwise intro-to-ML chapter). Migrated the Gabor mention to the Interpretability Deep Dive's early-history section.
- **Continual learning moved L11 → L10**: chapter 10 retitled "World models and continual learning" with the soft/hard-continual-learning material absorbed; chapter 11 stays "Concept learning."

### Sidebar structure
- **Renumbered 0..12**: preface manually titled "0  Preface," chapters carry "1 Introduction," "2 ...", etc.; `number-sections: false` globally to suppress Quarto's auto-numbering.
- **Reordered**: ch.0..12 → Deep Dives (collapsible part) → References → Glossary. Deep Dives visually grouped with main content; horizontal rule above References separates back-matter.
- **CSS tweaks**: hline above References via `:has()` selector; tiny vertical breathing room between sidebar items (0.7rem margin-top with !important to beat Bootstrap's default 0.4rem).
- **Author**: set to "Core Francisco Park" linking to corefranciscopark.com.

### Deep Dives section
- 15 entries created and seeded: theory, classical_ml, systems (merged with original llm_engineering), llm_architectures, data_centric, interpretability, bayesian_mcmc, neuroethology, neuroscience, cogsci, open_endedness, ai_for_science, ai_agents, mechanism_design, multimodal.
- Each ~600–1100 words, framed as "this is a field, here is a launching point" with a "where to go next" section.
- Preface gained a paragraph explaining what Deep Dives are: full chapters on adjacent fields, first-class material, not appendices.

### Glossary
- Seeded `src/glossary.qmd` with ~150 terms grouped by theme (architectures, training, phenomena, generative, RL, concepts, other). Definitions to be filled in as chapters mature; for now it functions as a vocabulary index.

### Em-dash reduction
- User flagged em-dashes as a style dislike. Saved as auto-memory (`feedback_no_emdashes.md`) so it persists across sessions.
- Mechanical `sed 's/ — /, /g'` sweep across all .qmd files (~370 em-dashes gone). Manual cleanup pass on the preface to fix the worst comma-splices that the mechanical pass produced.

### Code/materials structure
- Per-chapter code dirs: `src/code/chapters/NN_slug/` and `src/code/deep_dives/<slug>/`.
- Under each: `course/` (figure-generating code etc.) and `homework/solutions/`. Same skeleton for the 12 chapters and the 15 Deep Dives.
- `src/code/README.md` documents the convention and explicitly says Deep Dives get first-class treatment, not appendix treatment.

### GitHub buttons on each chapter
- Bootstrap-styled `<a class="btn btn-outline-secondary btn-sm">` with a `bi-github` icon at the top of every chapter and every Deep Dive, linking to the entry's `src/code/...` directory on GitHub.

### Python env
- Root `pyproject.toml` with `numpy, scipy, scikit-image, scikit-learn, matplotlib, torch, torchvision, transformers, datasets, huggingface_hub, accelerate`. Marked `[tool.uv] package = false`. `uv.lock` committed.
- Goal: `git clone && uv sync` is the one-command onboarding path.

### Cluster run
- Built a Gabor-emergence demo as the first runnable course code, then ran it on the `pc` cluster (CoreWeave H100s, custom `pc gpu N` CLI). First attempt mistakenly went to SkyPilot+RunPod, torn down quickly. Second attempt landed on the pc cluster correctly via a hand-written K8s pod manifest under `scratch/cluster/` (gitignored), `kubectl cp`'d the result back via the persistent login pod.
- Demo ran (3 epochs CIFAR-10 on 1×H100), but the filters were too noisy to actually show Gabor emergence. After review with the user, **the Gabor demo and the chapter 2 Gabor section were both dropped**; Gabor moved to the Interpretability Deep Dive as historical context.

## Files modified/created (high level)

Chapters: all 12 chapter qmd files rewritten/edited. Preface (`index.qmd`) rewritten and adjusted multiple times. Glossary created. References.qmd kept.

Deep dives: 15 new chapters under `src/deep_dives/`.

Materials structure: `src/code/{chapters,deep_dives}/<slug>/{course,homework/solutions}/.gitkeep`. Top-level `src/code/README.md`.

Infrastructure: `pyproject.toml`, `uv.lock`, `.env.example` (placeholder); `src/_quarto.yml` rewritten for the v5 spine, manual numbering, favicon, repo-actions, sidebar parts; `src/styles.css` with hline + spacing rules; `src/assets/{cover,icon-*,apple-touch-icon,favicon}.{png,ico}`.

GitHub: `.github/ISSUE_TEMPLATE/{errata,suggestion,plot_quality,other,config}.yml`.

Docs: this log; `docs/course_design/` consolidated; the materials README; an auto-memory for em-dashes.

Gitignored (not in repo): `scratch/cluster/gabor_pod.yaml`, `scratch/cluster/run_gabor.sh`, `.env`.

## Key decisions

- **Book scope is the v5 12-lecture spine.** Plus 15 Deep Dives. Renumbered 0..12 in the sidebar to make the alignment unambiguous.
- **Deep Dives are not appendices.** Each is a real chapter on an adjacent field. Treated as first-class in both prose framing and materials structure.
- **No prescribed per-chapter materials layout.** Each chapter gets `course/` and `homework/solutions/` and that is it; internal organization is up to whoever builds the chapter's materials.
- **One root pyproject.toml, uv-managed.** Future per-chapter extras can be added as `[project.optional-dependencies]` if any chapter's deps would bloat the common env.
- **Em-dashes are dispreferred.** Convention recorded in auto-memory; default punctuation is commas/semicolons/periods/parens.
- **Gabor-filter emergence is interpretability history, not chapter-2 phenomenology.** The naive demo is not a good example and chapter 2's framing did not earn it. Moved to the Interpretability Deep Dive.
- **Theory has been "wrong-footed," not "spectacularly wrong."** Softened framing in chapter 1 with explicit "this is the author's reading" caveat.

## Open questions / next steps

- **First real runnable demo**: still TBD. Author lean is **grokking on modular arithmetic** in chapter 7, since that is where the model-organism methodology actually pays off; small network, runs in minutes, dramatic phase-transition plot. Not built yet.
- **DVC**: not set up. Currently using `kubectl cp` for cluster→local file transfer. If outputs get larger or we want versioned course assets, set up `dvc[s3]` with `s3://cfpark00-science-of-dl/dvc-store` as the remote.
- **Word "book" vs "text"**: user flagged that "book" might be wrong. Recommended `text` as the neutral swap. Not yet applied.
- **`code-links` on Deep Dives** is in place; on chapters too. Both link patterns work, but no Deep Dive code dirs have content yet.
- **References.bib**: still has only ~10 entries from the initial scaffold. As chapters get real citations they should be added; for now most chapter references are inline plain-text (no fabricated keys).
- **Avenir Bold for plot labels**: user asked, deferred. Avenir is proprietary; for cross-platform consistency, suggested using `Nunito Sans Bold` (open) as a near-Avenir.
- **HW prompts**: every chapter/Deep Dive has an empty `homework/` directory. Content TBD.
- **Glossary definitions**: only the term list exists; actual definitions to be filled as chapters crystallize.

## Cluster artifacts (gitignored)

- `scratch/cluster/gabor_pod.yaml`: K8s pod manifest for 1×H100, mounts `/shared`, runs `uv sync` and the demo on first start.
- `scratch/cluster/run_gabor.sh`: applies the manifest, streams logs, `kubectl cp`s the output back.
- `.env`: AWS creds for whichever future cluster jobs need S3 access.

These are intentionally outside the public textbook repo.
