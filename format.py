# The goal here is to expand the raw_data_xxxx formats into a csv with only 3 columns. This is so that the d3 code can read it properly.

import csv;
import datetime;

data = [['key', 'value', 'date']];

# change the input file name here
with open('raw_data_darren.csv') as csvdata:
  reader = csv.reader(csvdata, delimiter=',');
  for i,row in enumerate(reader):
    if (i == 0): # skip the header row
      continue
    for index, val in enumerate(row[1:]):
      data.append([row[0], val, (datetime.date(2018, 1, 1) + datetime.timedelta(days=index)).strftime('%m/%d/%y')]); # please note that the year format HAS to be 2 digits long.

# change the output file name here
with open('darren.csv', 'w+') as csvdata:
  writer = csv.writer(csvdata, delimiter=',');
  for item in enumerate(data):
    writer.writerow([str(item[1][0]), str(item[1][1]), item[1][2]]); # output in 3 columns (key, value, date)