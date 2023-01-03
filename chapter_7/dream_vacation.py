polling_results = {}
polling_active = True
prompt = 'if you would visit one place in the world,\nwhere would you go? '


while polling_active:
    name = input('enter your name: ')
    dream_vacation = input(prompt)

    # adding user input to polling_results 
    polling_results[name] = dream_vacation

    # continue with the poll?
    continue_polling = input('would like let someone else take the poll(yes/no): ')
    if continue_polling.lower() == 'no':
        polling_active = False

print('Here are the results for the poll: ')
for name, dream_vacation in polling_results.items():
    print(f"{name.title()} would like to visit {dream_vacation.title()}")