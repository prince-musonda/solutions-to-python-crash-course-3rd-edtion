restaurant_menu = ('chicken and chips','sausage and chips','burger',
                    'pepperoni pizza','chicken pie')
print(f"{'FooD MENU':>30}")
counter = 1
for food in restaurant_menu:
    print(f'{counter}.{food}')
    counter += 1


# modifying one of the elements in the tuple
# won't work!!!!
#restaurant_menu[1] = 'polon sandwitch'


#modifying two items from the tuple through variable reassignment
restaurant_menu =  ('chicken and chips','polon sandwitch','burger',
                    'nshima with chicken and beans','chicken pie')
counter = 1
print(f'\n{"NEW MENU":>30}')
for food in restaurant_menu:
    print(f'{counter}.{food}')
    counter += 1