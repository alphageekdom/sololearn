import yfinance as yf

def ROE(ticker):

    data = yf.Ticker(ticker)
    roe = data.info['returnOnEquity']
    name = data.info['shortName']
    print(name, ":", roe)

ROE('AAPL')
ROE('MSFT')