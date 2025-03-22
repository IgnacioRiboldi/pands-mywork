# Ages
# This program makes an scatter plot of ages that has the same number random salaries.
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
plt.show()  