import numpy as np

data = np.array([1000, 2500, 1400, 1800, 900, 4200, 2200, 1900, 3500])

new = int(input())

new = np.append(data, new)

new = np.sort(new)

print(new)
