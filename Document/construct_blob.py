from docarray import Document

# construct a Document blob with other types
# numpy array
import numpy as np
d = Document(blob=np.array([1, 2, 3]))
assert isinstance(d.blob, np.ndarray)

# scipy sparse matrix
import scipy
from scipy.sparse import coo_matrix
sp_blob = coo_matrix([1, 0, 0, 0, 0, 0])
d = Document(blob=sp_blob)
assert scipy.sparse.issparse(d.blob)

# tensorflow tensor
import tensorflow as tf
tf_blob = tf.constant([[1.0, 2.0], [3.0, 4.0]])
d = Document(blob=tf_blob)
assert tf.is_tensor(d.blob)

# tensorflow SparseTensor
tf_sp_blob = tf.sparse.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])
d = Document(blob=tf_sp_blob)
assert isinstance(d.blob, tf.sparse.SparseTensor)

# torch Tensor
import torch
torch_blob = torch.tensor([1, 2, 3])
d = Document(blob=torch_blob)
assert torch.is_tensor(d.blob)
