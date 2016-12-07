# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 21:21:13 2014

@author: magnus
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

impCorr = 0.88
path = '/home/magnus/Downloads/BNPtest.sqy'
head = ['Date','Stock','Price']
data = pd.read_csv(path,sep='\t+',names=head,parse_dates=['Date']).dropna()
data.Price = [float(x.replace(',','.')) for x in data.Price]
df = data.pivot(columns='Stock',values='Price',index='Date').dropna()
df = df['2011-08-08':'2014-08-08']
df = df.resample('W',how='mean',kind='period')
rets = df / df.shift(1)-1
corrlst = []
#Bank of America
for i in range(0,len(rets)-50):
   matr = rets[i:len(rets)].corr().as_matrix()
   corrlst.append(matr[0,1])
tmp = pd.DataFrame(corrlst)


        


#BNP 
corrBNP = rets.corr().as_matrix()[0,1]
L1 = (impCorr/corrBNP-1)/(1/corrBNP-1)




