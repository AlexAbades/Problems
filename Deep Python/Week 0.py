# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 08:34:30 2022

@author: G531

Week 0 Exercises
"""



#%%
# Loop 1
n = 100
x = 0 
for i in range(n):
    for j in range(n):
        x += 1


# Loop 2
n = 100
x = 0 
for i in range(n):
    x += 1 
for j in range(n):
    x += 1
    

# Loop 3    
n = 4
x = 0
for i in range(n):
    if i == n-1:
        for j in range(n):
            x += 1
            

# Loop 4 
x = 0
n = 10
for i in range(n):
    for j in range(i, n):
        x += 1
        
#%% 

# Recursivity 

A = [1, 2, 3]
n = 3
def recu(A,n):
    if n == 0 :
        return 0 
    else:
        return recu(A,n-1) + A[n-1]


def iteri(A):
    x = 0 
    for i in A:
        x += i
    return x
#%%

# line = input() # Read line of input using input()
# input_number = int(input()) # Read line with one input integer
multiple_numbers = list(map(int, input().split())) # Multiple integers on a line
print(sum(multiple_numbers)) # Print result using print

#%% Exercise 3
multiple_numbers = list(map(int, input().split()))
print(sum(multiple_numbers))

#%% 
import time 

A = 4
L = 5
O = 6


count = 0

s = []
if A < L and A < O:
    s.append('Anna')
if L < A:
    s.append('Laura')
if O < A or O < L:
    s.append('Oscar')
# if not s:
#     s.append('None')
# return s.sort()
s.sort()
for name in s:
    print(name)

for i in range(1000):
    start = time.time()*1000
    s = []
    if A < L and A < O:
        s.append('Anna')
    if L < A:
        s.append('Laura')
    if O < A or O < L:
        s.append('Oscar')
    # if not s:
    #     s.append('None')
    # return s.sort()
    s.sort()
    for name in s:
        print(name)
    end = time.time()*1000
    count += end-start


means = count/1000
print(means)


def jealous(A,L,O):
    s = []
    if A < L and A < O:
        s.append('Anna')
    if L < A:
        s.append('Laura')
    if O < A or O < L:
        s.append('Oscar')
    # if not s:
    #     s.append('None')
    # return s.sort()
    s.sort()
    for name in s:
        print(name)

jealous(A, L, O)





