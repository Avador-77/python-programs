fileName = 'filesandexpressions/guestList.txt'

with open(fileName,'a') as fo:
    guest_name = input('Enter your name: ')
    number = int(input("Enter your mobile number: "))
    fo.write("\nWelcome " + guest_name + " to the guest's list!!\n")
    fo.write("\nThis is your Phone Number: " + str(number))

with open(fileName) as fo:
    lines = fo.readlines()

for line in lines:
    print(line.rstrip())
