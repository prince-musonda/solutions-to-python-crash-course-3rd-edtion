print('Enter 2 numbers and i will add the up for you.'\
'if you want to quit enter \'q\' to stop running the program.')
while(True):
    first_number = input('First number: ')
    if first_number.lower() == 'q':
        break
    second_number = input('second number: ')
    if second_number.lower() == 'q':
        break
    try:
        sum = int(first_number) + int(second_number)
    except ValueError:
        print('invalid input, you did not enter a valid number')
    else:
        print(f'{first_number} + {second_number} = {sum}')