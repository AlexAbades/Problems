# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 15:45:06 2021

@author: G531
"""

import pandas as pd 
import numpy as np 

x = np.ones(40)

x2 = np.ones(10)*2
x3 = np.ones(10)*3

x = np.concatenate((x,x2,x3))

d = pd.DataFrame(x)

d.boxplot()


V = [[0.45, -0.60, -0.64, 0.15],
[-0.40, -0.80, 0.43, -0.16],
[0.58, -0.01, 0.24, -0.78],
[0.55, -0.08, 0.59, 0.58]]

V = np.matrix(V)

x = np.matrix([-1,-1,-1,1])

# %%



x = [1, 1, 1, 1]

y =  [np.cos(np.pi/2*i) for i in x]


x = [[0.99962242169,0.99962242169,0.99962242169,0.99962242169], [0.027412, 0.0548036, 0.082154, 0.1094426]]
x = np.array(x).T

# %%

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np




data = {'Dibujo': 7, 'Nombres': 6}
names = list(data.keys())
values = list(data.values())

plt.figure(figsize=(9, 3))
plt.plot(names, values)

xmin = np.array([7, 7])
xmax = np.array([13,13])

plt.plot(names, xmin, linestyle='dashed', color='black')
plt.plot(names, xmax, linestyle='dashed', color='black')
ax = plt.gca()
ax.set_ylim([0, 15])
ax.set_xlim([0, 1])


for i,j in zip(names,values):
    ax.annotate(str(j),xy=(i,j))

plt.plot(names, values, 'ro')
plt.title('Puntuaciones Escalares')




