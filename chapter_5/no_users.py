usernames = [] # list of users is empty

if usernames: # checking to see if we have any usernames before taking any action         
    for user in usernames:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {user.title()}, thank you for logging in again.')
else:
    print('we need to find some users!') # when we don't have any users