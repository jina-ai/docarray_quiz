from docarray import Document
import numpy as np


# load text from uri
d = Document(uri='01_construct_attribute.py')
...
assert len(d.text) > 0

# convert text to blob with the vocabulary {'hello': 2, 'jina': 3}
# Note: `,` is gone because it is filtered
d = Document(text='hello, jina')
vocabulary = {'hello': 2, 'jina': 3}
...
assert np.array_equal(d.blob, [vocabulary.get('hello'), vocabulary.get('jina')])

# convert blob back to text
...
assert d.text == 'hello jina'
