def display_board(board):
    print('\n'*100)
    print(' ' + ' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ')
    print(' ' + board[7] + ' ' + '|' + ' ' + board[8] + ' ' + '|' + ' ' + board[9])
    print(' ' + ' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ')
    print('-----------')
    print(' ' + ' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ')
    print(' ' + board[4] + ' ' + '|' + ' ' + board[5] + ' ' + '|' + ' ' + board[6])
    print(' ' + ' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ')
    print('-----------')
    print(' ' + ' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ')
    print(' ' + board[1] + ' ' + '|' + ' ' + board[2] + ' ' + '|' + ' ' + board[3])
    print(' ' + ' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ')

def player_input():
    marker=''
    while marker != 'X' and marker !='O':
        marker = input("Player 1 What Do you want to be 'X' or 'O':").upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,mark):
    return ((board[1]==board[2]==board[3]==mark)or(board[4]==board[5]==board[6]==mark)or(board[7]==board[8]==board[9]==mark)or
        (board[7]==board[4]==board[1]==mark)or(board[8]==board[5]==board[2]==mark)or(board[9]==board[6]==board[3]==mark)or
        (board[9]==board[5]==board[1]==mark)or(board[7]==board[5]==board[3]==mark))

import random
def choose_first():
    if random.randint(0,1)==0:
        return 'player 2'
    else:
        return 'player 2'

def space_check(board,position):
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("Enter the next position :(1-9)"))
    return position

def replay():
    return input("Do you want to play again? 'yes' or 'no'").lower().startswith('y')

print("WELCOME to the game TIC TAC TOE")
while True :
    gboard= [" "]*10
    player_1_marker,player_2_marker=player_input()
    turn=choose_first()
    print(turn+"will go first")
    play_game=input("Are you ready to play game? 'yes' or 'no':")
    if play_game.lower()[0]=='y':
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn=='player 1':
            display_board(gboard)
            print("Player 1 turn")
            position=player_choice(gboard)
            place_marker(gboard,player_1_marker,position)
            if win_check(gboard,player_1_marker):
                display_board(gboard)
                print("player 1 Win!!")
                game_on=False
            elif full_board_check(gboard):
                display_board(gboard)
                print("Match draw!!")
                game_on=False
            else:
                turn='player 2'
        else :
            display_board(gboard)
            print("Player 2 turn")
            position = player_choice(gboard)
            place_marker(gboard, player_2_marker, position)
            if win_check(gboard, player_2_marker):
                display_board(gboard)
                print("player 2 Win!!")
                game_on = False
            elif full_board_check(gboard):
                display_board(gboard)
                print("Match draw!!")
                game_on = False
            else:
                turn = 'player 1'


    if not replay():
        print("Thanks for playing the game ,Hope you enjoyed it!")
        break

