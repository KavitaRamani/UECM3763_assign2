<<<<<<< HEAD
#1. Plot only 5 realizations of the GBM with proper labels

import pylab as p
mu=0.1;sigma=0.26;s0=39;
n_path=5;n=n_partitions=1000

#Creating Brownian paths
t=p.linspace(0,3,n+1)
dB=p.randn(n_path,n+1)/p.sqrt(n);dB[:,0]=0;
B=dB.cumsum(axis=1);

#Calculating stock prices
nu=mu-sigma*sigma/2.0
S=p.zeros_like(B);S[:,0]=s0
S[:,1:]=s0*p.exp(nu*t[1:]+sigma*B[:,1:])
p.xlabel('Time,t'); p.ylabel('Stock price, St'); p.title('Simulation of Geometric Brownian Motion')
p.plot(t,S.transpose())
p.show()

#2. Calculate the expectation value of S(3) based on the simulation

import numpy as py
Mean=py.mean(S[:,1000]) #Average of all stock prices from 5 simulations at time 3
Mean #To produce output

#3. Calculate the variance of S(3)

Variance=py.var(S[:,1000]) #Variance of stock prices at time 3
Variance # To produce output

#Calculating probabilities
mask=S[:,1000] > 39
Probability=sum(mask)/n_path
print('P(S[:,1000]>39)=' + str(Probability))

#Calculating expectation
mask=S[:,1000] > 39              #number of values more than 39
Probability = S[:,1000] * mask          #retrieving values greater than 39
Expectation= sum(Probability)/sum(mask)
print('E(S[:,1000]|S[:,1000]>39)=' + str(Expectation))

=======
#1. Plot only 5 realizations of the GBM with proper labels

import pylab as p
mu=0.1;sigma=0.26;s0=39;
n_path=5;n=n_partitions=1000

#Creating Brownian paths
t=p.linspace(0,3,n+1)
dB=p.randn(n_path,n+1)/p.sqrt(n);dB[:,0]=0;
B=dB.cumsum(axis=1);

#Calculating stock prices
nu=mu-sigma*sigma/2.0
S=p.zeros_like(B);S[:,0]=s0
S[:,1:]=s0*p.exp(nu*t[1:]+sigma*B[:,1:])
p.xlabel('Time,t'); p.ylabel('Stock price, St'); p.title('Simulation of Geometric Brownian Motion')
p.plot(t,S.transpose())
p.show()

#2. Calculate the expectation value of S(3) based on the simulation

import numpy as py
Mean=py.mean(S[:,1000]) #Average of all stock prices from 5 simulations at time 3
Mean #To produce output

#3. Calculate the variance of S(3)

Variance=py.var(S[:,1000]) #Variance of stock prices at time 3
Variance # To produce output

#Calculating probabilities
mask=S[:,1000] > 39
Probability=sum(mask)/n_path
print('P(S[:,1000]>39)=' + str(Probability))

#Calculating expectation
mask=S[:,1000] > 39              #number of values more than 39
Probability = S[:,1000] * mask          #retrieving values greater than 39
Expectation= sum(Probability)/sum(mask)
print('E(S[:,1000]|S[:,1000]>39)=' + str(Expectation))

>>>>>>> 94bd3c81592a8a66f34455493ea89a3db0384869
