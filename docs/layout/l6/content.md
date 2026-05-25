# L6 — LLM2: Post-training and Agents

> Read `../README.md` first.

## TL;DR
Picks up after L5 with the **post-training half** of the modern LLM pipeline: RLHF, DPO, reasoning, inference-time compute, agents, RAG. Note: the author explicitly characterized RLHF as **"not really RL, just reward model + weighted SFT"** — which is the justification for L6 not needing L9 (the real RL lecture) as a prereq.

## Aim
Second half of the LLM block (after L5). Covers what people *do* with pretrained models — the adaptation, alignment, and orchestration that turn a base model into something useful.

## Author's justification for RL appearing here before L9
User said (verbatim):
> "rl appears in l6, but rlhf is meh: reward model and just weighted sft kinda. l8 [now L9] will anyways talk more about exploration vs exploitation, credit assignment, long horizon, sparse reward etc etc."

In other words: RLHF is treated as a supervised-ish technique with a learned reward signal, not as "real RL." This sidesteps the dependency problem.

## Possible phenomenon hooks (TBD per planning convo)
- **Reasoning emerging from RL post-training** — o1/o3-style chain-of-thought from RL on verifiable rewards.
- **RLHF causing capability forgetting / alignment tax.**
- **Inference-time compute as a scaling axis** — test-time-compute scaling laws.

Author noted L6 is currently topic-bin-shaped and could benefit from a phenomenon hook at content-writing time.

## Topics

### Post-training methods
- **RLHF / RLAIF** — reward model + (weighted) SFT framing. Why the user is dismissive of calling it "real RL."
- **DPO** — direct preference optimization, eliminating the reward model.
- **PPO** — used in RLHF but real RL fundamentals deferred to L9.
- Instruction tuning broadly.
- **Distillation** in post-training: context distillation, on-policy distillation.
- **Calibration** — making model confidences match outcomes.

### Reasoning and inference-time compute
- **Chain of thought (CoT)** — prompt-elicited reasoning.
- **System 1 vs System 2** — the framing from cognitive science applied to LLMs.
- **Inference-time compute scaling** — letting the model think longer at test time (o1, o3 paradigm).
- **RL for reasoning** — what does RL actually teach? *Author's own paper: "Decomposing Elements of Problem Solving: What 'Math' Does RL Teach?"* — GRPO enhances **execution** ("temperature distillation") more than planning. Models hit a "coverage wall" on novel problems.

### Agents and tool use
- The agent paradigm — LLMs that call tools, plan, execute, retry.
- Multi-step / long-horizon agents.
- Evaluation — how do we measure agent quality?
- Open questions about reliability.

### RAG (retrieval-augmented generation)
- Why retrieval — context is finite, knowledge is large.
- How RAG works in practice.
- Limitations.

### Evals
- How we measure modern LLMs — benchmarks, capability evals, alignment evals.
- The "Humanity's Last Exam" / benchmark saturation.

### VLMs, omni-models (optional, lighter)
- Vision-language models, multimodal LLMs.
- Whether these are properly L5 (pretraining) or L6 (deployment/use). Probably split: pretraining here in L5, behavior in L6.

## HW (from earlier convo)
2. Experience BC vs RL in a setup, most likely one where BC first is needed before RL. *(This pair from earlier could split: BC vs RL might land more naturally in L9. Decide at content time.)*

## Cross-references
- **L5 (LLM1)** — supervised pipeline that L6 picks up after.
- **L9 (RL)** — real RL. RLHF here is the "easy" subset; L9 covers the hard problems (credit assignment, sparse reward, exploration).
- **L7 (Training dynamics)** — reasoning phenomena, scaling, etc. revisited as science.
- **L11 (Concept Learning)** — ICL connection. Author's own *New News (System-2 Fine-tuning)* paper sits between post-training and concept acquisition.

## Open questions / TBDs
- Phenomenon hook to lead with — see candidates above. Decide at content time.
- Inference-time compute / reasoning is currently a chunk inside this lecture but could expand if it deserves more weight (it's one of the most active frontier topics in 2026).
- VLMs/omni-models split between L5 and L6 — confirm.
- BC vs RL HW placement — here or L9?

## Author voice notes
- This is the most "what people actually ship" lecture; resist the urge to make it a survey of OpenAI/Anthropic/Google products. Frame around what's *scientifically* known about post-training.
- Author's *New News* and *What Math Does RL Teach* papers are direct research material to draw on.
- User noted "rlhf is meh" — channel that mild dismissiveness ("this is a useful trick, but don't conflate it with real RL").
