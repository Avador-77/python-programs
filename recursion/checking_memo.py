known = {0:0,1:1}
def fib(n):
    if n in known:
        return known[n]

    res = fib(n-1) + fib(n-2)
    known[n] = res
    return res


n = int(input("Enter some number:"))
for i in range(1, n+1):
    print(fib(i), end= " ")