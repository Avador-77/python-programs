favourite_numbers = {
    'rajat':[1,2,3,4,5,6,7],
    'bajirao':[10,5,7,8],
    'mastani':[2,6,19],
    'chacha chuha':[11]
}

for name, favNums in favourite_numbers.items():
    if len(favNums) == 1:
        print("\n",name.title(),"'s favourite number is ")
        for num in favNums:
            print("   ",num)
    elif len(favNums) > 1:
        print("\n",name.title(),"'s favourite numbers are ")
        for num in favNums:
            print("   ",num)
    else:
        print("Invalid Input")
