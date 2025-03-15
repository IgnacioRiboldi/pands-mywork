# Jason Test
# This program is a test json program to store a dict to a file
# By Ignacio Riboldi

import json 
FILENAME="testdict.json" 
sample= dict(name='fred', age=31, grades=[1,34,55]) 
def writeDict(obj): 
    with open(FILENAME, 'wt') as f: 
        json.dump(obj,f)
        
writeDict(sample)