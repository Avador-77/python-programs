import re

PhoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = PhoneNumRegex.search('this is my phone number 412-658-8546.')
print("Phone Number Found: ", mo.group())
