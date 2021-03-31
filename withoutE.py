def has_no_e(word):
    index = 0
    for letter in word:
        if letter[index] == 'e':
            return -1
    return True


word = input("Enter a word: ")
print(has_no_e(word))




