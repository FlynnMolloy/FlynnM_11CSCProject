''' 9/07 code '''

# imports
from game1 import *
from game2 import *
import time

#functions
def menu() :
    ''' menu function'''
    print('Welcome to the 11CSC Game Compendium!\n')
    time.sleep(1.5)
    flag = True
    while flag is True :
        print('1: Higher or Lower')
        print('2: Lucky Unicorn')
        print('3: Quit')
        try :
            user_choice = int(input('\nWhich game would you like to play?\n'))
            if user_choice > 3 or user_choice < 1 :
                print('Error with choice, 1, please choose a number in bounds')
            else :
                print(f'You picked option {user_choice}')
                print('--------------------------------------------------------------')
                time.sleep(1)
                flag = False
        except ValueError :
            print('Error with choice, 2')
    if user_choice == 1 :
        higher_lower()
    elif user_choice == 2 :
        lucky_unicorn()
    else :
        print('Goodbye!')
        time.sleep(1)
        quit()

#main routine
while True :
    menu()
