import pandas as pd
import matplotlib.pyplot as plt

watershed_data = pd.read_csv('./datacamp/datasets/complete_extraction.csv', index_col='ws_property_id')
print(watershed_data.info())

watershed_data=watershed_data.drop(['kitchen', 'shared'], axis=1)

rent_stats = watershed_data['Rent'].describe()
nightly_stats = watershed_data['NightlyRent'].describe
occupancy_stats = watershed_data['Occupancy'].describe

summary_stats = watershed_data[['Rent', 'NightlyRent', 'Occupancy']].describe()
print(summary_stats.round(2))

city_property_groups =watershed_data.groupby(['city', 'property_type'])
# avg_city_rent = rent_by_city.Rent.mean().sort_values()

# print(city_property_groups.size())
# rent_groups = city_property_groups.Rent.describe()
# rent_groups.to_csv('rent_groups.csv')

# st_groups = city_property_groups[['NightlyRent', 'Occupancy']].describe()
# st_groups.to_csv('st_groups.csv')

provided_stats = city_property_groups[['10th Percentile', '90th Percentile']].mean()
provided_stats.to_csv('provided_stats.csv')


# print(type(rent_by_city))
# print(rent_by_city.head())

# rent_by_prop_type = watershed_data.pivot(index='location', columns='property_type', values=['Rent', 'NightlyRent'])
# print(rent_by_prop_type.describe())

# break_by_prop_type = watershed_data.unstack(level='city')
# print(break_by_prop_type.head())

# prop_type_by_city = rent_by_city.groupby('property_type')
# avg_rent_city_type = prop_type_by_city.Rend.mean().sort_values()

# title = 'Average Rent By City and Property Type'
# avg_rent_city_type.plot(kind='barh', title=title)
# plt.show()



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