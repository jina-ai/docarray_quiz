from docarray import Document

# this doesn't work at the moment
# d = Document(uri='https://upload.wikimedia.org/wikipedia/commons/3/31/Beethoven_Piano_Sonata_Op_22%2C_2nd_movement%2C_bars_30-32.wav')

import os
import urllib.request
fn = 'beethoven.wav'
if not os.path.isfile(fn):
    urllib.request.urlretrieve('https://upload.wikimedia.org/wikipedia/commons/3/31/Beethoven_Piano_Sonata_Op_22%2C_2nd_movement%2C_bars_30-32.wav', fn)
d = Document(uri=fn)

# load the uri into blob
...
assert len(d.tensor.shape) == 2