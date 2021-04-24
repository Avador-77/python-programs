import json

def get_stored_username():

    fileName = 'filesandexpressions/json(javaScript object notation)/username.txt'
    try:
        with open(fileName) as fo:
            username = json.load(fo)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    username = input("What is your name: ")
    fileName = 'filesandexpressions/json(javaScript object notation)/username.txt'
    with open(fileName, 'w') as fo:
        json.dump(username, fo)
    return username
def greet_user():
    username = get_stored_username()
    if username:
        print("WelCome back, " + username + "!")
    else: 
        username = get_new_username()
        print("Your data has been saved succcessfully.")

greet_user()
           

