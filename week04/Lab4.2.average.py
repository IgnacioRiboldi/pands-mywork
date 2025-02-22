# Average
# This program keeps reading numbers until the user puts 0
# By Ignacio Riboldi

numbers = []
number = int(input("Please enter a number (0 to quit): "))

while number != 0 :
    numbers.append(number)

    number = int(input("Please enter a number (0 to quit): "))

for value in numbers:
    print(value)

average = float(sum(numbers)) / len(numbers)
print(f'The average is {average}')