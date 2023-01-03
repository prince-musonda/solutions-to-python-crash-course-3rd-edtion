prompt = 'enter a number'
prompt += ' and i will tell you whether it is a multiple of ten? '

multiple = int(input(prompt))

if multiple % 10 == 0:
    print(f"yes, {multiple} is a multiple of ten")
else:
    print(f'no, {multiple} is not a multiple of ten')