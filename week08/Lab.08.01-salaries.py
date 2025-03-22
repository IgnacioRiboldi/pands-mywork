# Salaries
# This program print a random list of 10 salaries between 20000 & 80000
# By Ignacio Riboldi

import numpy as np

minSalary = 20000
maxSalary = 80000
randomNumbers = 10

salaries = np.random.randint(minSalary,maxSalary,randomNumbers)

print (salaries)

