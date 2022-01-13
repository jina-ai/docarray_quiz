from docarray import Document
# construct a Document by copying from another Document
d_from = Document(text='before')
d_to = Document(d_from)
assert d_to.text == d_from.text
d_from.text = 'after'
assert d_to.text == d_from.text

# construct a Document by deep copying
d_from = Document(text='before')
d_to = Document(d_from, copy=True)
assert d_to.text == d_from.text
d_from.text = 'after'
assert d_to.text != d_from.text
