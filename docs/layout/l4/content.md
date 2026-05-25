# L4 — Transformers

> Read `../README.md` first.

## TL;DR
Deep dive on the transformer architecture. Pays off L3's framing of "transformer = the no-compression extreme of memory." Covers attention, residual stream, MLPs, positional encoding, multi-head, KV cache, MoE — the actual mechanics. Big enough lecture to deserve its own slot.

## Aim
"Transformers (big lecture just on this architecture)" — user's original L5 description.

## Possible phenomenon hook (TBD)
The plan was for this to be more of a structural / architectural lecture than a phenomenon-driven one. Author conceded at planning time: "we can adjust these at the content making time, we are high level planning right now."

Candidates for a phenomenon hook if desired:
- **"What does no-compression memory actually buy you?"** (continuation of L3's framing).
- **Attention generalizing to ICL** — though ICL is properly introduced in L5.
- **The residual stream as a "circuit" substrate** — feature for L7's interpretability tease.

If the lecture wants to stay phenomenon-light, that's also OK — the deep architectural understanding is itself the deliverable.

## Topics

### Attention — the core invention
- Query, key, value mechanic.
- Self-attention vs cross-attention.
- Scaled dot-product attention; why the scale.
- Soft, differentiable, parallel.
- The O(N²) cost and what it buys.

### The residual stream (frame for interpretability)
- Why residual connections in transformers are not just a training trick — they're the **computational substrate**.
- Each layer reads from / writes to the residual stream.
- This framing pays off in L7's interpretability discussion.

### MLPs — per-token processing
- After attention mixes across tokens, MLPs process per-token.
- Why this alternation matters.

### Multi-head attention
- Why multiple heads — different "circuits" for different patterns.
- Head pruning / mixture-of-heads phenomena.

### Positional encoding
- Why transformers need it (attention is permutation-equivariant).
- Sinusoidal, learned, RoPE.
- Why this is where memory-of-order lives.

### Transformer economics (modern engineering)
- **KV cache** — what it is, why it matters at inference, the memory cost.
- **Mixture of experts (MoE)** — sparse activations for parameter scaling.
- Hardware-aware design: FlashAttention etc. (gestural).

### Variants & history
- Original (Vaswani 2017) → BERT → GPT → encoder-decoder vs decoder-only.
- Vision transformers — same machinery, image patches as tokens.

## HW
TBD. Candidates:
- Implement a tiny transformer from scratch (small enough to fit on a laptop).
- Probe attention patterns on a trained model.

## Cross-references
- **L3** sets up the framing (transformer = no-compression extreme).
- **L5** uses everything here at scale (LLM pretraining).
- **L7** (training dynamics, interpretability) revisits residual stream and attention heads.
- **L10** (world models) — transformers are where world representations form in modern AI.

## Open questions / TBDs
- Decide whether to give this lecture an explicit phenomenon hook (see "Possible phenomenon hook" above) or keep it primarily architectural.
- Depth of math vs intuition tradeoff — Harvard grad physicists can absorb the math fast.
- Vision transformers — full coverage here or punted to L8 (since they overlap with generative)? Probably here, briefly.

## Author voice notes
- L4 is the most "topic-bin"-shaped lecture in the spine; conscious choice given how much there is to cover about transformers. Resist the urge to fragment.
- Keep some sense of *why* attention won — the no-compression framing from L3 sets this up.
