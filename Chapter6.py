# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 21:58:37 2014

@author: magnus
"""
import pandas as pd
import csv
from pandas import DataFrame

path =  '/home/magnus/Downloads/pydata-book-master/ch06/ex2.csv'

names = ['a','b','c','d','message']
data = pd.read_csv(path,names=names,index_col='message')
path2 = '/home/magnus/Downloads/pydata-book-master/ch06/csv_mindex.csv'
df1 = pd.read_csv(path2,index_col=['key1','key2'])
path3 = '/home/magnus/Downloads/pydata-book-master/ch06/ex3.txt'
result = pd.read_table(path3,sep='\s+')
path4 = '/home/magnus/Downloads/pydata-book-master/ch06/ex4.csv'
df3 = pd.read_csv(path4,skiprows=[0,2,3])
path5 = '/home/magnus/Downloads/pydata-book-master/ch06/ex5.csv'
result = pd.read_csv(path5)
path6 = '/home/magnus/Downloads/pydata-book-master/ch06/ex6.csv'
chunker = pd.read_csv(path6,chunksize=1000)

data2 = pd.read_csv(path5)
data2.to_csv(path6)
path7 = '/home/magnus/Downloads/pydata-book-master/ch06/ex7.csv'
path8 = '/home/magnus/Downloads/pydata-book-master/ch06/tseries.csv'

f = open(path7)
reader = csv.reader(f)
for line in reader:
    print line

lines = list(csv.reader(open(path7)))
header,values = lines[0], lines[1:]
data_dict = {h: v for h,v in zip(header,zip(*values))}
class my_dialect(csv.Dialect):
    linetermiator = '\n'
    delimiter = ';'
    quotechar = '"'
reader = csv.reader(f,delimiter='|')


obj= """
{
    "name":"Wes",
    "place_lived": ["United States","Spain","Germany"],
    "pet":null,
    "siblings": [{"name":"Scott","age":25,"pet":"Zuko"},
                 {"name": "Katie", "age":33, "pet":"Cisco"}]

}
"""
import json
result = json.loads(obj)
result = json.loads(obj)

from lxml.html import parse
from urllib2 import urlopen

parsed = parse(urlopen('http://finance.yahoo.com/q/op?s=AAPL+Options'))
doc = parsed.getroot()
links = doc.findall('.//a')
lnk = links[28]
urls = [lnk.get('href') for lnk in doc.findall('.//a')]
tables = doc.findall('.//table')
calls = tables[9]
puts = tables[13]
rows = calls.findall('.//tr')
def _unpack(row,kind ='td'):
    elts = row.findall('.//%s' % kind)
    return [val.text_content() for val in elts]
    
from pandas.io.parsers import TextParser

def parse_option_data(table):
    rows = table.findall('.//tr')
    header = _unpack(rows[0],kind='th')
    data = [_unpack(r) for r in rows[1:]]
    return TextParser(data,names=header).get_chunk()

call_data = parse_option_data(calls)
put_data = parse_option_data(puts)

from lxml import objectify
path = 'Performance_MNR.xml'
parsed=objectify.parse(open(path))
root = parsed.getroot()

for elt in root.INDICATOR:
    el_data = {}
    for child in elt.getchildren():
        if child.tag in skip_fields:
            continue
        el_data[child.tag]=child.pyval
    data.append(el_data)
perf = pd.DataFrame(el_data)

