import pandas as pd
import numpy as np

# lists = [
#   [100,80,10],
#   [90,70,7],
#   [120,100,14],
#   [80,50,2],
#   [80,50,2],
# ]
# dataframe = pd.DataFrame(lists,columns=["IQ","Marks","Package"])
# print(dataframe)

# dics = {
#   "name":["nitish","ankit","rupesh","risabh","amit","ankita"],
#   "iq":[100,90,120,80,0,0],
#   "marks":[80,70,100,50,0,0],
#   "package":[10,7,14,2,0,0],
# }

# dataframed = pd.DataFrame(dics)
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

# youchart= pd.read_csv("Pandas_Learning\\Pandas_DataFrame\\chart_data.csv")
# youchart= pd.read_csv("Pandas_Learning\\Pandas_DataFrame\\totals.csv")
# print(youchart.info())
# print(youchart.isnull().sum())
# print(dataframe.duplicated().sum())

# print(dataframed)
# use inplace=true to change permanently
# dataframed.rename(columns={"marks":"percent","package":"lpa"},inplace=True)
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

# dataframed.set_index("name",inplace=True)
# print(movies.iloc[0])
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


# selecting both rows and cols
# print(movies.iloc[0:2,0:3])
# print(movies.loc[0:2,'title_x':'poster_path'])

# filtering dataframe

# print(movies[movies['title_x']=='Uri: The Surgical Strike']['release_date'])
# print(ipl[ipl['MatchNumber']=='Final'][['Season','WinningTeam']])

# how many super overs finishes have occured
# print(ipl[ipl['SuperOver']=='Y'].shape[0])

# print(ipl[(ipl['City'] == 'Kolkata') & (ipl['WinningTeam'] == 'Chennai Super Kings')].shape[0])

# toss winner is match winner in percentage
# print((ipl[ipl['TossWinner'] == ipl['WinningTeam']].shape[0]/ipl.shape[0])*100)


# movies with rating higher than 8 and votes>10000
# print(movies[(movies['imdb_rating'] > 8.5) & (movies['imdb_votes'] > 10000)].shape[0])


# Action movies with rating higher than 7.5
# mask1 = movies['genres'].str.split('|').apply(lambda x:'Action' in x)
# print(movies[(movies['genres'].str.contains('Action') & (movies['imdb_rating']>7.5))])
# mask1 = movies['genres'].str.contains('Action')
# mask2 = movies['imdb_rating']>7.5

# print(movies[mask1 & mask2])


# how to add new cols
# movies['Country'] = 'India'
# print(movies)


# from existing ones
# replace the missing values rows
# movies.dropna(inplace=True)
# print(movies['actors'].isnull().sum())
# movies['lead_actor'] = (movies['actors'].str.split('|').apply(lambda x : x[0]))

# print(movies)

# important dataframe function

# astype function
# print(ipl.info())
# ipl['ID']=(ipl['ID'].astype("int32"))
# print(ipl['Margin'].isnull().sum())
# ipl['Margin']=(ipl['Margin'].astype("int32"))  #if nan present, error

# ipl['Season'] = ipl['Season'].astype("category")
# ipl['Team1'] = ipl['Team1'].astype("category")
# ipl['Team2'] = ipl['Team2'].astype("category")
# ipl.info()


# important methods of dataframe

# # value_counts (applicable on series and dataframe)

# # a = pd.Series([1,1,1,2,2,3])
# # print(a.value_counts())

# d = pd.DataFrame([
#   [100,80,10],
#   [90,70,7],
#   [120,100,14],
#   [80,70,14],
#   [80,70,14],
# ],columns=['First','seconbd','third'])

# print(d)
# print(d.value_counts())  will be more application on series

# print(ipl)
# find which player has won the post potm -> in finals and qualifiers
# ipl.info()
# print(ipl[~ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts())
# pd.set_option('display.max_columns', None)


import matplotlib.pyplot as plt
# toss decision plot
# tos  = (ipl['TossDecision'].value_counts()).plot(kind='pie')
# tos.plot(kind='pie')
# plt.show()

# how many matches each team has played
# print(ipl['Team1'].value_counts())
# print(ipl['Team2'].value_counts())
# print((ipl['Team1'].value_counts() + ipl['Team2'].value_counts()).sort_values(ascending=False))


# sort_values(series and dataframe) -> ascending -> na_position -> inplace -> multiple cols
# x = pd.Series([12,14,1,56,89])
# print(x.sort_values(ascending=False,inplace=True))
# print(x)


# print(movies)
# print(movies.sort_values('title_x'))

students = pd.DataFrame(
    {
        'name':['nitish','ankit','rupesh',np.nan,'mrityunjay',np.nan,'rishabh',np.nan,'aditya',np.nan],
        'college':['bit','iit','vit',np.nan,np.nan,'vlsi','ssit',np.nan,np.nan,'git'],
        'branch':['eee','it','cse',np.nan,'me','ce','civ','cse','bio',np.nan],
        'cgpa':[6.66,8.25,6.41,np.nan,5.6,9.0,7.4,10,7.4,np.nan],
        'package':[4,5,6,np.nan,6,7,8,9,np.nan,np.nan]

    }
)

# print(students)
# inplace=True makes the change permanent
# print(students.sort_values('name',na_position='first',ascending=False,inplace=True))
# print(students.sort_values('name',na_position='last',ascending=True))
# print(students.sort_values('name',ascending=True))
# print(students.sort_values('package',ascending=False))
# print(movies)
# print(movies.sort_values(['year_of_release','title_x']))
# print(movies.sort_values(['year_of_release','title_x'],ascending=[True,False]))


