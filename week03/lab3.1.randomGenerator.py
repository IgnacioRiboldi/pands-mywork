# Random Generator
# This Program prints out a random number between 1 and 10
# By Ignacio Riboldi

import random
a = int(input("Number input range from: "))
b = int(input("Number input range to: "))
number = random.randint(a,b)
print("Your random number on range from {} and {} is: {}".format(a,b,number))