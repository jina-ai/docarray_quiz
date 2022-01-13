from docarray import Document

# load the video into blob
d = Document(uri='http://techslides.com/demos/sample-videos/small.mp4')
# Answer: d.load_uri_to_video_blob()
...
assert d.blob.shape == (166, 560, 320, 3)

# load only the keyframe
# Answer: d.load_uri_to_video_blob(only_keyframes=True)
...
assert d.blob.shape == (1, 560, 320, 3)

