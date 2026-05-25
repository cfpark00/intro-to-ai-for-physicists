# L2 — Neural Networks and Image Classification

> Read `../README.md` first.

## TL;DR
Start the historical/architectural thread from image classification (skipping classical ML — no SVMs, kNN, decision trees, etc., which other books cover). Properly introduce neural networks here (rather than in L1) since IC is the natural setting. Phenomenon hook: **"why did it take so long?"** and **Gabor-filter emergence in trained CNNs**. Closes on the first bitter lesson: bigger is better — preview for L5.

## Aim (user's phrasing)
"Perhaps the most popular AI out there is LLMs, but here we do a bit of a historical take where we start by image classification (skipping the SVM stuff)."

## Phenomenon hooks
- **"Why did it take so long?"** Neural networks were proposed in the 1940s–60s. They worked end-to-end on ImageNet only in 2012 (AlexNet). Why the delay? Hardware, data, depth, initialization, normalization, residual connections, …
- **Gabor-filter emergence** — first-layer filters of a trained CNN look like Gabor wavelets, the same primitives that show up in V1 of biological visual cortex. A phenomenon a physicist or neuroscientist will recognize.
- **Bigger is better** — first taste of the scaling pattern. Sets up L5.

## Topics

### Neural networks (the proper introduction)
- MLPs as universal function approximators (mention universal approximation theorem with the "but theory said this was impossible elsewhere" arc from L1).
- SGD; minibatching; loss functions for classification (cross-entropy).
- Optimizers: SGD → momentum → Adam → AdamW (with weight decay).
- Initialization — why naive init breaks deep nets.
- Normalization layers — batch norm, layer norm, why they were necessary.
- Residual streams / skip connections — the move that unlocked deep training.
- Hyperparameters: batch size, learning rate, dropout, regularization, weight decay. Just enough intuition; not a full tour.
- **GPU technicals** briefly — why GPU and not CPU; what kind of math NNs are.

### Image classification specifically
- CNNs — convolutional inductive bias as the canonical example of **prior / inductive bias**.
- Why CNNs work for images: translation equivariance, locality, hierarchy.
- ImageNet as the benchmark that organized the field.
- AlexNet, VGG, ResNet — the historical arc, brief.
- **Inductive bias** vs **compression** — what does the network *actually learn*? Hint: it learns to compress data into useful representations.
- Gabor filters as emergent first-layer features — the phenomenon hook.

### The first bitter lesson (close)
- Bigger nets → better. Even before "scaling laws" was a phrase, the IC field already saw this pattern.
- Sets up L5's full scaling-laws treatment.

## HW
TBD. Candidates:
- Train a small CNN on CIFAR or a similar dataset, inspect first-layer filters, compare to Gabor.
- Compare CNN vs MLP on image classification — gain intuition on inductive bias.

## Cross-references
- "Bigger is better" → **L5** (scaling laws).
- Residual stream concept introduced here → reused in **L4** (residual stream as the computational substrate of transformers).
- Normalization, optimizers, initialization → applied throughout, esp. **L4, L5, L7**.
- "Gabor filters as emergent" framing → general theme of "what does a NN learn?" returns in **L7** (training dynamics) and **L11** (concept learning).

## Open questions / TBDs
- How much architecture history (LeNet → AlexNet → VGG → ResNet → ViT) to actually cover? Lean: brief, just enough.
- Where does shape vs texture sit? Could be a brief phenomenon mention (ImageNet shape bias debates).
- Should vision transformers be teased here or fully deferred to L4?
