# L7 — Science of DL 1: Training Dynamics

> Read `../README.md` first.

## TL;DR
The first of two **named Science-of-DL pillars** (the other is L11). Brief explicit intro to methods-of-scidl (revisiting the 5-step methodology from L1, with examples). Then a tour of the canonical training-dynamics phenomena: **double descent, generalization, ICL (as phenomenon), grokking**, plus related dynamics (lottery ticket, sharpness, emergence in concept space).

This is where the L1 manifesto visibly cashes out for the first time.

## Aim (user's verbatim)
"L7: Science of DL 1: Training Dynamics. will cover a bit intro to methods of scidl, and discuss double descent, generalization, icl, grokking,"

## Phenomenon hooks
**The whole lecture is phenomena.** Each topic IS a phenomenon, treated as a model-organism case study.

## Topics

### Brief intro to scidl methods (revisit L1's 5-step)
- Methodology recap from L1, now with concrete examples to ground each step.
- What does "a phenomenon" mean for a neural network? Striking, reproducible, surprising-enough-to-investigate.
- The synthetic-task discipline — pick something small enough to fully instrument.
- What "model system" means in the NN context (vs in biology).
- Probes, interventions, ablations — the experimentalist's toolkit briefly. (Interpretability methods get a light slot here; could expand if author decides.)

### Phenomenon: Double descent
- Test error decreasing → bumping → decreasing again as model size grows.
- Why classical statistical learning theory said this shouldn't happen.
- Related to over-parametrization mystery from L1.

### Phenomenon: Generalization (the mystery)
- Overparametrized models that should overfit but don't.
- Why this is weird for physicists trained in classical statistical thinking.
- Connection to (but not derivation of) the theory side — physicists in the theory half of the course will see NTK, capacity, etc. Here we stick to phenomenology.

### Phenomenon: In-context learning (as phenomenon)
- ICL was *introduced* in L5; here it's *dissected*.
- Algorithmic phases — author's own work (*Competition Dynamics Shape Algorithmic Phases of ICL*, ICLR 2025 Spotlight): ICL is a heterogeneous mixture of competing algorithms (fuzzy retrieval vs inference × unigram vs bigram), with sharp transitions.
- Representation re-organization — author's other work (*ICLR: In-Context Learning of Representations*, ICLR 2025): context length triggers sudden re-organization of pretrained semantics to context-specified ones.
- "Just the phenomena, not the bigger debate" (per user) — the *bigger debate* of ICL as concept acquisition belongs in L11.

### Phenomenon: Grokking
- Generalization *long after* training loss has converged.
- The phenomenon: train far past the point you thought was enough, suddenly the model generalizes.
- Why this is a physicist's dream — phase transitions in learning.

### Other training-dynamics phenomena (round out as time permits)
- **Lottery ticket hypothesis** — sparse subnetworks that train as well as the full net.
- **Sharpness** / flatness of minima — connection to generalization.
- **Emergence in concept space** — author's NeurIPS 2024 Spotlight (*Emergence of Hidden Capabilities*). Models harbor latent capabilities that emerge suddenly; latent interventions reveal capabilities not yet elicitable by naive prompting.
- **Swing-by dynamics / non-monotonic test loss** — author's *Swing-by Dynamics in Concept Learning* paper.

### Light touch on interpretability methods
- Probes, steering, dictionary learning, CKA, t-SNE, UMAP — what they are, when to use them.
- This is the most "methods toolkit" part of the lecture.
- Could expand if author decides interpretability deserves more weight (currently a small slot here).

## HW
TBD. Candidates:
- Reproduce a small grokking experiment.
- Probe a trained model for an emerging concept.
- Implement double descent on a small synthetic task.

## Cross-references
- **L1** 5-step methodology — explicitly revisited here.
- **L5** introduced ICL, scaling, emergence — here they're dissected scientifically.
- **L11 (Science of DL 2)** — companion lecture. L7 = training dynamics phenomena (mechanistic, surprising-during-training). L11 = concept-acquisition phenomena (conceptual, abstraction-scale).
- **Author's papers** — direct research material: *Emergence of Hidden Capabilities*, *Competition Dynamics*, *Swing-by Dynamics*, *ICLR*, *In-Context Learning Strategies Emerge Rationally*.

## Open questions / TBDs
- How much weight to give interpretability methods (currently small).
- Order of phenomena — by complexity, by historical significance, or thematic clustering?
- Should this lecture explicitly include some "how to write a paper in scidl" meta-content? Probably no, but possible.

## Author voice notes
- This is the most direct "author's research voice" lecture in the course. Many of the case studies *are* his published work.
- Channel the "model organism" framing throughout — each phenomenon is studied via synthetic tasks that allow full instrumentation.
- Keep it experimental in spirit; defer to the theory prof's lectures for proofs.
