# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 01:45:49 2019

@author: maxya
"""

from scipy.stats import *
import matplotlib.pyplot as plt
from matplotlib import rcParams

plt.rcParams["figure.figsize"] = [10,7.5]
rcParams['axes.titlepad'] = 20 
rcParams['axes.labelpad'] = 10 

#GEOMETRIC

fig, ax = plt.subplots(1, 1)

ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)

p = 0.5

x = np.arange(1, 10)
ax.set_xlabel("x",fontsize=20)
ax.set_ylabel("p(x)",fontsize=20)

ax.set_title("p(x) trials until 1st success" ,fontsize=20)

ax.plot(x, geom.pmf(x, p), 'bo', ms=6, label='p = 0.5')

p = 0.1

ax.plot(x, geom.pmf(x, p), 'ro', ms=6, label='p = 0.1')
ax.legend(loc='upper right',prop={'size': 18})