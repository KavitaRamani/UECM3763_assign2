#Simulating Ornstein_Uhlenbeck 

import numpy as np
import pylab as p

#Defining the parameters to be used
#This is the starting asset value   
R0=3.0;
#This is the number of partitions
n=n_partitions=1000;
#This is the number of paths to simulate for
n_paths=5;
#This is the long run average interest rate 
theta=0.064;
#This is the speed of mean reversion
alpha=1;
#This is the volatility of the stochastic process
sigma=0.27;
#Time
t=1.0; dt=t/n;T=p.linspace(0,t,n+1)[:-1];

#Creating the interest rate paths
dB=p.randn(n_paths,n+1)*p.sqrt(dt);dB[:,0]=0;
B=dB.cumsum(axis=1)
def function(s):
    Z=p.exp(alpha*s)
    return Z
F=function(B);
FdB=F[:,0:-1]*dB[:,1:]
ito=FdB.sum(axis=1)

#Creating a variable to ease calculations
nu=p.exp(-alpha*t1[1:])

#Creating an array 
R=p.zeros_like(B);R[:,0]=R0;
R[:,1:]=theta*(1-nu)+R0*nu+sigma*nu*ito.reshape(5,1)

#Plotting the lines
p.plot(T,R[:,1:].transpose())
p.xlabel('Time,t'); p.ylabel('Rt'); p.title('Simulation of Mean Reversal')
p.ion()

#Calculating mean
p.mean(R[:,1000])

#Calculating probability
mask=R[:,1000] > 2
Probability=sum(mask)/n_paths
print('P(R[:,1000]>2)=' + str(Probability))

