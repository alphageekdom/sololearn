import numpy as np

players = [180, 172, 178, 185, 190, 192, 200, 210, 190]

mean = np.mean(players)

variance = np.var(players)

deviation = np.sqrt(variance)

high = mean + deviation

low = mean - deviation

res = [i for i in players if low < i < high]

# How many players are in the one standard deviation range
print(len(res))
