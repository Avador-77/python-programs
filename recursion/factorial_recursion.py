try:
    def fact(n):
        if n >= 1:
            return n * fact(n-1)
        else:
            return 1
except:
    print("Programs Fails")

print(fact(4))

