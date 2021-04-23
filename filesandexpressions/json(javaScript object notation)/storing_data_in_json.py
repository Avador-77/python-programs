import json

contacts = {"Rajat":"7006728845"}
filename = 'contactsWithjson.json'
with open(filename, 'w') as fo:
    json.dump(contacts, fo)
