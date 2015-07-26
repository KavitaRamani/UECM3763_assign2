#Simulating Ornstein_Uhlenbeck(alpha,theta,sigma,R0,t,n,n_paths,dB,B,Rt,nu): 

import numpy as np
import scipy.stats as sc
from scipy.integrate import odeint
import pylab as p

#Defining the parameters to be used
#This is the starting asset value   
R0=3.0;
#This is the number of runs to simulate for
n=n_simulations=1000;
#This is the number of paths to simulate for
n_paths=5;
#This is the long run average interest rate 
theta=0.064;
#This is the speed of mean reversion
alpha=1;
#This is the volatility of the stochastic process
sigma=0.27;

#Creating the interest rate paths
t=p.linspace(0,1,n+1);
dB=p.randn(n_paths,n+1)/p.sqrt(n);dB[:,0]=0;
B=dB.cumsum(axis=1)

#Calulating returns
nu=p.exp(-alpha*t[1:]);
R=p.zeros_like(B); R[:,0]=R0

#solving the numerical integration
 def function(alpha,s):
     return (alpha*p.exp(alpha*s))
def int():
    return odeint(function,0,t)[0]
R[:,1:]=theta*(1-nu)+R0*nu+ sigma*B[:,1:]-sigma*nu*B[:,1:]*int()
p.plot(t,R.transpose())
p.xlabel('Time,t'); p.ylabel('Rt'); p.title('Simulation of Mean Reversal')

#Calculating mean
p.mean(R[:,1000])

#Calculating probability
mask=R[:,1000] > 2
Probability=sum(mask)/n_paths
print('P(R[:,1000]>2)=' + str(Probability))

