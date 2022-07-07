import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt
import yfinance as yf

# Bitcoin 2018-2021 price(s) 
data = yf.Ticker('BTC-USD')
x = data.history('1y')['Close']

start = 1000/x[0]
new_values = np.multiply(start, x)

annual_std = np.std(new_values) * np.sqrt(252)

sharpe = (np.mean(new_values) / np.std(new_values)) * np.sqrt(252)

plt.plot(new_values)
plt.savefig('bitcoin.png')

print("Risk: ", annual_std)
print("Sharpe: ", sharpe)