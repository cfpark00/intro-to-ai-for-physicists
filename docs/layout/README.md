# Layout

Working layout for the 12-lecture spine. Each `lN/content.md` is the gist of what that lecture covers — verbose enough that someone reading just that file (with this README) can understand the lecture's purpose, content, and pedagogical intent.

**Next session must read this README first, then read `next_session.md`, then visit individual `lN/content.md` files.** The next session starts with ZERO context — everything needed lives in this folder, in `docs/context.md`, and in `docs/course_design/`.

---

## Course-wide context

### What this is
A web textbook + the source material for a **Harvard Physics grad-level AI/ML course launching early 2027.** The book is hosted at <https://scienceofdl.com>.

### Course title (working)
**"A theoretical and experimental physicist's intro to ML."** This material covers the **experimental physicist** half. A different professor handles the **theoretical** half (NTK, neural manifold capacity, high-dimensional geometry, etc.) — those topics are explicitly out of scope here.

This material will *also* eventually be used as a standalone full course (~25 lectures planned for that version). When reading anything in this folder that says "second half," remember it'll need rewording for the standalone form.

### Genre
**Science of Deep Learning.** Treat modern AI as a *scientific object* — phenomena to surface through controlled synthetic experiments, mechanistic probing, and phenomenology. Neural networks as model organisms. Not a software tutorial. Not a pure theory exposition.

### Audience
Harvard physics grad students. Comfortable with linear algebra, calculus, probability, statistical mechanics. Fast at quant. They already know what MLPs and SGD are — don't waste lectures re-establishing that.

### Lead author / authorial voice
Core Francisco Park (cfpark00). PhD Harvard Physics 2025 — thesis *"Deep Learning as a Scientific Tool and a Model Organism of Intelligence."* Currently CTO of Prior Computers (part-time) + course design. Research voice: model-organism framing, synthetic-task experiments, phenomenology of training dynamics. See `resources/core_park_web_context/` (gitignored) for full bio, CV, publications.

Author's voice is **conversational, anti-encyclopedic, frontier-focused.** Examples: "before diving into getting GPUs hot..." / "feel free to also not think in the theory way" / "RL is its own world — most of RL we'll just say 'go take an RL class for that'." Don't try to cover everything; explicitly hand off topics outside scope.

---

## Philosophy (5-step methodology — taught explicitly in L1, revisited in L7 and L11)

The course mostly follows how physicists study biological systems. Neural networks in their natural habitat — designed for performance, trained on real-world data — are a big mess, not a cleanly defined problem. To make scientific progress, borrow from **neuroethology**: the study of the neural basis of natural animal behavior in its ecological context.

The guiding workflow:

1. **Notice a phenomenon.** Start from an interesting behavior actually observed in a real neural network.
2. **Explore broadly.** Through open-ended exploration, narrow the phenomenon down to a clear question.
3. **Build a model system.** Develop a synthetic, controllable model that reproduces the phenomenon — small enough to instrument fully.
4. **Experiment on the model system.** Run the kinds of experiments the original network doesn't allow.
5. **Cross-check.** Bring the findings back to the original big monster and verify.

The order won't always be strict — sometimes a theoretical hunch comes first, sometimes a model system precedes a crisp question — but this is the guiding philosophy.

Direct neuroethology parallel: observe animals → find specific behavior (better if shared across species) → opens a clear question → run experiments on a model-organism animal (Drosophila, *C. elegans*, zebrafish), often open-endedly → bring it back to the original animal.

"Overall, the science here is close in spirit to neurophysics, but takes a heavily experimental approach."

---

## 12-Lecture Spine (v5, agreed 2026-05-25)

| L | Title | One-liner |
|---|---|---|
| 1 | Introduction | Philosophy, thesis, short history of ML/DL/AI, neuroethology parallel, bitter lesson |
| 2 | Neural Networks and Image Classification | Start the historical thread; phenomenon = "why did it take so long?" + Gabor-filter emergence |
| 3 | Sequence Modeling | Memory as the central question; SSM-style state vs Transformer-style "no compression" |
| 4 | Transformers | Architecture deep dive; the no-compression extreme paid off |
| 5 | LLM1: Pretraining and Fine Tuning | Scale, foundation models, SFT, scaling laws, emergence, ICL (intro) |
| 6 | LLM2: Post-training and Agents | RLHF/DPO, reasoning, inference-time compute, agents, RAG, evals |
| 7 | Science of DL 1: Training Dynamics | Methods of scidl + grokking, double descent, generalization, ICL phenomena |
| 8 | Diffusion Models | Probabilistic generation, model collapse |
| 9 | Reinforcement Learning | Real RL — different from supervised training; hard problems |
| 10 | World Models | World modeling + theory-of-mind-style debates; user's "Origins of World Representations" research |
| 11 | Science of DL 2: Concept Learning | Concept learning, compositional gen, continual learning, "what is a concept", cogsci, abstraction scales |
| 12 | Science of Intelligence: From DL to General Intelligence | Evolution, multi-agent, QD, open-endedness, creativity, "learning" broadly — broader than task-learning |
| (sep) | Project presentations | Separate session, not numbered as L13 |

