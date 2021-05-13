# www.regexpal.com to visualize how regex works

import re

PhoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = PhoneNumRegex.search('this is my phone number 412-658-8546.')
#area_code, main_num = mo.groups()
#print(f"Phone Number Found: \nArea Code: {area_code}\nMain Number: {main_num}")
print(f"Phone Number Found: " + mo.group())



'''Here, we pass our desired pattern to re.compile() and store the resulting
Regex object in phoneNumRegex. Then we call search() on phoneNumRegex and pass
search() the string we want to search for a match. The result of the search
gets stored in the variable mo. In this example, we know that our pattern
will be found in the string, so we know that a Match object will be returned.
Knowing that mo contains a Match object and not the null value None, we can
call group() on mo to return the match. Writing mo.group() inside our print
statement displays the whole match, 415-555-4242.'''

