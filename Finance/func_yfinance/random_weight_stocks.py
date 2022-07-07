import numpy as np

wts = np.random.uniform(size = 4)
wts = wts/np.sum(wts)

print(wts)