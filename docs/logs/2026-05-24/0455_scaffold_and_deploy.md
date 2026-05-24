# Session log — 2026-05-24, scaffold and deploy

## Summary

Scoped, scaffolded, and deployed an empty-but-real Quarto book for the **"Intro to AI for Physicists"** textbook. Site is built on the `gh-pages` branch; live at `scienceofdl.com` once user-side DNS propagates.

## Decisions made

- **Framework: Quarto** (MIT, Posit). Chose over Jupyter Book (less notebook-native is actually a feature here), MkDocs Material (weaker for math/code textbooks), and Astro Starlight (too web-dev-flavored).
- **Hosting: GitHub Pages**, custom domain `scienceofdl.com`. Rejected Vercel/Netlify/Cloudflare Pages — user explicitly does not want SaaS dependencies.
- **DNS: Cloudflare, proxy OFF (gray cloud).** Necessary for Let's Encrypt cert provisioning to work and to avoid SSL-mode redirect loops.
- **Repo layout:** Quarto book lives in `src/`, output to `src/_site/` (gitignored). Kept `src/` per repo template's "one source dir" convention even though Quarto idiomatically lives at root.
- **Scope: deliberately skips classical ML survey material** (SVMs, kNN, trees). Focus is post-2017 paradigm — transformers, scaling laws, LLMs, RL post-training, reasoning, diffusion, inference.

## Tasks completed

- Installed Quarto 1.9.37 locally via the official `.deb`.
- Created `src/_quarto.yml` with book config, sidebar parts, KaTeX math, light/dark theme.
- Wrote `src/index.qmd` (preface).
- Wrote 10 chapter `.qmd` files (~100–200 lines each) with real intro/framing content — not just stubs:
  1. The modern AI landscape
  2. A deep learning primer
  3. The transformer
  4. Scaling laws (includes an executable Python power-law fit)
  5. Pretraining LLMs
  6. Fine-tuning (SFT, LoRA, distillation)
  7. RL for LLMs (RLHF, DPO, RLVR, GRPO)
  8. Reasoning and test-time compute
  9. Diffusion and score-based models
  10. Inference
- Added `references.qmd`, `references.bib` (10 starter citations), `styles.css`.
- `src/CNAME` with `scienceofdl.com`, configured as a Quarto `resources:` entry so it gets copied to the output.
- `.github/workflows/publish.yml` — renders Quarto and publishes to `gh-pages` via the official `quarto-dev/quarto-actions/publish@v2` action.
- Updated `.gitignore` to exclude `_site/`, `.quarto/`, `_freeze/`, Python artifacts.
- Filled in `docs/context.md` (was a TODO stub) and `README.md` (was a TODO stub).
- `git init`, initial commit, `gh repo create cfpark00/intro-to-ai-for-physicists --public --push`.
- Bootstrapped the orphan `gh-pages` branch (the Quarto publish action requires it to already exist).
- Re-ran the publish workflow; site successfully built. GitHub Pages auto-detected the CNAME and configured custom domain.

## What still needs the user

- Add 5 DNS records at Cloudflare for `scienceofdl.com` (4 × A `@` → GitHub IPs, 1 × CNAME `www` → `cfpark00.github.io`), all with proxy OFF.
- Once DNS resolves, ask me to verify and flip the **Enforce HTTPS** toggle (`gh api -X PUT /repos/.../pages -F https_enforced=true`).

## Open questions / next session

- User said "next session we will start writing." Most chapters currently have intro framing + section outlines but are not yet finished textbook chapters. Next session: pick chapters to flesh out first. Most natural order: 1 → 2 → 3 → 4, then probably 9 (diffusion) since it's the most self-contained and most physicist-friendly.
- Should we add a `quarto preview` workflow / make target / convenience script? Currently just `cd src && quarto preview` by hand.
- Author name in `_quarto.yml` is set to `cfpark00`. Real name would be nicer once user confirms.
- No figures yet. `src/figures/` exists but is empty. As chapters get fleshed out, we'll need real diagrams (residual stream, attention pattern, scaling-law plot).
- Decide whether to enable JupyterLite / Pyodide for in-browser code execution (vs. just static code blocks) — punt until at least one chapter is in good shape.

## Files created/modified this session

```
A  .github/workflows/publish.yml
A  .gitignore                     (extended)
A  README.md                      (rewritten from stub)
A  docs/context.md                (filled in)
A  docs/logs/2026-05-24/0455_scaffold_and_deploy.md  (this file)
A  src/_quarto.yml
A  src/CNAME
A  src/chapters/01_landscape.qmd
A  src/chapters/02_dl_primer.qmd
A  src/chapters/03_transformer.qmd
A  src/chapters/04_scaling_laws.qmd
A  src/chapters/05_pretraining.qmd
A  src/chapters/06_finetuning.qmd
A  src/chapters/07_rl.qmd
A  src/chapters/08_reasoning.qmd
A  src/chapters/09_diffusion.qmd
A  src/chapters/10_inference.qmd
A  src/index.qmd
A  src/references.bib
A  src/references.qmd
A  src/styles.css
A  src/figures/                   (empty dir, placeholder for later)
```
