class Restaurant:
    '''modelling a restaurant'''
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''show restaurants's name and the type of cuisine severed
        at the restaurant'''
        print(f"retaurant name: {self.restaurant_name.title()}\nCuisine:"
         f"{self.cuisine_type.title()}\n")
    
    def open_restaurant(self):
        '''simulate opening the restuarant'''
        print(f"{self.restaurant_name.title()} is now open for business\n")

    def set_number_served(self,value):
        '''set value for number_served attribute'''
        self.number_served = value
    
    def increment_number_served(self, increment_value):
        '''increment number_served attribute by specified amount'''
        self.number_served += increment_value



restaurant = Restaurant('mama','african')
print(f"number of customers served: {restaurant.number_served}")
restaurant.number_served = 67
print(f"number of customers served: {restaurant.number_served}")
restaurant.set_number_served(123)
print(f'number of customers served: {restaurant.number_served}')
restaurant.increment_number_served(30)
print(f'number of customers served: {restaurant.number_served}')
