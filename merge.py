import pandas as pd

sheets = ['COLOMBIA', 'ARGENTINA', 'BRASIL', 'CHILE', 'MEXICO', 'PERU', 'URUGUAY']

#TODO list comprehension!!
def merge(filename):
    dataframes = []

    for sheet in sheets:
        dataframes.append(pd.read_excel (filename, sheet_name=sheet))

    output = pd.concat(dataframes,  keys=sheets)

    output.to_excel('appended.xlsx')

