# Guess 1
# This program prompts the user to guess a number
# By Ignacio Riboldi

number = 30
guess = int(input("Insert guess number: "))
while (guess != number):
    print("Wrong")
    guess = int(input("Enter guess number: "))
print("Well done! The number was", number)