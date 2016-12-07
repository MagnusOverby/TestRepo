import pandas as pd
import numpy as np

s1 = [33,1,2,3,4]
index1= ['mon','tues','Wed','Thu','Fri']
s2 = pd.Series(data=s1,index=index1)
s3 = [range(1,4)]
dicter = {'Mon':22,'Tue':11}
s4= pd.Series(dicter)
