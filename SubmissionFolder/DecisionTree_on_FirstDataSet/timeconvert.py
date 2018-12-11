from datetime import datetime
date_format = "%m/%d/%Y"
a = datetime.strptime('12/31/2010', date_format)

import numpy
import csv
from collections import defaultdict

columns = defaultdict(list) # each value in each column is appended to a list

with open('C:/Users/Kay/Desktop/cleaned_test_values.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k

print(columns['date_recorded'])
print(columns['date_recorded'][0])

dates = []
for i in range(len(columns['date_recorded'])):
    b = datetime.strptime(columns['date_recorded'][i], date_format)
    delta = b - a
    dates.append(delta.days)

print(dates)


out = open('C:/Users/Kay/Desktop/zzzzzz.txt', "w")
for date in dates:
    out.write(str(date))
    out.write('\n')

out.close()
