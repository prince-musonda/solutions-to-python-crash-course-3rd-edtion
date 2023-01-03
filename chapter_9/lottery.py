from random import choice

def play_lottery():
    winning_characters = []
    '''return a list containing 4 winning characters for a lottery'''
    lottery_list = [0,1,2,3,4,5,6,7,8,9,10,'A','B','C','D']

    first_pick = choice(lottery_list)
    second_pick = choice(lottery_list)
    third_pick = choice(lottery_list)
    fourth_pick = choice(lottery_list)

    winning_characters.append(first_pick)
    winning_characters.append(second_pick)
    winning_characters.append(third_pick)
    winning_characters.append(fourth_pick)
    
    return winning_characters


