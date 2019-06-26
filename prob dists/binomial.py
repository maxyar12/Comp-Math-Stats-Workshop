# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 01:35:59 2019

@author: maxya
"""
from scipy.stats import *
import matplotlib.pyplot as plt
from matplotlib import rcParams

plt.rcParams["figure.figsize"] = [10,7.5]
rcParams['axes.titlepad'] = 20 
rcParams['axes.labelpad'] = 10 

#Binomial

fig, ax = plt.subplots(1, 1)

ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)

# SET PARAMETERS OF THE DISTRIBUTION

n, p = 100, 0.5

x = np.arange(0, n)
ax.set_xlabel("x",fontsize=20)
ax.set_ylabel("p(x)",fontsize=20)

ax.set_title("p(x) successes in n  trials",fontsize=20)

ax.plot(x, binom.pmf(x, n, p), 'bo', ms=3, label='n=100, p=0.5')

# ANOTHER SET OF PAREMETERS FOR THE DISTRIBUTION

p = 0.1

#PLOT FOR COMPARISON

ax.plot(x, binom.pmf(x, n, p), 'ro', ms=3, label='n=100, p=0.1')
ax.legend(loc='upper right',prop={'size': 18})