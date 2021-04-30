current_users = ['RAJat','ANMOL','bajaj','tekchand','mohit', 'shubam','pankaj']

new_users = ['Rajat','Anmol','bajaj','sathiya','nilofar']

Cu_lower = [user.lower() for user in current_users]

for username in new_users:
    if username.lower() in Cu_lower:
        print("Sorry, the name " + username + ' has been taken. Try using a different username.')
    else:
        print('Username ' + username +' is available.')
