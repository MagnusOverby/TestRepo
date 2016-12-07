# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 20:41:35 2015

@author: magnus
"""
import numpy as np
from IPython.core.debugger import Pdb
from bisect import bisect_left
ipdb = Pdb()
path = "/home/magnus/Downloads/algo1_programming_prob_2sum.txt"
numbers = np.loadtxt(path)
numbers = [int(x) for x in numbers]
#remove dupplicates
numbers = list(set(numbers))
numbers.sort()

def TwoSumProblem(data,startIndex,stopIndex):
    counter = 0
    usedT = {}
    for t in range(startIndex,stopIndex):
            for x in data:
                y = t-x
                if x>y and t not in usedT:                
                    a = binary_search(data,y,0,len(numbers))
                    if a != -1 and y!=x and t not in usedT:
                        usedT[t] = 0
                        #print "pair x:" +str(x) +" and y: "+str(y)
                        counter +=1
                        if counter % 1000 == 0:
                            print counter
    return counter



def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end
    
print TwoSumProblem(numbers,-10000,10001)