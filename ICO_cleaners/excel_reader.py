import numpy as np
import pandas as pd
import json
'''All values are represented with a unit of Weight: 60-kg bags in thousands'''

# TODO make this formatter parameterised so that we can connect it to the scrapers

# TODO create data frames for all the xlsxs given by ICO
disappearance = pd.read_excel('DisappearanceCalendarYear1963-2016.xlsx', header=5)
domestic_consumption = pd.read_excel('DomesticConsumptionCalendarYear1963-2016.xlsx', header=5)

years = list(disappearance.columns.values)[1:]

# TODO convert this repetitive for loop into a cleaner method
disappearance_dictionary = {}
for country in disappearance.filter(regex="Country").values:
    country = country[0]
    disappearance_vals = disappearance.loc[disappearance['Importing Country'] == country].values.tolist()[0][1:]
    disappearance_dictionary[country] = dict(zip(years, disappearance_vals))

domestic_consumption_dictionary = {}
for country in [y for x in domestic_consumption.filter(regex="Country").values for y in x]:
    # format and generate an array of values for each country each year
    country_data_as_array = np.array(domestic_consumption.loc[domestic_consumption['Country'] == country].values.tolist()[0][2:])
    # change all NaNs to 0s
    domestic_consumption_values = np.nan_to_num(country_data_as_array).astype(int).tolist()
    # bind each value to its respective year
    domestic_consumption_dictionary[country] = dict(zip(years, domestic_consumption_values))


print(domestic_consumption.loc[domestic_consumption['Country'] == 'Bolivia'])

''' 
automated scraper should look into DB find the most recent year that there is data for, compare it against the new excel 
file that it downloads and only extract and clean new data that it finds
'''

with open('ICO.json', 'w') as output:
    json.dump(disappearance_dictionary, output)
