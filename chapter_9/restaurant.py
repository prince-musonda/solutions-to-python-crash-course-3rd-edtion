class Restaurant:
    '''modelling a restaurant'''
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''show restaurants's name and the type of cuisine severed
        at the restaurant'''
        print(f"retaurant name: {self.restaurant_name.title()}\nCuisine:"
         f"{self.cuisine_type.title()}\n")
    
    def open_restaurant(self):
        '''simulate opening the restuarant'''
        print(f"{self.restaurant_name.title()} is now open for business\n")


restaurant = Restaurant("amigo's restaurant",'mexican')
restaurant.describe_restaurant()
restaurant.open_restaurant()