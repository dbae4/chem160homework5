import numpy as np

ntrials=1000000
dist = 0

for i in range (ntrials):
    x1=np.random.random(ntrials)
    x2=np.random.random(ntrials)
    y1=np.random.random(ntrials)
    y2=np.random.random(ntrials)
    dist += (np.mean(np.sqrt((x1-x2) **2 + (y1-y2) ** 2)))

print(dist/ntrials)
