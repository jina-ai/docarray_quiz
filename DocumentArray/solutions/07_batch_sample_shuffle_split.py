from docarray import Document, DocumentArray

da = DocumentArray.empty(1000)

# generate batches of the batch size 300 from da
batches = [b_da for b_da in da.batch(batch_size=300)]
assert len(batches) == 4
assert len(batches[-1]) == 100

# sample
# sample 10 Documents from da
samples = da.sample(10)
assert len(samples) == 10

# split
da = DocumentArray()
for i in range(10):
    da.append(Document(tags={'level': f'level_{i%2}'}))
# group the Documents by the `tags['level']`
groups = da.split_by_tag('level')
assert len(groups) == 2
for k, g in groups.items():
    assert len(g) == 5
