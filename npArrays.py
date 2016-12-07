import random
import matplotlib.pyplot as plt
import numpy as np
pos = 0
walk = [pos]
steps = 1000
for i in xrange(steps):
    step = 1 if random.randint(0,1) else -1
    pos += step
    walk.append(pos)



nsteps = 1000
nwalks = 1000
draws = np.random.randint(0,2,size=(nwalks,nsteps))
steps = np.where(draws>0,1,-1)
walk = steps.cumsum(1)
hits30 = (np.abs(walk)>=30).any(1)
hits30.sum()
crossing_times = (np.abs(walk[hits30])>=30).argmax(1)
crossing_times.mean()
steps = np.random.normal(loc=0,scale=0.25,size=(nwalks,nsteps))
