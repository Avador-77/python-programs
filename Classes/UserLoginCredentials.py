class Users():

    def __init__(self, Fname,Lname, City, PinCode):
        self.Fname = Fname
        self.Lname = Lname
        self.City = City
        self.PinCode = PinCode
        self.login_attempts = 0
    
    def describe_user(self):

        print("\nHere is the full information about you:")
        print("\nFirst Name: " + self.Fname.title() + "\t\tLast Name: " + self.Lname.title() + "\nCity: " + self.City.title() + "\t\tPin Code: " + str(self.PinCode) )

    def greet_user(self):
        fullName = self.Fname + " " + self.Lname
        print("Good Morning, " + fullName.title() + ".")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print("Log In Attempts: ", self.login_attempts)
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Re-setting Login Attempts: ", self.login_attempts)

user1 = Users('rajat','sharma','udhampur', 182101)

user1.greet_user()
user1.describe_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()
user1.increment_login_attempts()

"""user2 = Users('ashutosh','sharma','udhampur', 182101)

user2.greet_user()
user2.describe_user()

user3 = Users('begda','drenkad','londle', 182104)

user3.greet_user()
user3.describe_user()"""