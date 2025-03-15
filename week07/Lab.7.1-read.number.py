# Read number
# This program read the number inside a txt archive
# By Ignacio Riboldi

FILENAME = "count.txt" 
def readNumber(): 
    with open(FILENAME) as f: 
        number = int(f.read()) 
    return number 


def writeNumber(number): 
    with open(FILENAME, "wt") as f: 
     f.write(str(number))  
     
num = readNumber()
num += 1
print (f'This program was run {num} times')
writeNumber(num)