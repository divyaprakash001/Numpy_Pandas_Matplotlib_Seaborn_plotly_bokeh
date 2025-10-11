import pandas as pd

# print(pd.__version__)

# series => A Pandas 1-Dimensional labelled array that
# can hold any data type 

data = [100,102,104,200,202]
# data = [100,102.2,104]  #float64
# data = ["100","hello","104"] #objects
# data = [True,False,True] #bool

series = pd.Series(data, index=["a","b","c","d","e"])
# series = pd.Series(data, index=["apartment #1","apartment #2","apartment #3"])
# series.loc["c"] = 200
# print(series.loc["a"])
# print(series.loc["c"])
# print(series.iloc[0])
# print(series.iloc[1])
# print(series.iloc[2])
# series.iloc[2] = 109
# print(series)

# print(series >= 200)
print(series[series >= 200])
print(series[series <= 200])