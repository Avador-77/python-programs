def capitalize_all(wordList):
    
    res = []
    for s in wordList:
        if type(s) is list:
            s = capitalize_all(s)
        else:
            s = s.capitalize()
        res.append(s)
    return res

res = capitalize_all([['rajat'],['manoj']])
print(res)