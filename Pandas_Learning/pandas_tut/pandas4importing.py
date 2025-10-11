import pandas as pd

# df = pd.read_csv("data.csv")
df = pd.read_json("poke.json")
# print(df)
print(df.to_string())
