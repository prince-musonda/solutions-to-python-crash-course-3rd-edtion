from lottery import play_lottery

lottery_winning_combination = play_lottery()

attempts_number = 0
while True:
    attempts_number += 1
    correctly_guessed_char = 0 
    our_random_attempt = play_lottery()
    for char in our_random_attempt:
        if char in lottery_winning_combination:
            correctly_guessed_char += 1
        
    if correctly_guessed_char == 4:
        print(f'\nwe have guessed the right combination and it took {attempts_number} attempts.')
        print(f'And these were the winning characters: {our_random_attempt} ')
        break