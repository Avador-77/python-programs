def count(word, letter):
    counts = 0

    for alphabet in word:
        if alphabet == letter:
            counts += 1
    return counts

word = input("Enter a word:")
letter = input("Enter a letter you want to count:")

print("Total number of time your letter appears in your word is ",count(word,letter))
