Responses = {}

active = True

while active:
    name = input("\nWhat is your good name sir?\n")

    response = input("which Political party do you like or follow?\n")

    Responses[name] = response

    repeat = input("Would you like to let another person respond?('yes'/'no'): ")
    if repeat == 'no':
        active = False
    
print("\n----Announcing Favourite Parties----\n")

for name, response in Responses.items():
    print(name.title(),"'s favourite political party is",response.title())