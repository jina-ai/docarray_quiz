from docarray import Document
import numpy as np
import torch

model = torch.nn.Sequential(
    torch.nn.Linear(
        in_features=128,
        out_features=128,
    ),
    torch.nn.ReLU(),
    torch.nn.Linear(in_features=128, out_features=32))

d = Document(tensor=np.random.rand(128).astype(np.float32))

# calculate the embedding
d.embed(model)
assert d.embedding.shape == (32,)