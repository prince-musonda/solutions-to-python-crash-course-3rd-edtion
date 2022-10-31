#list of existing usernames
current_users = ['Grand','Charles','Evans','Sibeso','Alfred']
#list of new usernames
new_users = ['GRAND','prince','shadrick','kedrick','samson','EVAns']

# copying all items in current users and saving them in lower case
current_users_copy = []
for user in current_users:
    current_users_copy.append(user.lower())

# checking if a new username already exists
for new_user in new_users:
    if new_user.lower() in current_users_copy:
        print(f'sorry, you need to enter a new username, {new_user} already exists')
    else:
        print(f'{new_user}, is available')