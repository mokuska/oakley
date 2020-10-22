
filename = 'example_files/accounts.txt'

specification = [
	('Entry', 7),
	('Per', 11),
	('PostDate', 23),
	('GLAccount', 36),
	('Description', 63),
	('Srce', 68),
	('Cflow', 72),
	('Reference', 82),
	('Post', 86),
	('Debit', 105),
	('Credit', 127),
	('Alloc', 133)
]

data_arr = []

with open(filename) as fp:
	
	for row_cnt, row in enumerate(fp):
		spec_cnt = 0
		data_dict = {}	
		data_item = ''

		for letter_cnt, letter in enumerate(row):
			data_item += letter

			if specification[spec_cnt][1] == letter_cnt:
				data_dict[specification[spec_cnt][0]] = data_item.strip()
				data_item = ''
				spec_cnt += 1

		data_arr.append(data_dict)

print(data_arr)