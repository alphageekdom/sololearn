import yfinance as yf
import matplotlib.pyplot as plt

data = yf.Ticker('TSLA')

x = data.earnings
print(x)

x.plot(kind="bar")
plt.savefig('earnings.png')