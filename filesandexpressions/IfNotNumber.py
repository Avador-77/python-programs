num1, num2 = input("1st numbers: "), input("2nd numbers: ")
try:
    print(int(num1) + int(num2))

except ValueError:
    print("Please enter integers not any other values.")