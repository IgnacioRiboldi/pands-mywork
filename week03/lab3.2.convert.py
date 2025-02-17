# Convert
# This program take two numbers a convert them as money and absolute value
# By Ignacio Riboldi

a = float(input('Insert an ammount here: '))
absolut = abs(a)
answer = absolut * 100
roundAnswer = round(answer)
print('Your value in cents is: {}'.format(roundAnswer))