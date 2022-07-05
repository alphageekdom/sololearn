import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

# Bitcoin 2018-2021 price(s) 
bitcoin = [3869.47, 7188.46, 22203.31, 29391.78]
years = ['2018', '2019', '2020', '2021']

pv = 1000
coin = pv/bitcoin[0]
new_values = np.multiply(bitcoin, coin)

plt.plot(years, new_values)
plt.savefig('bitcoin.png')