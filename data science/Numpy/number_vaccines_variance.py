import numpy as np

vac_nums = [0, 0, 0, 0, 0,
            1, 1, 1, 1, 1, 1, 1, 1,
            2, 2, 2, 2,
            3, 3, 3,
            ]

mean = np.mean(vac_nums)

variance = np.sum((vac_nums - mean)**2)/len(vac_nums)

print(mean)
print(variance)
