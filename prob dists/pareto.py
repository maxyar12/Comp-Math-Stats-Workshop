# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 17:37:27 2019

@author: maxya
"""

from scipy.stats import *
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
import math

plt.rcParams["figure.figsize"] = [10,7.5]
rcParams['axes.titlepad'] = 20 
rcParams['axes.labelpad'] = 10 

# Gamma

#parameters k is called a, set scale = theta

fig, ax = plt.subplots()

ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)

x = np.linspace(1,4, 10000)

ax.set_xlabel("x",fontsize=20)
ax.set_ylabel("P(x)",fontsize=20)

ax.set_title(" Pareto Probability Density" ,fontsize=20)

a = 1.5 # shape parameters

ax.plot(x, pareto.pdf(x,a),'r-', label=r'a = 1.5, $x_m$ = 1')

a = 6

ax.plot(x, pareto.pdf(x,a),'b-', label=r'a = 6, $x_m$ = 1')

ax.legend(loc='upper right',prop={'size': 18})

fig2, ax2 = plt.subplots()
ax2.tick_params(axis = 'both', which = 'major', labelsize = 15)
ax2.tick_params(axis = 'both', which = 'minor', labelsize = 15)
ax2.set_title(" Pareto Probability density Log-Log scale" ,fontsize=20)

a = 1.5

ax2.loglog(x, pareto.pdf(x, a),'r-',ms=8,label='a=1.5, $x_m$ = 1')

a= 6

ax2.loglog(x, pareto.pdf(x, a),'b-',ms=8,label='a=6, $x_m$ = 1')

ax2.legend(loc='upper right',prop={'size': 18})