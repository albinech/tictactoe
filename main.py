board = [['x', '', ''], ['', '', ''], ['', '', '']]


def print_board():
    for i in range(3):
        for j in range(3):
            print("|", board[i][j], "|", end="")
        print("\n", "__________")


print_board()
