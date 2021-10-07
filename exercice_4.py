# Auteur : Antoine La Boissière
# Date : 1 octobre 2021
#
# Ce programme sert à afficher à la console une grille de tic-tac-toe de taille n

n = 3 # taille du tic-tac-toe
hauteur = n * 3 + 2 # hauteur du tic-tac-toe
largeur = (n * 2) * 3 + 2 # largeur du tic-tac-toe
caractereDesLignes = '#' # caractère utilisé pour afficher le tic-tac-toe
ticTacToe = '' # variable utilisée pour garder en mémoire l'affichage

# Pour chaque ligne qui forme la hauteur
for ligne in range(hauteur):
    # Pour chaque colonne qui forme la largeur
    for colonne in range(largeur):
        # Si la ligne est au 1/3 ou au 2/3 de la hauteur
        if(ligne == (hauteur // 3) or ligne == (hauteur * 2 // 3)):
            ticTacToe += caractereDesLignes
        else:
            # Si la colonne est au 1/3 ou au 2/3 de la largeur
            if(colonne == (largeur // 3) or colonne == (largeur * 2 // 3)):
                ticTacToe += caractereDesLignes
            else:
                ticTacToe += ' '
    # Changement de ligne si ce n'est pas la dernière ligne
    if(ligne < hauteur - 1):
        ticTacToe += '\n'

print(ticTacToe)