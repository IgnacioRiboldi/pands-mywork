# Guess 2
# This program prompts the user to guess a random number
# By Ignacio Riboldi

import random
number = random.randrange(0,100)
guess = int(input("Insert guess number: "))
while (guess != number):
    if(guess < number):
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Enter guess number: "))
print("Well done! The number was", number)