from docarray import Document

# this doesn't work at the moment
#d = Document(uri='https://modelviewer.dev/shared-assets/models/Astronaut.glb')

import os
import urllib.request
fn = 'astronaut.glb'
if not os.path.isfile(fn):
    urllib.request.urlretrieve('https://modelviewer.dev/shared-assets/models/Astronaut.glb', fn)
d = Document(uri=fn)
# load the 3D model mesh to blob with 1000 sample points
...
assert d.tensor.shape == (1000, 3)
print(d.tensor.shape)