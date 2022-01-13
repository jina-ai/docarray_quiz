from docarray import Document, DocumentArray

da = DocumentArray([Document(uri='http://techslides.com/demos/sample-videos/small.mp4') for _ in range(10)])

def foo(d):
    return d.load_uri_to_video_blob(only_keyframes=True)

# run foo function on each Document in da and save the results to da_new
# Answer: da_new = da.map(foo)
da_new = ...
assert list(da_new)[0].blob.shape == (1, 560, 320, 3)

# run foo function in-place on each Document in da
# Answer: da.apply(foo)
...
assert da[0].blob.shape == (1, 560, 320, 3)

