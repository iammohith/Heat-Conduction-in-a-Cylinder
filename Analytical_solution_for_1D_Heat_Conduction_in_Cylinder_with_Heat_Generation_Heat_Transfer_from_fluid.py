# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:39:00 2020

@author: Mohith Sai
"""

# Heat conduction in a long cylinder with heat generation, immersed in a fluid.
# The cylinder is subject to internal heat generation Qg, and it is in contact
# with a surrounding fluid at temperature Tinf. The cylinder's outer wall is at temperature Tw.
# The temperature distribution in the cylinder is given by the equation:
# T(r) = (Qg * R^2) / (4 * K) * (1 - (r/R)^2) + Tinf + (Qg * R) / (2 * hc)
# Where:
# T(r) = Temperature at radial distance r from the center of the cylinder
# Tw = Wall temperature (°C)
# Tinf = Surrounding fluid temperature (°C)
# R = Radius of the cylinder (m)
# Qg = Heat generation per unit volume (W/m^3)
# K = Thermal conductivity of the cylinder material (W/m*K)
# hc = Heat transfer coefficient, calculated based on Tw and Tinf

import numpy as np
import matplotlib.pyplot as plt

# Input parameters
Tw = 100         # Wall temperature (°C)
Tinf = 30        # Surrounding fluid temperature (°C)
R = 1            # Radius of the cylinder (m)
Qg = 100         # Heat generation per unit volume (W/m^3)
K = 10           # Thermal conductivity of the material (W/m*K)

# Calculate temperature difference between the wall and surrounding fluid
theta = abs(Tw - Tinf)

# Calculate heat transfer coefficient based on Qg, R, and the temperature difference (theta)
hc = (Qg * R) / (2 * theta)

# Generate linearly spaced points for radial positions from the center (r=0) to the wall (r=R)
n = 10            # Number of points
r = np.linspace(0, R, n)  # Radial positions

# Preallocate temperature array
T = np.ones(n)

# Calculate temperature at each radial position
for i in range(n):
    T[i] = ((Qg * R**2) / (4 * K)) * (1 - (r[i] / R)**2) + Tinf + ((Qg * R) / (2 * hc))

# Plot the temperature distribution
plt.figure(1)
plt.plot(r, T, color='red', linestyle='dashed', marker='.', markerfacecolor='blue')
plt.xlabel('Distance from center (m)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Distribution in a Cylinder Immersed in Fluid')
plt.grid(True)
plt.show()

# Output the calculated temperatures
print("The calculated temperatures at different radial positions are:", T)
