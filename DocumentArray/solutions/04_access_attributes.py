from docarray import Document, DocumentArray

# construct a DocumentArray with 3 Documents
# each Document has 2 chunks and 4 matches
da = DocumentArray()
for i in range(3):
    d = Document(text=f'doc_{i}', tags={'name': f'tag_{i}'})
    for j in range(2):
        d.chunks.append(Document(text=f'chunk_{j}'))
    for k in range(4):
        d.matches.append(Document(text=f'match_{k}'))
    da.append(d)

# select single attribute
# select the 'text' attribute for all the Documents
attr = da.texts
assert attr == ['doc_0', 'doc_1', 'doc_2']

# select multiple attributes
# select the 'text' and the 'id' attributes for all the Documents
attr_list = da[:, ['text', 'id']]
assert len(attr_list) == 2
assert attr_list[0] == ['doc_0', 'doc_1', 'doc_2']

# select attributes with slicing
# select the 'text' and the 'id' attributes for the first 2 Documents
attr_list = da[:2, ['text', 'id']]
assert len(attr_list) == 2
assert attr_list[0] == ['doc_0', 'doc_1']

# select tags with dunder syntax
# select the 'name' field from the 'tags'
attr = da[:, ['tags__name']]
assert attr == ['tag_0', 'tag_1', 'tag_2']

# select attributes with traveral paths
# select the 'text' and the 'id' attributes for all the chunks and matches
attr_list = da['@c,m', ['text', 'id']]
assert len(attr_list) == 2
assert len(attr_list[0]) == len(da) * (len(da[0].chunks) + len(da[0].matches))

# delete attributes
# delete the 'text' attribute
del da[:, 'text']
assert not da[0].text
