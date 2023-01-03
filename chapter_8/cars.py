def build_car(manufacture, model, **car_info):
    '''store info about a car'''
    car_info['manufacture'] = manufacture
    car_info['model']  = model
    return car_info

my_car = build_car('BMW','M8 competition',doors = 2, color = 'red')
print(my_car)