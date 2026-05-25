# L5 — LLM1: Pretraining and Fine Tuning

> Read `../README.md` first.

## TL;DR
LLMs as the showcase of scaled transformers. Covers the **supervised half** of the modern training pipeline: pretraining (next-token prediction at massive scale) and fine-tuning (SFT, LoRA, etc.). Introduces the headline phenomena — scaling laws, emergence at scale, and in-context learning — which get revisited and dissected scientifically in L7.

L6 picks up where this ends with post-training (RLHF/DPO, agents, inference compute).

## Aim
The user merged "transformers + LLM-pretraining + LLM-posttraining" into a tight three-lecture block (L4, L5, L6), justified by: "transformers + LLMs are really hard to separate." L5 is the first half of the LLM block.

## Phenomenon hooks
The flagship phenomena of modern AI all live in this lecture (introduced here, dissected in L7):
- **Scaling laws** — loss as a power-law function of compute, data, parameters (Kaplan, Chinchilla).
- **Emergence at scale** — capabilities that appear discontinuously at a threshold.
- **In-context learning (ICL)** — a pretrained model can learn new tasks from prompt examples without weight updates. Phenomenon introduced here, properly dissected in L7 (mechanistic), and revisited in L11 (as concept acquisition).

## Topics

### Pretraining
- Next-token prediction objective revisited (after L3's intro), now at scale.
- Tokens, tokenization (BPE, sentencepiece), vector quantizers (for non-text modalities).
- Pretraining data: scale, quality, deduplication, curation.
- **Data-centric ML** — the realization that data quality often beats architecture tweaks.
- Foundation models as a concept (→ glossary entry).
- Self-supervised learning more broadly — SimCLR, CLIP — as variants of "predict-something-from-something" pretraining.

### The scaling story
- **Scaling laws** — Kaplan, Chinchilla, the actual functional forms.
- Scaling economics — compute, data, params, tokens-per-param ratios.
- Why scaling has worked so reliably — the bitter lesson cashed out.
- **GPU parallelism** — data parallel, tensor parallel, pipeline parallel, FSDP. Just enough to understand why "scale" is hard.
- **KV cache at scale** revisited.
- **Mixture of experts at scale** — sparse routing.

### Emergence at scale
- The phenomenon: some capabilities appear discontinuously when scaling.
- Famous examples: arithmetic, chain-of-thought, etc.
- Open question: is emergence real, or a metric artifact? (Schaeffer et al.)
- Lecture introduces; L7 dissects with concept-space framing (user's NeurIPS 2024 spotlight).

### In-context learning (ICL) — introduce, deepen later
- The phenomenon: prompt the model with examples, it learns the pattern, no weight update.
- Why this is weird — meta-learning emerging from next-token training.
- Pointer forward to L7 (mechanistic analysis) and L11 (ICL as concept acquisition).
- User's own research: *ICLR: In-Context Learning of Representations*, *Competition Dynamics Shape Algorithmic Phases of ICL* (ICLR 2025 spotlight).

### Fine-tuning (the second half of the supervised pipeline)
- Supervised fine-tuning (SFT) — the dominant adaptation move.
- LoRA — parameter-efficient fine-tuning.
- Distillation — teacher-student, knowledge distillation.
- Behavioral cloning (BC) — "plateaus near data performance" / "trash in, trash out regime." User flagged this phrase explicitly.

## HW (from earlier convo)
1. Experience pretraining vs fine-tuning on some task → grow intuition on when to PT vs FT.

(The "experience BC vs RL" HW from the same earlier discussion lands more naturally in L6 or L9.)

## Cross-references
- **L4 (Transformers)** — provides the architecture L5 scales up.
- **L7 (Science of DL 1)** — scaling laws, emergence, ICL all dissected as phenomena there.
- **L6 (LLM2: Post-training)** — picks up after this with RLHF/agents/reasoning.
- **L11 (Concept Learning)** — ICL revisited as concept acquisition / abstraction.
- **L1 bitter lesson** — paid off in full here.

## Open questions / TBDs
- How much of the **mechanistic** ICL story belongs here vs L7? Lean: phenomenon stated here, mechanism saved for L7.
- VLMs / omni-models / video models — fit here or in L6? Probably here briefly (since they're pretrained), with deployment / post-training in L6.
- Self-supervised learning depth — full SSL family review or just SimCLR/CLIP highlights?

## Author voice notes
- This is the flagship "modern AI" lecture. Author has shipped code for the underlying components (markov-mixtures, concept-learning) so examples can pull from real research, not toys.
- Keep the awe of scale present — physicists will appreciate scaling laws as phenomenology.
