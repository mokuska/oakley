import xml.etree.ElementTree as ET

plants = ET.parse('example_files/plants.xml').getroot()
catalog = []
for idx, plant in enumerate(plants):
	catalogitem = dict()
	for item in plant:
		catalogitem[item.tag] = item.text
	catalog.append(catalogitem)
