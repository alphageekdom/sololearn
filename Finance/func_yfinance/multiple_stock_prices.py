import  yfinance as yf
import matplotlib.pyplot as plt


data = yf.download("AAPL MSFT TSLA", start='2022-01-01')
data['Close'].plot()

plt.savefig('multiple_closing_prices.png')