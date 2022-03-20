# import find_position as f_p
#
#
# board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
#
#
# def print_board(board):
#     for i in range(3):
#         for j in range(3):
#             print("|", board[i][j], "|", end="")
#         print("\n", "_____________")
#
#
# print_board(board)
#
# winner = "1"
#
#
# def check_board(board, winner):
#     if board[0][0] == board[0][1] == board[0][2] \
#             or board[1][0] == board[1][1] == board[1][2] \
#             or board[2][0] == board[2][1] == board[2][2] \
#             or board[0][0] == board[1][0] == board[2][0] \
#             or board[0][1] == board[1][1] == board[2][1] \
#             or board[2][0] == board[1][2] == board[2][2] \
#             or board[0][0] == board[1][1] == board[2][2] \
#             or board[0][2] == board[1][1] == board[2][0] \
#             :
#         print(winner)
#     else:
#         print("error")
#
#
# check_board(board,winner)
#
#
# def enter_valid_value():
#     print("enter valid value on valid position : ")
#     new_position=input()
#
#
# def check_pos(position, board,value):
#     print((f_p.find_position(position,board)))
#     posx,posy=(f_p.find_position(position,board))
#     posx=int(posx)
#     posy=int(posy)
#     print(posx, type(posx),posy,type(posy))
#     print('-----------')
#     print(board[posx][posy])
#     if board[posx][posy] != "x" or board[posx][posy] != "0":
#         board[posx][posy]=value
#     else:
#         enter_valid_value()
#     print(board)
#
#
# check_pos('5',[['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']],value='z')
#
#
# def make_move(position, board):
#     if position not in range(9):
#         print("enter valid position")
#     else:
#         check_pos(position,board)
