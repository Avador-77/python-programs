first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
third_num = int(input("Enter the third number: "))

if first_num > second_num:
    if first_num > third_num:
        print(first_num, ' is the greatest number.')
    
    else:
        print(third_num, 'is the greatest number.')
    
else:
    if second_num > third_num:
        print(second_num, 'is the greatest number.')
    
    else:
        print(third_num, 'is the greatest number.')