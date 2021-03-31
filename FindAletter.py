def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

word = input("Enter a word:")
letter = input("Input the letter that you want to find:")
index = int(input("From where you want to begin your search:"))

print(find(word,letter,index))