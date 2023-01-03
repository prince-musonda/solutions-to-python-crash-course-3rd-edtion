def describe_city(city,country = 'zambia'):
    '''describe a city'''
    print(f"\n{city.title()} is in {country.title()}")

describe_city(city = 'copperbelt')
describe_city('hong kong','china')
describe_city('istambu','turkey')