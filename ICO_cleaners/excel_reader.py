import numpy as np
import pandas as pd
import json
'''All values are represented with a unit of Weight: 60-kg bags in thousands'''

# TODO make this formatter parameterised so that we can connect it to the scrapers

# TODO create data frames for all the xlsxs given by ICO
disappearance = pd.read_excel('DisappearanceCalendarYear1963-2016.xlsx', header=5)
domestic_consumption = pd.read_excel('DomesticConsumptionCalendarYear1963-2016.xlsx', header=5)

# years = list(disappearance.columns.values)[1:]

# disappearance_dictionary = {}
# for country in disappearance.filter(regex="Country").values:
#     country = country[0]
#     disappearance_vals = disappearance.loc[disappearance['Importing Country'] == country].values.tolist()[0][1:]
#     disappearance_dictionary[country] = dict(zip(years, disappearance_vals))
#
# domestic_consumption_dictionary = {}
# for country in [y for x in domestic_consumption.filter(regex="Country").values for y in x]:
#     # format and generate an array of values for each country each year
#     country_data_as_array = np.array(domestic_consumption.loc[domestic_consumption['Country'] == country].values.tolist()[0][2:])
#     # change all NaNs to 0s
#     domestic_consumption_values = np.nan_to_num(country_data_as_array).astype(int).tolist()
#     # bind each value to its respective year
#     domestic_consumption_dictionary[country] = dict(zip(years, domestic_consumption_values))
# data = {"Domestic Consumption": domestic_consumption_dictionary}


# TODO sort out the coffee type conflict causing years to not be correctly assigned
def ico_excel_formatter(excel_file, data_title):
    df = pd.read_excel(excel_file, header=5)
    # Get country column name
    column_name = df.filter(regex="Country").columns.values[0]
    years = list(df.columns.values)[2:]
    ### print(years) ###
    df_dictionary = {}
    for country in df[column_name]:
        ### print(len(df.loc[df[column_name] == country].values.tolist()[0])) ###
        # format and generate an array of values for each country each year
        country_data_as_array = np.array(
            df.loc[df[column_name] == country].values.tolist()[0][2:])
        # change all NaNs to 0s
        df_values = np.nan_to_num(country_data_as_array).astype(int).tolist()
        # bind each value to its respective year
        df_dictionary[country] = dict(zip(years, df_values))
    return {data_title: df_dictionary}


print(ico_excel_formatter('DomesticConsumptionCalendarYear1963-2016.xlsx', 'Data_TEST'))

''' 
automated scraper should look into DB find the most recent year that there is data for, compare it against the new excel 
file that it downloads and only extract and clean new data that it finds
'''

# with open('ICO.json', 'w') as output:
#     json.dump(data, output)
