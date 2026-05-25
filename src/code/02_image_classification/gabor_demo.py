"""
Gabor-filter emergence in a CNN trained on natural images.

Train a small CNN on CIFAR-10 for a few epochs, then visualize the
first convolutional layer's filters. The first-layer filters reliably
converge to oriented, localized, wavelet-like patterns: the Gabor-style
primitives that also appear in V1 of biological visual cortex.

Nothing in the architecture asks for Gabor structure. It falls out of
the interaction between (a) translation-equivariant convolutional
inductive bias and (b) the statistics of natural images.

Usage:
    uv run python src/code/02_image_classification/gabor_demo.py

Output:
    src/code/02_image_classification/gabor_filters.png
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


def main(n_epochs: int = 3, batch_size: int = 128, seed: int = 0) -> None:
    here = Path(__file__).resolve().parent
    repo_root = here.parents[3]
    data_root = repo_root / "data" / "cifar10"
    data_root.mkdir(parents=True, exist_ok=True)

    torch.manual_seed(seed)
    np.random.seed(seed)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"device: {device}")

    tfm = transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
        ]
    )
    train = datasets.CIFAR10(
        root=str(data_root), train=True, download=True, transform=tfm
    )
    loader = DataLoader(train, batch_size=batch_size, shuffle=True, num_workers=2)

    class SmallCNN(nn.Module):
        def __init__(self) -> None:
            super().__init__()
            self.conv1 = nn.Conv2d(3, 32, kernel_size=7, padding=3)
            self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
            self.pool = nn.MaxPool2d(2)
            self.fc = nn.Linear(64 * 8 * 8, 10)

        def forward(self, x: torch.Tensor) -> torch.Tensor:
            x = self.pool(F.relu(self.conv1(x)))
            x = self.pool(F.relu(self.conv2(x)))
            x = x.flatten(1)
            return self.fc(x)

    model = SmallCNN().to(device)
    optim = torch.optim.AdamW(model.parameters(), lr=3e-3)

    for epoch in range(n_epochs):
        running = 0.0
        n_seen = 0
        for x, y in loader:
            x, y = x.to(device), y.to(device)
            optim.zero_grad()
            loss = F.cross_entropy(model(x), y)
            loss.backward()
            optim.step()
            running += loss.item() * len(x)
            n_seen += len(x)
        print(f"epoch {epoch + 1}/{n_epochs}  train_loss={running / n_seen:.4f}")

    filters = model.conv1.weight.detach().cpu().numpy()
    fmin = filters.min(axis=(1, 2, 3), keepdims=True)
    fmax = filters.max(axis=(1, 2, 3), keepdims=True)
    filters_disp = (filters - fmin) / (fmax - fmin + 1e-8)

    n_filters = filters_disp.shape[0]
    cols = 8
    rows = int(np.ceil(n_filters / cols))
    fig, axes = plt.subplots(rows, cols, figsize=(cols, rows))
    axes_flat = np.array(axes).flatten()
    for i, ax in enumerate(axes_flat):
        if i < n_filters:
            ax.imshow(filters_disp[i].transpose(1, 2, 0))
        ax.axis("off")
    fig.suptitle(
        "First-layer CNN filters after training on CIFAR-10\n"
        "(oriented, localized, Gabor-like emergence)",
        fontsize=10,
    )
    fig.tight_layout()

    out = here / "gabor_filters.png"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    print(f"saved: {out}")


if __name__ == "__main__":
    main()
