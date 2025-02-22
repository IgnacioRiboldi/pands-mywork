# Top Three
# This program generate 10 random numbers and print the top 3
# By Ignacio RIboldi

import random
howMany = 10
topNumbers = 3
rangeFrom = 0
rangeTo = 100

numbers = []

for i in range (0,howMany):
    numbers.append(random.randint(rangeFrom,rangeTo))
print(f'{howMany} random numbers\t {numbers}')

topOnes = numbers.copy()

topOnes.sort(reverse = True)
print(f'The top {topNumbers} are \t\t {topOnes[0:topNumbers]}')