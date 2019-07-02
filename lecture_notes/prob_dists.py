# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 01:35:59 2019

@author: maxya
"""
from scipy.stats import *
import math
from scipy.stats import randint
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

plt.rcParams["figure.figsize"] = [10,7.5]
rcParams['axes.titlepad'] = 20 
rcParams['axes.labelpad'] = 10 


def dunif(N):
    fig, ax = plt.subplots()

    ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)

    x = np.arange(1, N+1)
    rv = randint(1,N+1)
    ax.set_xlabel("X",fontsize=20)
    ax.set_ylabel("p(X)",fontsize=20)

    ax.set_title(" ",fontsize=20)

    ax.plot(x, rv.pmf(x), 'ko', ms=8, label='N='+str(N))
    ax.legend(loc='upper right',prop={'size': 18})
    
def binomial(n,p):

    fig, ax = plt.subplots()

    ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)

    x = np.arange(0, n+1)
    ax.set_xlabel("X",fontsize=20)
    ax.set_ylabel("p(x)",fontsize=20)

    ax.set_title("p(X) successes in n  trials, each with individual prob, p",fontsize=20)

    ax.plot(x, binom.pmf(x, n, p), 'ko', ms=8, label='n = '+str(n)+", p = " + str(p))
    ax.legend(loc='upper right',prop={'size': 18},bbox_to_anchor=(1.25, 1.0))
def geometric(p):
    fig, ax = plt.subplots(1, 1)

    ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)

    x = np.arange(1, 10/p)
    ax.set_xlabel("X",fontsize=20)
    ax.set_ylabel("p(X)",fontsize=20)

    ax.set_title("p(X) trials until 1st success" ,fontsize=20)

    ax.plot(x, geom.pmf(x, p), 'bo', ms=6, label='p = ' +str(p))

    ax.legend(loc='upper right',prop={'size': 18})

def poiss(a):

    fig, ax = plt.subplots()

    ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)

    x = np.arange(0, int(4*a))

    ax.set_xlabel("X",fontsize=20)
    ax.set_ylabel("p(X)",fontsize=20)

    ax.set_title("p(X) events in finite interval" ,fontsize=20)

    ax.plot(x, poisson.pmf(x, a), 'ko', ms=8, label=r'$\alpha = $' +str(a))

    ax.legend(loc='upper right',prop={'size': 18})
    
def hyperg(N,K,n):
    rv = hypergeom(N, K, n)
    x = np.arange(0,n+1)
    fig, ax = plt.subplots()
    ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)
    ax.set_title("p(X) vs X hypergeometric" ,fontsize=20)
    ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)
    ax.set_xlabel('X',fontsize=20)
    ax.set_ylabel('hypergeom PMF',fontsize=20)
    ax.plot(x, rv.pmf(x), 'ko',label='N,K,n = ' + str(N)+', '+str(K)+', '+str(n))
    ax.legend(loc='best',prop={'size': 18},bbox_to_anchor=(1.15, 1.0))

def zpf(s):
    fig, ax = plt.subplots()

    ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)

    x= np.arange(1, 8)

    ax.set_xlabel("X",fontsize=20)
    ax.set_ylabel("p(X)",fontsize=20)

    ax.set_title(" Zipf Probability" ,fontsize=20)

    ax.plot(x, zipf.pmf(x, s), 'bo', ms=6, label='s = ' + str(s))    
    ax.legend(loc='upper right',prop={'size': 18})
    
def loglog_zpf(s):

    x= np.arange(1, 8)
    fig, ax2 = plt.subplots()
    ax2.tick_params(axis = 'both', which = 'major', labelsize = 15)
    ax2.tick_params(axis = 'both', which = 'minor', labelsize = 15)
    ax2.set_title(" Zipf Probability Log-Log scale" ,fontsize=20)
    ax2.loglog(x, zipf.pmf(x, s),'ko',ms=8,label='s = ' + str(s))

    ax2.legend(loc='upper right',prop={'size': 18})
  
def cunif(a,b):

    fig, ax = plt.subplots()

    ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)

    x = np.linspace(a - 0.05*(b-a), b+0.05*(b-a), 10000)

    ax.set_xlabel("X",fontsize=20)
    ax.set_ylabel("P(X)",fontsize=20)

    ax.set_title(" uniform Probability Density" ,fontsize=20)

    ax.plot(x, uniform.pdf(x,loc=a,scale=b-a),'k-', label='a = '+str(a)+', b = '+str(b))
    ax.legend(loc='lower center',prop={'size': 18})  
    
def triangle(l,m,r):
    fig, ax = plt.subplots()

    ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)

    x = np.linspace(l-0.04*(r-l),r+0.04*(r-l),3000)

    ax.set_xlabel("x",fontsize=20)
    ax.set_ylabel("P(x)",fontsize=20)

    ax.set_title(" " ,fontsize=20)

    ax.plot(x, triang.pdf(x,loc=l,scale=r-l,c=(m-l)/(r-l)),'k-', label=' $l$ = '+str(l)+', m = '+str(m)+', r = '+str(r))

    ax.legend(loc='upper right',prop={'size': 18},bbox_to_anchor=(1.0, 1.25)) 

def normal(mu,sigma):
    fig, ax = plt.subplots()

    ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)

    x = np.linspace(mu-5*sigma,mu +5*sigma, 10000)

    ax.set_xlabel("X",fontsize=20)
    ax.set_ylabel("P(X)",fontsize=20)

    ax.set_title(" Normal Probability Density" ,fontsize=20)

    ax.plot(x, norm.pdf(x,loc=mu,scale=sigma),'r-', label='$\mu$ = ' +str(mu)+', $\sigma$ = '+str(sigma))

    ax.legend(loc='upper right',prop={'size': 18},bbox_to_anchor=(1.2, 1.0))

def lognormal(mu,sigma):
    fig, ax = plt.subplots()

    ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)

    x = np.linspace(0,mu + 10*sigma, 10000)

    ax.set_xlabel("X",fontsize=20)
    ax.set_ylabel("P(X)",fontsize=20)

    ax.set_title(" Lognormal Probability Density" ,fontsize=20)

    ax.plot(x, lognorm.pdf(x,s=sigma,scale=math.exp(mu)),'r-', label='$\mu$ = '+str(mu)+', $\sigma$ = '+str(sigma))

    ax.legend(loc='upper right',prop={'size': 18})   
 
def expo(lam):
    fig, ax = plt.subplots()

    ax.tick_params(axis = 'both', which = 'major', labelsize = 15)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 15)
    
    x = np.linspace(0,10/lam, 10000)

    ax.set_xlabel("X",fontsize=20)
    ax.set_ylabel("P(X)",fontsize=20)

    ax.set_title(" Exponential Probability Density" ,fontsize=20)

    ax.plot(x, expon.pdf(x,scale=1/lam),'r-', label='$\lambda = $' +str(lam))

    ax.legend(loc='upper right',prop={'size': 18})
    
def semilog_expo(lam):

    x = np.linspace(0,10/lam, 10000)
    
    fig2,ax2 = plt.subplots()
    ax2.tick_params(axis = 'both', which = 'major', labelsize = 15)
    ax2.tick_params(axis = 'both', which = 'minor', labelsize = 15)
    ax2.set_xlabel("X",fontsize=20)
    ax2.set_ylabel("P(X)",fontsize=20)
    ax2.set_title(" Exponential pdf semi-log vertical scale" ,fontsize=20)

    ax2.semilogy(x, expon.pdf(x,scale=1/lam),'r-', label='$\lambda = $' +str(lam))

    ax2.legend(loc='upper right',prop={'size': 18})

    plt.savefig("exp_lam_" + str(lam) + ".png")