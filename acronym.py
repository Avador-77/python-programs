user_input = str(input("Enter your phrase: "))
text = user_input.split()
a = ''
for i in text:
    a += str(i[0]).upper()
print(a)
