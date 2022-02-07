# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 21:00:14 2022

@author: G531
"""
import time
# Exercise 4 
A = 5
L = 6
O = 7

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

