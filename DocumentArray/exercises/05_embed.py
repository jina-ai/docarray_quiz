from docarray import DocumentArray
import numpy as np
import torch

model = torch.nn.Sequential(
    torch.nn.Linear(
        in_features=128,
        out_features=128,
    ),
    torch.nn.ReLU(),
    torch.nn.Linear(in_features=128, out_features=32))

docs = DocumentArray.empty(10)
docs.tensors = np.random.random([10, 128]).astype(np.float32)
...

assert docs.embeddings.shape == (10, 32)