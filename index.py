# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 21:09:47 2017

@author: re
"""

import matplotlib.pyplot as plt

import TGen

print("Genesis")

Genesis = TGen.TGenesis(5)

Genesis.Calcs()

Genesis.Type()

sol = list()

for n in range(500):
    print("------")
    Genesis.Generate()
    Genesis.Calcs()
    sol.append(Genesis.Type())

plt.figure(1)
plt.plot(sol)
plt.grid(True)
plt.xlabel("Time")
plt.ylabel("Solution")
#plt.axis(ymin = 0, ymax = 1050, xmax = 28)
plt.show()
