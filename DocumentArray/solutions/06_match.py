import numpy as np
from docarray import DocumentArray

da1 = DocumentArray.empty(4)
da1.embeddings = np.random.rand(4, 10)

da2 = DocumentArray.empty(5)
da2.embeddings = np.random.rand(5, 10)

# for each Document in da1, find the nearest neighbors from da2 using `euclidean` distances
da1.match(da2, metric='euclidean', limit=3)

# get matching score for the top 1 match of the 1st Document in da1
val = da1[0].matches[0].scores['euclidean'].value
assert isinstance(val, float)