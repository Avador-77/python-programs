names = ['rajat','shilpa','garry','samantha']

#if you want to print hello messages to each member of the list, you can do it in two different ways:

'''for name in names:
    print('Hello, ' + name ) #this statement right here is very readble 

    print(' '.join(["Hello,", name])) #This is not very understandable, 
                                      #but i think it really doesn't matter as this will always be reading by a 
                                      # programmer and not by any 
                                      # user so it's fine.

'''
## if you want to print all the names of the list as a string you can do it like this: 
print(', '.join(names))
