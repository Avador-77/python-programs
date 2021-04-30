f = open('ThinkPythonBookSolutions/words.txt')

for line in f:
    if len(line) > 20:
        word = line.strip()
        print(word)

