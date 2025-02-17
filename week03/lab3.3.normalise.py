# Normalise
# This program reads in string and strips.
# By Ignacio Riboldi

string = input ("Please enter string: ")
normalisedString = string.strip().lower()

lenghtOfString = len(string)
lenghtOfNormalised = len(normalisedString)

print(f'That String normalised is {normalisedString}')
print(f'We reduced the input string from {lenghtOfString} to {lenghtOfNormalised}')