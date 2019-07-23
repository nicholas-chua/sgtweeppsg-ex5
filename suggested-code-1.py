import csv
import itertools
data = list()
reader = csv.reader(open("avocado.csv"))
next(reader)

for row in reader:
    data.append({"region": row[13], "price": float(row[2])})

data.sort(key=lambda x: x["region"])

for region, records in itertools.groupby(data, key=lambda x: x["region"]):
    print(region+"------------------------------------")
    prices=[it["price"] for it in records]
    print(sum(prices)/len(prices))
    
