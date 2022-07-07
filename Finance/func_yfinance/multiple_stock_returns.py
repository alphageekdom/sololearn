import yfinance as yf
import matplotlib.pyplot as plt

# compare daily stocks
data = yf.download('AAPL MSFT TSLA', start='2022-01-01')
data['Close'].plot()
plt.savefig('multiple_stock_daily.png')


# daily returns
x = data['Close'].pct_change()
x.plot()
plt.savefig('multiple_daily_returns.png')

# cumulative returns
(x + 1).cumprod().plot()
plt.savefig('multiple_cumulative_returns.png')