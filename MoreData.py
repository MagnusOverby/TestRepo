# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 20:41:21 2014

@author: magnus
"""

import pandas as pd
"""
path = '/home/magnus/Downloads/pydata-book-master/ch06/ex1.csv' 
frame = pd.read_csv(path)
frame.save('/home/magnus/Downloads/pydata-book-master/ch06/frame_pickle.csv')
pd.load('/home/magnus/Downloads/pydata-book-master/ch06/frame_pickle.csv')

path2 = '/home/magnus/Downloads/pydata-book-master/ch06/mydata.h5'
store = pd.HDFStore(path2)
store['obj1'] = frame
store['obj1_col'] = frame['a']
"""
import requests

url = 'http://search.twitter.com/search.json?q=python%20pandas'
resp = requests.get(url)

import json 
data = json.loads(resp.text)
data.keys()



#tag = '<a href="http://www.google.com">Google</a>'
#root = objectify.parse(StringIO(tag)).getroot()

