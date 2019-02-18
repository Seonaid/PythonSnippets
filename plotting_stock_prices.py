from pandas_datareader import DataReader

from datetime import date
import matplotlib.pyplot as plt

start = date(2016,1,1)
end = date(2016, 12, 31)
ticker = 'AAPL'
data_source = 'iex'
stock_prices = DataReader(ticker, data_source, start, end)
print(stock_prices.head())

stock_prices['close'].plot(title = ticker)
plt.show()