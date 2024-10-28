board = [" "," "," "," "," "," "," "," "," "]

# Function to print the board
def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])

# Player "X" always begin
current_player = "X"

# Function to alternate players turn after turn, from "X" to "O"
def alternate_player(current_player):
    return "O" if current_player == "X" else "X"

# Loop to define the differents turns in the game, with a maximum of 9 turns
for turn in range(9):

    print_board()
    
    new_value = int(input(f"Player {current_player} choose your move (1-9): ")) # Using "new_value" to chose the player's move
    
    # The different conditions to respect to print the choice of the current player
    if 1 <= new_value <= 9 and board[new_value - 1] == " ":
        board[new_value - 1] = current_player
    else:
        print("Invalid move, try again.")
        continue

    # Conditions to win the game
    if ((board[0] == board[1] == board[2] != " ") or # Victories by lines
        (board[3] == board[4] == board[5] != " ") or
        (board[6] == board[7] == board[8] != " ") or
        (board[0] == board[3] == board[6] != " ") or # Victories by columns
        (board[1] == board[4] == board[7] != " ") or
        (board[2] == board[5] == board[8] != " ") or
        (board[0] == board[4] == board[8] != " ") or # Victories by diagonals
        (board[2] == board[4] == board[6] != " ")):
        print_board()
        print(f"Player {current_player} wins!") # The message if victory
        break

    # Conditions of equality
    if " " not in board:
        print_board()
        print("It's a draw !") # The message if equality
        break

    current_player = alternate_player(current_player) # Changing player at the end of the turn