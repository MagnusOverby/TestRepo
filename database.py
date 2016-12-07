# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 21:05:52 2014

Magnus Mock Db

@author: magnus
"""

import sqlite3
import pandas as pd

query = """
CREATE TABLE test 
(a VARCHAR(20),b VARCHAR(20),
c REAL, d INTEGER
);"""
con = sqlite3.connect(':memory:')
con.execute(query)
con.commit()
#Insert some data

data = [('Atlanta','Georgia',1.25,6),
        ('Tallahasse','Florida',2.6,3),
        ('Sacramento','California',1.7,5)]
stmt = "INSERT INTO test VALUES(?,?,?,?)"
con.executemany(stmt,data)




import pandas.io.sql as sql



cursor = con.execute('select * from test')

rows = cursor.fetchall()


df = sql.read_frame('select * from test',con)

import pymongo

con = pymongo.Connection('localhost',port=27017)
tweets = con.db.tweets
"""
import requests,json
url = 'http://search.
"""

