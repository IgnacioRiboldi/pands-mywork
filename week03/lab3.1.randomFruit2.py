# Random Fruit
# This program prints out a random fruit.
# By Ignacio Riboldi

import random

fruits = ('Apple','Banana','Melon','Pinneaple','Watermelon','Orange','Pear')

index = random.randint(0,len(fruits)-1)

fruits = fruits[index]
print ("A Random Fruit: {}".format(fruits))
