car_choice = input('What kind of car would you like? ')
if car_choice.lower() != 'bmw':
    chosen_car = car_choice.title()
else:
    chosen_car = car_choice.upper()

print(f"let me see if i can find you a {chosen_car}")