# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:42:00 2019

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

x = np.linspace(0,20, 10000)

ax.set_xlabel("x",fontsize=20)
ax.set_ylabel("P(x)",fontsize=20)

ax.set_title(" Gamma Probability Density" ,fontsize=20)

a = 1 # shape parameters

ax.plot(x, gamma.pdf(x,a,scale = 5),'r-', label=r'$k = 1, \theta = 2 $')

a = 2

ax.plot(x, gamma.pdf(x,a,scale = 2),'b-', label=r'$k = 2, \theta = 2 $')

a = 7.5

ax.plot(x, gamma.pdf(x,a,scale = 1),'g-', label=r'$k = 7.5, \theta = 1 $')
ax.legend(loc='upper right',prop={'size': 18})