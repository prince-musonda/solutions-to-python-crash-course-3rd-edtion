river_n_country = {'nile':'egypt','ob':'russia','zambezi':'zambia'}

for river, country in river_n_country.items():
    print(f' The {river.title()} river runs through {country.title()}')

print('\nList of Rivers:')
number = 1
for river in river_n_country:
    print(f"{number}.{river.title()}")
    number += 1

print('\nList of countries where the rivers above run through:')
number = 1
for country in river_n_country.values():
    print(f"{number}.{country.title()}")
    number += 1

