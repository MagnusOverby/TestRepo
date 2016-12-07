# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 18:50:19 2014

@author: magnus
"""

import pandas as pd
import numpy as np
import time
from lxml import objectify
import sqlite3

 

path = '/home/magnus/Downloads/DataSop/SopData.xml'
#path = 'C:\Data\TheoreticalAvst\Vanillas\SopData.xml'
ePath1 = '/home/magnus/Downloads/DataSop/Data1'+time.strftime("%d%m%Y")+'.csv'
ePath2 = '/home/magnus/Downloads/DataSop/Data2_'+time.strftime("%d%m%Y")+'.csv'
#data = 'C:\Data\data.csv'
# read the Xml
print "Starting program makesure "+path+" is updated"
#data = 'C:\Data\data.csv'
parsed = objectify.parse(open(path))
root = parsed.getroot()

useCols = ['Reference','Last','Theoretical','Nominal','Price Diff (Abs)','Sector Pricing Status','Quotation type','Sector Emission']

data = []

for elt in root.Window.Line:
    el_data = {}
    for child in elt.getchildren():
        if child.attrib['name'] in useCols:
            el_data[child.attrib['name']] = child.pyval
    data.append(el_data)
    
df = pd.DataFrame(data)    
#df = pd.read_csv(data,sep ='\t+')
#data.Last = [float(str(x).replace(',','.')) for x in data['Last']]
# Rule 1) Understand what you do even when you copy code always read through it...
def mod_int(inStr):
    if inStr == '':
        return 0.0
    else:
        return float(inStr)

def mod_dataSet(df,sensi,lessThan):
  # THIS IS FUCKING FRUSTRATING !!!!!!!!!!!!!!!!!!!!!!!!
  # DiffCol = []
   T1 = df[df['Quotation type']!='In Price']
   T1['Diff'] = np.absolute(T1['Last']-T1['Theoretical'])
   T2 = df[df['Quotation type']=='In Price'] 
   T2['Diff'] = np.absolute(T1['Last']-T1['Theoretical'])/np.maximum(T1['Nominal'],1)
   T3 = pd.merge(T1,T2,how='outer')
   """
            DiffCol.append(np.absolute(T1['Last']-T1['Theoretical']))
        else:
            DiffCol.append(np.absolute(T1['Last']-T1['Theoretical'])/np.maximum(T1['Nominal'],1))
            """
   print T1['Diff']
   TT = T3.sort(columns='Diff',ascending=False)
   if lessThan:
        return TT[TT['Diff'] < 0.04]
   else:
        return TT[TT['Diff'] > 0.04]


#Convert data to a better format.

df['Last'] = [mod_int(str(k).replace(",",".")) for k in df['Last']]
df['Nominal'] = [mod_int(str(k).replace(",",".")) for k in df['Nominal']]
df['Theoretical'] = [mod_int(str(k).replace(",",".")) for k in df['Theoretical']]
df['Price Diff (Abs)'] = [mod_int(str(k).replace(",",".")) for k in df['Price Diff (Abs)']]
#Remove all expired products

df = df[df['Sector Emission']!='']
useCols = ['Reference','Last','Theoretical','Nominal','Price Diff (Abs)','Sector Pricing Status','Quotation type']
T1 = mod_dataSet(df[df['Sector Pricing Status']=='Theo Price OK'][useCols],0.04,False)
T2 = mod_dataSet(df[df['Sector Pricing Status']== 'Theo Price Differ'][useCols],0.04,True)

# Print to An Excel Sheet as last Resort.

T2.to_csv(ePath2,sep='\t')
T1.to_csv(ePath1,sep='\t')
print "Created "+ePath1
print "Created "+ePath2