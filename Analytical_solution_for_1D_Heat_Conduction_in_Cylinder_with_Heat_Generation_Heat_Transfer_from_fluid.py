# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:39:00 2020

@author: Mohith Sai
"""
"""Let us consider a long cylinder with radius R with heat generation Qg
and wall temperature Tw and the cylinder is immersed in a fluid with temperature Tinf
with heat transfer coefficient hc
the temperature distribution over the cylinder is given by
T(r) = Qg*R**2/4*k*(1 - (r/R)**2) + Tinf + Qg*R/2*hc
where hc = Qg*R/2*theta theta = Tw - Tinf or Tinf - Tw """

import numpy as np
import matplotlib.pyplot as plt

Tw = 100 #temperature of wall units must be degC
Tinf = 30 #temperature of surrounding fluid units must be degC
if Tw > Tinf:
    theta = Tw - Tinf
elif Tinf > Tw:
    theta = Tinf - Tw
R = 1 #radius of the cyinder units must be in meters
Qg = 100 #heat generation the units must be W/m**3
K = 10 #thermal conductivity of the material
hc = (Qg*R)/(2*theta) #heat transfer coefficient 
n = 10 #the number of points
r = np.linspace(0,R,n) #linearlyspaced points
T = np.ones(n)
for i in range(0,n):
    T[i] = (((Qg*R**2)/(4*K))*(1 - ((r[i]/R)**2))) + Tinf + ((Qg*R)/(2*hc))
plt.figure(1)
plt.plot(r,T,color='red', linestyle='dashed', marker='.', markerfacecolor='blue')
plt.xlabel('Distacnce (m)')
plt.ylabel('Temperature (C)')
plt.title('Axisymmetrical Temperature Graph')
print("The temperatures are:",T)