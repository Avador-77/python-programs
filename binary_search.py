def binary_search(my_list, item):
    low = 0
    high = len(my_list)
    high -= 1
    while low <= high:
        mid = (low + high)
        guess = my_list[mid]
        if guess == item:   
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
my_list = [1, 3, 5, 7, 9]
print (binary_search(my_list, 3)) # => 1
print (binary_search(my_list, -1)) # => None