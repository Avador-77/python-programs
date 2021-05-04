def longestItemOfList(alist):
    longestLength = -1
    for s in alist:
        if len(s) > longestLength:
            longestLength = len(s)
    return longestLength

def tablePrint(listOfLists):
    lengthOfInnerList = len(listOfLists[0])
    
    for row in range(0, lengthOfInnerList):
        s = ''
        for i in range(0, len(listOfLists)):
            s += " " + listOfLists[i][row].rjust(longestItemOfList(listOfLists[i]))
        print(s)
    




tableData = [['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose']
]

tablePrint(tableData)
