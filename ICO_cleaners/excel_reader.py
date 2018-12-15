import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join
import json
'''All values are represented with a unit of Weight: 60-kg bags in thousands
automated scraper should look into DB find the most recent year that there is data for, compare it against the new excel 
file that it downloads and only extract and clean new data that it finds
'''

# TODO make this formatter parameterised so that we can connect it to the scrapers

result = {}


def ico_excel_formatter(excel_file, data_title):

    df = pd.read_excel(excel_file, header=5)
    # Get country column name
    column_name = df.filter(regex="Country").columns.values[0]
    years = list(df.columns.values)[2:]

    for country in df[column_name]:
        country_data_as_array = np.array(df.loc[df[column_name] == country].values.tolist()[0][2:])
        # TODO currently returning as float but int conversion causes nan to mess up
        df_values = country_data_as_array.tolist()
        try:
            result[country].append({data_title: dict(zip(years, df_values))})
        except KeyError:
            result[country] = [{data_title: dict(zip(years, df_values))}]


excel_files = [f for f in listdir('xl_files/') if isfile(join('xl_files/', f)) and f[-5:] == '.xlsx']
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
