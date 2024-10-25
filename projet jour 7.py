grille = [" " for x in range(10)]  # Tic Tac Toe


def montre():
    print(" " + grille[1] + " " + "|" + " " + grille[2] + " " + "|" + " " + grille[3])
    print('----------')
    print(" " + grille[4] + " " + "|" + " " + grille[5] + " " + "|" + " " + grille[6])
    print('----------')
    print(" " + grille[7] + " " + "|" + " " + grille[8] + " " + "|" + " " + grille[9])


def lettremettre(lettre, position):
    grille[position] = lettre


def joueur_input():
    joueur = 'X'
    for i in range(9):
        montre()
        print(f"Joueur {joueur}, choisissez une position (1-9): ")
        position = int(input())


        while position < 1 or position > 9 or grille[position] != " ":
            print("Position invalide. Choisissez une autre position (1-9): ")
            position = int(input())

        lettremettre(joueur, position)


        if (grille[1] == grille[2] == grille[3] != " " or
                grille[4] == grille[5] == grille[6] != " " or
                grille[7] == grille[8] == grille[9] != " " or
                grille[1] == grille[4] == grille[7] != " " or
                grille[2] == grille[5] == grille[8] != " " or
                grille[3] == grille[6] == grille[9] != " " or
                grille[1] == grille[5] == grille[9] != " " or
                grille[3] == grille[5] == grille[7] != " "):
            montre()
            print(f"Le joueur {joueur} a gagné!")
            return

        joueur = 'O' if joueur == 'X' else 'X'

    montre()
    print("Egalité!")


montre()
joueur_input()

