import sys
import pandas as pd

csvPath = sys.argv[1]
operation = sys.argv[2]
column = sys.argv[3]
csv = pd.read_csv(csvPath)

def parseUnique():
    uniqueValues = csv[column].unique()
    print(uniqueValues)

def calcAvailablity():
    if operation != '':
        totalRows = csv[column].count()
        availableRows = csv[column].notnull().sum()
        availablity = availableRows / totalRows
        print('Is available for ' + str(availablity) + '% of samples')
    else:
        availability_map = [] 
        print('stuff')

if operation == 'lf':
    parseUnique()
elif operation == 'a':
    jalcAvailablity()
