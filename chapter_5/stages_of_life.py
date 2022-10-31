age = 19

#detamining the age group
if age < 2:
    stage ='baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
else:
    stage = 'elder'

#printing out the age group
if stage == 'adult' or stage == 'elder':
    print(f'you are an {stage}')
else:
    print(f'you are a {stage}')