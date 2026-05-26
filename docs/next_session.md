# Next Session: Per-Lecture Flow Plan

All 12 lectures already have draft chapters (`src/chapters/NN_*.qmd`, ~80–120 lines each). All 16 Deep Dives have at least a substantive sketch. This document is the per-lecture flow plan for the next authoring session: for each lecture, the canonical section sequence with a one-line role per section, then the concrete next moves to bring the draft into alignment with the plan.

This doc is the *current* spec. The older gist files in `docs/course_design/lN/content.md` are richer background but in places describe planning decisions that have since been reconsidered (notably continual-learning placement, see below). When the two disagree, this doc wins.

## How to use

1. Open `src/chapters/NN_*.qmd` for the lecture you are working on.
2. Compare its H2 sequence against the **Section flow** here.
3. Execute the **Next-session moves**. Skip lectures whose draft is already aligned.

Reference docs:
- `docs/context.md` — project context.
- `docs/course_design/README.md` — course-wide context, philosophy, audience, voice.
- `docs/course_design/lN/content.md` — per-lecture gist (background, *not* spec).
- `src/chapters/NN_*.qmd` — current draft (canonical state).

## Cross-lecture decisions to lock in

- **Continual learning lives in L10**, bundled with world models under the framing "a world model is only useful if it stays accurate." The gist `l11/content.md` still says continual learning is in L11; that is stale. Either keep the gist as historical or trim it. **Do not move the section.**
- **5-step methodology** is introduced in L1 and revisited in L7 and L11. Whenever any of those three is rewritten, re-check that the cross-references and the framing language stay live.
- **Bitter lesson** thread: quoted in L1, foreshadowed in L2 ("bigger is better"), cashed out in L5 (full scaling laws). Keep this through-line visible.
- **ICL** is *introduced* in L5, *dissected* in L7, *philosophically revisited* in L11. Three different treatments, do not collapse them.
- **Author's own papers** are cited illustratively, not exhaustively. The current pattern is: ICL phase transitions and hidden capabilities in L7, world representations in L10, Swing-by / SIM in L11, diffusion-for-cosmology in L8. Keep that distribution roughly stable.

---

## L1 — Introduction

**Section flow:**
1. **The thesis: NNs as model organisms** — frames the genre, sets the voice.
2. **The 5-step methodology** — workhorse, revisited L7/L11.
3. **A short, opinionated history** — connectionism vs symbolism, AI winters, the "things were hated at various times" arc.
4. **The bitter lesson** — what it claims and (importantly) what it doesn't.
5. **A very brief gesture at the substrate** — NN, SGD, foundation models in ~5 min. Physicist audience already knows MLPs.
6. **Where we are going** — chapter signposting.

**Next-session moves:**
- Audit for any leftover "welcome to the second half" framing; reword for standalone.
- Tighten §5 to really be ~5 minutes of text.
- Make sure the "over-parametrized generalization will look weird, you'll see it dissected in L7" hook is visible.

---

## L2 — Neural networks and image classification

**Section flow:**
1. **Neural networks, properly** — MLPs, SGD, optimizers (SGD → momentum → Adam → AdamW), init, normalization, residuals, hyperparams, GPU note.
2. **Image classification, specifically** — CNNs, translation equivariance, ImageNet, AlexNet/VGG/ResNet arc.
3. **Inductive bias vs compression** — what the network actually learns; representations as compression.
4. **The first bitter lesson: bigger is better** — sets up L5.

