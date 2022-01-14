from docarray import Document, DocumentArray

da = DocumentArray([Document(content=f'{i}') for i in range(10)])

# select the first 5 Documents with slicing
selected = da[:5]
assert len(selected) == 5

# select the Documents at position 2, 4, 6, 8 with slicing
selected = da[2:10:2]
for idx, d in enumerate(selected):
    assert d.text == f'{(idx + 1) * 2}'
assert len(selected) == 4

# select the Documents at position 0, 3, 6, 9 by using a boolean mask
mask = [i%3 == 0 for i in range(10)]
selected = da[mask]
for idx, d in enumerate(selected):
    assert d.text == f'{idx * 3}'
assert len(selected) == 4

# delete the last 5 Documents
del da[5:]
assert len(da) == 5