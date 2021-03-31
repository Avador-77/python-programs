def backward_string(a_strng):
    length = len(a_strng) * (-1)
    index = -1
    while index >= length:
        letter = a_strng[index]
        print(letter)
        index -= 1 

a_strng = input("Enter a string:")
backward_string(a_strng)