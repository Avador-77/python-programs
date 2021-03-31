def rotate_word(userString, num):
    new_word = []
    for c in userString:
        numeric_value = ord(c)
        if numeric_value + num >= 97:
            new_char = numeric_value + num 
            add = chr(new_char)
            new_word.append(add)
    print(new_word)

userString, num = input("Enter the string"), int(input("how many times you want to rotate the word:"))
rotate_word(userString,num)