import yfinance as yf
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Corr => how securities move in relation to each other
data = yf.download('FB AMZN AAPL NFLX GOOG', start='2022-01-01')
x = data['Close'].pct_change()
corr = x.corr()

sm.graphics.plot_corr(corr, xnames=list(x.columns))

plt.savefig('correlation_graph.png')