import csv

portfolio = []
def a_cost(filename):
	with open(filename, 'r') as f:
		rows = csv.reader(f)
		headers = next(rows)
		rowno = 1

		for row in rows:
			rowno += 1
			
			#Cleaning up data
			row[0] = int(row[0])
			row[2] = float(row[2])
			row[3] = float(row[3])
			
			#Dictionary in Lists
			record = {
				'rownum': row[0],
				'date': row[1],
				'avgprice': row[2],
				'totalvol': row[3],
				'4046': row[4],
				'4225': row[5],
				'4770': row[6],
				'totalbag': row[7],
				'smallbag': row[8],
				'largebag': row[9],
				'xlargebag': row[10],
				'type': row[11],
				'year': row[12],
				'region': row[13]
			}
			portfolio.append(record)
	return portfolio
data = a_cost('avocado.csv')
#print (data)

# def region_name(row):
# 	return row['region']

import itertools
# # for region, items in itertools.groupby(data, key=region_name):
# # 	print ('REGION', region)
# # 	for it in items:
# # 		print('		', it)

#Sort data by region
data.sort(key = lambda row: row['region'])

for region, records in itertools.groupby(data, key= lambda row: row['region']):
	print(region+"-------")
	prices = [ it["avgprice"] for it in records]
	print(sum(prices)/len(prices))

# #Group data by region
# by_name = {region: list(items)
# for region, items in itertools.groupby(data, key= lambda row: row['region'])}

# #Pull out names of every single region
# unique_names = {row['region'] for row in data}
# print(unique_names)

# #Perform calculations (for one region only)
# sum_average = 0.0
# rowno = 0

# for row in by_name['Albany']:
# 	rowno += 1
# 	sum_average += row['avgprice']

# average = sum_average/rowno
# total = average*rowno
# print(total, rowno, average)

# #Use a loop to get values using individual regions


