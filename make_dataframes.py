import pandas as pd

cities = ['Halifax', 'Sydney', 'Toronto', 'St. John\'s']
signups = [7, 9, 14, 3]
visitors = [123, 43, 299, 47]
weekdays = ['Sunday', 'Sunday', 'Tuesday', 'Tuesday']

list_labels = ['city', 'signups', 'visitors', 'weekday']
list_columns = [cities, signups, visitors, weekdays]

zipped = list(zip(list_labels, list_columns))
print("Type: ", type(zipped))
print(zipped)

data = dict(zipped)
print("data:", data)

users = pd.DataFrame(data)  #you can turn a dictionary into a dataframe


users['fees'] = 10 #broadcasting: sending a single value to an entire column

print(users)