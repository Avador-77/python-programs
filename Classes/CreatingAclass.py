class Restaurant():

    def __init__(self, resName, cuisineType):
        self.resName = resName
        self.cuisineType = cuisineType
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant Name: " + self.resName.title() + "\nCuisine Type: " + self.cuisineType.title() + "\nCustomers Served: " + str(self.number_served))
        

    def set_number_served(self, newCustomers):
        self.number_served = newCustomers
    
    def increment_number_served(self, cstmrNumb):
        self.number_served += cstmrNumb

    def open_or_close(self):
        print("(" + self.resName.title() + " restaurant is Opened" + ")")

class IceCreamStand(Restaurant):

    def __init__(self):
        
        self.flavours = ['choclate', 'vanilla', 'butterscotch']

    def display_flavours(self):
        print("let's see what flavours do we have in our favourite ice cream parlour.")
        print("Flavours = ",self.flavours)
        
        


iceCream = IceCreamStand()
#iceCream.describe_restaurant()
iceCream.display_flavours()

restaurant = Restaurant('the moon light', 'chinese')

restaurant.open_or_close()
restaurant.number_served = 25
restaurant.describe_restaurant()
print("\nLet's update the number served using a method.")
restaurant.set_number_served(50)
restaurant.increment_number_served(150)
restaurant.describe_restaurant()

