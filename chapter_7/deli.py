sandwitch_order = ['chicken','egg','seafood','roasted beef','grilled cheese','ham','tuna']
finished_sandwitch = []

while sandwitch_order:
    sandwitch_type = sandwitch_order.pop()
    print(f'making {sandwitch_type.title()} sandwitch')
    finished_sandwitch.append(sandwitch_type)

print('\nThe following sandwitches have been made:')
for sandwitch in finished_sandwitch:
    print(sandwitch.title())