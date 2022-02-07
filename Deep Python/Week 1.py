# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 09:41:40 2022

@author: G531
"""


#%% 
# Exercise 1 

# 1.1 Specify all peaks in A.


A  = [2, 1, 3, 7, 3, 11, 1, 5, 7, 10]


def findpeaks(A):
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


# 1.2 Specify which peaks the two linear time algorithms find




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