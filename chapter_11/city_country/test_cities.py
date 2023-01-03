from city_country import city_function

def test_city_country():
    '''test inputs of a city name and the name of the country a city is
    located in'''

    city_country_name = city_function('santiago','chile')
    assert city_country_name == 'Santiago, Chile'

def test_city_country_population():
    city_country_population = city_function('santiango','chile','50000')
    assert city_country_population == 'Santiango, Chile - population 50000'