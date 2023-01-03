def city_function(city,country,population=''):
    if population:
        results = f'{city.title()}, {country.title()} - population {population}'
    else:
        results =  f'{city.title()}, {country.title()}'
    return results