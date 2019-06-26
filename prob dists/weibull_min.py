# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 17:29:01 2019

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

x = np.linspace(0,4, 10000)

ax.set_xlabel("x",fontsize=20)
ax.set_ylabel("P(x)",fontsize=20)

ax.set_title(" Weibull Probability Density" ,fontsize=20)

c = 1.19 # shape parameters

ax.plot(x, weibull_min.pdf(x,c),'r-', label=r'$k = 1.19, \lambda = 1 $')

c = 3

ax.plot(x, weibull_min.pdf(x,c),'b-', label=r'$k = 3, \lambda = 1 $')

ax.legend(loc='upper right',prop={'size': 18})