# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 13:26:11 2019

@author: maxya
"""

from scipy.stats import *
import matplotlib.pyplot as plt
from matplotlib import rcParams
import math

plt.rcParams["figure.figsize"] = [10,7.5]
rcParams['axes.titlepad'] = 20 
rcParams['axes.labelpad'] = 10 

# Lognormal

fig, ax = plt.subplots()

ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)

mu, sigma = 0, 0.25 # mean and standard deviation

x = np.linspace(0,3, 10000)

ax.set_xlabel("x",fontsize=20)
ax.set_ylabel("P(x)",fontsize=20)

ax.set_title(" Lognormal Probability Density" ,fontsize=20)

ax.plot(x, lognorm.pdf(x,s=sigma,scale=math.exp(mu)),'r-', label='$\mu = 0, \sigma = 0.25 $')

mu, sigma = 0, 1

ax.plot(x, lognorm.pdf(x,s=sigma,scale=math.exp(mu)),'b-', label='$\mu = 0, \sigma = 1 $')
ax.legend(loc='upper right',prop={'size': 18})