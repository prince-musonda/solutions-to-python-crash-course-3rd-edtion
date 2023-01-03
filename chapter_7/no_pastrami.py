sandwitch_order = [
    'pastrami','chicken','egg','pastrami','seafood',
    'roasted beef','pastrami','grilled cheese',
    'ham','tuna','pastrami'
    ]
print('We have run out of pastrami.')
while 'pastrami' in sandwitch_order:
    sandwitch_order.remove('pastrami')

print('\nThe following sandwitches have been made:')
for sandwitch in sandwitch_order:
    print(sandwitch)