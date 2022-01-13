import scipy.sparse

from docarray import Document, DocumentArray

######### id
# create an empty Document and check out its id
# what is the attribute in an empty Document?
d = Document()
assert len(d.id) == 32

# construct a Document with id 'j_1024'
d = Document(id='j_1024')
print(d.id)
assert d.id == 'j_1024'

# id can have arbitrary data type, it is better to keep it as strings

######### main attributes
# construct a Document with text 'hello, jina'
d = Document(text='hello, jina')
assert d.text == 'hello, jina'

# construct a Document with a blob [1, 2, 3]
d = Document(blob=[1, 2, 3])
assert d.blob == [1, 2, 3]

# construct a Document with buffer b`123`
d = Document(buffer=b'hello, jina')
assert d.buffer == b'hello, jina'

# construct a Document with text 'hello, jina' and a blob [1, 2, 3]
d = Document(text='hello, jina', blob=[1, 2, 3])
# assert d.text == 'hello, jina' and d.blob.shape == [1, 2, 3]
# no, you can not do this, `text`, `blob` and `buffer` are mutually exclusive. A Document can have only one of them at
# the same time

# construct a Document with tags={'name': 'jina', 'age': 2}
d = Document(name='jina', age=2)
assert d.tags['name'] == 'jina'
assert d.tags['age'] == 2
