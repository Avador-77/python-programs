def any_lowercase1(s):           #the problem with this function is it is returning true or false by only checkingthe first character of the string and couldn't proceed further as it encounters return statement after this.'''
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    for c in s: 
        if 'c'.islower():    #the problem with this function is it is only checking 'c' and as it is lowercase, it always print true.'''
            return 'true'
        else:
            return 'false'

def any_lowercase3(s): #correct
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s): #correct
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s): #false
    for c in s:
        if not c.islower():
            return False
    return True



s = input("Enter any word: ")

#print(any_lowercase1(s))

#print(any_lowercase2(s))

#print(any_lowercase3(s))

#print(any_lowercase4(s))

print(any_lowercase5(s))