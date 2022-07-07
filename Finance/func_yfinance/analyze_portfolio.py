import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np

stocks = ['AAPL', 'AMZN', 'MSFT', 'TSLA']
weights = [0.3, 0.2, 0.4, 0.1]

data = yf.download(stocks, start='2022-01-01')

# daily returns
x = data['Close'].pct_change()

# portfolio return
ret = (x * weights).sum(axis = 1)

# total cumulative return
cumulative = (ret + 1).cumprod()

cumulative.plot()
plt.savefig('total_cumulative_return_portfolio.png')

# daily volatility
daily_std = np.std(ret)
print("Daily volatility: ", daily_std)

# annual volatility
annual_std = np.std(ret) * np.sqrt(252)
print("Annual volatility: ", annual_std)

# measure of risk-adjusted return, 
sharpe = (np.mean(ret) / np.std(ret)) * np.sqrt(252)
print("Sharpe: ", sharpe)