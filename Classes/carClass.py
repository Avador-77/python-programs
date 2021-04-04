class Car():

    def __init__(self, make, model , year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #setting a default value for an attribute
    
    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def read_odometer(self):
        print("This car has ", self.odometer_reading, " miles on it.")

my_car = Car('audi', 'a4', 2016)

print(my_car.get_descriptive_name())

#my_car.odometer_reading = 22 #modifying the default value of the attribute of instance my_car DIRECTLY

my_car.update_odometer(2) #modifying the default value of the attribute of instance my_car using a method

my_car.read_odometer()

my_car.increment_odometer(12560)

my_car.read_odometer()
