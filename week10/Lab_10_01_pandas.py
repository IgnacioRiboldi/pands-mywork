# Lab 10.01 Pandas
# This program will take a data from a list and sort it in different columns
# By Ignacio Riboldi

import pandas as pd

dataList= [
    ['Ignacio',   'Handball',      28],
    ['Ignacio',   'Gym',           28],
    ['Cristina',  'Voleyball',     27],
    ['Cristina',  'Walking',       27],
    ['Julian',    'Football',      24],
    ['Julian',    'Running',       24],
    ['Sarawut',   'Gym',           30],
    ['Sarawut',   'Calisthenics',  30]
]

df = pd.DataFrame(dataList, columns= ['Name','Sport','Age'])

#It pints out the quantity of names mentioned in the parenthesis
print(df.head(10))

#Overall of the stats
print(df.describe())

# Prints this output in a dataframe
print(type(df.describe())) 

path = "./data/"
csvFilename = path + 'grades.csv'
df.to_csv(csvFilename)

# This program creates 3 columns even if we gave 2 because pandas, by default add an index of the DataFrame.
# The way to remove this is addind index = false to the last code " df.to_csv(csvFilename, index=False) " 

excelFilename = path +'grades.xlsx' 
df.to_excel(excelFilename, index=False, sheet_name='data') 

with pd.ExcelWriter(excelFilename, engine='openpyxl', mode='a') as writer:     
    df.describe().to_excel(writer, sheet_name="summary") 

mean = df['Age'].mean() 
print (mean) 