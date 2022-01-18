from docarray import Document

# construct a Document with granularity=2 and adjacency=3
# Answer: d = Document(granularity=2, adjacency=3)
d = Document(granularity=2, adjacency=3)
assert d.granularity == 2 and d.adjacency == 3

# construct a Document with 2 chunks and each chunk has 3 chunks
d = Document()
for _ in range(2):
    d.chunks.append(Document())
for c in d.chunks:
    for _ in range(3):
        c.chunks.append(Document())

assert len(d.chunks) == 2

for c in d.chunks:
    assert c.granularity == 1
    assert len(c.chunks) == 3
    for cc in c.chunks:
        assert cc.granularity == 2

# construct a Document with 3 matches and each match has 4 matches
d = Document()
for _ in range(3):
    d.matches.append(Document())
for m in d.matches:
    for _ in range(4):
        m.matches.append(Document())

assert len(d.matches) == 3
for m in d.matches:
    assert m.adjacency == 1
    assert len(m.matches) == 4
    for mm in m.matches:
        assert mm.adjacency == 2
