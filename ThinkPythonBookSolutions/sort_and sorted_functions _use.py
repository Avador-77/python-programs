t1= [4,1,2,4,5,6]
t2 = sorted(t1) #it creates the copy first and modifies it and stores it in t2 and leave the original 
                #list unaffected
print(t2)
print(t1)

t1 = [4,1,2,4,5,6]
t2 = t1.sort() #returns nothing but modifies the original list
print(t1)
