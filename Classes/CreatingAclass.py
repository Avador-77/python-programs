class Restaurant():

    def __init__(self, resName, cuisineType):
        self.resName = resName
        self.cuisineType = cuisineType
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant Name: " + self.resName.title() + "\nCuisine Type: " + self.cuisineType.title() + "\nCustomers Served: " + str(self.number_served))
        print("\nLet's update the number served using a method.")

    def set_number_served(self, newCustomers):
        self.number_served = newCustomers
    
    def increment_number_served(self, cstmrNumb):
        self.number_served += cstmrNumb

    def open_or_close(self):
        print("(" + self.resName.title() + " restaurant is Opened" + ")")



restaurant = Restaurant('the moon light', 'chinese')

restaurant.open_or_close()
restaurant.number_served = 25
restaurant.describe_restaurant()
restaurant.set_number_served(50)
restaurant.increment_number_served(150)
restaurant.describe_restaurant()

