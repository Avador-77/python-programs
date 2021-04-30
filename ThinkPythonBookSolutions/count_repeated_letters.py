def count(word, w, letter):
    counter = 0
    
    while w < len(word):
        if word[w] == letter:
            counter += 1
            w += 1
            continue
        elif word[w] != letter:
            w += 1
            continue
    if not counter:
        return ("Not Found!")
    else:
        return counter

print(count('banana', 3, 'a'))