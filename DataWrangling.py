# -*- coding: utf-8 -*-
"""
Created on Sun Jun 29 18:51:15 2014

@author: magnus
"""

import pandas as pd

pathUser = "/home/magnus/Downloads/ml-1m/users.dat"
pathRate = "/home/magnus/Downloads/ml-1m/ratings.dat"
pathMovie= "/home/magnus/Downloads/ml-1m/movies.dat"

unames = ['user_id','gender','age','occupation','zip']
users = pd.read_table(pathUser,sep ='::',header=None,names=unames)
rnames = ['user_id','movie_id','rating','timestamp']
rating = pd.read_table(pathRate,sep='::',header=None,names=rnames)
"""mnames = ['movie_id'.'title','genres']
"""
mnames=['movie_id','title','genres']
movies = pd.read_table(pathMovie,sep='::',header=None,names=mnames)
print users[:5]
print rating[:5]
print movies[:5]
data = pd.merge(pd.merge(rating,users),movies)
mean_ratings=data.pivot_table('rating',rows='title',cols='gender',aggfunc='mean')
rating_by_title = data.groupby('title').size()
ratings_by_title=data.groupby('title').size()
active_titles = rating_by_title.index[ratings_by_title >= 250]
mean_ratings=mean_ratings.ix[active_titles]
rating_by_title=data.groupby('title').size()
ratings_by_title[:10]
active_titles = rating_by_title.index[ratings_by_title>=250]
top_female_ratings = mean_ratings.sort_index(by='F',ascending=False)
mean_ratings['diff']=mean_ratings['M']-mean_ratings['F']
sorted_by_diff = mean_ratings.sort_index(by='diff')
sorted_by_diff[:15]
rating_std_by_title=data.groupby('title')['rating'].std()
rating_std_by_title.order(ascending=False)[:10]


