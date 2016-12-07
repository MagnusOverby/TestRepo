# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 19:05:01 2014

@author: magnus
"""
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'key':['b','b','a','c','a','a','b'],'data1':range(7)})
df2 = pd.DataFrame({'key':['a','b','d'],
                    'data2':range(3)})
df3 = pd.DataFrame({'lkey':['b','b','a','c','a','a','b'],'data1':range(7)})
df4 = pd.DataFrame({'rkey':['a','b','d'],'data2':range(3)})
merg = pd.merge(df3,df4,left_on='lkey',right_on='rkey')
mergout = pd.merge(df1,df2,how='outer')
mrrg = pd.merge(df1,df2,on='key',how='left')
mrg = pd.merge(df1,df2,how='inner')
left1 = pd.DataFrame({'key':['a','b','a','a','b','c'],'value':range(6)})
right1 = pd.DataFrame({'group_val':[3.5,7]},index=['a','b'])
arr = np.arange(12).reshape(3,4)
con = np.concatenate([arr,arr],axis=1)
s1 = pd.Series([0,1],index=['a','b'])
s2 = pd.Series([2,3,4],index=['c','d','e'])
s3 = pd.Series([5,6],index=['f','g'])
s4 = pd.concat([s1*5,s3])
ss = pd.concat({'level1':df1,'level2':df2},axis=1)
sara = pd.concat([df1,df2],axis=1,keys=['level1','level2'],names=['upper','lower'])

a = pd.Series([np.nan,2.5,np.nan,3.5,4.5,np.nan],index = ['f','e','d','c','d','a'])
b = pd.Series(np.arange(len(a),dtype=np.float64),index=['f','e','d','c','b','a'])
