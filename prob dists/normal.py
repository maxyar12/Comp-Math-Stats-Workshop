# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 12:57:44 2019

@author: maxya
"""

from scipy.stats import *
import matplotlib.pyplot as plt
from matplotlib import rcParams

plt.rcParams["figure.figsize"] = [10,7.5]
rcParams['axes.titlepad'] = 20 
rcParams['axes.labelpad'] = 10 

# Normal

fig, ax = plt.subplots()

ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)

mu, sigma = 0, 0.1 # mean and standard deviation

x = np.linspace(-2,10, 10000)

ax.set_xlabel("x",fontsize=20)
ax.set_ylabel("P(x)",fontsize=20)

ax.set_title(" Normal Probability Density" ,fontsize=20)

ax.plot(x, norm.pdf(x,loc=mu,scale=sigma),'r-', label='$\mu = 0, \sigma = 0.1 $')

mu, sigma = 4, 1

ax.plot(x, norm.pdf(x,loc=mu,scale=sigma),'b-', label='$\mu = 4, \sigma = 1 $')
ax.legend(loc='upper right',prop={'size': 18})