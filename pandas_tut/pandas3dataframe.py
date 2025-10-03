import pandas as pd
import numpy as np

# DataFrame = A tabular data structure with rows and columns.
# (2 Dimensional). Similar to an Excel Spreadsheet


data = {
  "Name":["Sponge","Patrick","Sopho"],
  "Age":[35,26,30],
}

dataframe = pd.DataFrame(data, index=["Employee 1","Employee 2","Employee 3"])

print(dataframe.loc["Employee 2"])

print(dataframe.iloc[0])



# add a new column
dataframe["Job"] = ["CEO","Junior Developer","Senior Developer"]
print(dataframe)

# add new rows
new_rows = pd.DataFrame([{"Name":"Sandy","Age":28,"Job":"Engineer"},
                        {},
                        {"Name":"Cancy","Age":38,"Job":"Manager"}],
                       index=["Employee 4","Employee 5","Employee 6"])
dataframe = pd.concat([dataframe,new_rows])
print(dataframe)