**Next-session moves:**
- Surface the **Gabor-filter emergence** phenomenon hook prominently (it's the natural physicist/neuroscience entry point). The gist flags it; verify it's in the draft with the right framing, not buried.
- Check whether the "why did NNs take from the 1940s to 2012" hook is still in the draft; if not, add a paragraph.
- Confirm CNN HW (train + inspect first-layer filters vs Gabor) is in the code subtree.

---

## L3 — Sequence modeling

**Section flow:**
1. **Memory as the central problem** — what is "memory" in a sequence model. The two philosophies: compress (state) vs do not compress (attention).
2. **Historical sequence models (briefly)** — RNN → LSTM → GRU → wall.
3. **The state-space resurgence** — Mamba, S4. Control-theory hook for physicists.
4. **Attention as the move that unlocked it** — preview only, deep dive lives in L4.
5. **Next-token prediction** — cross-entropy, perplexity, "why so simple works."
6. **Where to next** — bridge to L4.

**Next-session moves:**
- Ensure the "compress vs do-not-compress" framing is the explicit spine, not just a passing comparison.
- §4 should *not* steal §L4's thunder; keep attention here gestural.

---

## L4 — Transformers

**Section flow:**
1. **Attention, the core invention** — Q/K/V, scaled dot-product, soft/differentiable/parallel, O(N²).
2. **The residual stream** — computational substrate, not just a training trick. Pays off in L7.
3. **MLPs, per-token processing** — why the alternation matters.
4. **Multi-head attention** — different "circuits" for different patterns.
5. **Positional encoding** — sinusoidal, learned, RoPE; where memory-of-order lives.
6. **Causal masking and the training loss** — auto-regressive training mechanics.
7. **Transformer economics: KV cache and mixture of experts** — what matters at scale.
8. **Variants & history** — brief.
9. **Where this is going** — bridge to L5.

**Next-session moves:**
- L4 was flagged in the prior session as "most topic-bin-shaped" and needing a **phenomenon hook**. Candidate hooks from the gist: residual stream as a circuit substrate (already foreshadowed in §2), attention → ICL (handed off to L5/L7). Pick one and surface it in §1 or §2 to give the lecture a phenomenological frame, not just a tour of mechanics.
- §7 (economics) is at risk of becoming a software-engineering tangent; keep it short and motivated.

---

## L5 — LLM pretraining

**Section flow:**
1. **Pretraining** — next-token at scale, tokenization, data-centric ML, self-supervised broadly (SimCLR, CLIP).
2. **The scaling story** — Kaplan, Chinchilla, scaling laws, GPU parallelism (DP/TP/PP/FSDP) just enough to motivate the difficulty.
3. **Emergence at scale** — phenomenon; mention the "real vs metric-artifact" debate (Schaeffer et al.).
4. **In-context learning** — phenomenon introduced; deep dissection deferred to L7.
5. **Fine-tuning** — bridge into post-training (L6).
6. **Where the LLM story continues** — pointer to L6.

**Next-session moves:**
- Confirm scaling-law functional forms are stated (not just gestured at).
- Make sure the **emergence** discussion previews L7's concept-space framing without spoiling it.

---

## L6 — LLM post-training and agents

**Section flow:**
1. **Post-training methods** — RLHF (with the author's "RLHF is meh, ~weighted SFT" framing), DPO, instruction tuning, distillation, calibration.
2. **Reasoning and inference-time compute** — CoT, System 1/2, inference-time scaling, RL-for-reasoning + the author's GRPO/execution-vs-planning paper.
3. **Agents and tool use** — policy + tools + scaffolding; reliability bottleneck.
4. **RAG** — retrieval, limits, the long-context-vs-RAG hybrid.
5. **Evals** — benchmark saturation, capability-vs-alignment evals, noise on terminal-difficulty benchmarks. (Deep treatment now lives in the **AI evaluation** Deep Dive — cross-reference it here.)
6. **Vision-language and omni-models, briefly** — VLMs, internal-rep angle.
7. **Where this chapter sits** — bridge into L7.

**Next-session moves:**
- §2 (inference-time compute / reasoning) deserves *more* weight than its current size suggests, per the prior session's flag. Consider expanding the inference-time-compute scaling discussion with a concrete schematic.
- §5 should now explicitly hand off the methodology of evaluation to the **AI evaluation Deep Dive** rather than re-litigating it inline.
- The "RLHF is not real RL" framing should not be repeated in L9; here it lives, L9 should reference it once.

---

## L7 — Science of deep learning I: training dynamics

**Section flow:**
1. **A brief intro to the methods of science-of-DL** — methodology recap from L1 with concrete examples; probes/interventions/ablations sketched.
2. **Phenomenon: double descent.**
3. **Phenomenon: the generalization mystery** — over-parametrization, physicist's classical-stat-thinking shock.
4. **Phenomenon: in-context learning, dissected** — author's *Competition Dynamics* (ICLR 2025 spotlight) and *ICLR: In-Context Learning of Representations* (ICLR 2025). Phenomena only, the philosophical question goes to L11.
5. **Phenomenon: grokking** — generalization long after loss converges; phase-transition-in-learning framing.
6. **Other training-dynamics phenomena** — lottery ticket, sharpness/flatness, **emergence in concept space** (author's NeurIPS 2024 spotlight *Emergence of Hidden Capabilities*).
7. **A light touch on interpretability methods** — probing, SAEs, circuits gestural; deep treatment is the Interpretability Deep Dive.
8. **What this chapter set up** — bridge.

**Next-session moves:**
- This is the most distinctive lecture; protect the voice. The author's "neural networks as model organisms" framing should feel concrete by the end of §1, not still abstract.
- §4 must stay phenomenological; if you find yourself defining "concept" carefully, you have drifted into L11 — push that material there.
- §7's pointer to the Interpretability dive should be one paragraph, not a full section.

---

## L8 — Diffusion models

**Section flow:**
1. **The probabilistic view** — generative modeling as learning a distribution; quick survey of pre-diffusion approaches (VAE, GAN, NF) and why diffusion won.
2. **Diffusion: the main event** — forward noising, reverse denoising, score matching, DDPM, sampling/quality trade.
3. **Flow matching** — more general framing; why it scaled.
4. **The phenomenon: model collapse** — recursive training on synthetic data degrades the model; what it implies for the "just train on more data" stance.
5. **Applications and the physics connection** — author's diffusion-for-cosmology work (*Probabilistic reconstruction of Dark Matter fields*, *Debiasing with Diffusion* — ApJ 2024).
6. **Where this fits in the book** — bridge.

**Next-session moves:**
- §4 (model collapse) is the phenomenon hook; make sure it lands hard, not as an afterthought.
- §5 is a natural place to lean physicist-friendly; expand if pacing allows.

---

## L9 — Reinforcement learning

**Section flow:**
1. **Why RL is different** — the data is generated by the policy; supervised vs RL contrast; the "but in some sense quite similar" caveat.
2. **Minimal RL machinery** — MDPs, policy gradient (REINFORCE, actor-critic), PPO, DPO (revisited as contrast to L6's framing), on-policy vs off-policy.
3. **The hard problems** — credit assignment, sparse reward, exploration/exploitation, long horizon, reward hacking.
4. **Modes of RL** — offline RL, model-based RL (bridge to L10).
5. **A note on RL for LLM reasoning** — short, reference L6's framing once.
6. **Where RL fits in the broader picture** — bridge to L10, and gesture to L12's multi-agent.

**Next-session moves:**
- §1 should establish *the* RL framing in one striking sentence ("the data is generated by the policy") — verify the draft opens with this.
- §5 must not re-litigate L6; one paragraph, then point back.

---

## L10 — World models and continual learning

**Section flow:**
1. **What does "world model" mean?** — operational definition; why the definition is fuzzy and why that's worth saying.
2. **World models in RL** — Dreamer, MuZero; why model-based RL hasn't decisively won.
3. **World representations in transformers** — author's *Convergent World Representations and Divergent Tasks* (2026), *When does Observational Data Teach Latent Dynamics?* (ICLR 2026 workshop), *Vision Language Models Inherit Human Color Perception* (ICLR 2026 workshop).
4. **Continual learning** — the soft (forgetting, EWC, rehearsal) vs hard (Bayesian-style updating of a structured model) versions; the hard version is the world-model framing.
5. **The "shit-show debates" subset** — "does X have a world model / theory of mind", how to contribute meaningfully despite the ill-definition.
6. **A light touch on neuroscience** — place cells, grid cells, predictive coding; brief.
7. **Where this fits** — bridge.

**Next-session moves:**
- Keep continual learning in L10 (do not move it to L11; the older gist is stale on this).
- Prior session flagged §2 could absorb **Dreamer/MuZero deeper** — verify the current depth, expand if pacing allows.
- §5 ("shit-show debates") is doing meta-skill work — flag it as such in §1 so students know what they are being trained in.

---

## L11 — Science of deep learning II: concept learning

**Section flow:**
1. **Concept learning in NNs (technical)** — author's concept-space framework; *Emergence of Hidden Capabilities* (NeurIPS 2024 spotlight); latent interventions vs naive prompting.
2. **Compositional generalization** — author's *Swing-by Dynamics in Concept Learning and Compositional Generalization*; SIM (Structured Identity Mapping) task as model system; non-monotonic learning dynamics.
3. **The drift: what is a concept, anyway?** — mid-lecture pivot from concrete-technical to philosophical-open. This drift *is* the argument.
4. **Learning at different abstraction scales** — concepts at different scales; ICL-as-concept-acquisition vs gradient-as-concept-acquisition; "having a rationality without info is what learning is about."
5. **Cogsci and human priors** — pointer to the Cognitive Science Deep Dive; *Vision Language Models Inherit Human Color Perception* may be referenced here too if not over-cited in L10.
6. **Closing** — bridge into L12.

**Next-session moves:**
- The mid-lecture drift is the most distinctive moment in the whole course. Protect the pacing — don't smooth the transition between §2 and §3.
- This lecture **does not** contain a continual-learning section; that lives in L10. Verify no leftover continual-learning paragraphs were copied here from older gist plans.
- If §1 spends too long on technical setup, the drift in §3 won't land. Cut technical detail if needed to preserve the philosophical pivot.

---

## L12 — Science of intelligence

**Section flow:**
1. **Where we are coming from** — recap L11's closing; if learning lives at multiple abstraction scales, intelligence is broader than any single learning process.
2. **Evolution as a learning process** — natural selection as optimization; evolutionary methods in ML; gradient-free RL settings.
3. **Multi-agent intelligence** — self-play (AlphaGo/Zero), Nash, MARL, cooperative/competitive dynamics, intelligence as population-property.
4. **Quality-diversity** — search for diverse high-quality solutions; novelty search, MAP-Elites.
5. **Open-endedness** — POET, OMNI-EPIC; the aspiration of indefinite challenge/capability generation.
6. **Creativity** — what counts as creativity for a learned system; ill-defined, gesture only.
7. **Learning, in the expansive view** — the through-line that ties §2–§6 together.
8. **Some adjacent threads, briefly** — pointer-paragraphs to Deep Dives (Neuroethology, Open-endedness, Cogsci, AI for science, Mechanism design).
9. **Capstone: closing the course** — what the course tried to teach beyond the technical content.

**Next-session moves:**
- L12 is at risk of being a grab-bag (flagged in the prior session). §7 ("Learning, in the expansive view") is the synthesizing section that prevents that — make sure it is genuinely synthesizing, not just summarizing.
- §8 should be short, dense, and explicitly pointer-shaped. If a thread needs more than two sentences, it belongs in its Deep Dive, not here.
- §9 (capstone) is the last impression of the course; spend disproportionate care on it.

---

## After this session

If all 12 lectures are aligned, the next natural pass is:
1. Per-chapter HW: verify each `src/code/chapters/NN_*/homework/` has at least one prompt + a solution.
2. Deep-dive content quality: 16 dives, several still skeleton-only. Pick the most-visited ones first (Interpretability, AI evaluation, Theory, Systems).
3. Figures and `[Plot]` callouts: the chapters are full of placeholder `[Plot]` notes; resolve them to actual rendered figures from `src/code/chapters/.../course/`.
