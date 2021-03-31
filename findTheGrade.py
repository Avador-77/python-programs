percentage = int(input("Enter the percentage of student: "))

if(percentage >= 80 and percentage <= 100):
    print("A")

elif(percentage >= 73 and percentage <= 79):
    print("B")

elif(percentage >= 65 and percentage <= 72):
    print("C")

elif(percentage >= 0 and percentage <= 64):
    print("D")

else:
    print("Z")

