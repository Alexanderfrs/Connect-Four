from connect_four import *

def random_eval(board):
  return random.randint(-100, 100)

# Chech whether X or O has more streaks going into a direction
def my_evaluate_board(board):
  if has_won(board, "X") == True:
    return float("Inf")
  if has_won(board, "O") == True:
    return -float("Inf")
  x_two_streak = 0
  o_two_streak = 0
  # loop through every space on the board 
  for col in range(len(board) -1):
    for row in range(len(board[0])):
      # check for identical symbol to the right of the present col
      if board[col][row] == "X" and board[col + 1][row] == "X":
        x_two_streak += 1
      if board[col][row] == "O" and board[col + 1][row] == "O":
        o_two_streak += 1
      # check for identical symbol to the left of the present col
      if board[col][row] == "X" and board[col - 1][row] == "X":
        x_two_streak += 1
      if board[col][row] == "O" and board[col - 1][row] == "O":
        o_two_streak += 1
      # check for identical symbol above the present row
      # if board[col][row] == "X" and board[col][row + 1] == "X":
      #   x_two_streak += 1
      # if board[col][row] == "O" and board[col][row + 1] == "O":
      #   o_two_streak += 1
      # check for identical symbol below the present row
      # if board[col][row] == "X" and board[col][row - 1] == "X":
      #   x_two_streak += 1
      # if board[col][row] == "O" and board[col][row - 1] == "O":
      #   o_two_streak += 1
  return x_two_streak - o_two_streak
  
def two_ai_game():
    my_board = make_board()
    while not game_is_over(my_board):
      #The "X" player finds their best move.
      result = minimax(my_board, True, 4, -float("Inf"), float("Inf"), my_evaluate_board)
      print( "X Turn\nX selected ", result[1])
      print(result[1])
      select_space(my_board, result[1], "X")
      print_board(my_board)

      if not game_is_over(my_board):
        #The "O" player finds their best move
        result = minimax(my_board, False, 4, -float("Inf"), float("Inf"), codecademy_evaluate_board)
        print( "O Turn\nO selected ", result[1])
        print(result[1])
        select_space(my_board, result[1], "O")
        print_board(my_board)
    if has_won(my_board, "X"):
        print("X won!")
    elif has_won(my_board, "O"):
        print("O won!")
    else:
        print("It's a tie!")

# Making a few moves on the board
new_board = make_board()
select_space(new_board, 5, "X")
select_space(new_board, 7, "O")
select_space(new_board, 4, "X")
select_space(new_board, 7, "O")

print_board(new_board)

print(my_evaluate_board(new_board))

# Function to let AI's play against each other
two_ai_game()


