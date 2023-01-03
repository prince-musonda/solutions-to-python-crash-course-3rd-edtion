from random import randint

class Dice:
    '''modeling a dice'''
    def __init__(self,sides = 6):
        '''initialize the number of sides attribute'''
        self.sides = sides
    
    def roll_dice(self):
        '''roll the dice and print the out come'''
        result = randint(1,self.sides)
        print(result)


dice_with_6 = Dice()
print(f'\nresults for rolling a {dice_with_6.sides} the dice 10 times:')
for i in range(1,11):
    dice_with_6.roll_dice()


dice_with_10 = Dice(10)
print(f'\nresults for rolling a {dice_with_10.sides} sided dice 10 times:')
for i in range(1,11):
    dice_with_10.roll_dice()

dice_with_20 = Dice(20)
print(f'\nresults for rolling a {dice_with_20.sides} the dice 10 times:')
for i in range(1,11):
    dice_with_20.roll_dice()
