import numpy as np

data = np.array(
    [
        150000, 125000, 320000, 540000,
        200000, 120000, 160000, 230000,
        280000, 290000, 300000, 500000,
        420000, 100000, 150000, 280000,
    ]
)

mean = np.mean(data)
std_dev = np.std(data)

low = mean - std_dev
high = mean + std_dev

res = [i for i in data if low < i < high]

percentage = int((len(res)/len(data)) * 100)

print(percentage)
