import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join
import json
'''All values are represented with a unit of Weight: 60-kg bags in thousands
automated scraper should look into DB find the most recent year that there is data for, compare it against the new excel 
file that it downloads and only extract and clean new data that it finds
'''

# TODO upload ICO.json to server

result = []


def ico_excel_formatter(excel_file, data_title):
    multiplier = 1
    multiplier_check = pd.read_excel(excel_file, header=1, nrows=1, usecols=0)
    multiplier_value = multiplier_check.values[0][0]
    if multiplier_value == "(Thousands)":
        multiplier = 1000

    df = pd.read_excel(excel_file, header=5)
    # Get country column name
    column_name = df.filter(regex="Country").columns.values[0]
    # Offset to column with first set of values
    offset = 1
    if list(df.columns.values)[1] == "Unnamed: 1":
        offset = 2

    years = list(df.columns.values)[offset:]
    num_of_data_points = len(years)

    for country in df[column_name]:
        df_values = (np.array(df.loc[df[column_name] == country].values.tolist()[0][offset:]) * multiplier).tolist()

        country_profile = list(filter(lambda item: item['country'] == country, result))
        data = []
        for i in range(num_of_data_points):
            data.append({"year": years[i], "value": df_values[i]})

        if not country_profile:
            result.append({"country": country, data_title: data})
        else:
            country_profile[0].update({data_title: data})


def run():
    excel_files = [f for f in listdir('xl_files/') if isfile(join('xl_files/', f)) and f[-5:] == '.xlsx' and f[0] != '~']
    unextracted_files = []
    for sheet in excel_files:
        try:
            ico_excel_formatter('xl_files/' + sheet, sheet[:-18])
        except IndexError:
            unextracted_files.append(sheet)

    if len(unextracted_files) != 0:
        raise FileExistsError(str(unextracted_files) + " could not be parsed")

    with open('ICO.json', 'w') as output:
        json.dump(result, output)

    if not result:
        raise ValueError("No data could be parsed")


# should be removed in production
run()


