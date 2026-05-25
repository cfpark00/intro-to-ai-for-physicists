# L8 — Diffusion Models

> Read `../README.md` first.

## TL;DR
The dominant probabilistic-generative paradigm. Spotlight diffusion specifically; treat **VAEs/GANs as historical predecessors** (1-slide each, the way L2 treats Gabor filters historically). Phenomenon hook: **model collapse**.

## Aim
The author agreed (verbatim): "L8: agreed. highlight on diffusion." Earlier discussion: cramming VAE+GAN+Diffusion into one lecture was "brutal" — fix by spotlighting diffusion and treating VAE/GAN as scaffolding.

## Phenomenon hook
**Model collapse** — repeatedly training generative models on their own outputs causes degradation. Tells us something fundamental about the limits of generative modeling. Good phenomenon for a science-of-DL lecture.

Secondary: **high-fidelity generation from a probabilistic model** — why diffusion works so well, when GAN-era methods didn't.

## Topics

### Probabilistic view (light foundation)
- Generative modeling as learning a distribution over data.
- Why this is hard (high-dim, mode coverage, sample quality).
- Quick survey of approaches before diffusion won:
  - **VAE** (1 slide) — encode to a latent, decode back; principled probabilistic but blurry samples.
  - **GAN** (1 slide) — adversarial training; sharp samples but mode collapse, unstable.
  - **Normalizing flows** (1 slide) — exact likelihood but architectural constraints.
  - **Energy-based models** (1 slide) — flexible but sampling is hard.
- These set up *why* diffusion was the breakthrough.

### Diffusion models — the main event
- The forward process: incremental noising.
- The reverse process: learn to denoise.
- Score matching as the unifying view (Song & Ermon).
- DDPM (Ho et al.) — the version that made it click.
- Sampling and the trade between speed and quality.

### Flow matching (modern variant)
- A more general framing — diffusion as a special case.
- Why flow matching has been useful in scaling.

### Phenomenon: Model collapse
- What it is — recursive training on synthetic data degrades the model.
- Why it matters (especially as the web fills with model-generated content).
- What it tells us about the limits of "just train on more data."

### Applications & connection to physics
- Author's PhD work on diffusion for cosmology — *Probabilistic reconstruction of Dark Matter fields*, *Debiasing with Diffusion* (ApJ 2024). Worth mentioning as a physics example.
- Diffusion for scientific data more broadly — emulation, debiasing, completion.

## HW
TBD. Candidates:
- Implement a tiny diffusion model on MNIST or similar.
- Reproduce a model-collapse experiment with two iterations of self-training.

## Cross-references
- **L7 (Training dynamics)** — model collapse is a training-dynamics phenomenon in disguise.
- **L11 (Concept learning)** — what does a diffusion model actually learn? Connects to compositional generalization (author's *Concept Space* work uses text-conditioned diffusion).
- **L5/L6 (LLMs)** — different paradigm but similar scale story.

## Open questions / TBDs
- How much math (SDEs, score matching derivation) vs intuition? Lean: intuition first, math gestures for physicists who can fill in.
- Whether to include NeRFs (3D generation) — mentioned in topic dump but unclear home. Could fit here lightly.
- Where do aleatory/epistemic uncertainty and Gaussianity discussions live? Could anchor here (probabilistic view) or skip.

## Author voice notes
- Author has shipped diffusion code (`vdm4cdm`) — examples can pull from real research code.
- Keep the "diffusion as model-organism for studying generation" angle alive — same spirit as the rest of the course.
