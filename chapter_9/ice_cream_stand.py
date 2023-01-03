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


class IceCreamStand(Restaurant):
    '''attempt to model anice cream stand'''
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)

        self.ice_cream_flavours = ['vanilla','chocolate','banana']

    def display_ice_cream_flavours(self):
        '''print available ice cream flavours'''
        print(f'Here at {self.restaurant_name} we have the following ice cream flavours:\n')
        for flavour in self.ice_cream_flavours:
            print(f'\t{flavour}')

my_restaurant = IceCreamStand("kid's world", 'ice cream cuisine')
my_restaurant.display_ice_cream_flavours()
