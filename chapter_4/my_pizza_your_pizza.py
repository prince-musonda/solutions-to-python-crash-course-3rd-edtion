my_pizza = ['pepperoni','cheese','chicken','mashroom']
friends_pizza = my_pizza[:]

my_pizza.append('banana')
friends_pizza.append('rice')
counter = 1 # adding a counter that will be used as prefix for each item in the list

print("my favourite pizza's are: ")
for pizza_topping in my_pizza:
    print(f'{counter}.{pizza_topping}')
    counter += 1

counter = 1 # resetting the counter
print('\nmy friend\'s favourite pizza toppings are:')
for pizza_topping in friends_pizza:
    print(f'{counter}.{pizza_topping}')
    counter = counter + 1