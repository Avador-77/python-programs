prompt = "'Let's create a list of sandwiches that you want us to make."

oneMore = True  

sandwichOrders = []

finishedOrders = []

i = 1
print("Enter the names of sandwiches (type '\end' if you have made your list):")
while oneMore:
    toPrepare = input('{}{} '.format(i,'.'))
    if toPrepare == '\end':
        oneMore = False
    else:
        sandwichOrders.append(toPrepare)
    i += 1

i = 1

print("\n----List of sandwhiches has been recorded.----\n")

while sandwichOrders:
    preparing = sandwichOrders.pop()
    print("\nPreparing your",preparing.title(),"sandwich.")

    finishedOrders.append(preparing)

print("\nAll your sandwiches have been prepared.\nHere is the list.")

for item in finishedOrders:

    print(i,".","",item.title())
    i += 1
