import numpy as np
import pandas as pd

# pandas series => 1D array holding any data types

# series from list
# string
country = ["India","Pakistan","USA","Nepal","Srilanka"]
series = pd.Series(country)
# print(series)

# integers
runs = [13,24,56,78,100]
runseries = pd.Series(runs,name="Virat Runs")
# runseries = pd.Series(runs,index=[1,2,3,4,5],name="Virat Runs")
# runseries = pd.Series(runs,dtype=pd.Int32Dtype)
# print(runseries)
# print(runseries.iloc[0])

# custom index
marks = [67,57,89,100,100]
subjects = ["Maths","English","Science","Hindi","Computer"]

# sseries = pd.Series(marks,index=subjects)
markss = pd.Series(marks,index=subjects,name="Divya Mark's")
# print(markss)
# print(sseries.loc["Computer"])


# series using dictionary

marks = {
  "maths":99,
  "english":93,
  "hindi":83,
  "science":97,
  "computer":100
}

subjects = ["Maths","English","Science","Hindi","Computer"]
marks_series = pd.Series(marks,name="Divya ka marks")
# print(marks_series)

# attributes
# print(marks_series.size)
# print(marks_series.dtype)
# print(marks_series.name)
# print(marks_series.is_unique)
# print(marks_series.index)
# print(runseries.index)
# print(marks_series.values) 


# Series using read_csv ----------
subs = pd.read_csv("Pandas_Learning\\Pandas_Series\\subs.csv")
subs_series = subs.squeeze()
# print(type(subs)) #DataFrame
# print("------------------")
# print(subs.squeeze())  # convert dataframe to Series
# print(type(subs.squeeze())) 


# kohli_runs = pd.read_csv("Pandas_Series\\kohli_ipl.csv",index_col="runs")
kohli_runs = pd.read_csv("Pandas_Learning\\Pandas_Series\\kohli_ipl.csv",index_col="match_no")
kohli_run_series = kohli_runs.squeeze()
# print(kohli_runs)
# print(type(kohli_runs))
# print("------------------")
# print(kohli_runs.squeeze())  # convert dataframe to Series
# print(type(kohli_runs.squeeze())) 


movies = pd.read_csv("Pandas_Learning\\Pandas_Series\\bollywood.csv",index_col="movie")
movie_series = ((movies.squeeze()))
# print(type(movie_series))
# print(movies)
# print(type(movies))  #DataFrame
# print("------------------")
# print(movies.squeeze())  # convert dataframe to Series
# print(type(movies.squeeze())) 

# data = pd.read_csv("Pandas_Series\\data.csv",index_col="Name")
# print(data)
# print(type(data))  #DataFrame
# print("------------------")
# print(data.squeeze())  # cannot be convert dataframe to Series because to convert it into series file should have only one or two columns
# print(type(data.squeeze())) 
# # print(movies.squeeze().values)  

# *************************************
# Series methods

# # head, tail
# print(type(movies))
# print(movie_series.head(10))
# print(movie_series.tail())
# print(movie_series.tail(10))

# # sample 
# print(movie_series.sample())
# print(movie_series.sample(8))

# # value_counts()  => frequency of data
# print(movie_series.value_counts())
# print(movie_series.value_counts().sample(10))
# print(type(movie_series.value_counts()))  #Series 
# print(kohli_run_series.sort_values(by="runs",ascending=False).head(1).values[0,1])
# print(kohli_run_series.sort_values(by="runs").head(10))

# inplace = true will sort the series object permanently
# kohli_run_series.sort_values(by="runs",inplace=True)

# print(movie_series.sort_index())
# print(movie_series.sort_index(ascending=False))
# print(movie_series.sort_index(inplace=True))
# print(kohli_run_series.sort_index())


# Series Maths Methods -------------------------

# print(movie_series.count())
# print((kohli_run_series.count()))
# print((subs_series.sum()))
# print(subs_series.product())


# # mean -> median -> mode -> std -> var------------
# print(subs_series.mean())
# print(kohli_run_series.mean())
# print(subs_series.median())
# print(kohli_run_series.median())
# print(movie_series.mode())

# print(subs_series.std())
# print(kohli_run_series.std())
# print(subs_series.var())
# print(kohli_run_series.var())
# print(subs_series.max())
# print(kohli_run_series.max())
# print(subs_series.min())
# print(kohli_run_series.min())
# print(movie_series.describe())
# print(kohli_run_series.describe())
# print(subs_series.describe())

