import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join
import json
import country_converter as coco

'''All values are represented with a unit of Weight: 60-kg bags in thousands
automated scraper should look into DB find the most recent year that there is data for, compare it against the new excel 
file that it downloads and only extract and clean new data that it finds
'''
# sort out warnings
# TODO upload ICO.json to server
# TODO nans were change to 0 sort this out
result = []


def manually_add_alpha_code(country):
    alpha_code = input("Enter alpha two code for " + country + ": ")
    if alpha_code == "":
        return "null"
    return alpha_code


def set_multiplier(excel_file):
    multiplier = 1
    multiplier_check = pd.read_excel(excel_file, header=1, nrows=1, usecols=0)
    multiplier_value = multiplier_check.values[0][0]
    if multiplier_value == "(Thousands)":
        multiplier = 1000
    return multiplier


def get_alpha_code(country):
    code = coco.convert(names=country, to='ISO2')
    if code == "not found":
        return manually_add_alpha_code(country)
    else:
        return code


def ico_excel_formatter(excel_file, data_title):
    multiplier = set_multiplier(excel_file)
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
        country_profile = list(filter(lambda item: item['country'] == country, result))
        df_values = np.nan_to_num(np.array(df.loc[df[column_name] == country].values.tolist()[0][offset:]) * multiplier).tolist()

        if not country_profile:
            alpha_code = get_alpha_code(country)
            result.append({"id": alpha_code, "country": country, 'data': [{"year": years[i], data_title: df_values[i]} for i in range(num_of_data_points)]})
        else:
            for d in country_profile[0]['data']:
                i = country_profile[0]['data'].index(d)
                d[data_title] = df_values[i]


def run():
    excel_files = [f for f in listdir('xl_files/') if isfile(join('xl_files/', f)) and f[-5:] == '.xlsx' and f[0] != '~']
    unextracted_files = []
    for sheet in excel_files:
        try:
            ico_excel_formatter('xl_files/' + sheet, sheet[:-26])
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


