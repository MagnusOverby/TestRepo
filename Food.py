# -*- coding: utf-8 -*-
"""
Created on Sun Aug 17 13:41:24 2014

@author: magnus
"""

import json
import pandas as pd

path = '/home/magnus/Downloads/FoodDatabase/foods-2011-10-03.json'

db = json.load(open(path))
nutrients = pd.DataFrame(db[0]['nutrients'])
info_keys = ['description','group','id','manufacture']
info = pd.DataFrame(db,columns=info_keys)

nutrients = []
for rec in db:
    fnuts = pd.DataFrame(rec['nutrients'])
    fnuts['id'] = rec['id']
    nutrients.append(fnuts)

nutrients = pd.concat(nutrients,ignore_index=True)
nutrients.duplicated().sum()
nutrients = nutrients.drop_duplicates()
col_mapping= {'description':'food','group':'fgroup'}

nutrients = nutrients.rename(columns=col_mapping,copy=False)
ndata = pd.merge(nutrients,info,on='id', how='outer')
ndata.ix[30000]
result = ndata.groupby(['food','fgroup'])['value'].quantile(0.5)
result['Zinc, Zn'].order().plot(kind='barh')
