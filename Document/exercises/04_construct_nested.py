from docarray import Document

# construct a Document with granularity=2 and adjacency=3
d = ...
assert d.granularity == 2 and d.adjacency == 3

# construct a Document with 2 chunks and each chunk has 3 chunks
d = ...
assert len(d.chunks) == 2
for c in d.chunks:
    assert c.granularity == 1
    assert len(c.chunks) == 3
    for cc in c.chunks:
        assert cc.granularity == 2

# construct a Document with 3 matches and each match has 4 matches
d = ...
assert len(d.matches) == 3
for m in d.matches:
    assert m.adjacency == 1
    assert len(m.matches) == 4
    for mm in m.matches:
        assert mm.adjacency == 2
