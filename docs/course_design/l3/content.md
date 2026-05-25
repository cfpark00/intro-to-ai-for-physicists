# L3 — Sequence Modeling

> Read `../README.md` first.

## TL;DR
Reframe sequence modeling as a **memory problem**. Two opposite philosophies for handling history: **SSM-style** (RNN/LSTM/GRU → Mamba/S4) maintains a running state and compresses history into it; **Transformer-style** doesn't compress — it trains a function over the whole context. Tradeoffs (efficiency vs expressivity; O(N) vs O(N²); generalization to longer contexts) set up L4's deep dive.

## Aim (user's phrasing)
"L4 [now L3] can be a general state space model and transformer model: different ways to manage memory: SSM: maintain a memory state, Transformer: fuck it all train a function, context is all."

The user explicitly framed this as the "memory" lecture: "I can talk about 'memory' than that takes time!"

## Phenomenon hook
**"How does a network remember?"** — same question physicists/neuroscientists have asked about animals. Memory is a problem the brain solves, and it's the problem sequence models solve. Two extreme answers in NNs: maintain state, or just keep the past around.

## Topics

### Memory as the central concept
- What is memory in a sequence model? A way to access the past at the present time.
- Two philosophies (the lecture's spine):
  - **SSM-style** — maintain a running state `h_t` that compresses history. Memory is bounded (state size).
  - **Transformer-style** — don't compress. Train a function over the whole sequence (attention). Memory is the context window.
- Tradeoffs:
  - Efficiency: SSM ~O(N), Transformer ~O(N²) (or O(N) with KV-cache amortization).
  - Expressivity: Transformer attends to anything; SSM has compression bottleneck.
  - Generalization to longer contexts: SSMs interestingly do better in some cases.
  - Inference cost vs training cost — different shapes.

### Historical sequence models (briefly — like L2 treats Gabor filters)
- RNNs — the original recurrent computation. Vanishing/exploding gradients.
- LSTMs — gating to control memory flow.
- GRUs — simplified LSTM.
- Why these all hit a wall — and what attention solved.

### The state-space resurgence (modern revival)
- Mamba, S4, and friends — selective state spaces.
- Why they're back: long-context efficiency.
- Connection to control theory and dynamical systems (a physicist hook).

### Attention as the move that unlocked it
- Brief preview of attention — but the deep dive is L4.
- Why "fuck it, train a function over context" works at scale.
- Sets up: "if attention solves memory by not compressing, what does the next lecture (L4) look like?"

### Next-token prediction (light here, deeper in L5)
- The objective that drove sequence modeling — predict the next token.
- Cross-entropy loss for next-token; perplexity.
- Why this objective seems too simple but somehow gives you language.

## HW
TBD.

## Cross-references
- **L4 (Transformers)** — the no-compression extreme paid off in architectural detail.
- **L5 (LLMs)** — sequence modeling scaled to language at massive scale.
- **L10 (World Models)** — memory architectures revisited with more stakes (updatable world models, hard continual learning).
- **L9 (RL)** — long-horizon problem touches memory architectures too.

## Open questions / TBDs
- How much detail on RNN/LSTM math (BPTT, gating equations) vs gestural? Lean: gestural — these are pre-attention archaeology.
- Should Mamba/S4 get its own deep dive or just a positioning slide?
- Where does recurrent computation in transformers (in-context recurrent processes) sit? Probably L7 territory.

## Author voice notes
- The "fuck it all train a function, context is all" line from the user is good — keep something of that energy in the framing.
- Physicists will appreciate the state-space connection to control theory and dynamical systems.
