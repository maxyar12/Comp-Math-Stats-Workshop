# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 02:45:59 2019

@author: maxya
"""
from scipy.stats import *
import matplotlib.pyplot as plt
from matplotlib import rcParams

plt.rcParams["figure.figsize"] = [10,7.5]
rcParams['axes.titlepad'] = 20 
rcParams['axes.labelpad'] = 10 

# Exponential

fig, ax = plt.subplots()

ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)

lam = 1

x = np.linspace(0,10, 10000)

ax.set_xlabel("x",fontsize=20)
ax.set_ylabel("P(x)",fontsize=20)

ax.set_title(" Exponential Probability Density" ,fontsize=20)

ax.plot(x, expon.pdf(x,scale=1/lam),'r-', label='$\lambda = 1$')

lam = 2

ax.plot(x, expon.pdf(x,scale=1/lam),'b-', label='$\lambda = 2$')
ax.legend(loc='upper right',prop={'size': 18})

lam = 1

fig2,ax2 = plt.subplots()
ax2.tick_params(axis = 'both', which = 'major', labelsize = 15)
ax2.tick_params(axis = 'both', which = 'minor', labelsize = 15)
ax2.set_xlabel("x",fontsize=20)
ax2.set_ylabel("P(x)",fontsize=20)
ax2.set_title(" Exponential pdf semi-log vertical scale" ,fontsize=20)

ax2.semilogy(x, expon.pdf(x,scale=1/lam),'r-', label='$\lambda = 1$')
lam = 2

ax2.semilogy(x, expon.pdf(x,scale=1/lam),'b-', label='$\lambda = 2$')
ax2.legend(loc='upper right',prop={'size': 18})
