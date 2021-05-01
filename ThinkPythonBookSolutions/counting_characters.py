'''s = 'czechosolovakia'

def histogram(s):
    d = dict()
    
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

print(histogram(s))'''

#more precise way to do it...
s = 'czechosolovakia'

def histogram(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)
    return d
    
print(histogram(s))