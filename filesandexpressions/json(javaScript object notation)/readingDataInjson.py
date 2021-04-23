import json

contacts = {"Rajat":"7006728845"}
filename = 'filesandexpressions/json(javaScript object notation)/contactsWithjson.json'
with open(filename) as fo:
    data = json.load(fo)

print(data)