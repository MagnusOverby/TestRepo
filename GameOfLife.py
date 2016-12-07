# -*- coding: utf-8 -*-
"""
Created on Sun Jun 29 10:57:37 2014
" Game Of Life
    store possition in dictionary as a coordinate (x,y)
    Check sorrounding if x-1,

@author: magnus
"""

"starting state" 
s1 = (1,2)
s2 = (1,1)
s3 = (0,1)
glider = set([s1,s2,s3])

print "STARTING PROGRAM"
        
def neigbours(x,y):
    return [(x+1,y),(x-1,y),(x,y-1),(x,y+1),(x-1,y-1),(x+1,y+1)]
        
def run_game(AllP):
 newstate = set()  
 for (x,y) in AllP:        
         for (xnew,ynew) in neigbours(x,y):
          count = sum([(x1,y1) in AllP for (x1,y1) in neigbours(xnew,ynew)])
          if count == 3 or ((xnew,ynew) in AllP and count == 2):    
               newstate.add((xnew,ynew))
 return newstate 

 
for i in range(1,100):               
  glider= run_game(glider)
  print glider
    
    
     