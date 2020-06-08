import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='Parse sample data .csv to find unique values and availablity for a field')
parser.add_argument('path', type=str, help='Path to sample data .csv')
parser.add_argument('field', type=str, help='Field from csv to analyze')
parser.add_argument('-a', action='store_true', help='availablitiy percent of a field')
parser.add_argument('-lf', action='store_true', help='list unique values')

args = parser.parse_args()
csv = pd.read_csv(args.path)

if args.lf:
    uniqueValues = csv[args.field].unique()
    print(uniqueValues)
elif args.a:
        availableRows = csv[args.field].notnull().sum()
        availablity = availableRows / len(csv) * 100
        print('Is available for ' + str(availablity) + '% of samples')
else:
    for column in csv:
        totalRows = len(csv)
        availableRows = csv[column].notnull().sum()
        availability = availableRows / len(csv) * 100
        print(column + ": " + str(availability) + "%")

