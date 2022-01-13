from docarray import Document

d = Document(uri='toy.wav').load_uri_to_audio_blob()

print(d.blob.shape, d.blob.dtype)