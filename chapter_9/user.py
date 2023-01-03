class User:
    """attempt to model a user of a website"""
    def __init__(self, first_name, last_name,age ,phone_number=None,Email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
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

user1 = User('prince','musonda','20')
user1.greet_user()
user1.describe_user()

user2 = User('grand','gize','19','048746748493')
user2.greet_user()
user2.describe_user()

user3 = User('steve sibeso','nyambe','20','8373636463783','mrsteve@yahoo.com')
user3.greet_user()
user3.describe_user()

