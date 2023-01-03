def city_country(city,country):
    '''return a city name and country of location, neatly formatted'''
    city_country = f"{city}, {country}".title()
    return city_country

print('loading ...\n')
city_1 = city_country('new york city','america')
print(city_1)
city_2 = city_country('mumbai','india')
print(city_2)
city_3 = city_country('delhi','india')
print(city_3)

