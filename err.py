# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 01:44:37 2017

@author: V5
"""

import numpy as np
from matplotlib import pyplot as plt
import math
plt.interactive('on')

x= np.linspace(-2.5e8, 2.5e8, 100)
s_y = .7e8

Bx = 9e-10
y = [Bx*math.erf(x[i]/s_y) for i in range(100)]
y = -np.asarray(y)

plt.figure()
plt.plot(x,y,'r')
plt.ylim([-1.05e-9,1.05e-9])
plt.ylabel('Bx (G)')
plt.xlabel('Y (m)')
plt.savefig('images/Bx_ana.png',dpi=300)