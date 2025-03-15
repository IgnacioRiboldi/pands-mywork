# Init
# This program creates a new file
# By Ignacio Riboldi

def readNumber(): 
    try: 
        with open(FILENAME) as f: 
            number = int(f.read()) 
            return number 
    except IOError:
        return 0
    
def writeNumber(number): 
    with open(FILENAME, "wt") as f: 
     f.write(str(number)) 

import os.path
FILENAME = "count.txt"
if not os.path.isfile(FILENAME):
    print ("File does not exist")
    writeNumber(0)