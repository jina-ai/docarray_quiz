from docarray import Document
import numpy as np


# load text from uri
d = Document(uri='construct_attribute.py')
# Answer: d.load_uri_to_text()
...
assert len(d.text) > 0

# convert text to blob with the vocabulary {'hello': 2, 'jina': 3}
# Note: `,` is gone because it is filtered
d = Document(text='hello, jina')
vocabulary = {'hello': 2, 'jina': 3}
# Answer: d.convert_text_to_blob(vocab=vocabulary)
...
assert np.array_equal(d.blob, [vocabulary.get('hello'), vocabulary.get('jina')])

# convert blob back to text
# Answer: d.convert_blob_to_text(vocab=vocabulary)
...
assert d.text == 'hello jina'
