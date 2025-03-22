# Salaries
# This program print a random list of 1 salary + 5% between 20000 & 80000 10 times.
# By Ignacio Riboldi

import numpy as np

minSalary = 20000
maxSalary = 80000
randomNumbers = 10

np.random.seed(1)

salaries = np.random.randint(minSalary,maxSalary,randomNumbers)

salariesMult = salaries * 1.05 # Addind a 5% of salary on each of them

print (salariesMult)

newSalaries = salariesMult.astype(int) # Converting from floating number to Int

print(newSalaries)
