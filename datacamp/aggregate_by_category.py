import pandas as pd
import matplotlib.pyplot as plt

nasdaq = pd.DataFrame(pd.read_csv('./DataSets/nasdaq-listings.csv'))

# print(nasdaq.info())

nasdaq['market_cap_mil'] = nasdaq['Market Capitalization'].div(1e6)
nasdaq = nasdaq.drop('Market Capitalization', axis=1)

nasdaq_by_sector = nasdaq.groupby('Sector')

# for sector, data in nasdaq_by_sector:
#     print(sector, data.market_cap_mil.mean())

mcap_by_sector = nasdaq_by_sector.market_cap_mil.mean()

title = 'NASDAQ - Market Capitalization by Sector'
mcap_by_sector.plot(kind='barh', title=title)
plt.show()