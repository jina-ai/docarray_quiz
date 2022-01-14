from docarray import Document, DocumentArray
from pathlib import Path

# construct from a single doc
doc = Document()
da = ...
assert len(da) == 1

# construct from a list
doc_list = [Document(), Document]
da = ...
assert len(da) == 2

# construct from a generator
def doc_generator():
    for _ in range(3):
        yield Document()
da = ...
assert len(da) == 3

# construct from all .py files in the current folder
da = ...
assert len(da) > 0
for d in da:
    assert Path(d.uri).suffix == '.py'