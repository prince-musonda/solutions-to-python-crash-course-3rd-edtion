class User:
    """attempt to model a user of a website"""
    def __init__(self, first_name, last_name,age ,phone_number=None,Email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempt = 0
        if phone_number:
            self.phone_number = phone_number
        else:
            self.phone_number = ''
        if Email:
            self.email = Email
        else:
            self.email = ''
            

    def describe_user(self):
        """display all known details about a user"""
        print(f"first name: {self.first_name.title()}")
        print(f"last name: {self.last_name.title()}")
        print(f"age : {self.age}")
        if self.phone_number:
            print(f"phone number: {self.phone_number}")
        if self.email:
                print(f"Email: {self.email}")
      
      
    def greet_user(self):
        '''display a personalized greeting to the user'''
        print(f"Hello {self.first_name.title()}")

    def increment_login_attempt(self):
        '''increment login_attempt attribute by 1'''
        self.login_attempt += 1
    
    def rest_login_attempt(self):
        '''reset the value of login_attempt attribute to 0'''
        self.login_attempt = 0


# create an instance of the User class
user1 = User('prince','musonda',19)
# increment  login attempts
user1.increment_login_attempt()
user1.increment_login_attempt()
user1.increment_login_attempt()
user1.increment_login_attempt()

print(f'number of login_attemts by {user1.first_name}: {user1.login_attempt}')

# reset login attempts
user1.rest_login_attempt()
print(f'number of login attempts by {user1.first_name}: {user1.login_attempt}')