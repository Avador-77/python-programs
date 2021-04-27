'''def fib(n):
    if n == 1:                                 #time consuming
        return 0 
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input("Enter some number:"))

for i in range(1, n+1):
    print(fib(i), end= " ")'''


'''def fib(n):
    a= 0
    print(a,end=" ")
    b = 1
    print(b,end=" ")
    for i in range(1,n-1):
        c = a + b
        a = b
        b = c
        print(c,end=" ")

fib(100)'''

'''from math import sqrt as sq

def calc_fib(n):
    for i in range(0,(n+1)):
        f_no = round(((1 + 2.23606797749979)**i - (1 - 2.23606797749979)**i) / ((2**i) * 2.23606797749979))
        print(f_no,end=" ")

no_of_terms = int(input("Enter the number of terms you want to find in fibonacci series: "))
calc_fib(no_of_terms)'''


'''def iterativeFib(n):
    a, b = 0, 1

    for i in range(n):                      #better than the previous programs
        a, b = b, a + b
    
    return a'''


import decimal
import math
def formulaFibWithDecimal(n):
    decimal.getcontext().prec = 80000

    root_5 = decimal.Decimal(5).sqrt()
    phi = ((1 + root_5) / 2)

    a = ((phi ** n) - ((-phi) ** -n)) / root_5

    return round(a)

print(formulaFibWithDecimal(1000000))