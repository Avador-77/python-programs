def ackerman_function(m, n):
    if m > 0 and n > 0:
        return ackerman_function(m - 1, ackerman_function(m, n - 1))
    elif m > 0 and n == 0:
        return ackerman_function(m - 1, 1)
    elif m == 0:
        return n + 1

print(ackerman_function(3, 4))