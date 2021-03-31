import math
#from columnar import columnar

def test_square_root(value):
    initial = 1.0
    while initial <= value:
        a = initial
        if a==1:
            x = 1
        else:
            x = a - 1
        while True:

            y = (x + a/x) / 2
            if y == x:
                break
            x = y
        
        my_function = y

        sqrt_function = math.sqrt(a)
        
        absolute_difference = abs(my_function - sqrt_function)

        print('{:<20}'.format(initial),'{:<20}'.format(my_function),'{:<20}'.format(sqrt_function),'{:<20}'.format(absolute_difference))
        '''the above line of code is called output formatting, here i am justifying my output as left justify as i have used < sign, if i used ^ sign the
        output will be center justify and if i used > sign the output will be right justified.'''
    
        '''headers = ('value','sqrt by my_function','math.sqrt','absolute_difference')

        data = [
            [initial],
            [my_function],
            [sqrt_function],
            [absolute_difference]
        ]

        table = columnar(data, headers, no_borders = True)
        print(table)'''
        initial += 1





value = float(input("Enter a number upto which you want to compute their square root:"))

test_square_root(value)








