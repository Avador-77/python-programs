'''So, I am in a Python for GIS class and have tried and failed at this one part (out of five) home work assignments for the week.
Write a program to retrieve the fourth grade from the following list: 62, 68, 93, 75, 89, 85. Print out the numerical grade and letter grade based on the scale:
90-100: A
80-89: B
70-79: C
60-69: D
0-59: F'''

marks = int(input("Enter your marks: "))
if marks >= 90 and marks <= 100:
    print("90-100: A")
elif marks >= 80 and marks <= 89:
    print("80-89: B")
elif marks >= 70 and marks <= 79:
    print("70-79: C")
elif marks >= 60 and marks <= 69:
    print("60-69: D")
elif marks >= 0 and marks <= 59:
    print("0-59: F")
else:
    print("Invalid Input")
