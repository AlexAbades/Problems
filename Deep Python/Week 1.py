# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 09:41:40 2022

@author: G531
"""


#%% 
# Exercise 1 

# 1.1 Specify all peaks in A.


A  = [2, 1, 3, 7, 3, 11, 1, 5, 7, 10]

A = [1, 1, 1, 1, 1, 1, 1, 1]

def findallpeaks(A):
    peaks = []
    n = len(A)
    print(n)
    
    if A[0] >= A[1]:
        peaks.append(A[0])
    for i in range(len(A)-1):
        if A[i] >= A[i-1] and A[i] > A[i+1]:
            peaks.append(A[i])
    if A[n-1] >= A[n-2]:
        peaks.append(A[n-1])
    return peaks


n = findallpeaks(A)




#%% Exercise 2 

A  = [2, 1, 3, 7, 3, 11, 1, 5, 7, 10]

def findvalleys(A):
    valleys = []
    n = len(A)
    print(n)
    
    if A[0] <= A[1]:
        valleys.append(A[0])
    for i in range(len(A)-1):
        if A[i] <= A[i-1] and A[i] <= A[i+1]:
            valleys.append(A[i])
    if A[n-1] <= A[n-2]:
        valleys.append(A[n-1])
    return valleys

C = findvalleys(A)




#%% Exercise 4: Properties of peaks 
# Let be A an array of length n>= 1.

# Probe that at least there's a pick.

def maxpeaks(A:list):
    # The worst case would be if n = 2, but as the definition of peak explains
    # that the number must be grater or equal than its neighbour, then at minimum 
    # we'll 2 peaks as both will be peaks.
    n = len(A)
    return n 



def maxpeaks_new(A:list):
    
    n = len(A)
    if n % 2 != 0:
        m = (n+1)/2
        # As n it id odd to obtain the max number of peaks, the first should
        # be situated on the first position A[0]
        return m 
    else:
        m = n/2
        # As n it id even it doesn't matter where it's the first peak. 
        return m 

#%% Exercise 5: Test algorithms 


import time 
import numpy as np 
import pandas as pd 

def findpeak(A):
    
    n = len(A)
    
    if A[0] >= A[1]:
        return A[0]
    for i in range(n-1):
        if A[i] >= A[i-1] and A[i] > A[i+1]:
            return A[i]
    if A[n-1] >= A[n-2]:
        return A[n-1]
    

A = np.array([1, 5])


n = findpeak(A)

n = 10000 
m = 500

times = []
time2average = []

for i in range(n):
    print(i)
    A = np.random.randint(0,10000,i+2)
    for j in range(m):
        start_time = time.time()*1000
        number = findpeak(A)
        end_time = time.time()*1000 
        diff = end_time - start_time
        time2average.append(diff)
    times.append(np.mean(time2average))

    
#%% 

import matplotlib.pyplot as plt 

B = []
for i in range(n):
    B.append(i+2)
    
fig, ax = plt.subplots(1)
ax.plot(B, times)
