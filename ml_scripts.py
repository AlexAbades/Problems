# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 11:38:32 2021

Create a function that gets input x and thetas to calculate the softmax
function. We have to specify 


@author: Alex Abades 
"""
from scipy.special import softmax
import numpy as np


def softmaxprob(x:list, *args:list):
    thetas = [*args]
    result = []
    for theta in thetas:
        result.append(sum([a*b for a,b in zip(x, theta)]))
    
    return softmax(result)
        
l1 = [1, 1]
l2 = [-1, -1]
l3 = [1, -1]

x = [0, 0.6]


a = softmaxprob(x, l1, l2,l3)

print(a)


a = [0,0.5]


x = [1, a[0], a[1], a[0]*a[1]]

w1 = np.array((2, 0, 0, 10))

w2 = np.array((-2, 0, 0, -10))
w3 = np.array((-2, 1, 1, 10))
w4 = np.array((2, 1, 1, -10))

softmaxprob(x,w1)

a = 1/(1 + np.exp(sum(-(x*w1))))
print(a)

a = 1/(1 + np.exp(sum(-(x*w2))))
print(a)

a = 1/(1 + np.exp(sum(-(x*w3))))
print(a)

a = 1/(1 + np.exp(sum(-(x*w4))))
print(a)



def norm1(x:tuple):
    x1, x2 = x
    return x1 + x2


def norm2(x:tuple):
    x1, x2 = x
    return np.sqrt(x1**2,x2**2)


def norm3(x:tuple):
    x1, x2 = x
    return max(x1,x2)
    

x = np.array([1, 2, 3, 4, 5, 6])
mu = 2
mu1 = 3
mu2 = 4


# %% 

# =============================================================================
# Calcultate if a given datapoint it's an oulier given the normal kernel density 
# function. The disctance is given by the norm 2, Euclidean distance. It could
# accept two dimesional datasets 
# =============================================================================



def kernelestimity(x:list, N:int, M:int, sigma:int):

    a = []
    for i in x:
        if type(i) == np.float64:
            I = np.identity(1)
        else:
           I = np.identity(x[0].shape) 
            
        x = (1/((2*np.pi)**(M/2)*np.sqrt(np.linalg.det(sigma**2*I)))*
                 np.exp(-1/2*i*(1/sigma**2*I)*i))
        a = np.append(a,x)
    return 1/N*sum(a)
        

x = np.array([5.11, 4.79, 4.90, 4.74, 2.96, 5.16, 2.88])
N,M = 7,7
sigma = 1

a = kernelestimity(x, N, M, sigma)
print(a)


# %%

x = [1, 0, 393.5, 68.1, 165.4, 271.8, 200.6, 210.9, 206.1, 166.3, 365.0]


# %%
# =============================================================================
# We have to programm an algorithm that actualizes the centroid of a KNN 
# clusters until reaches convergence with k number of neighbours
# =============================================================================


def k_cluster(x:list,*args):
    mus = [*args]
    
    
    for mu in mus:
        np.append([], (x-mu),axis=0)
        

    return 

a = k_cluster(x, mu, mu1, mu2)
    



# %% 
# =============================================================================
# JACARD AND SMC: Comparing clusters.
# Create the similarity matrix between 2 clusters 
# =============================================================================

# Array same length
x = [1,1,2,2,2,3,3,3,3,3]
y = [1,1,3,1,1,1,1,3,3,2]



def similarity(x:list, y:list):
    x = np.array(x)
    y = np.array(y)
    
    [clusters_z,N_z] = np.unique(x, return_counts=True)
    [clusters_q,N_q] = np.unique(y, return_counts=True)
    M = np.zeros((N_z.shape[0], N_q.shape[0]))
    
    # Create the matrix Nmk
    for cluster in clusters_z:
        for clu in clusters_q:
            M[cluster-1, clu-1] = sum((np.equal(y,clu)*np.equal(x,cluster)))
    
    [r,c] = M.shape
    S = 0
    for i in range(3):
        for j in range(3):
            S += (M[i][j]*(M[i][j]-1))/2
    
    N = x.shape[0]
    p = (N*(N-1))/2
    z = sum([(x*(x-1))/2 for x in N_z])
    q = sum([(x*(x-1))/2 for x in N_q])
    D = p-z-q+S
    print(N,S,D)
    
    J = S/(0.5*N*(N-1)-D)     
    R = (S+D)/(0.5*N*(N-1))        
    return J, R

# %% 

N=333
N_z = [122, 119, 92]
N_q = [146,119,68]
M = np.array([[114,0,32],
              [0,119,0],
              [8,0,60]])
S = 0
for i in range(3):
    for j in range(3):
        S += (M[i][j]*(M[i][j]-1))/2


p = (N*(N-1))/2
z = sum([(x*(x-1))/2 for x in N_z])
q = sum([(x*(x-1))/2 for x in N_q])
D = p-z-q+S
    
J = S/(0.5*N*(N-1)-D)  
R = (S+D)/(0.5*N*(N-1))  
    


print(R)

    
# %%

from scipy.stats import norm


mus = [18.347, 14.997, 18.421]
st = [1.2193, 0.986,1.1354]





    
    
    
    
    
    
    
    
    
    
    
    

    
