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
    
    def fill_gas_tank(self):
        print("This car has 30L gas tank.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def read_odometer(self):
        print("This car has ", self.odometer_reading, " miles on it.")

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        #self.battery_size = 70   ----- providing value using a separate battery class   
        self.battery = Battery()

    """def describe_battery(self):     #shifting the method in battery class
        print("This car has " + str(self.battery_size) + "-kWh battery.")"""
    
    def fill_gas_tank(self):
        print("Tesla is an Electric Car so It has no gas tank.")

class Battery():

    def __init__(self, battery_size = 70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has " + str(self.battery_size) + "-kWh battery.")
    
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 80:
            range = 270
        message = "This car can travel " + str(range)
        message += " miles on a full charge."
        print(message)

my_tesla = ElectricCar('Tesla', 'Model S', 2016)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()

my_tesla.fill_gas_tank()

my_tesla.battery.get_range()

my_car = Car('audi', 'a4', 2016)

print(my_car.get_descriptive_name())

#my_car.odometer_reading = 22 #modifying the default value of the attribute of instance my_car DIRECTLY

my_car.update_odometer(2) #modifying the default value of the attribute of instance my_car using a method

my_car.read_odometer()

my_car.increment_odometer(12560)

my_car.read_odometer()

my_car.fill_gas_tank()
