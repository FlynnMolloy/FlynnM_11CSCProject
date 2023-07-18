''' 9/07 code '''

# imports
from game1 import *
from game2 import *

#functions
def menu() :
    ''' menu function'''
    print('Welcome to the 11CSC Game Compendium!\n')
    num_choices = 3
    flag = True
    while flag is True :
        print('1: Higher or Lower')
        print('2: Lucky Unicorn')
        print('3: Quit')
        try :
            user_choice = int(input('\nWhich game would you like to play?\n'))
            if user_choice > num_choices or user_choice < 1 :
                print('Error with choice, 1, please choose a number in bounds')
            else :
                print(f'You picked option {user_choice}')
                flag = False
        except ValueError :
            print('Error with choice, 2')

    if user_choice == 1 :
        higher_lower()
    elif user_choice == 2 :
        lucky_unicorn()
    else :
        print('Goodbye!')
        quit()

#main routine
while True :
    menu()
