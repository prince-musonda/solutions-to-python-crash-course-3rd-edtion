pet1 = {'animal_type': 'dog','owner':'james'}
pet2 = {'animal_type': 'cat','owner':'sizwayo'}
pet3 = {'animal_type': 'pony','owner':'given'}
pet4 = {'animal_type': 'miniture horse','owner':'jenny'}

pets = [pet1,pet2,pet3,pet4]

for pet in pets:
    print(f"Animal Type: {pet['animal_type'].title()}")
    print(f"Owner: {pet['owner'].title()}\n")