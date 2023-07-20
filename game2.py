'''19/07'''

import random
import time

def input_num_float(max_f, min_f, msg_f) : #input numbers for game 2
    input_flag = True
    while input_flag is True :
        try :
            user_input = float(input(msg_f + str('\n')))
            if user_input > max_f or user_input < min_f :
                print(f"Error with choice, 3, must place choice between {max_f} and {min_f}")
            else :
                return user_input
        except ValueError :
            print("Error with choice, 4")

def input_num_int(max_f, min_f, msg_f) : #input numbers for game 1
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

def lucky_unicorn() :
    print('Lucky Unicorn Game')
    time.sleep(1)
    print('Instructions:\n')
    time.sleep(1)
    print('You will enter an amount of money less than/equal to $10.\n')
    time.sleep(3)
    print('You will enter how much money you want to gamble on this bet.\n')
    time.sleep(3)
    print('You will be given a random chance to win more money.\n')
    time.sleep(3)
    unicorn = 5
    horse = 0.5
    zebra = 0.5
    donkey = 0
    balance = input_num_float(10, 1, 'How much money would you like to input?')
    while balance > 0 :
        bet = input_num_float(balance, 0.5, 'How much would you like to bet?\n')
        
        win_num = random.randint(1, 10)
        if win_num == 10 :
            print('You got a unicorn!')
            time.sleep(2)
            winnings = bet * unicorn
            print(f'You won ${winnings}!')
        elif win_num == 9 or win_num == 8 :
            print('You got a horse!')
            time.sleep(2)
            winnings = bet * horse
            print(f'You won ${winnings}!')
        elif win_num == 7 or win_num == 6 :
            print('You got a zebra!')
            time.sleep(2)
            winnings = bet * zebra
            print(f'You won ${winnings}!')
        else :
            print('You got a donkey!')
            time.sleep(2)
            winnings = bet * donkey
            print(f'You won ${winnings}!')
        balance = balance + winnings - bet
        time.sleep(2)
        print(f'Your balance is now ${balance}.\n')
        time.sleep(1.5)
        print('Would you like to cash out?')
        time.sleep(1.5)
        cash_out = input_num_int(2, 1, '1 for yes, 2 for no.\n')
        print('--------------------------------------------------------------')
        if cash_out == 1 :
            break
    if balance <= 0 :
        print("\nYou gambled all your money away.\n I hope you're happy.\n")
    else :
        print(f'You cashed out with ${balance} to spare.')
    time.sleep(3)
    print('Resetting to menu...\n')
    time.sleep(1)
