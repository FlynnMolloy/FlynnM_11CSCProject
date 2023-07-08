'''27/06 code'''

import math

def game1() : #game1
    print('Game 1')
    print('Instructions')
    max_bound = input_num(1000, 1, str('\nWhat would you like the maximum value to be?\n'))
    min_bound = input_num(1000, 1, str('\nWhat would you like the minimum value to be?\n'))
    rounds = input_num(100, 1, str('\nHow many rounds would you like to play?\n'))
    guesses = math.ceil(math.log((max_bound - min_bound), 2))

def input_num(max_f, min_f, msg_f) : #input numbers for game 1
    input_flag = True
    while input_flag is True :
        try :
            user_input = float(input(msg_f + str('\n')))
            if user_input > max_f or user_input < min_f :
                print("Error with choice, 3")
            else :
                return user_input
        except ValueError :
            print("Error with choice, 4")

test = int(input_num(10, 1, str('test')))
print(test)