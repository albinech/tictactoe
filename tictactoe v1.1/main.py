import pprint

BOARD = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
val = ''
pos_x = ''
STATE = True
MOVES = 0


def print_board(board):
    print(BOARD[0], "|", BOARD[1], '|', BOARD[2])
    print(BOARD[3], "|", BOARD[4], '|', BOARD[5])
    print(BOARD[6], "|", BOARD[7], '|', BOARD[8])


def input_value(MOVES):
    print('input x or 0 ')
    val = input()
    print('input position of your value to board from 1-9 ')
    pos_x = int(input())

    if pos_x not in range(9):
        input_value()
    else:
        BOARD[pos_x] = val
        print_board(BOARD)
        MOVES += 1
        print(MOVES)

    STATE = False


def continue_game(MOVES):
    if STATE:
        input_value(MOVES)
    check_winner(BOARD)


def check_winner(board):
    if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or \
            board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8]:
        # STATE=True
        print(STATE)
        print('game is ended')
    else:
        continue_game(MOVES)


continue_game(MOVES)
