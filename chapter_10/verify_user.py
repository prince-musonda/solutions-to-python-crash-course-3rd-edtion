from pathlib import Path
import json

def get_stored_user_info(path):
    '''retrieve stored infomation about a user'''
    if path.exists():
        content = path.read_text()
        user_info = json.loads(content)
        return user_info
    else:
        return None


def store_new_user_info(path):
    '''store infomation about a new user'''
    name = input("what is your name: ")
    email = input('your email address: ')
    phone_number = input('your phone number, beginning with country code: ')
    user_info = {
        'name' : name,
        'email' : email,
        'phone number' : phone_number
    }
    content = json.dumps(user_info)
    path.write_text(content)
    return user_info['name']

def verify_that_its_old_user(path):
    '''verify that the one using the account is the actual user
    or just someone else. if it is some else, then create a new account for them.'''
    user_info = get_stored_user_info(path)
    if user_info:
        old_user = input(f"Are you {user_info['name'].title()}.(yes/no): ")
        if old_user.lower() == 'yes':
            return True
        else:
            store_new_user_info(path)
           
def greet_user():
    '''greet a user'''
    path = Path('remember_me.json')
    user_info = get_stored_user_info(path)
    if user_info:
        old_user = verify_that_its_old_user(path)
        if old_user:
            print(f"welcome back {user_info['name']}. Here is what we currently"
            " know about you:")
            for key,value in user_info.items():
                print(f'{key.title()}: {value.title()}')
                
    else:
       new_user =  store_new_user_info(path)
       print(f'we will remember you {new_user.title()}')

if __name__ == '__main__':
    greet_user()
