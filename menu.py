''' 16/06 code '''
# space for imports
import sys

def menu() :
    ''' menu function'''
    num_choices = 3
    flag = True
    while flag is True :
        print('1: Higher or Lower')
        print('2: Game')
        print('3: Quit')
        try :
            user_choice = int(input('Which game would you like to play?'))
            if user_choice > num_choices or user_choice < 1 :
                print('Error with choice, 1')
            else :
                print(f'You picked option {user_choice}')
                flag = False
        except ValueError :
            print('Error with choice, 2')

    if user_choice == 1 :
        game1()
    elif user_choice == 2 :
        game2()
    else :
        print('Bye')
        sys.exit()

def game1() :
    '''placeholder'''
    print('Game 1')

def game2() : #a
    '''placeholder'''
    print('Game 2')

menu()
