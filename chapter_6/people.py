person_1= {
        'first_name': 'samson',
        'last_name' : 'kaluba',
        'age': 22,
        'city' : 'kabwe'
}

person_2 = {
    'first_name' : 'melvin',
    'last_name' : 'musonda',
    'age':16,
    'city' : 'kabwe'
}

person_3 = {
    'first_name' : 'willson',
    'last_name' : 'nkunga',
    'age' : 20,
    'city' : 'lusaka'
}

people = [person_1, person_2, person_3]

for person in people:
    print(f"name: {person['first_name'].title()} {person['last_name'].title()}")
    print(f"age: {person['age']}")
    print(f"city: {person['city'].title()}\n")
    