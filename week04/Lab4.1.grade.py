# Grade 
# This program reads the student´s marks and print their grade.
# By Ignacio Riboldi

mark = float(input("Insert student mark between 0 and 100: "))
if (mark < 40):
    print("Fail")
elif (mark >=40 and mark <=49):
    print("Pass")
elif (mark >=50 and mark <=59):
    print("Merit 2")
elif (mark >=60 and mark <=69):
    print("Merit 1")
else: print("Distinction")