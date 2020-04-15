# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 22:42:45 2020

@author: Mohith Sai
"""
"""Let us consider a long cylinder with radius R with heat generation Qg
and wall temperature Tw the temperature distribution over the cylinder is given by
T(r) = Qg*R**2/4*k*(1 - (r/R)**2) + Tw"""

import numpy as np
import matplotlib.pyplot as plt

Tw = 100 #temperature of wall units must be degC
R = 1 #radius of the cyinder units must be in meters
Qg = 100 #heat generation the units must be W/m**3
K = 10 #thermal conductivity of the material
n = 10 #the number of points
r = np.linspace(0,R,n) #linearlyspaced points
T = np.ones(n)
for i in range(0,n):
    T[i] = (((Qg*R**2)/(4*K))*(1 - ((r[i]/R)**2))) + Tw
plt.figure(1)
plt.plot(r,T,color='red', linestyle='dashed', marker='.', markerfacecolor='blue')
plt.xlabel('Distacnce (m)')
plt.ylabel('Temperature (C)')
plt.title('Axisymettrical Temperature Graph')
print("The temperatures are:",T)
            

