squares = []

for number in range(1,10):
    squares.append(number ** 2)

print(squares)
print()
print('The first 3 items in the list are:')
print(squares[0:3])
print()
print('3 items from the middle are:')
print(squares[3:6])
print()
print('the last 3 items from the list are:')
print(squares[-3:])