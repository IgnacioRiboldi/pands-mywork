# Histogram
# This program is going to return histogram of the salaries.
# By Ignacio Riboldi

import numpy as np 
import matplotlib.pyplot as plt 

minSalary = 20000
maxSalary = 80000
randomNumbers = 100


np.random.seed(1) 

salaries = np.random.randint(minSalary, maxSalary, randomNumbers) 

plt.hist(salaries) 
plt.show() 