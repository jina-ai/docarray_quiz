from docarray import Document
import numpy as np

# construct a Document tensor with other types
# numpy array
d = ...
assert isinstance(d.tensor, np.ndarray)

# scipy sparse matrix
import scipy
from scipy.sparse import coo_matrix
sp_tensor = coo_matrix([1, 0, 0, 0, 0, 0])
d = ...
assert scipy.sparse.issparse(d.tensor)

# tensorflow tensor
import tensorflow as tf
tf_tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]])
d = ...
assert tf.is_tensor(d.tensor)

# tensorflow SparseTensor
tf_sp_tensor = tf.sparse.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])
d = ...
assert isinstance(d.tensor, tf.sparse.SparseTensor)

# torch Tensor
import torch
torch_tensor = torch.tensor([1, 2, 3])
d = ...
assert torch.is_tensor(d.tensor)
