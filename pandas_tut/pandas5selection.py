import pandas as pd

df = pd.read_csv("data.csv",index_col="Name")
# print(df.to_string())

# selection by column

# print(df["Name"].to_string())

# print(df["Height"].to_string())
he = df["Height"]
# he = df["Weight"]
# he = df[["Name","Height","Weight"]].to_string()
# print((he))
# print(sum(he))
# 

# selection by row/s
# print(df.loc["Venusaur"])
# print(df.loc["Venusaur",["Height","Weight"]])
# print(df.loc["Venusaur":"Blastoise",["Height","Weight"]])

# print(df.iloc[0:11:2, 0:4])

pokemon = input("Enter a pokemon name :").title()

try:
  print(df.loc[pokemon])
except KeyError as ke:
  print(f"{pokemon} not found.")