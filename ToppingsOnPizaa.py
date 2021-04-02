prompt = "Please enter the name of your toppings that you want us to add on your pizza:(Type quit to end your enteries)\n"

toppings = ""

while toppings != 'quit':
    toppings = input(prompt)
    if toppings == 'quit':
        break
    else:
        print("\nWe will add ",toppings," in your pizza.")