from itertools import combinations

game_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
players_turn = "X"
WINNING_COMBINATION = [
    (0, 1, 2), (0, 0, 0),
    (1, 1, 1), (2, 2, 2), (2, 1, 0)
    ]

def print_board(board: list):
    counter = 1
    for item in board:
        print(f"  {item[0]}  |  {item[1]}  |  {item[2]}  ")
        if counter < len(item):
            print("-----------------")
        counter = counter + 1

def check_board(board: list, current_player: str):
    x_positions = []
    for item in board:
        x_position = []
        for tic in item:
            try:
                if not x_position:
                    x_index = item.index(current_player)
                else:
                    x_index = item.index(current_player, int(x_position[-1]) + 1)
                x_position.append(x_index)
            except ValueError:
                pass
        x_positions.append(x_position)
    winning = [x for tic in x_positions for x in tic]

    winning = combinations(winning, 3)
    winning = list(winning)
    winner = ""
    for win in WINNING_COMBINATION:
        if win in winning:
            print(f"{current_player} won")
            winner = current_player
            return False
    return True

def make_move(row: int, column: int):
    global current_turn
    row = row - 1
    column = column - 1
    if game_board[row][column] == " ":
        game_board[row][column] = players_turn
        return True
    print("\nInvalid Movement please choose another move\n")
    return False
print_board(game_board)
while True:
    row = int(input("Please enter the row index:  "))
    column = int(input("Please enter the column index:  "))
    if column < 1 or column > 3 or row < 1 or row > 3:
        print("Invalid row or column please enter from 1 to 3")
        continue
    game_movement = make_move(row, column)
    print_board(game_board)
    if not check_board(game_board, players_turn):
        break
    if game_movement:
        players_turn = "O" if players_turn == "X" else "X"

