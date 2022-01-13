from docarray import Document

######### id

# construct a Document with id 'j_1024'
# Answer: d = Document(id='j_1024')
d = ...
assert d.id == 'j_1024'

# id can have arbitrary data type, it is better to keep it as strings

######### main attributes
# construct a Document with text 'hello, jina'
# Answer: d = Document(text='hello, jina')
d = ...
assert d.text == 'hello, jina'

# construct a Document with a blob [1, 2, 3]
# Answer: d = Document(blob=[1, 2, 3])
d = ...
assert d.blob == [1, 2, 3]

# construct a Document with buffer b`123`
# Answer: d = Document(buffer=b'hello, jina')
d = ...
assert d.buffer == b'hello, jina'

# construct a Document with text 'hello, jina' and a blob [1, 2, 3]
# d = Document(text='hello, jina', blob=[1, 2, 3])
d = ...
assert d.text == 'hello, jina' and d.blob.shape == [1, 2, 3]
# Answer: no, you can NOT do this, `text`, `blob` and `buffer` are mutually exclusive. A Document can have only one of them at
# the same time

# construct a Document with tags={'name': 'jina', 'age': 2}
# Answer: d = Document(name='jina', age=2)
d = ...
assert d.tags['name'] == 'jina'
assert d.tags['age'] == 2
