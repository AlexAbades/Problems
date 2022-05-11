# -*- coding: utf-8 -*-
"""
Cafeteria problem

Social distancing requires that K seats next to the occupied seat are empty. 
The cafeteria consists of a big table. 

N: number of seats in the cafeteria.
K: Number of empty seats a dinner must have next.
M: Number of dinners that are currently in the cafeteria.
S: positions on the table of the actual dinners. 


"""

import numpy as np 
import pandas as pd


k = 2 
N = 10
a = np.zeros(N)
b = np.array([1, 6])
bmin = b-k
bmin[bmin<0]=0
bmax = b+k+1
bmax[bmax>N]=N

for i in zip(bmin,bmax):
    a[i[0]:i[1]]=1


# %% 

def cal_seats(N,K,M,S:list):
    """
    

    Parameters
    ----------
    N : TYPE
        DESCRIPTION.
    k : TYPE
        DESCRIPTION.
    m : TYPE
        DESCRIPTION.
    s : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    n = np.zeros(N)
    n = n[S] = 1
    