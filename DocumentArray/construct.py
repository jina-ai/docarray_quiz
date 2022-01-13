from docarray import Document, DocumentArray
from pathlib import Path

# construct from a single doc
doc = Document()
# Answer: da = DocumentArray(doc)
da = ...
assert len(da) == 1

# construct from a list
doc_list = [Document(), Document]
# Answer: da = DocumentArray(doc_list)
da = ...
assert len(da) == 2

# construct from a generator
def doc_generator():
    for _ in range(3):
        yield Document()
# Answer: da = DocumentArray(doc_generator())
da = ...
assert len(da) == 3

# construct from all .py files in the current folder
# Answer: da = DocumentArray.from_files('./*.py')
da = ...
assert len(da) > 0
for d in da:
    assert Path(d.uri).suffix == '.py'