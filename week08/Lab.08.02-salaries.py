# Salaries
# This program print a random list of 1 salary between 20000 & 80000 10 times.
# By Ignacio Riboldi

import numpy as np

minSalary = 20000
maxSalary = 80000
randomNumbers = 10

np.random.seed(1)

salaries = np.random.randint(minSalary,maxSalary,randomNumbers)

print (salaries)
