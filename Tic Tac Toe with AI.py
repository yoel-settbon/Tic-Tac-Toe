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

# Function to build the reactions of the IA
def ai_move():
    if board[0] == "X" and board[1] == "X" and board[2] == " ":    # Block lines
        board[2] = "O"
    elif board[1] == "X" and board[2] == "X" and board[0] == " ":
        board[0] = "O"
    elif board[0] == "X" and board[2] == "X" and board[1] == " ":
        board[1] = "O"
    elif board[3] == "X" and board[4] == "X" and board[5] == " ":
        board[5] = "O"
    elif board[4] == "X" and board[5] == "X" and board[3] == " ":
        board[3] = "O"
    elif board[3] == "X" and board[5] == "X" and board[4] == " ":
        board[4] = "O"
    elif board[6] == "X" and board[7] == "X" and board[8] == " ":
        board[8] = "O"
    elif board[7] == "X" and board[8] == "X" and board[6] == " ":
        board[6] = "O"
    elif board[6] == "X" and board[8] == "X" and board[7] == " ":
        board[7] = "O"
    elif board[0] == "X" and board[3] == "X" and board[6] == " ":  # Block columns
        board[6] = "O"
    elif board[3] == "X" and board[6] == "X" and board[0] == " ":
        board[0] = "O"
    elif board[0] == "X" and board[6] == "X" and board[3] == " ":
        board[3] = "O"
    elif board[1] == "X" and board[4] == "X" and board[7] == " ":
        board[7] = "O"
    elif board[4] == "X" and board[7] == "X" and board[1] == " ":
        board[1] = "O"
    elif board[1] == "X" and board[7] == "X" and board[4] == " ":
        board[4] = "O"
    elif board[2] == "X" and board[5] == "X" and board[8] == " ":
        board[8] = "O"
    elif board[5] == "X" and board[8] == "X" and board[2] == " ":
        board[2] = "O"
    elif board[2] == "X" and board[8] == "X" and board[5] == " ":
        board[5] = "O"
    elif board[0] == "X" and board[4] == "X" and board[8] == " ":  # Block diagonals
        board[8] = "O"
    elif board[4] == "X" and board[8] == "X" and board[0] == " ":
        board[0] = "O"
    elif board[0] == "X" and board[8] == "X" and board[4] == " ":
        board[4] = "O"
    elif board[6] == "X" and board[2] == "X" and board[4] == " ":
        board[4] = "O"
    elif board[2] == "X" and board[4] == "X" and board[6] == " ":
        board[6] = "O"
    elif board[6] == "X" and board[4] == "X" and board[2] == " ":
        board[2] = "O"
    else:   # If no possibilities to block, AI will chose the first empty case
        for i in range(len(board)):
            if board[i] == " ":
                board[i] = "O"
                break

# Loop to define the differents turns in the game, with a maximum of 9 turns
for turn in range(9):

    print_board()

    if current_player == "X":
        new_value = int(input(f"Player {current_player} choose your move (1-9): "))-1 # Using "new_value" to chose the player's move
    
        # The different conditions to respect to print the choice of the current player
        if 0 <= new_value <= 8 and board[new_value] == " ":
            board[new_value] = current_player
        else:
            print("Invalid move, try again.")
            continue
    else:
        ai_move()
        print("AI has made it's move")

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