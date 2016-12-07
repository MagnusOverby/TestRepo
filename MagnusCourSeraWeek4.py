# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 15:45:10 2015

@author: magnus
"""

import random
import numpy as np
from IPython.core.debugger import Pdb
ipdb = Pdb()
#Concentrate on building a data structure that can efficently store the graph
#path = "/home/magnus/Downloads/week4test.txt"
path = "/home/magnus/Downloads/Test4.txt"
#path = "/home/magnus/Downloads/MagnusTest.txt"
vertexes = np.loadtxt(path)

#globals 
counter = 0
finishingTimes = {}
#--------------------




nodes = list(set(list(vertexes[:,:1].T[0])))
def BuildGraph(vertexes,nodes,reverse):
    iUse = 1
    if reverse:
        iUse = 0
    p = {}
    for i in nodes:
        tmp = []
        for j in range(0,len(vertexes)):
            if i == vertexes[j,1-iUse]:
                tmp.append(vertexes[j,iUse])
        p[i] = tmp
    return p

G = BuildGraph(vertexes,nodes,False)
Grev = BuildGraph(vertexes,nodes,True)

#Build Depth first search when should i mark a rout as explored ? 

#list can be used as stacks in python.
def DFS(G,Explored,n):
    Stack = []
    BackTrack = []
    Stack.append(n)
    while len(Stack) > 0:
        u = int(Stack.pop())
        if not Explored[u]:
            BackTrack.append(u)
            Explored[u] = True
            for edge in G[u]:
                Stack.append(edge)
    while len(BackTrack) > 0:
        global counter
        counter +=1
        node = BackTrack.pop()
        global finishingTimes
        finishingTimes[node] = counter

#this funciton will perform a search and return the size of all the SCC
def SecondStage(G,Explored,n):
    Stack = []
    BackTrack = []
    Stack.append(n)
#print G
    while len(Stack)>0:
        u = int(Stack.pop())
        if not Explored[u]:
            #ipdb.set_trace()
            Explored[u] = True
            BackTrack.append(u)
            for edge in G[u]:
                Stack.append(edge)
    
    Mycounter = 0
    while len(BackTrack)>0:
        BackTrack.pop()
        Mycounter +=1
    return Mycounter 

counter = 0
finishingTimes = {}
Explored = {key: False for key in nodes}
for nod in nodes:
    n = int(nod)
    if not Explored[n]:
        DFS(Grev,Explored,n)
#DFS counter check 
#Need to relable the entire thing and search for the nodes with highest weight
#--------------------------------------------------------------------
GG = {}
for i in G.keys():
    tmp = [finishingTimes[j] for j in G[i]]  
    GG[finishingTimes[i]]=tmp
#--------------------------------------------------------------------
SCCLIST = []
Explored = {key: False for key in nodes}
for nod in range(len(nodes),0,-1):
    #print uNod
    #ipdb.set_trace()
    uNod = nod
    if not Explored[uNod]:
        tmpCount = SecondStage(GG,Explored,uNod)
        SCCLIST.append(tmpCount)
SCCLIST.sort(reverse=True)
print SCCLIST