### Arc
- **L1–L7: Fundamentals & methods.** Thesis, model classes (IC, sequence, transformer, LLM, diffusion), training dynamics. *Wait* — note that with the v5 ordering, LLMs come in the middle of fundamentals because they're treated as a natural continuation of transformers; diffusion and RL come after as "the other major paradigms."
- **L8–L12: Beyond LLMs into the broader scientific picture.** Diffusion, real RL, world models, concept learning, intelligence broadly.

### Key cross-references between lectures
- L1 5-step methodology → revisited in L7, L11 (the two "Science of DL" lectures)
- L2 "bigger is better" (first bitter lesson) → sets up L5 scaling laws
- L3 memory framing → L4 (transformers as no-compression extreme)
- L4 transformers → L5 LLMs scaled up
- L5 introduces ICL → revisited in L7 (phenomenon), L11 (concept acquisition)
- L7 training dynamics phenomena → companion to L11 concept dynamics (numbered pair: "Science of DL 1/2")
- L6 RLHF treated as "not really RL, just reward model + weighted SFT" → real RL is in L9
- L9 RL → L10 world models in RL (Dreamer/MuZero), L11 continual learning, L12 multi-agent/evolution
- L10 world models → user's current research thread ("Origins and Roles of World Representations in Transformers")
- L11 → L12 bridge: "what is a concept" is ill-defined → "learning at different abstraction scales" → intelligence is broader than task-learning

---

## Out-of-scope reminders

- **ML theory** (NTK, neural manifold capacity, high-dim geometry, generalization bounds, lottery-ticket theory) — covered by the **theoretical-physicist half** of the course (different prof). Don't duplicate.
- **Classical ML** (SVMs, kNN, decision trees, random forests) — covered well by other textbooks. Skip.
- **Software/engineering tutorials** ("how to train your LLM," kubernetes, MLOps) — these are recipes, not science. Out.

---

## Pending design questions (not blocking, but unresolved)

- Should L4 and L6 each have a more explicit phenomenon hook? (Author lean: fine to handle at content-writing time, not a planning issue.)
- Where does interpretability get headline weight? Currently a small slot in L7. Could expand if author decides it deserves more.
- Inference-time compute / reasoning is currently a bullet in L6 — frontier topic in 2026, may deserve more weight inside L6 or even a sub-section.
- L10 (World Models) is lighter than earlier versions (continual learning moved to L11). Could absorb world-model-in-RL (Dreamer, MuZero) to give it more body.
- HW is only specified for L1, L5 (the BC vs RL exp), L6 (PT vs FT exp). All other lectures: HW TBD.

---

## Topics that don't yet have a clear lecture home
From the topic dump in `docs/course_design/topics_dump.md`, these terms haven't been firmly mapped:

- **perception, action** — abstract; threads through L2/L9/L10 implicitly
- **nerfs** — could fit L8 (generative) or be skipped
- **knightian uncertainty, aleatory/epistemic uncertainty** — could be L8 (probabilistic) or L9 (RL) or L12 (intelligence broadly)
- **gaussianity** — L8 maybe
- **shape vs texture** — could be a phenomenon mention in L2 (ImageNet-era debates) or skipped
- **individuality** — author's industry focus; could appear in L12 broader-intelligence context or skip
- **active learning** — could go in L9 (RL-adjacent) or L5 (data efficiency) or skip
- **EM algorithm** — classical, could appear in L8 (VAE prereq) or skip

Flag these at content-writing time.

---

## Locations of related artifacts

- `docs/context.md` — overall project context (tech stack, deployment, scope)
- `docs/course_design/topics_dump.md` — raw keyword list (will become the glossary seed)
- `docs/course_design/lecture_outline.md` — earlier outline summary (may be slightly behind v5)
- `docs/layout/lN/content.md` — per-lecture gist (this folder)
- `docs/layout/next_session.md` — what to do next
- `resources/core_park_web_context/` — author bio/CV (gitignored)
- `src/` — the Quarto book itself (mostly empty scaffolding currently)
