# Random
# This program puts 10 random numbers into a queue. 
# By Ignacio Riboldi

import random
queue = []
quantityOfNumbers= 10
rangeTo = 100

for n in range(0,quantityOfNumbers):
    queue.append(random.randint(0,rangeTo))

print(f"Queue is {queue}")

while len(queue) != 0:

    currentNumber = queue.pop(0) 
    print (f"current Number is {currentNumber} and the queue is {queue} ")

print ("the queue is now empty")
