def takingNames():
    n = input('Kindly enter user names: ')
    if not n:
        print("We need to find some user names. Please enter some names.")
    
    usernames = n.split()
    return usernames


def greeting():
    usernames = takingNames()
    for name in usernames:
        
        if name == 'Admin' or name == 'admin':
            print('Hello' + name, 'howz your day going?')
        else:
            print('hello ' + name,'Thank you for logging in.' )

greeting()