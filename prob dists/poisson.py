# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 01:48:07 2019

@author: maxya
"""

from scipy.stats import *
import matplotlib.pyplot as plt
from matplotlib import rcParams

plt.rcParams["figure.figsize"] = [10,7.5]
rcParams['axes.titlepad'] = 20 
rcParams['axes.labelpad'] = 10 

# Poisson

fig, ax = plt.subplots(1, 1)

ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)

mu = 3

x = np.arange(0, 10)
ax.set_xlabel("x",fontsize=20)
ax.set_ylabel("p(x)",fontsize=20)

ax.set_title("p(x) events in finite interval" ,fontsize=20)

ax.plot(x, poisson.pmf(x, mu), 'bo', ms=6, label=r'$\alpha = 1$')

#mu = 4

#ax.plot(x, poisson.pmf(x, mu), 'ro', ms=6, label=r'$\alpha = 4$')
#mu = 10

#ax.plot(x, poisson.pmf(x, mu), 'go', ms=6, label=r'$\alpha = 10$')
#ax.legend(loc='upper right',prop={'size': 18})