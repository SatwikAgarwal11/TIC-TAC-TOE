from IPython.display import clear_output
import random
#create board
#take user input
#player_side
def display_board(board):
    clear_output()
    print(' '+board[7]+" | "+board[8]+" | "+board[9])
    print("-----------")
    print(' '+board[4]+" | "+board[5]+" | "+board[6])
    print("-----------")
    print(' '+board[1]+" | "+board[2]+" | "+board[3])

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1, Do you want to be 'X' or 'O': ").upper()
        if marker == 'X':
            return ('X','O')
        else:
            return('O','x')

def place_marker(board,marker,position):
    board[position] = marker
    display_board(board)

def check_win(board,marker):
    return ((board[7] == marker and board[8] == marker and board[9] == marker)or
            (board[4] == marker and board[5] == marker and board[6] == marker)or
            (board[1] == marker and board[2] == marker and board[3] == marker)or
            (board[1] == marker and board[4] == marker and board[7] == marker)or
            (board[2] == marker and board[5] == marker and board[8] == marker)or
            (board[3] == marker and board[6] == marker and board[9] == marker)or
            (board[7] == marker and board[5] == marker and board[3] == marker)or
            (board[1] == marker and board[5] == marker and board[9] == marker))

def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Enter the position (1-9): "))

    return position

def replay():
    choice = input("Play Again? Y or N: ")

    return choice == 'Y'

print("Welcome to Tic Tac Toe! ")
while True:

    # PLAY THE GAME
    # SET EVERYTHING UP (BOARD, WHOS FIRST, CHOOSE MARKER X,O)

    the_board = [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print( turn + " will be going first")

    play_game = input("Ready to play? Y or N: ")

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    ## GAME PLAY

    while game_on:

        if turn == 'Player 1':
            #CHOOSE BOARD
            display_board(the_board)
            #CHOOSE POSITIONa
            position = player_choice(the_board)
            #PLACE THE MARKER ON THE POSITION
            place_marker(the_board,player1_marker,position)
            
            #CHECK IF THEY WON 
            if check_win(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 has won the game!')
                game_on = False
            
            #CHECK IF THERE IS A TIE
            else: 
                if full_board_check(the_board):
                    display_board(the_board)
                    print('It was a TIE!')
                    game_on = False
            #NO TIE, NO WIN THEN NEXT PLAYER'S TURN
                else:
                    turn = 'Player 2'
    
        ### PLAYER 1 TURN

        else:

            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            if check_win(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 has won the game! ')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It was a TIE! ")
                    game_on = False
                else:
                    turn = 'Player 1'

        ### PLAYER 2 TURN



    if not replay():
        break
    # BREAK OUT OF THE WHILE LOOP