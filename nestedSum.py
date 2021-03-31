def sum_all(list_of_integers):
    total = 0
    for x in list_of_integers:
        total += sum(x)
    
    return total

nestedList = [[1,2,3],[4,5,6]]

print("The sum of all the nested lists is ",sum_all(nestedList))