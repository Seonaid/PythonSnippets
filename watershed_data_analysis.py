import pandas as pd
import matplotlib.pyplot as plt

watershed_data = pd.read_csv('./datacamp/datasets/complete_extraction.csv')
print(watershed_data.info())

watershed_data=watershed_data.drop(['kitchen', 'shared'], axis=1)

rent_stats = watershed_data['Rent'].describe()
nightly_stats = watershed_data['NightlyRent'].describe
occupancy_stats = watershed_data['Occupancy'].describe

summary_stats = watershed_data[['Rent', 'NightlyRent', 'Occupancy']].describe()
print(summary_stats.round(2))

rent_by_city =watershed_data.groupby('city')
avg_city_rent = rent_by_city.Rent.mean().sort_values()

title = 'Average Rent By City'
avg_city_rent.plot(kind='barh', title=title)
plt.show()

#Is there any link between Nightly Rent and ST Nightly Occupancy?
# watershed_data.plot(kind='scatter', x='NightlyRent', y='Occupancy')

#How do Monthly and Daily Rates Compare?
# watershed_data.plot(kind='scatter', x='Rent', y='NightlyRent')

#Is there any link between Monthly Rent and ST Nightly Occupancy?

# watershed_data.plot(kind='scatter', x='Rent', y='Occupancy')
# plt.xlabel('Monthly Rent')
# plt.ylabel('Nightly Occupancy')



#Box plots for looking at spread of data

# cols = ['Rent', 'NightlyRent']
# watershed_data[cols].plot(kind='box', subplots=True)

# plt.show()