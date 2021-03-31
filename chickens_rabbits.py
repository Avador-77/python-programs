def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    store_heads = heads
    if legs > heads:
        heads = heads * 2
        legs = legs - heads
        if legs % 2 != 0:
            print(error_msg)
        else:
            legs = legs // 2
            rabbit_count = legs
            chicken_count = store_heads - rabbit_count
            print(chicken_count,rabbit_count)

    

    

#Provide different values for heads and legs and test your program
solve(20,10)