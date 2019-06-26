# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 01:49:45 2019

@author: maxya
"""

from scipy.stats import *
import matplotlib.pyplot as plt
from matplotlib import rcParams

plt.rcParams["figure.figsize"] = [10,7.5]
rcParams['axes.titlepad'] = 20 
rcParams['axes.labelpad'] = 10 

# Zipf

fig, ax = plt.subplots()

ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)

a = 1.2

x= np.arange(1, 8)

ax.set_xlabel("x",fontsize=20)
ax.set_ylabel("p(x)",fontsize=20)

ax.set_title(" Zipf Probability" ,fontsize=20)

ax.plot(x, zipf.pmf(x, a), 'bo', ms=6, label='a=1.2')

a = 3

ax.plot(x, zipf.pmf(x, a), 'ro', ms=6, label='a=3')
ax.legend(loc='upper right',prop={'size': 18})

fig2, ax2 = plt.subplots()
ax2.tick_params(axis = 'both', which = 'major', labelsize = 15)
ax2.tick_params(axis = 'both', which = 'minor', labelsize = 15)
ax2.set_title(" Zipf Probability Log-Log scale" ,fontsize=20)
a = 1.2

ax2.loglog(x, zipf.pmf(x, a),'bo',ms=8,label='a=1.2')
ax2.loglog(x, zipf.pmf(x, a),'b--')

a= 3

ax2.loglog(x, zipf.pmf(x, a),'ro',ms=8,label='a=3')
ax2.loglog(x, zipf.pmf(x, a),'r--')
ax2.legend(loc='upper right',prop={'size': 18})