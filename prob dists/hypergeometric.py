# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 01:48:41 2019

@author: maxya
"""

from scipy.stats import *
import matplotlib.pyplot as plt
from matplotlib import rcParams

plt.rcParams["figure.figsize"] = [10,7.5]
rcParams['axes.titlepad'] = 20 
rcParams['axes.labelpad'] = 10 

#HYPERGEOMETRIC

[M, n, N] = [20, 7, 12]
rv = hypergeom(M, n, N)
x = np.arange(0, n+1)
pmf_dogs = rv.pmf(x)
fig, ax = plt.subplots(1, 1)
ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)
ax.set_title("p(x) vs x dogs drawn from N trials, n total dogs, M total animals" ,fontsize=20)
ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)
ax.set_xlabel('# of dogs in our group of chosen animals',fontsize=20)
ax.set_ylabel('hypergeom PMF',fontsize=20)
ax.plot(x, pmf_dogs, 'bo',label='(M,n,N) = (20,7,12)')
ax.legend(loc='upper right',prop={'size': 18})
