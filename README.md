# tictactoe

Tic Tac Toe
1.
Write a function print_board() that just prints the empty board:
| |
-----
| |
-----
| |
Next, we have to think about how to store the state of the game (the location of
X’s and O’s). You can use a nested list:
board = [['', '', ''], ['', '', ''], ['', '', '']]
The outer list represents the three rows, so board[0] is the top row, board[2]
the bottom row. board[0][0] is the left field in the top row, board[1][2] the
right field of the middle row.
2.
Add an argument board to the function, so you have print_board(board).
This should now print the board.
board = [['X', 'O', 'X'], ['', 'X', 'O'], ['', 'X', 'O']]
print_board(board)
prints this:
X|O|X
-----
|X|O
-----
|X|O
3.
Write a function check_board(board). It should check if a player has won. It
should return "X", "O", or "" (X won, O won, or nobody won yet).
board = [['X', '', ''], ['', 'X', ''], ['O', 'O', 'X']]
winner = check_board(board)
print(winner)
should print X.
1
4.
Write a function make_move(board, symbol). It should ask the user to type
two numbers in the terminal: The row and column index for the next move.
You can use the function input() for that. You can find more information here:
https://www.w3schools.com/python/ref_func_input.asp
If the input is invalid (e.g. the field is not empty, or the indices are not 0, 1, or
2), ask for input again. You can use a while loop for that.
Example:
board = [['', '', ''], ['', '', ''], ['', '', '']]
make_move(board, "X")
# program prints "please enter the row index"
# user types "0" and presses Enter
# program prints "please enter the column index"
# user types "1" and presses Enter
print(board)
prints this:
[['', 'X', ''], ['', '', ''], ['', '', '']]
And
print_board(board)
prints this:
|X|
-----
| |
-----
| |
5.
Now, you can combine everything. Start with an empty board, then do the
following until one player won or the board is full (X starts):
• print the board
• let the next player make a move
• check if a player has won
• check if the board is full (after 9 moves)
Lastly, print the outcome of the game.
2
