with open('filesandexpressions/food_items.txt') as fileObject:
    items = fileObject.readlines()
    for item in items:
        print(item.replace('waffer','ice cream'))
        
        



