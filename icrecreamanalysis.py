#
# Analysis if the ice cream dataset.
#

import csv


file = open('ice_cream.csv', 'r')

type(file)

csvreader = csv.reader(file)

start = next(csvreader)
print(start)

rows = []

for row in csvreader:
    rows.append(row)
print(rows)
file.close()

#I cant get this to format properly.....uhg


