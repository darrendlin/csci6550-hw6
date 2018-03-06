import csv;
import datetime;

data = [['key', 'value', 'date']];

with open('raw_data_darren.csv') as csvdata:
  reader = csv.reader(csvdata, delimiter=',');
  for i,row in enumerate(reader):
    if (i == 0):
      continue
    for index, val in enumerate(row[1:]):
      data.append([row[0], val, (datetime.date(2018, 1, 1) + datetime.timedelta(days=index)).strftime('%m/%d/%y')]);


with open('darren.csv', 'w+') as csvdata:
  writer = csv.writer(csvdata, delimiter=',');
  for item in enumerate(data):
    writer.writerow([str(item[1][0]), str(item[1][1]), item[1][2]]);