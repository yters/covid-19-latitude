import sys

f = open(sys.argv[1])
coronavirus_records = {}
for line in f.read().splitlines():
    items = line.split('|')
    record = [items[0].lower().replace(' ','')]
    start = 1
    if items[0] == items[1]: start = 2
    for i in range(start, len(items)):
        record += [items[i].replace(',','')]
    coronavirus_records[record[0]] = (record[1], record[3])
f.close()

f = open(sys.argv[2])
coordinates_records = {}
for line in f.read().splitlines():
    items = line.split('|')
    name = items[3].lower().replace(' ','')
    latitude = float(items[1])
    coordinates_records[name] = latitude
f.close()

for k in coronavirus_records.keys():
    if k in coordinates_records:
        cases, deaths = coronavirus_records[k]
        latitude = coordinates_records[k]
        print(k, latitude, cases, deaths)
