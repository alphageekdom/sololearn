import yfinance as yf
import matplotlib.pyplot as plt

data = yf.Ticker('TSLA')

x = data.history()['Close']
x.plot()
plt.savefig('closing_prices.png')

# print(data.history(period='5d'))

# print(data.history(start='2022-01-01', end='2022-06-30'))