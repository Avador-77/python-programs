fileName = 'filesandexpressions/1million.txt'

with open(fileName) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.rstrip()

birthday = input('Enter your birthday in the format mmddyy: ')

if birthday in pi_string:
    print('Your birthday appears in the first million digits of pi.')
else:
    print('Sorry, Your birthday appears in the first million digits of pi.')

