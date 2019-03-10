import pandas as pd

filename = 'Energy Indicators.xls'
energy = pd.read_excel(filename, skiprows=17, skipfooter=38, usecols=[2,3,4,5], na_values='...')
energy.columns = ['Country','Energy Supply (PJ)', 'Energy Supply per Capita', '% Renewable']
energy['Country'] = energy['Country'].apply(lambda x: x.split(' (')[0])
energy['Country'] = energy['Country'].apply(lambda x: x.rstrip('0123456789'))
energy.replace({'China, Hong Kong Special Administrative Region':'Hong Kong',
    "China, Macao Special Administrative Region":"Macao",
    "Democratic People's Republic of Korea":'South Korea',
    "United States of America": "United States",
    "The former Yugoslav Republic of Macedonia":"Macedonia",
    "United Kingdom of Great Britain and Northern Ireland":"United Kingdom"}, inplace=True)

#energy.set_index('Country', inplace=True)
print(energy.head())

energy.to_csv('energy_indicators_clean.csv')