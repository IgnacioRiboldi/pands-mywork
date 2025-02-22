# Is Even
# This program will confirm with the user if the number provided is Even or Odd
# By Ignacio Riboldi

number = int(input("Please insert a number:"))

if (number % 2 == 0):
    print(f'{number} is Even number')
else: 
    print (f'{number} is Odd number')
