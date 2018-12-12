import numpy as np
import pandas as pd
import json

disappearance = pd.read_excel('DisappearanceCalendarYear1963-2016.xlsx', header=5)
domestic_consumption = pd.read_excel('DomesticConsumptionCalendarYear1963-2016.xlsx', header=5)

years = list(disappearance.columns.values)[1:]

country_dictionary = {}
for country in disappearance.filter(regex="Country").values:
    country = country[0]
    disappearance_vals = disappearance.loc[disappearance['Importing Country'] == country].values.tolist()[0][1:]
    country_dictionary[country] = dict(zip(years, disappearance_vals))

country_dictionary2 = {}
for country in domestic_consumption.filter(regex="Country").values:
    country = country[0]
    domestic_consumption_vals = np.nan_to_num(np.array(domestic_consumption.loc[domestic_consumption['Country'] == country].values.tolist()[0][2:])).astype(int).tolist()
    country_dictionary2[country] = dict(zip(years, domestic_consumption_vals))


print(country_dictionary2)

with open('ICO.json', 'w') as output:
    json.dump(country_dictionary, output)
