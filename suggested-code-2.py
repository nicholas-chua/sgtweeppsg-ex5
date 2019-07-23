import csv
data = dict()
reader = csv.reader(open("avocado.csv"))
next(reader)

for row in reader:
    region = row[13]
    if region not in data.keys():
        data[region] = list()
    data[region].append(float(row[2]))

for region, prices in data.items():
    print(region+"------------------------------------")
    print(sum(prices)/len(prices))
