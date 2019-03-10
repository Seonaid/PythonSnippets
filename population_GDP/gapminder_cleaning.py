import pandas as pd

gapminder = pd.read_csv('data/gapminder.csv')
gapminder_populations = pd.pivot_table(gapminder, index='country', columns='year', values=['pop'])
gapminder_lifeExp = pd.pivot_table(gapminder, index='country', columns='year', values=['lifeExp'])

gapminder_populations.to_csv('data/gapminder_populations.csv')
gapminder_lifeExp.to_csv('data/gapminder_lifeExp.csv')

print(gapminder_lifeExp.head())