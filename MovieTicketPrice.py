prompt = "\t\t\t\tWelcome to Sunday Night Movie Theatre!!"

active = True

while active:
    age = int(input("Enter the age of person: "))
    if age < 3:
        print("You don't need to pay for cute little angels, The ticket is free.")
    elif age >=3 and age <= 12:
        print("You need to pay $12.")
    elif age > 12:
        print("You need to pay $15.")
    else:
        print("Sorry Invalid Input")
    conti = input("Do you want to continue?(type 'yes' or 'no'): ")
    if conti == 'no':
        active = False
