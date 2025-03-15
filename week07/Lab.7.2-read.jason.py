# Read Jason
# This program reads the text in a jason file
# By Ignacio Riboldi

import json
FILENAME = "testdict.json"

def reader():
    with open (FILENAME) as f:
        return json.load(f)

someDict = reader()
print (someDict)
