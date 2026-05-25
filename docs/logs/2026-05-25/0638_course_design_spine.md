# 2026-05-25 — Course Philosophy, Author Context, and 12-Lecture Spine

## Summary
Long planning session. Fixed the missing HTTPS cert for scienceofdl.com, gathered author context, articulated the course's philosophy and methodology, and converged on a 12-lecture spine (v1 → v5) with per-lecture content stubs in `docs/layout/`. No book content written yet — this was design.

## Tasks completed

### 1. Deployment fix — HTTPS for scienceofdl.com
- Diagnosed that GitHub Pages was serving the default `*.github.io` cert instead of a Let's Encrypt cert for the custom domain (`https_error: peer_failed_verification`).
- Confirmed DNS, CAA, Cloudflare proxy mode (DNS-only, intentional) were all correct.
- Resolved by toggling the custom domain via the Pages API: PUT `cname=""` → wait → PUT `cname=scienceofdl.com`. Cert provisioned in <30 minutes.
- Enabled `https_enforced: true` once cert was approved. `https://scienceofdl.com` now serves a valid cert; HTTP redirects 301 to HTTPS.
- Discussed Cloudflare proxy upsell — confirmed DNS-only is correct for this setup; updated `docs/context.md` reflects this.

### 2. Author context — Core Francisco Park
- Researched author from public sources (personal site, GitHub, CV, arXiv, Harvard CBS directory).
- Author-provided PDF CV (`CFPark_CV.pdf`) moved to `resources/core_park_web_context/` (gitignored).
- Discovered author is now **CTO of Prior Computers** (Jan 2026–current, part-time), in addition to designing the Harvard Physics grad AI/ML course launching early 2027. CBS-NTT postdoc ended Jan 2026.
- Current research thread: *"Origins and Roles of World Representations in Transformers"* (talks at MIT Isola, Northeastern Bau, CBAI).
- Compiled bio, research, publications, GitHub, CV files under `resources/core_park_web_context/`.

### 3. Course philosophy (the thesis)
- Articulated and polished the **5-step methodology** the course follows (neuroethology-inspired):
  1. Notice a phenomenon in a real NN
  2. Explore broadly → narrow to a clear question
  3. Build a synthetic model system
  4. Experiment on the model system
  5. Cross-check on the original big monster
- Course genre committed to: **"Science of Deep Learning"** — modern AI as a scientific object, neural networks as model organisms.
- Scope split clarified: this material is the **experimental-physicist** half of a joint Harvard course; the **theoretical** half (NTK, neural manifold capacity, high-dim geometry, etc.) belongs to a different prof. Material will also eventually be used as a standalone ~25-lecture full course.

### 4. Course title (working)
**"A theoretical and experimental physicist's intro to ML."** Material in this repo covers the experimental half.

### 5. 12-Lecture spine, iterated v1 → v5
Final spine (v5):

| L | Title |
|---|---|
| 1 | Introduction |
| 2 | Neural Networks and Image Classification |
| 3 | Sequence Modeling |
| 4 | Transformers |
| 5 | LLM1: Pretraining and Fine Tuning |
| 6 | LLM2: Post-training and Agents |
| 7 | Science of DL 1: Training Dynamics |
| 8 | Diffusion Models |
| 9 | Reinforcement Learning |
| 10 | World Models |
| 11 | Science of DL 2: Concept Learning |
| 12 | Science of Intelligence: From DL to General Intelligence |
| (sep) | Project presentations (not numbered) |

Key design decisions:
- L1 absorbs philosophy + brief AI/FM/NN gesture (Harvard grad physicists already know basics).
- L3 reframed as a **memory problem** (SSM vs Transformer) — gives the lecture a phenomenon hook.
- L5/L6 split LLMs cleanly by pretraining vs post-training.
- **Real RL (L9) comes AFTER LLMs** because RLHF in L6 was characterized as "reward model + weighted SFT, not real RL" — no forward reference to undefined RL.
- Two named **"Science of DL" pillars** (L7, L11) — distinctive structural choice.
- L11 drifts from concrete to philosophical ("what is a concept" → "learning at abstraction scales"), setting up L12.
- L12 ends on a question, not a topic list — capstone vibe.

### 6. Documentation artifacts created
- `docs/course_design/topics_dump.md` — raw keyword brain-dump from author (~108 terms), seed for future glossary.
- `docs/course_design/lecture_outline.md` — v5 spine summary with design rationale.
- `docs/layout/README.md` — course-wide context, audience, voice, philosophy, spine, out-of-scope, pending questions.
- `docs/layout/l{1..12}/content.md` — verbose per-lecture gist files capturing all implicit knowledge from this session (so next session can start with zero context).
- `docs/layout/next_session.md` — onboarding doc for the next session: what's done, what to do next, what NOT to do.

### 7. Memory updates (auto-memory system)
- `user_role.md` — updated to reflect CTO of Prior Computers + Harvard course designer.
- `project_course.md` — updated with v5 framing, scope split, "science of DL" genre.
- `MEMORY.md` — index updated.

## Files modified / created

**Tracked (in repo):**
- `docs/context.md` — added science-of-DL framing and out-of-scope list
- `docs/course_design/topics_dump.md` — new
- `docs/course_design/lecture_outline.md` — new (v5)
- `docs/layout/README.md` — new
- `docs/layout/l{1..12}/content.md` — 12 new files
- `docs/layout/next_session.md` — new
- `docs/logs/2026-05-25/0638_course_design_spine.md` — this file

**Local-only (gitignored):**
- `resources/core_park_web_context/*` — bio, CV, pubs, GitHub, links + the author-provided PDF CV

**Outside repo (auto-memory):**
- `~/.claude/projects/.../memory/user_role.md`
- `~/.claude/projects/.../memory/project_course.md`
- `~/.claude/projects/.../memory/MEMORY.md`

## Key decisions / insights

- HTTPS toggle trick is the standard fix for stuck GH Pages cert provisioning. Recorded for future runbook.
- The author's *own* published research voice ("model organism," "synthetic experiments," "phenomenology") is the textbook's pedagogical voice. Don't invent a different register.
- The course's value is its *perspective*, not its topic coverage. Pure-topic encyclopedism is the failure mode to avoid.
- "Science of DL 1/2" as named pillars is the most distinctive structural choice — most ML courses bury those phenomena.
- L1 → L11 → L12 has a deliberate arc from manifesto → concrete phenomena → expanded notion of intelligence. The ending should leave students with questions, not a checklist.

## Open questions / next steps

- **Content authoring hasn't started.** `src/` is still the default Quarto scaffold. Next session likely picks a lecture (L1 or L7 are natural starts) and drafts into `src/chapters/`.
- **HW** is only specified for L1, L5, L6; all others TBD.
- **Phenomenon hooks** for L4 and L6 are TBD — author said "fine to handle at content-writing time."
- **Glossary** — `topics_dump.md` is the seed; convert to `src/glossary.qmd` once lectures stabilize.
- **L1 phrasing** — "second half" framing assumes the joint Harvard offering; needs rewording for the eventual standalone full course.
- **Inference-time compute / reasoning** is currently a bullet in L6 — might deserve more weight.
- **L10 (World Models)** is lighter after continual learning moved to L11 — could absorb Dreamer/MuZero.

## Loose ends NOT addressed this session

- Project-presentation session format (separate from L12).
- Whether the book and lectures should map 1:1 or have different structures.
- Slides (separate from book) — author's preference unclear.
- Code companion notebooks vs inline code.
