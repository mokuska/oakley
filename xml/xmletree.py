import xml.etree.ElementTree as ET

filename = 'example_files/plants.xml'

catalog = []


tree = ET.parse(filename)
plants = tree.getroot()

for idx, plant in enumerate(plants):
	print()
	print("---[%d.]-------------------"%idx)
	catalogitem = dict()
	
	for item in plant:
		print(item.tag+':', item.text)
		catalogitem[item.tag] = item.text
	
	catalog.append(catalogitem)


print()
print(catalog[3]['LIGHT'])