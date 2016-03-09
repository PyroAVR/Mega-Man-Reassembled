import json

leveldata = dict()

while True:
    key = input("key:")
    if key == ";": break
    data = input("data:")
    if data == ";": break
    leveldata[key] = data
json_string = json.dumps(leveldata)
with open("test.json", 'w') as file:
    file.write(json_string)
