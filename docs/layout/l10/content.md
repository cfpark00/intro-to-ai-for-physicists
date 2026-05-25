# L10 — World Models

> Read `../README.md` first.

## TL;DR
World modeling — what it means for a network to have an internal model of the world. Connects directly to the author's **current research thread**: *"Origins and Roles of World Representations in Transformers."* Carries the world-model-specific subset of the "shit-show debates" framing: does X have a world model? Theory of mind? (Continual learning, originally bundled here, moved to L11.)

## Aim
After continual learning moved out to L11, L10 is now focused specifically on **world modeling**. The "shit-show debates" framing the author introduced earlier still applies, but trimmed to world-model-adjacent debates (world models, theory of mind). Creativity / consciousness / "what is intelligence" go in L12.

## Author's earlier framing (verbatim, originally proposed for the combined lecture — now split)
> "Does X have a world model? Does X have theory of mind, consciousness, creativity? Is always going to be a shit show, BUT one can contribute to this question meaningfully and incrementally: i.e. how to build taste is ill-defined debates."
>
> "Keep adapting to new worlds by having a good updateable world model. Very different from passive getting new gradients." [→ this part moved to L11]

For L10 specifically: keep the world-model + theory-of-mind subset. Continual-learning aspects belong in L11.

## Phenomenon hooks
- **World representations emerge in transformers trained on next-token prediction.** Author's 2026 papers — *Convergent World Representations and Divergent Tasks*, plus the talk-series "Origins and Roles of World Representations in Transformers" at MIT (Isola), Northeastern (Bau), CBAI.
- **Theory of mind as world-modeling-of-minds** — modeling another agent's beliefs is structurally a world-modeling problem.

## Topics

### What is a world model?
- A learned representation of the environment that supports prediction, planning, or counterfactual reasoning.
- Why it's hard to define operationally — and why that ill-definition is itself worth discussing (preview of L11/L12).

### World models in RL (substantial weight here — fills the lecture)
- Model-based RL revisited from L9.
- **Dreamer** family — world-model-in-latent-space, dream rollouts.
- **MuZero** — learn the dynamics, search through them.
- Why model-based RL hasn't decisively won despite the intuition that it should.

### World representations in transformers
- Author's research thread.
- *Convergent World Representations and Divergent Tasks* (2026 preprint).
- *When does Observational Data Teach Latent Dynamics?* (ICLR 2026 workshop with Nishi et al.).
- *Vision Language Models Inherit Human Color Perception* (ICLR 2026 workshop) — world representations from human-generated training data.

### The "shit-show debates" subset (world-model-specific)
- "Does X have a world model?" — author's framing: usually a shit show, but contributions can be made meaningfully and incrementally.
- **How to build taste in ill-defined debates** — this is a meta-skill the lecture wants to teach.
- **Theory of mind** as a special case (modeling other agents' minds is world-modeling).
- Other debates (consciousness, creativity, taste, intelligence) deferred to L12.

### Connection to neuroscience / human cognition (light)
- Place cells, grid cells as world-model substrates in brains.
- Predictive coding.
- Brief — full cogsci ties land in L11.

## HW
TBD. Candidates:
- Train a small model on a partially-observable navigation task; probe for emergent map representations.
- Reproduce a "world representation in a transformer" experiment (e.g., Othello-GPT-style).

## Cross-references
- **L9 (RL)** — model-based RL and search.
- **L11 (Concept learning)** — continual learning (was originally here) lives there; "what is a concept" is the analog question to "what is a world model."
- **L12 (Intelligence broadly)** — the harder debates (consciousness, creativity) end up there.
- **L4 (Transformers)** — transformers are where modern world representations form.
- **L7 (Science of DL 1)** — representational re-organization (ICLR 2025) sets methods used here.
- **Author's research** — this is the lecture closest to his *current* (2026) thread.

## Open questions / TBDs
- L10 is now lighter (continual learning gone). Should it absorb Dreamer/MuZero with more weight, or stay focused on transformer-world-reps?
- How much of the "is X a world model?" debate to spend lecture time on vs delegating to a HW essay.
- Connection to author's industry work (Prior Computers — "human individuality modeling") — author indicated this is not load-bearing for the lecture, but adjacent.

## Author voice notes
- Channel "shit-show debates that can be made meaningful and incremental" — this lecture's meta-lesson is *how to do good science on slippery questions*.
- This is the lecture closest to the author's live 2026 research; expect ongoing changes as that research develops.
- Sets up L11's deeper engagement with "what is a concept" / cogsci ties.
