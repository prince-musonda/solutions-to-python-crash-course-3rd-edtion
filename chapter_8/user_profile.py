def build_profile(first,last,**user_info):
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

new_user = build_profile('prince','musonda',location= 'lusaka', age = 20)
print(new_user)