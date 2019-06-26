# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 02:05:25 2019

@author: maxya
"""
from scipy.stats import *
import matplotlib.pyplot as plt
from matplotlib import rcParams

plt.rcParams["figure.figsize"] = [10,7.5]
rcParams['axes.titlepad'] = 20 
rcParams['axes.labelpad'] = 10 

# Uniform

#Parameters

a = 2
b = 9

fig, ax = plt.subplots(1, 1)

ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)

x = np.linspace(-1, 10, 10000)

ax.set_xlabel("x",fontsize=20)
ax.set_ylabel("P(x)",fontsize=20)

ax.set_title(" uniform Probability Density" ,fontsize=20)

ax.plot(x, uniform.pdf(x,loc=a,scale=b-a),'b-', label=' a = 2, b = 9')

a = 4
b = 7

ax.plot(x, uniform.pdf(x,loc=a,scale=b-a),'r-', label=' a = 4, b = 7')
ax.legend(loc='upper left',prop={'size': 18})