# series indexing

x = pd.Series([12,14,13,35,46,57,58,79,9,91])


# 'this is possible'
# print(movie_series[1])
# print((movie_series['Why Cheat India']))

# print(movie_series)
# print(movie_series[0])
# print(movie_series[:2])
# print(movie_series[-5:])
# print(movie_series[::2])
# print(kohli_run_series[5:16])
# print(kohli_run_series[-5:])

# print(kohli_run_series[[1,3,4,5]])
# print(movie_series['Evening Shadows'])

# print(x)
x[0]=100
# print(x)
# print(marks_series)
# if the index not avaialble then it will add that index and data
marks_series['sst'] = 100
# print(marks_series)


# slicing in editing series
# print(kohli_run_series)
kohli_run_series[2:4] = [100,100]
# print(kohli_run_series)

# editing series using fancy indexing
# kohli_run_series[[1,3,4]] = [0,0,0]
# print(kohli_run_series)

# editing series using label
# movie_series['Evening Shadows'] = 'Alia Bhatt'
# print(movie_series)

# print(len(subs_series))
# print(type(subs_series))
# print(dir(subs_series))
# print(sorted(subs_series))
# print(max(subs_series))
# print(min(subs_series))


# type conversion
# print(list(subs_series))
# print(dict(marks))
# print(dict(marks_series))

# membership operator
# print('Evening Shadows' in movies)
# print('Evening Shadows' in movie_series)
# print('Akshay Kumar' in movie_series.values)


# looping
# for i in movie_series:
#   print(i)
# for i in movie_series.index:
#   print(i)


# operators
# Arithmatic (Broadcasting)
# print(100-marks_series)

# relational operators
# print(kohli_run_series >= 50)
# print(kohli_run_series[kohli_run_series >= 50])

# boolean indexing
# print(kohli_run_series >= 50)
# print(kohli_run_series[kohli_run_series>50])
# print(kohli_run_series[kohli_run_series>50].size)
# print(kohli_run_series[kohli_run_series==0].size)

# print(subs_series[subs_series>200].size)

# find actors who have done more than 20 movies
# num_movies = movie_series.value_counts()
# print(num_movies)
# print(num_movies[num_movies>20])
# import matplotlib.pyplot as plt
# kohli_run_series.plot(kind='pie')
# subs_series.plot(kind='pie')
# movie_series.value_counts().head(50).plot(kind='bar')
# plt.show()
# 


# important function 25 minutes

# astype

# print(kohli_run_series)
# import sys

# print(sys.getsizeof(kohli_run_series))

# kohli_run_series.astype('int16')
# print(sys.getsizeof(kohli_run_series.astype('int16')))

# between
# print(kohli_run_series[kohli_run_series.between(51,99)].size)

# clip
# print(subs_series.clip(100,200))

# drop_duplicates
# print(subs_series.duplicated().size)
# print(subs_series.drop_duplicates())
# print(subs_series.drop_duplicates(keep='last'))

# print(movie_series.size)
# print(movie_series.drop_duplicates().size)

temp = pd.Series([1,1,2,2,3,3,4,4])
# print(temp)
# print(temp.drop_duplicates(keep='first'))
# print(temp.drop_duplicates(keep='last'))
# print(temp.drop_duplicates().sum())
# print(kohli_run_series.drop_duplicates().sum())

# to find duplicated values and num of duplicated values
# print(temp.duplicated().sum())
# print(kohli_run_series.duplicated().sum())

temp = pd.Series([1,2,3,np.nan,5,6,np.nan,8,np.nan,10])
# print(temp.size)
# print(temp.count())
# print(temp.isnull().sum())
# print(temp.isna().sum())
# print(temp.dropna())
# print(temp.mean())
# print(temp.fillna(temp.mean()))

# print(kohli_run_series[(kohli_run_series == 49) | (kohli_run_series == 99)])
# print(kohli_run_series[kohli_run_series.isin([49,99])])

# apply ---------------
# print(movie_series.apply(lambda x : x.split()[0].upper()))
# avg = subs_series.mean()
# print(subs_series.apply(lambda x : 'Good Day' if x > subs_series.mean() else 'Bad Day'))

# copy -------------------------

# new_d = (kohli_run_series.head())
# print(new_d)
# new_d[1] = 100
# print(new_d)

newwd = kohli_run_series.head().copy()
kohli_run_series[1] = 100
print(newwd)