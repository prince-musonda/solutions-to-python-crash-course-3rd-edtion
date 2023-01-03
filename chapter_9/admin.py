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



class Admin(User):
    '''attempt to model an account for the admin'''
    def __init__(self, first_name, last_name,age ,phone_number=None,Email=None):
        '''initialize attributes for the admin account'''
        super().__init__(first_name,last_name,age,phone_number,Email)
        self.privileges = ["can ban users","suspend user's account","can delete posts"]

    def show_privileges(self):
        '''show admin privileges'''
        print('---------------________PRIVILEGES________-------------')
        for privilege  in self.privileges:
            print(privilege.title())

website_admin = Admin('prince','musonda',19)
website_admin.describe_user()
website_admin.show_privileges()