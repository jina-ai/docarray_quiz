from docarray import Document, DocumentArray

# construct a DocumentArray with 2 Documents
# each Document has 2 chunks and 3 matches
# each chunk has 4 chunks
# here is the structure of each Document
# <Document ('id', 'chunks', 'matches')
#    └─ matches
#          ├─ <Document ('id', 'adjacency')
#          ├─ <Document ('id', 'adjacency')
#          └─ <Document ('id', 'adjacency')
#    └─ chunks
#          ├─ <Document ('id', 'parent_id', 'granularity', 'chunks')
#              └─ chunks
#                    ├─ <Document ('id', 'parent_id', 'granularity')
#                    ├─ <Document ('id', 'parent_id', 'granularity')
#                    ├─ <Document ('id', 'parent_id', 'granularity')
#                    └─ <Document ('id', 'parent_id', 'granularity')
#          └─ <Document ('id', 'parent_id', 'granularity', 'chunks')
#              └─ chunks
#                    ├─ <Document ('id', 'parent_id', 'granularity')
#                    ├─ <Document ('id', 'parent_id', 'granularity')
#                    ├─ <Document ('id', 'parent_id', 'granularity')
#                    └─ <Document ('id', 'parent_id', 'granularity')

da = DocumentArray()
NUM_DOCS = 2
NUM_CHUNKS = 2
NUM_MATCHES = 3
NUM_CHUNKS_OF_CHUNK = 4
for i in range(NUM_DOCS):
    d = Document()
    for _ in range(NUM_CHUNKS):
        d.chunks.append(Document())
    for _ in range(NUM_MATCHES):
        d.matches.append(Document())
    for c in d.chunks:
        for _ in range(NUM_CHUNKS_OF_CHUNK):
            c.chunks.append(Document())
    da.append(d)

# select all the chunks of chunks
selected = da['@cc']
assert len(selected) == NUM_DOCS*NUM_CHUNKS*NUM_CHUNKS_OF_CHUNK

# select all the chunks of chunks and matches
selected = da['@cc,m']
assert len(selected) == NUM_DOCS*(NUM_CHUNKS*NUM_CHUNKS_OF_CHUNK + NUM_MATCHES)

# select all the root Documents and matches
selected = da['@r,m']
assert len(selected) == NUM_DOCS + NUM_DOCS*NUM_MATCHES

# flatten the nested Document
selected = da[...]
assert len(selected) == NUM_DOCS*(NUM_CHUNKS*NUM_CHUNKS_OF_CHUNK + NUM_CHUNKS + NUM_MATCHES) + NUM_DOCS
