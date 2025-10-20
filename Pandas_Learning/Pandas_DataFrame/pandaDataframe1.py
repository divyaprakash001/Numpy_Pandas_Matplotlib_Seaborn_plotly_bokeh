import pandas as pd

lists = [
  [100,80,10],
  [90,70,7],
  [120,100,14],
  [80,50,2],
  [80,50,2],
]
dataframe = pd.DataFrame(lists,columns=["IQ","Marks","Package"])
# print(dataframe)

dics = {
  "name":["nitish","ankit","rupesh","risabh","amit","ankita"],
  "iq":[100,90,120,80,0,0],
  "marks":[80,70,100,50,0,0],
  "package":[10,7,14,2,0,0],
}

dataframed = pd.DataFrame(dics)
# print(dataframed)

movies= pd.read_csv("Pandas_Learning\\Pandas_DataFrame\\movies.csv")
# print(movies.shape)
# print(movies.dtypes)

ipl= pd.read_csv("Pandas_Learning\\Pandas_DataFrame\\ipl-matches.csv")
# print(ipl.shape)
# print(ipl.dtypes)
# print(ipl.index)
# print(movies.columns)
# print(ipl.columns)

# print(dataframe.values)
# print(ipl.values)
# print(movies.values)

# print(ipl.head(10))
# print(ipl.tail(10))
# print(ipl.sample(10))

# ipl.info()
# movies.info()

# print(ipl.describe())
# print(movies.describe())
# print(movies.isnull().sum())
# print(ipl.isnull().sum())

youchart= pd.read_csv("Pandas_Learning\\Pandas_DataFrame\\chart_data.csv")
youchart= pd.read_csv("Pandas_Learning\\Pandas_DataFrame\\totals.csv")
# print(youchart.info())
# print(youchart.isnull().sum())
# print(dataframe.duplicated().sum())

# print(dataframed)
# use inplace=true to change permanently
dataframed.rename(columns={"marks":"percent","package":"lpa"},inplace=True)
# print(dataframed)


# mathematical function

# print(dataframed.sum())
# print(dataframed.sum(axis=1))
# print(dataframe.mean())
# print(dataframe.mean(axis=1))

# print(dataframe.var())
# print(dataframe.var(axis=1))


# ------------------
# selecting cols from a dataframe

# print(movies['title_x'])  #this gives a series
# print(ipl)
# print(ipl['City'])

# multiple cols
# print(movies)
# print(movies[['title_x','release_date','actors']])

# print(ipl)
# print(ipl[['Team1','Team2','WinningTeam']])


# selecting rows in dataframe

# print(dataframed)

dataframed.set_index("name",inplace=True)
print(movies.iloc[0])
# print(movies.iloc[0:5])
# print(movies.iloc[5:15:2])

# fancy indexing
# print(movies.iloc[[0,4,5]])

# print(dataframed.loc['nitish'])
# print(dataframed.loc['nitish':"risabh"])
# print(dataframed.iloc[0])

# fancy indexing
# print(dataframed.loc[['nitish','risabh']])
# print(dataframed.iloc[[0,3]])


