# Lecture Outline — v5

12 lectures + a separate project-presentation session. Covers the **experimental-physicist half** of the joint Harvard offering. Theory half (NTK, neural manifold capacity, etc.) lives with the other prof. Material will eventually also be the basis for a standalone full course of ~25 lectures.

For **verbose per-lecture content**, see `docs/layout/lN/content.md` (one file per lecture, intended to be authoritative).

Last revised 2026-05-25.

## Arc

- **L1–L7 — Fundamentals & methods.** Thesis, model classes (image, sequence, transformer, LLM), training dynamics. *Note:* LLMs come mid-block because they're treated as a natural continuation of transformers; diffusion and RL come *after* as "the other major paradigms."
- **L8–L12 — Beyond LLMs into the broader scientific picture.** Diffusion, real RL, world models, concept learning, intelligence broadly.

## Spine

| L | Title | One-liner |
|---|---|---|
| 1 | Introduction | Philosophy, thesis, history of ML/DL/AI, neuroethology, bitter lesson |
| 2 | Neural Networks and Image Classification | Inductive bias + Gabor filters; "why did it take so long?" |
| 3 | Sequence Modeling | Memory as the central question; SSM vs Transformer |
| 4 | Transformers | Architecture deep dive; the no-compression extreme |
| 5 | LLM1: Pretraining and Fine Tuning | Scaling, emergence, ICL, foundation models, SFT |
| 6 | LLM2: Post-training and Agents | RLHF, reasoning, inference-time compute, agents, RAG |
| 7 | Science of DL 1: Training Dynamics | scidl methods + double descent, grokking, generalization, ICL phenomena |
| 8 | Diffusion Models | Probabilistic generation, model collapse |
| 9 | Reinforcement Learning | Real RL — different from supervised training; the hard problems |
| 10 | World Models | World modeling + theory-of-mind-style debates |
| 11 | Science of DL 2: Concept Learning | Concepts, compositional gen, continual learning, "what is a concept", cogsci |
| 12 | Science of Intelligence | Evolution, multi-agent, QD, open-endedness, creativity, broader intelligence |
| (sep) | Project presentations | Separate session, not numbered |

## Key design decisions encoded in this spine

- **L1 merges philosophy + AI/FM/NN intro.** Grad physicists at Harvard already know what MLPs and SGD are; no point spending a lecture on them.
- **L3 reframes sequence modeling as a memory problem** — gives the lecture a phenomenon hook and sets up L4 as "transformer = no-compression extreme."
- **L4 and L5 are tightly coupled.** Transformers and LLMs are hard to teach separately given how much they interweave; consecutive lectures handle it.
- **L5/L6 split LLMs by stage** — pretraining/SFT in L5, post-training/agents in L6. Note: the "science" of L5 phenomena (scaling, emergence, ICL) is properly dissected in L7.
- **Real RL (L9) comes AFTER LLM lectures.** Justification: RLHF in L6 is "reward model + weighted SFT, not real RL." So no forward reference to undefined RL when we discuss RLHF.
- **Two named "Science of DL" pillars** (L7, L11). Distinctive structural choice — most ML courses bury these phenomena inside topic lectures.
- **L11 drifts into philosophy** ("what is a concept" → "learning at different abstraction scales") to set up L12's expanded notion of intelligence.
- **L12 ends on a question, not a topic list.** Capstone vibe.

## Out of scope

- **ML theory** (NTK, manifold capacity, generalization bounds proofs) — other prof.
- **Classical ML** (SVMs, kNN, decision trees) — other books.
- **Software/MLOps tutorials** — recipes, not science.

## Pending design questions

See `docs/layout/README.md` and individual `docs/layout/lN/content.md` files for per-lecture TBDs.
