import json

with open('example_files/users.json') as jsoninput:
	data = json.load(jsoninput)

# pretty printing json data
print(json.dumps(data, indent = 4, sort_keys=True))

for user in data:
	print(user['lastName'], user['firstName']+':', user['emailAddress'])

