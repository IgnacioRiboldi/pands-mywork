# Plot X2
# This program choose a randoms numbers and ages and create a plot and a red line.
# By Ignacio Riboldi

import numpy as np 
import matplotlib.pyplot as plt 

minSalary = 20000
maxSalary = 80000
randomNumbers = 100


np.random.seed(1) 

salaries = np.random.randint(minSalary, maxSalary, randomNumbers) 

ages = np.random.randint(low=21, high = 65, size = randomNumbers)

plt.scatter(ages, salaries)

xpoints = np.array(range(1, 101)) 
ypoints = xpoints * xpoints 


plt.plot(xpoints, ypoints, color= 'r')
plt.show()  