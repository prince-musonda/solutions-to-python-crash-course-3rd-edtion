def make_sandwitch(*sandwitch_topping):
    '''simulate making a sandwitch with the specified arbitrary number of arguments
    as toppings on the sandwutch'''
    print('making you a sandwitch with the following on it:')
    for topping in sandwitch_topping:
        print(f"- {topping}")

make_sandwitch('bananas','chicken','corn','cabbage','fish')
make_sandwitch('egg','tomatoes','onion')
make_sandwitch('egg','poron','tuna')