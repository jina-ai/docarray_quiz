from docarray import Document

# load the video into blob
d = Document(uri='http://techslides.com/demos/sample-videos/small.mp4')
...
assert d.tensor.shape == (166, 560, 320, 3)

# load only the keyframe
...
assert d.tensor.shape == (1, 560, 320, 3)

