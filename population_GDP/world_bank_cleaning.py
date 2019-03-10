import pandas as pd

filename2='world_bank.csv'
GDP=pd.read_csv(filename2, skiprows=4)
GDP.rename(columns={'Country Name':'Country'}, inplace=True)
GDP.drop(['Indicator Code', 'Indicator Name'],axis=1, inplace=True)
trailers = [', The', ', Fed', ', Arab', ', Islam', ' SAR, China', ', FYR']
for trailer in trailers:
    GDP['Country'] = GDP['Country'].apply(lambda x: x.split(trailer)[0])

GDP.replace({'Virgin Islands (U.S.)':'United States Virgin Islands',
    'Congo, Dem. Rep.': 'Democratic Republic of the Congo',
    'Congo, Rep.':'Congo',
    'Korea, Dem. People’s Rep.':'South Korea',
    'Sint Maarten (Dutch part)':'Sint Maarten',
    'Yemen, Rep.':'Yemen',
    'Venezuela, RB':'Venezuela',
    'St. Martin (French part)':'St. Martin'}, inplace=True)

#GDP.set_index('Country', inplace=True)
GDP.to_csv('data/world_bank_clean.csv')
print(GDP.head())