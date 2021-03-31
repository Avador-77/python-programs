favourite_number = {'rajat':7,'hussain':5,'narang':2,'shweta':10}

def newValues():
    favourite_number['riya'] = 45
    favourite_number['raju'] = 12
    favourite_number['parrot'] = 20

def displaying_contents():
    for k,v in favourite_number.items():
        print(k.title() + "'s favourite number is", v ,".")

displaying_contents()
print('Now adding some new key-pair values in our dictionary.')
newValues()
print('Now displaying our modified dictionary.')
displaying_contents()
    

