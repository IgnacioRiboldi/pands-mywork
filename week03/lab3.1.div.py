# Div
# This program calculates a division
# By Ignacio Riboldi

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int (x//y) # Gives int the division
remainder = x%y # Gives the remainder
print ("{} divided by {} is {} with remainder {}".format (x, y, answer, remainder))