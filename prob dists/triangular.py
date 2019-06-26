# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 02:25:11 2019

@author: maxya
"""
from scipy.stats import *
import matplotlib.pyplot as plt
from matplotlib import rcParams

plt.rcParams["figure.figsize"] = [10,7.5]
rcParams['axes.titlepad'] = 20 
rcParams['axes.labelpad'] = 10 

# Triangular

fig, ax = plt.subplots(1, 1)

ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)

l = 20
m = 30
r = 40

x = np.linspace(0,50, 1000)


ax.set_xlabel("x",fontsize=20)
ax.set_ylabel("P(x)",fontsize=20)

ax.set_title(" Triangular Probability Density" ,fontsize=20)

ax.plot(x, triang.pdf(x,loc=l,scale=r-l,c=(m-l)/(r-l)),'b-', label=' $l$ = 20,m = 30,r=40')

l = 4
m = 5
r = 8

#ax.plot(x, triang.pdf(x,loc=l,scale=r-l,c=(m-l)/(r-l)),'r-', label=' $l$ = 4,m = 5,r=8')

ax.legend(loc='upper right',prop={'size': 18})