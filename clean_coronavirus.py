import sys
f = open(sys.argv[1])

for line in f.read().splitlines():
    items = line.split('|')
    record = [items[0]]
    start = 1
    if items[0] == items[1]: start = 2
    for i in range(start, len(items)):
        record += [items[i].replace(',','')]
    print(record[0] + '|' + str(record[1]) + '|' + str(record[3]))
        
