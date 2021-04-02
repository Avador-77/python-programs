prompt = "'Let's create a list of sandwiches that you want us to make."

oneMore = True  

sandwichOrders = []

finishedOrders = []

i = 1
print("Enter the names of sandwiches (type '\end' if you have made your list):\n[Note that 'Deli' has run out of 'Pastrami']")
while oneMore:
    toPrepare = input('{}{} '.format(i,'.'))
    if toPrepare == '\end':
        oneMore = False
    else:
        sandwichOrders.append(toPrepare)
    i += 1

i = 1

print("\n----List of sandwhiches has been recorded.----\n")

for item in sandwichOrders:
    preparing = item.lower()
    if preparing == 'deli':
        print("\nNote that 'Deli' has run out of 'Pastrami'")
        #sandwichOrders.remove('deli')
    else:
        print("\nPreparing your",preparing.title(),"sandwich.")
        finishedOrders.append(preparing)

    

print("\nAll your sandwiches have been prepared.\nHere is the list.")

for item in finishedOrders:

    print(i,".","",item.title())
    i += 1

print("\nPrinting sandwich orders list:")
i = 1

'''for item in sandwichOrders:
    if item == 'deli':
        sandwichOrders.remove('deli')'''

for item in sandwichOrders:
    print(i,".","",item.title())
    i += 1