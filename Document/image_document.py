from docarray import Document
import os

# load image from data uri
d = Document(
    uri='data:image/png;base64,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',
)
d.plot()

# save the image to 'jina.png'
# Answer: d.save_uri_to_file('jina.png')
...
assert os.path.isfile('jina.png')

# load image from uri
d = Document(uri='./jina.png')
# Answer: d.load_uri_to_image_blob()
...
assert d.blob.shape == (146, 344, 3)

# save the image blob to 'jina.jpg'
# Answer: d.save_image_blob_to_file('jina.jpg')
...
assert os.path.isfile('jina.jpg')

# change the image size to (20, 20)
# Answer: d.set_image_blob_shape(shape=(20, 20))
...
assert d.blob.shape == (20, 20, 3)

# create chunks by using a sliding window of shape (10, 10) with strides=(5, 5)
# Answer: d.convert_image_blob_to_sliding_windows(window_shape=(10, 10), strides=(5, 5), as_chunks=True)
...
assert len(d.chunks) == 9
assert d.chunks[0].blob.shape == (10, 10, 3)

# set the color channel from HWC to CHW
# Answer: d.set_image_blob_channel_axis(-1, 0)
...
assert d.blob.shape == (3, 20, 20)

