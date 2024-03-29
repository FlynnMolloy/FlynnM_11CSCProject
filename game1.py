''' 9/07 code'''

import math
import random
import time

def higher_lower() :
    ''' higher or lower game '''
    print('Game 1')
    time.sleep(1)
    print('Instructions:')
    time.sleep(1)
    print('\nThe computer will pick a number between the boundaries you provide.')
    time.sleep(3)
    print('\nYou will have to guess the number the computer has chosen.')
    time.sleep(2.5)
    print("\nYou will be told if the number you guessed is higher/lower than the computer choice.")
    time.sleep(4)
    max_bound = input_num(1000, 1, str('\nWhat would you like the maximum value to be?\n'))
    min_bound = input_num(1000, 1, str('\nWhat would you like the minimum value to be?\n'))
    rounds = input_num(100, 1, str('\nHow many rounds would you like to play?\n'))
    guesses = math.ceil(math.log((max_bound - min_bound), 2))
    score_array = []
    dropped = 0
    for i in range(rounds) :
        print(f'Round {i}')
        time.sleep(1)
        print('\nStarting round...')
        time.sleep(1)
        win = 0
        score = 0
        computer_choice = random.randint(min_bound, max_bound)
        for a in range(guesses) :
            print(f'You have {(guesses - a)} guesses left.')
            user_choice = input_num(max_bound, min_bound, 'Your guess:\n')
            score+=1
            if user_choice == computer_choice :
                print('You win!\n')
                time.sleep(1)
                win = 1
                break
            elif user_choice > computer_choice :
                print('Lower!\n')
                time.sleep(1)
            else :
                print('Higher!\n')
                time.sleep(1)
        if win == 1 :
            score_array.append(score)
        else :
            dropped+=1
        avg_score = round(sum(score_array) / len(score_array), 2)
        worst_score = max(score_array)
        best_score = min(score_array)
        print(f'You have an average score of {avg_score}.\n')
        time.sleep(2)
        print(f'You have a worst score of {worst_score}.\n')
        time.sleep(2)
        print(f'You have a best score of {best_score}\n')
        time.sleep(2)
        print(f'You have dropped {dropped} rounds.')
        time.sleep(2)
        print('--------------------------------------------------------------')
    print('Your rounds have expired, would you like to play again?')
    replay = input_num(2, 1, '1 for yes, 2 for no')
    if replay == 1 :
        higher_lower()
    print('Resetting to menu...\n')
    time.sleep(1)



def input_num(max_f, min_f, msg_f) :
    '''input numebrs for game 1'''
    input_flag = True
    while input_flag is True :
        try :
            user_input = int(input(msg_f + str('\n')))
            if user_input > max_f or user_input < min_f :
                print("Error with choice, 3")
            else :
                return user_input
        except ValueError :
            print("Error with choice, 4")
