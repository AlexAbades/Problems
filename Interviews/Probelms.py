# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:28:05 2021

@author: Alex Abades Grimes
"""


def getWrongAnswers(N: int, C: str) -> str:
  s=""
  l = ['A' if x=='B' else 'B' for x in C]
  s.join(l)
  print(s)
  return s

N = 4
C = 'ABBA'

# =============================================================================
# a = getWrongAnswers(N, C)
# print(a)
# =============================================================================

b= ['A' if x=='B' else 'B' for x in C]

s = ''.join(b)
print(s)

#%% 


# =============================================================================
# You're playing Battleship on a grid of cells with RR rows and CC columns.
# There are 00 or more battleships on the grid, each occupying a single 
# distinct cell. The cell in the iith row from the top and jjth column from 
# the left either contains a battleship (G_{i,j} = 1 G i,j=1) or doesn't 
# (G_{i,j} = 0 ​
# You're going to fire a single shot at a random cell in the grid. You'll 
# choose this cell uniformly at random from the R*CR∗C possible cells. You're 
# interested in the probability that the cell hit by your shot contains a 
# battleship.
# Your task is to implement the function getHitProbability(R, C, G) which 
# returns this probability. # Note: Your return value must have an absolute or 
# relative error of at most 10^{-6}10−6 to be considered correct.
# =============================================================================

G = [[1, 0],[2, 1]]

from typing import List


def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  if 1 >= R >= 100 or 1 >= C >= 100 or not all(i <= 1 and i >= 0 for i in sum(G,[])):
    raise ValueError('apsd')
  return sum(sum(G,[]))/(R*C)
