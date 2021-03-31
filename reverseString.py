def rev_string(word):
    rev_string = word[::-1]

    if word == rev_string:
        print("Your string is palindrome.")
        print("You entered: ",word)
        print("Reverse of your string: ",rev_string)
    else:
        print("NO, not a palindrome.")
        print("You entered: ",word)
        print("Reverse of your string: ",rev_string)

word = input("Enter a string: ")

rev_string(word)

