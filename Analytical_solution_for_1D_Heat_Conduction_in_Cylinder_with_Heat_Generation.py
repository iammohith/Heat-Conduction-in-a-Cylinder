# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 22:42:45 2020

@author: Mohith Sai
"""

# Heat conduction in a long cylinder with uniform heat generation and specified wall temperature.
# The temperature distribution in the cylinder is given by the equation:
# T(r) = (Qg * R^2) / (4 * K) * (1 - (r/R)^2) + Tw
# where:
# T(r) = temperature at radial distance r
# Qg = heat generation per unit volume (W/m^3)
# R = radius of the cylinder (m)
# K = thermal conductivity of the material (W/m*K)
# Tw = wall temperature (°C)

import numpy as np
import matplotlib.pyplot as plt

# Input parameters
Tw = 100          # Wall temperature in degrees Celsius
R = 1             # Radius of the cylinder in meters
Qg = 100          # Heat generation per unit volume in W/m^3
K = 10            # Thermal conductivity of the material in W/m*K
n = 10            # Number of points for temperature calculation

# Generate linearly spaced points from the center (r=0) to the wall (r=R)
r = np.linspace(0, R, n)

# Preallocate temperature array
T = np.ones(n)

# Calculate the temperature at each radial position r
for i in range(n):
    T[i] = ((Qg * R**2) / (4 * K)) * (1 - (r[i]/R)**2) + Tw

# Plot the temperature distribution
plt.figure(1)
plt.plot(r, T, color='red', linestyle='dashed', marker='.', markerfacecolor='blue')
plt.xlabel('Distance from center (m)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Distribution in a Cylinder')
plt.grid(True)
plt.show()

# Print the calculated temperatures
print("The calculated temperatures at different radial positions are:", T)
