from docarray import Document

# load the video into blob
d = Document(uri='http://techslides.com/demos/sample-videos/small.mp4')
d.load_uri_to_video_blob()
assert d.blob.shape == (166, 560, 320, 3)

# load only the keyframe
d.load_uri_to_video_blob(only_keyframes=True)
print(d.blob.shape)
assert d.blob.shape == (1, 560, 320, 3)

