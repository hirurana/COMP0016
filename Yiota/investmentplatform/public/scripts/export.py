import pandas as pd
from pandas import DataFrame
import sys

# arguments
# country name and record type
country_input = sys.argv[1]

# Will have to change to pull from database
print("Loading JSON file...")
df = pd.read_json("../external_data/ICO.json")

print("Processing JSON file...")
# get longest set of years
print("Setting excel file column names")
years = []
for dp in df['data']:
    dp_years = [i['year'] for i in dp]
    if len(dp_years) > len(years):
        years = dp_years

# get types
print("Finding " + country_input + " in records...")
data = df.loc[df['country'] == country_input]['data'].values.T.tolist()[0]
data_types = list(data[0].keys())
columns = data_types

# # formatting data to fit in columns
empty = {}
output = DataFrame(empty, columns= columns)

print("Formatting data...")

for i in data:
    row_values = []
    for j in data_types:
        row_values.append(i[j])
    output.loc[data.index(i)] = row_values

# renaming columns to include units
for i in range(1,len(columns)):
    columns[i] = columns[i] + " (60 kg bags of green coffee beans)"
output.columns = columns

print("Writing to XLSX file...")
output.to_excel("exported_data.xlsx")
print("Done!")
