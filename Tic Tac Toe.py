# Ici, il s'agit de créer une liste "board", composée de 9 index qui correspond à notre futur plateau de jeu.
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

"""L'usage de la fonction 'print_board' permet d'afficher la liste 'board' sur 3 lignes distinctes afin de composer notre plateau de jeu.
Cela nous permettra d'éviter de répéter les trois lignes print dans le futur. Il nous suffira d'appeler notre fonction print_board."""
def print_board():
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

# Ici, nous définissons le joueur actuel en utilisant la variable "current_player". De ce fait, le joueur qui commence sera toujours le joueur "X".
current_player = "X" 

"""Par cette fonction alternate_player, nous faisons en sorte qu'à chaque fois que le joueur "X" joue, la fonction retournera 'O'.
L'usage du else nous permet d'appliquer cette même fonction en sens inverse. Cela revient à écrire : si le current_player est 'O', 
la fonction retournera 'X'.
Nous aurions pu écrire : if current_player == 'X' return 'O' elif current_player == 'O' return 'X'."""
def alternate_player(current_player):
    return "O" if current_player == "X" else "X"

"""En utilisant une boucle for, nous limitons la partie à une répétions de 9 tours maximum.
Au sein de cette boucle, nous appelerons simplement les différentes fonctions créées précédemment afin de construire le 'game play',
et nous mettrons en place des conditions afin de stopper la boucle et de finir la partie."""
for turn in range(9):

    print_board()  # Premièrement, nous voulons à chaque début de tour afficher le plateau de jeu
    
    """Nous mettons en place un input qui correspond à une variable nommée 'new_value' et qui permettre au joueur actuel
    de choisir son coup sur le plateau en écrivant sa position sur la liste 'board'."""
    new_value = int(input(f"Player {current_player} choose your move (1-9): "))
    
    """A partir de là, si la valeur saisie par l'utilisateur est bien comprise entre 1 et 9, et que cette nouvelle valeur -1
    correspond bien à une case vide sur notre plateau, alors cette valeur correspondant à l'index choisi dans la liste 'board'
    sera remplacée par la variable 'current_player', soit 'X' ou 'O'."""
    if 1 <= new_value <= 9 and board[new_value - 1] == " ":
        board[new_value - 1] = current_player
    else:
        print("Invalid move, try again.")  # Si la 'new_value' saisie par l'utilisateur ne répond pas à ces deux conditions, nous afficherons ce print.
        continue  #Si le print précedent s'affiche, alors le joueur pourra de nouveau saisir son coup.

    """Toujours dans cette boucle, si durant les neuf tours, les valeurs des index cités ci-dessous sont égaux entre eux,
    et qu'il ne s'agit effectivement pas d'une case vide, alors il s'agira d'une victoire pour le 'current_player'.
    Egalement, si plus aucune case vide n'est présente sur le tableau, il s'agira d'une fin de partie par égalité."""
    if ((board[0] == board[1] == board[2] != " ") or # Victoire par 1ère ligne horizontale
        (board[3] == board[4] == board[5] != " ") or # Victoire par 2ème ligne horizontale
        (board[6] == board[7] == board[8] != " ") or # Victoire par 3ème ligne horizontale
        (board[0] == board[3] == board[6] != " ") or # Victoire par 1ère colonne
        (board[1] == board[4] == board[7] != " ") or # Victoire par 2ème colonne 
        (board[2] == board[5] == board[8] != " ") or # Victoire par 3ème colonne
        (board[0] == board[4] == board[8] != " ") or # Victoire par diagonale
        (board[2] == board[4] == board[6] != " ")):  # Victoire par diagonale
        print_board()                                # Affichage du plateau final
        print(f"Player {current_player} wins!")      # Affichage du vainqueur
        break                                        # Rupture de la boucle, le jeu se termine

    if " " not in board:           # L'égalité sera prise en compte si aucune case vide n'est plus présente sur le plateau
        print_board()              # Dans ce cas, nous afficherons le tableau final
        print("It's a draw !")     # Le message d'égalité s'affichera
        break                      # La boucle, et par la même la partie, prendra fin

    """A la fin de notre boucle, donc d'un tour, nous appelons la fonction 'alternate_player' afin de changer le symbole qui sera
    assigné sur le tableau lors du prochain tour."""
    current_player = alternate_player(current_player)