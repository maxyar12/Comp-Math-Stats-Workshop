# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:36:17 2019

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

# Beta

fig, ax = plt.subplots()

ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)

x = np.linspace(0,1, 10000)

ax.set_xlabel("x",fontsize=20)
ax.set_ylabel("P(x)",fontsize=20)

ax.set_title(" Beta Probability Density" ,fontsize=20)

a, b = 0.5, 0.5 # shape parameters

ax.plot(x, beta.pdf(x,a,b),'r-', label=r'$\alpha = 3, \beta = 3 $')

a, b = 2, 5

ax.plot(x, beta.pdf(x,a,b),'b-', label=r'$\alpha = 2, \beta = 5 $')

a, b = 5, 2

ax.plot(x, beta.pdf(x,a,b),'g-', label=r'$\alpha = 5, \beta = 2 $')
a, b = 1, 2

ax.plot(x, beta.pdf(x,a,b),'y-', label=r'$\alpha = 1, \beta = 2 $')

ax.legend(loc='upper right',prop={'size': 18})

fig2, ax2 = plt.subplots()
ax2.tick_params(axis = 'both', which = 'major', labelsize = 15)
ax2.tick_params(axis = 'both', which = 'minor', labelsize = 15)

x = np.linspace(0,10, 10000)

a, b = 5, 2

ax2.plot(x, beta.pdf(x,a,b),'g-', label=r'$\alpha = 2.5, \beta = 3 $')
a, b = 2.5, 3

ax2.plot(x, beta.pdf(x,a,b,loc=4,scale=3),'y-', label=r'$\alpha = 2.5, \beta = 3 $')

ax2.legend(loc='upper right',prop={'size': 18})