import csv

filename = 'example_files/hurricanes.csv'

fields = []
rows = []


with open(filename, 'r') as csvinput:
	
	inputreader = csv.reader(csvinput)
	fields = next(inputreader)

	for row in inputreader:
		rows.append(row)

	print("Total numbers of rows: %d"%(inputreader.line_num))


for row in rows:
	print(row)


for row in rows:

	if len(row) == 0:
		continue

	for idx, item in enumerate(row):
		
		if idx == 0:
			caption = item
			sumValue = 0
			minValue = 10000
			maxValue = 0
		
		else:
			item = int(item)
			sumValue = sumValue + item

			if item < minValue:
				minValue = item

			if item > maxValue:
				maxValue = item

	print("In %s month:"%(caption))
	print("Sum = %d"%(sumValue))
	print("Min = %d"%(minValue))
	print("Max = %d"%(maxValue))
	print()

