import numpy as np
from docarray import DocumentArray

da1 = DocumentArray.empty(4)
da1.embeddings = np.random.rand(4, 10)

da2 = DocumentArray.empty(5)
da2.embeddings = np.random.rand(5, 10)

# for each Document in da1, find the nearest neighbors from da2 using `euclidean` distances
...

# get matching score for the top 1 match of the 1st Document in da1
val = ...
assert isinstance(val, float)