# L11 — Science of DL 2: Concept Learning

> Read `../README.md` first.

## TL;DR
The second of the two **named Science-of-DL pillars** (the first is L7). Technically: **concept learning, compositional generalization, continual learning**. Conceptually: the lecture *slowly drifts* from technical-concept-learning into "what is a concept" → cogsci ties → human priors → **"learning at different abstraction scales"**, setting up L12's expanded notion of intelligence.

## Aim (user's verbatim)
"L11: Science of DL 2: Concept Learning. will cover mostly concept learning, compositional generalization, and continual learning topics. -> slowly move into a more general debate."

And: "L11 will also play the role of connecting to cogsci and human priors."

And (the lecture's deepest move):
> "Actually L11 will kinda nicely merge into: what is a concept is actually ill-defined! ICL learn a new concept? Continual learning is about keep acquiring new concepts. Maybe that — and having a rationality without info — is really what learning is about: 'learning at different abstraction scales'"

## Phenomenon hooks
- **Concept learning** — networks learning discrete, reusable abstractions during training. Author's research (concept-learning repo, *Emergence of Hidden Capabilities*, *Swing-by Dynamics*).
- **Compositional generalization** — networks combining learned concepts in novel ways. (Or failing to.)
- **Continual learning** — networks acquiring new concepts over time without forgetting old ones.
- **Concept ambiguity** — "what is a concept" — the discovery, mid-lecture, that the technical phenomena point to a deep ill-definition.

## Topics

### Technical: Concept learning in NNs
- What does it mean for a network to learn a "concept"?
- Author's research framework: concept space, concept signal, learning dynamics in concept space.
- *Emergence of Hidden Capabilities* — concepts can be present in the model but not yet elicitable (NeurIPS 2024 Spotlight).
- Latent interventions vs naive prompting — the gap reveals hidden capabilities.

### Technical: Compositional generalization
- Combining learned concepts to generalize to unseen combinations.
- Author's research: *Swing-by Dynamics in Concept Learning and Compositional Generalization* (Yang, Park et al.).
- Networks generalize *sequentially*, respecting compositional hierarchy.
- Novel non-monotonic learning dynamics in early training.
- The SIM (Structured Identity Mapping) task as a model system.

### Technical: Continual learning
- Hard continual learning — *not* just avoiding loss of plasticity. The hard problem is: keep adapting to new worlds by having a good *updatable* world model. Very different from passive gradient updates. (This framing was originally in L10 but moved here when L10 was trimmed.)
- Catastrophic forgetting as classical baseline.
- Modern approaches: rehearsal, regularization, modular methods.
- Why continual learning is unsolved at scale.

### The drift into "what is a concept" (lecture pivot point)
- Once you've taught compositional generalization and continual learning, the question naturally arises: **what counts as a concept?**
- ICL learns a "new concept" from a prompt — is that the same as learning a concept via gradient descent?
- Continual learning is about keep-acquiring-concepts — but you can't define "acquire" without defining "concept."
- "Having a rationality without info is really what learning is about" — the author's gnomic but useful framing.
- **"Learning at different abstraction scales"** — the proposed reframing. Some learning happens at the level of pixels, some at concepts, some at meta-concepts, some at scientific frameworks.

### Cogsci & human priors (the closing arc)
- Connection to cognitive science: how do humans learn concepts? Children, language acquisition, learning hierarchies.
- Human priors / inductive biases — what we come pre-loaded with.
- Connection to author's *Vision Language Models Inherit Human Color Perception* (ICLR 2026 workshop) — VLMs absorb human-shaped priors via training data.
- This sets up L12: if concepts are abstraction-scale phenomena, then "intelligence" is even broader than just learning concepts.

## HW
TBD. Candidates:
- Reproduce a small concept-emergence experiment.
- Write a short essay on "what is a concept" using one technical example.

## Cross-references
- **L7 (Science of DL 1)** — companion pillar. L7 covered training-dynamics phenomena; L11 covers concept-acquisition phenomena.
- **L1** 5-step methodology — explicitly recalled.
- **L5 (LLM Pretraining)** ICL — reintroduced here as concept acquisition.
- **L10 (World Models)** — "what is a concept" parallels "what is a world model."
- **L12 (Intelligence broadly)** — direct setup. The closing of L11 (abstraction scales) is the opening of L12.
- **Author's research** — central to this lecture: *Concept Space* paper, *Swing-by Dynamics*, *Emergence of Hidden Capabilities*, ICLR papers.

## Open questions / TBDs
- Order: technical-first then drift to abstract, or interleave? Lean: technical first, drift toward the end.
- How much cogsci tie-in — full digression or just a slide or two?
- Whether to formally introduce "abstraction scales" as a named concept or keep it informal.
- Author noted "having a rationality without info" is part of the framing — needs unpacking at writing time.

## Author voice notes
- This lecture has the *most distinctive voice* in the course — drifts from concrete to philosophical with deliberate pacing.
- Channel the "what is X actually" energy — the lecture rewards students for sitting with definitional uncertainty rather than rushing to closure.
- "Slowly move into a more general debate" — user explicitly wants the lecture to feel like a gradual zoom-out.
