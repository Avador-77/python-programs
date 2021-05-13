import re

timesMoccurs = re.compile('m|M')

print(" Number Of 'm' or 'M' occurs in your string is ", len(timesMoccurs.findall('MynameisManojMirza.IamEarlymorninghereinsidethemalcolmsmansionandmatchingmymatchesinmymemory.')))