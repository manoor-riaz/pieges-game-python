from fltk import *
from Version1 import *
from acceuil import *
#GHANEM ZAHRA, RIAZ MANOOR ET RANIA BERGERON

def dessiner_plateau():
    """
    Dessine un plateau avec des cases blanches avec nb_colonnes et nb_lignes
    Paramètres : aucun
    Valeur de retour : aucune 
    """
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            x1 = j * largeur_case
            y1 = i * hauteur_case
            x2 = x1 + largeur_case
            y2 = y1 + hauteur_case
            est_bordure = i == 0 or i == nb_lignes - 1 or j == 0 or j == nb_colonnes - 1
            if est_bordure:
                polygone([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], remplissage='white', epaisseur=1)
                bordures.append((x1, y1, x2, y2))
            else:
                rectangle(x1, y1, x2, y2, remplissage='white', epaisseur=1)
               
               
def est_dans_plateau(x, y):
    """
    Vérifie si les deux entiers sont bien compris dans le plateau
    Paramètres :
      - x (int) : un entier
      - y (int) : un entier
    Valeur de retour :
      - True ou False
    
    """
    return 0 < x < (nb_colonnes - 1) * largeur_case and 0 < y < (nb_lignes - 1) * hauteur_case


def placer_billes(grille):
    """
    Place les billes dans les cases du plateau en vérifiant que ce ne soit ni une tirette, ni un trou
    et qu'il n'y ait pas déjà une bille placée dans la case .
    Paramètres :
      - grille (list) : une liste   
    Valeur de retour : Aucune 
    """
    for i in range(5):
        for i in range(len(lst_joueurs)):
            x, y = attend_clic_gauche()
            if est_dans_plateau(x, y):
                ligne = int(y // hauteur_case)
                colonne = int(x // largeur_case)
                est_bordure = (ligne == 0 or ligne == nb_lignes - 1 or colonne == 0 or colonne == nb_colonnes - 1)
                est_trou = est_dans_trou(ligne,colonne,liste_tuples_trous(grille))
                bille_placée = (ligne,colonne) in billes_placées
                if not est_bordure and not est_trou and not bille_placée :
                    centre_x = (colonne + 0.5) * largeur_case
                    centre_y = (ligne + 0.5) * hauteur_case
                    cercle(centre_x, centre_y, hauteur_case * 0.4 , remplissage=lst_joueurs[i])
                    billes_placées.append((ligne,colonne))
                    grille_initiale[ligne-1][colonne-1] = lst_joueurs[i]


def est_dans_trou(ligne,colonne,liste):
    """
    Vérifie si la case dans laquelle l'utilisateur a cliqué est un trou
    Paramètres :
      - ligne (int)
      - colonne (int)
      - liste (list)
    Valeur de retour : True ou False
    """
    return (ligne-1,colonne-1) in liste
    

def bordure():
    """
    Dessine un cercle rose ou jaune dans les cases du bord du plateau
    (qui représente les tirettes), des cercles roses sur les bordures du haut et
    du bas et jaunes pour les bordures à droite et à gauche.
    Sans paramètres et sans valeur de retour
    """
    for bordure in bordures:
        x1, y1, x2, y2 = bordure
        centre_x = (x1 + x2) / 2
        centre_y = (y1 + y2) / 2
        if (x1, y1, x2, y2) in bordures[9:23:2] or (x1, y1, x2, y2) in bordures[10:24:2]:
            cercle(centre_x, centre_y, hauteur_case * 0.4 , remplissage='yellow')
        elif (x1, y1, x2, y2) in bordures[1:8] or (x1, y1, x2, y2) in bordures[24:31] :
            cercle(centre_x, centre_y, hauteur_case * 0.4 , remplissage='pink')
            

def liste_tuples_trous(grille):
    """
    Récupère le tuple (i,j) correspondant aux coordonnées des cases qui sont des trous.
    Paramètres :
      - grille (list) : une liste
    Valeur de retour :
      - lst (list) : une liste
    """
    lst = []
    for i in range(7):
        for j in range(7):
            if grille[i][j] == 'trou':
                lst.append((i,j))
    return lst
        

def dessiner_tirettes_trous(grille_init):
    """
    Colorie les cases du plateau en fonction de si il y a un trou dans le plateau de tirettes verticales
    et/ou horizontales. La case est grise si le trou est présent au même endroit dans les deux plateaux,
    rose si il est présent seulement dans le plateau de tirettes verticales et jaune pour les trous du
    plateau de tirettes horizontales
    Paramètres :
     - grille_init (list) : une liste de lsites
     Valeur de retour : None
    """
    for i in range(7):
        for j in range(7):
            x1 = largeur_case + j*largeur_case
            y1 = hauteur_case + i*hauteur_case 
            x2 = x1 + hauteur_case
            y2 = y1 + largeur_case
            if grille_init[i][j] == "trou" :
                rectangle(x1, y1, x2, y2, remplissage='grey', epaisseur=1)
            elif grille_init[i][j] == "hor" :
                rectangle(x1, y1, x2, y2, remplissage='yellow', epaisseur=1)
            else:
                rectangle(x1, y1, x2, y2, remplissage='pink', epaisseur=1)


def jouer_coup(lstTirettesHor,lstTirettesVer):
    """
    Permet de tirer sur les tirettes ainsi de décaler les éléments de gauche à droite,
    de droite à gauche, du bas vers le haut ou du haut vers le bas selon la tirette sur laquelle le joueur va cliquer.
    Paramètres :
      - lstTirettesHor (list) : une liste
      - lstTirettesVer (list) : une liste
    Valeur de retour : rien
    """
    x, y = attend_clic_gauche()
    lst_tirettes = bordures[1:8] + bordures[24:31] + bordures[9:23:2] + bordures[10:24:2]
    for bordure in lst_tirettes:
        if bordure[0] < x < bordure[2] and bordure[1] < y < bordure[3]:
            ligne = int(y // hauteur_case)
            colonne = int(x // largeur_case)
            if ligne == 0 :
                lst3 = decale_gauche(lstTirettesVer[colonne-1])
                lstTirettesVer[colonne-1] = lst3
            elif colonne == 0 :
                lst2 = decale_gauche(lstTirettesHor[ligne-1])
                lstTirettesHor[ligne-1] = lst2                                
            elif ligne == 8 :
                lst4 = decale_droite(lstTirettesVer[colonne-1])
                lstTirettesVer[colonne-1] = lst4    
            else :
                lst1 = decale_droite(lstTirettesHor[ligne-1])
                lstTirettesHor[ligne-1] = lst1                 
                    
 
def mise(grille_init):
    """
    Met à jour la grille
    Paramètres :
      - grille_init (list) : une liste
    """
    for i in range(7):
        for j in range(7):
            x1 = largeur_case + j*largeur_case
            y1 = hauteur_case + i*hauteur_case 
            x2 = x1 + hauteur_case
            y2 = y1 + largeur_case
            if grille_init[i][j] == 'hor':
                rectangle(x1, y1, x2, y2, remplissage='yellow', epaisseur=1)
            elif grille_init[i][j] == 'ver':
                rectangle(x1, y1, x2, y2, remplissage='pink', epaisseur=1)
            elif grille_init[i][j] == 'trou':
                rectangle(x1, y1, x2, y2, remplissage='grey', epaisseur=1)
                
   
if __name__ == '__main__':
    taille_fenetre = 500
    cree_fenetre(taille_fenetre, taille_fenetre)
    nb = menu()
    lst_joueurs = couleur(nb)
    largeur_case,hauteur_case =50,50
    nb_lignes,nb_colonnes = 9,9
    bordures = []
    billes_placées = []
    cercles_dessines = []
    dessiner_plateau()
    grille_tirettes_horizontales,grille_tirettes_verticales,grille_initiale = init_grille(7),init_grille(7),init_grille(7)
    trous(grille_tirettes_horizontales)
    trous(grille_tirettes_verticales)
    vrais_trous(grille_tirettes_horizontales,grille_tirettes_verticales,grille_initiale)
    lst = liste_tuples_trous(grille_initiale)
    dessiner_tirettes_trous(grille_initiale)
    bordure()
    placer_billes(grille_initiale)
    affiche_grille(grille_initiale)
    gagnerPièges = False     
    while not gagnerPièges :
        for joueur in lst_joueurs:
            jouer_coup(grille_tirettes_horizontales,grille_tirettes_verticales)
            lst2 = mettre_à_jour(grille_tirettes_horizontales,grille_tirettes_verticales,grille_initiale)
            grille_initiale = lst2
            mise(grille_initiale)
            if gagne(grille_initiale,joueur):
                gagnerPièges = True
                break      
    attend_fermeture()
    









