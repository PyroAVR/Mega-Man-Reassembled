import json

data = ''
with open("test.json", 'r') as file:
    data = file.read()
json_data = json.loads(data)
print(json_data)
print('\n')
#sssssoooooo faaaaancy
for i in json_data:
    print(i["1"])
    print(i["2"])