# rank applicable on series only
batsman = pd.read_csv('Pandas_Learning\\Pandas_DataFrame\\batsman.csv')
# pd.set_option('display.max_rows', None)
batsman['batsman_rank'] = batsman['batsman_run'].rank(ascending=False)
# print(batsman.sort_values('batsman_rank'))

# sort_index  application on series and dataframe

marks = {
    'maths':67,
    'english':57,
    'science':89,
    'hindi':100
}

marks_series = pd.Series(marks)
# print(marks_series.sort_index())
# print(marks_series.sort_index(ascending=False))

# print(movies.sort_index())
# print(movies.sort_index(ascending=False))

# set_index applicable on datafram - inplace
# print(batsman)
# print(batsman.set_index('batter'))
# batsman.set_index('batter',inplace=True)
# print(batsman)

# reset_index(series + dataframe) -> drop parameter
# batsman.reset_index(inplace=True)
# print(batsman)


# how to replace existing index without loosing
# batsman.reset_index().set_index('batsman_rank',inplace=True)

# print(batsman)

# series to dataframe using reset_index
# print(marks_series.reset_index())
# print(type(marks_series.reset_index()))

# rename --- function applicable on dataframe -> index

# movies.set_index('title_x',inplace=True)
# movies.rename(columns={'imdb_id':'imdb','poster_path':'link'},inplace=True)
# movies.rename(index={'Uri: The Surgical Strike':'Uri: The Divya Prakash','Battalion 609':'Divya Battalion'},inplace=True)
# # print(movies)

# unique applicable on series
# temp = pd.Series([1,1,2,2,3,3,4,4,5,5,np.nan,np.nan])
# print(temp)
# print(temp.unique())
# print(len(ipl['Season'].unique()))

# nunique  applicable on (series + dataframe) -> does not count nan -> dropna parameter
# print(ipl['Season'].nunique())
# print((temp.nunique()))


# # isnull  applicable on (series + dataframe)
# print(students['name'][students['name'].isnull()])

# # notnull(series + dataframe)
# print(students['name'][students['name'].notnull()])


# hasnans(series)
# print(students['name'].hasnans)

# print(students.isnull())
# print(students.notnull())
# print(students.hasnans())  #not applicable here


# dropna(series + dataframe) -> how parameter -> works like or
# print(students)
# print(students['name'].dropna())
# print(students.dropna())  #remove all rows where columns has nan
# print(students.dropna(how='any')) #remove all rows if any nan found
# print(students.dropna(how='all')) #remove  rows where all column values are missing or nan
# print(students.dropna(subset=['name'])) #remove  rows where name column has nan or missing value
# print(students.dropna(subset=['name','college'])) #remove  rows where name and college column has nan or missing value
# (students.dropna(inplace=True))
# print(students)

# fillna(series + dataframe)
# print(students['name'].fillna('unknown'))
# print(students['name'].fillna('unknown',inplace=True))

# print(students['package'].fillna(students['package'].mean()))
# print(students['package'].fillna(students['package'].mean(),inplace=True))
# print(students)

# print(students['name'].fillna(method='bfill'))
# print(students.ffill())
# print(students.bfill())


# drop_duplicates (series + dataframe) -> works like and -> duplicated()

# temp = pd.Series([1,1,1,2,3,3,4,4])
# print(temp.drop_duplicates())

marks = pd.DataFrame([
  [100,80,10],
  [90,70,7],
  [120,100,14],
  [80,70,14],
  [80,70,14],
])
# print(marks.duplicated().sum())
# print(marks.drop_duplicates(keep='first'))
# print(marks.drop_duplicates(keep='last'))

# find the last match played by virat kohli in Delhi
ipl['all_players']=(ipl['Team1Players'] + ipl['Team2Players'])
# print(ipl['all_players'].unique())

# def did_kohli_play(players_list):
#   return 'V Kohli' in players_list

# ipl['did_kohli_play']  = ipl['all_players'].apply(did_kohli_play)
# # we can do also like this instead of creating function, we use lambda function
# ipl['did_kohli_play']  = ipl['all_players'].apply(lambda x : True if 'V Kohli' in x else False)
# # using subsets so that we can drop_duplicates only on based on city and did_kohli_play
# print(ipl[(ipl['did_kohli_play']==True) & (ipl['City'] == 'Delhi')].drop_duplicates(subset=['City','did_kohli_play'],keep='first'))


# drop series and dataframe ------------------
# temp = pd.Series([10,2,3,16,35,98,74,19])
# print(temp.drop(index=[0,6]))

# print(students)
# # print(students.drop(columns=['branch','cgpa']))
# print(students.drop(index=[0,8]))
# print(students.set_index('name').drop(index=['nitish','aditya']))
# print(students.drop(index=[0,8]))


# apply(series + dataframe)
temp = pd.Series([10,20,30,40,50])

# def sigmoid(value):
#   return 1/1+np.exp(-value)

# print(temp.apply(lambda x : x*2))
# print(temp.apply(lambda value : 1/1+np.exp(-value)))
# print(temp.apply(sigmoid))

# on dataframe
points_df = pd.DataFrame(
    {
        '1st point':[(3,4),(-6,5),(0,0),(-10,1),(4,5)],
        '2nd point':[(-3,4),(0,0),(2,2),(10,10),(1,1)]
    }
)

def euclidian(row):
  pt_a = row['1st point']
  pt_b = row['2nd point']
  return ((pt_a[0] - pt_b[1]) **2 + (pt_a[1] - pt_b[0])**2 )** .5

points_df['distance']=(points_df.apply(euclidian,axis=1))
print(points_df)