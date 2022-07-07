import yfinance as yf
import matplotlib.pyplot as plt

data = yf.Ticker('TSLA')
price = data.history(period='1y')

# pct_change => percentage change
x = price['Close'].pct_change()


# creating a histogram
x.plot(kind='hist')
plt.savefig('stock_returns_histogram.png')


# how a $1 investment would grow
returns = (x + 1).cumprod()
returns.plot()
plt.savefig('cumulative_returns.png')
