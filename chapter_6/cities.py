cities = {
    'london':{
        'country':'united kingdom',
        'population':'8.98 million',
        'fact':'London is the samallest city in England'
    },

    'new york city':{
        'country':'united states of america',
        'population':'8.93 million',
        'fact': 'new york city is the noisest city in the world, a city that never sleeps.',
    },

    'paris':{
        'country':'france',
        'population': '2.16 million',
        'fact':'paris, is considered as the most romantic city in the world'
    }

}


for city, city_info in cities.items():
    print(f'\n{city.upper()}:')
    print(f"\tcountry: {city_info['country'].title()}")
    print(f"\tpopulation: {city_info['population'].title()}")
    print(f"\tInteresting fact: {city_info['fact'].title()}")