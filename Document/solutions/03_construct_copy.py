from docarray import Document

# construct a Document by copying from another Document
d_from = Document(text='before')
d = Document(d_from)
assert d.text == d_from.text
d_from.text = 'after'
assert d.text == d_from.text

# construct a Document by deep copying
d_from = Document(text='before')
d = Document(d_from, copy=True)
assert d.text == d_from.text
d_from.text = 'after'
assert d.text != d_from.text
