class Restaurant():

    def __init__(self, resName, cuisineType):
        self.resName = resName
        self.cuisineType = cuisineType

    def describe_restaurant(self):
        print("Restaurant Name: " + self.resName.title() + "\nCuisine Type: " + self.cuisineType.title())

    def open_or_close(self):
        print("(" + self.resName.title() + " restaurant is Opened" + ")")



restaurant = Restaurant('the moon light', 'chinese')

restaurant.open_or_close()

restaurant.describe_restaurant()