# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 22:45:36 2014

@author: magnus
"""

path = "/home/magnus/Downloads/USName/yob1880.txt"
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
names1880 = pd.read_csv(path, names = ['name','sex','births'])
names1880.groupby('sex').births.sum()
years = range(1880,2011)
columns = ['name','sex','births']
pieces = []
for year in years:
    path = '/home/magnus/Downloads/USName/yob%d.txt' % year
    frame = pd.read_csv(path,names=columns)
    frame['year'] = year
    pieces.append(frame)
    names = pd.concat(pieces,ignore_index=True)

total_births = names.pivot_table('births',rows='year',cols='sex',aggfunc=sum)
total_births.tail()

def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births/births.sum()
    return group
names = names.groupby(['year','sex']).apply(add_prop)

np.allclose(names.groupby(['year','sex']).prop.sum(),1)

def get_top1000(group):
    return group.sort_index(by='births',ascending=False)[:1000]
grouped = names.groupby(['year','sex'])
top1000 = grouped.apply(get_top1000)
pieces = []
for year,group in names.groupby(['year','sex']):
    pieces.append(group.sort_index(by='births',ascending=False)[:1000])
top1000 = pd.concat(pieces,ignore_index=True)
boys = top1000[top1000.sex =='M']
girls = top1000[top1000.sex =='F']

total_births = top1000.pivot_table('births',rows='year',cols='name',aggfunc=sum)
subset = total_births[['John','Harry','Mary','Marilyn']]

#subset.plot(subplots=True,figsize=(12,10),grid=False,title="Number of births per year")

table = top1000.pivot_table('prop',rows='year',cols='sex',aggfunc = sum)
#table.plot(title='Sum of table1000.prop by year and sex',yticks=np.linspace(0,1.1,13),xticks=range(1880,2020,10))
df = boys[boys.year == 2010]
prop_cumsum = df.sort_index(by='prop',ascending=False).prop.cumsum()
prop_cumsum[:10]
df=boys[boys.year == 1900]
in1900 = df.sort_index(by='prop',ascending=False).prop.cumsum()

#Below does not work due to some raggadydo in the library
"""
def get_quantile_count(group,q=0.5):
    group = group.sort_index(by='prop',ascending=False)
    return group.prop.cumsum().searchsorted(q)+1
diversity = top1000.groupby(['year','sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')
diversity.plot(title="Number of popular names in top 50%")
# extract last letters from name column
"""
get_last_letter = lambda x:x[-1]

last_letters=names.name.map(get_last_letter)
last_letters.name = 'last_letter'
table = names.pivot_table('births',rows=last_letters,cols=['sex','year'], aggfunc=sum)
subtable = table.reindex(columns=[1910,1960,2010],level = 'year')
subtable.head()
subtable.sum()

letter_prop = subtable/subtable.sum().astype(float)
dny_ts = letter_prop.ix[['d','n','y'],'M'].T
dny_ts.head()
dny_ts.plot()
all_names=top1000.name.unique()
mask = np.array(['lesl' in x.lower() for x in all_names])
lesley_like = all_names[mask]

filtered = top1000[top1000.name.isin(lesley_like)]
filtered.groupby('name').births.sum()
table = filtered.pivot_table('births',rows='year',cols='sex',aggfunc='sum')
table = table.div(table.sum(1),axis=0)
table.tail()
table.plot(style={'M':'k-','F':'k--'})


