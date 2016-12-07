# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 23:57:22 2014
EDGAR test
@author: magnus
"""
import pandas as pd
import numpy as np
import gzip as zz
import urllib as ur

#read the full list
path = '/home/magnus/Downloads/cik.coleft.c'
index = ['Companies']
indexNew = ['Companies','EdgarNr','dropp']
df = pd.read_csv(path,names=index,sep='\t+')
dMod = df.Companies.str.split(':')

#ftp://ftp.sec.gov/edgar/full-index/{YYYY}/QTR{1-4}/{index-name}.[gz|zip]
patht = 'ftp://ftp.sec.gov/edgar/full-index/2013/QTR3/xbrl.gz'
req = ur.urlretrieve(patht)
z_f = ur.urlopen(req)
f = zz.GzipFile(fileobj=z_f, mode="r")
df = pd.read_fwf(patht,compression='gzip',sep='\t')
#dfNew = pd.read_table(z_f,compression='gzip',sep='\t')