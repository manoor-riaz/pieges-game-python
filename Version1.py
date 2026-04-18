from random import randint
#GHANEM ZAHRA, RIAZ MANOOR ET RANIA BERGERON

def init_grille(n):
    """
    Initialise une grille(liste de listes)
    Paramètres:
      - n (int) : un entier
    Valeur de retour :
      - lst (list) : une liste de listes
    Exemples :
    >>> init_grille(2)
    >>>[[False,False],[False,False]]
    """
    lst = []
    for i in range(n):
        lst2 = []
        for j in range(n):
            lst2.append(False)
        lst.append(lst2)                             
    return lst


def trous(grille):# une fonction à effet de bord
    """
    Place aléatoirement dans la grille des trous qui sont représentés par des 'True'
    Paramètres:
      - grille (list) : une liste de listes
    Effets de bord : modifie la grille
    """
    for j in range(3):
        for i in range(7):
            r = randint(0,6)
            grille[i][r] = True


def decale_droite(liste):
    """
    Décale vers la droite tous les éléments de la liste
    Paramètres :
      - liste (list) : une liste
    Valeur de retour :
      - lst (list) : une liste décalée vers la droite
    >>>decale_droite([False, True, False, False, False, False, True])
    [True, False, True, False, False, False, False]
    """
    lst = [liste[len(liste)-1]]+liste[0:len(liste)-1]
    return lst


def decale_gauche(liste):
    """
    Décale vers la gauche tous les éléments de la liste
    Paramètres :
      - liste (list) : une liste
    Valeur de retour :
      - lst (list) : une liste décalée vers la gauche
    >>>decale_gauche([False, True, False, False, False, False, True])
    [True, False, False, False, False, True, False]
    """    
    lst = liste[1:len(liste)]+[liste[0]]
    return lst


def vrais_trous(lstTirettesHor,lstTirettesVer,grille_init): #fonction à effet de bord
    """
    Vérifie si il y a des trous dans les tirettes verticales et horizontales au même endroit si c'est le cas ,
    il y a un 'trou' qui apparait dans la grille initiale
    Si le trou se trouve uniquement dans la tirette verticale, 'hor' apparait dans la grille initiale
    Si le trou se trouve uniquement dans la tirette horizontale, 'ver' apparait dans la grille initiale
    Paramètres:
      - lstTirettesHor(list)
      - lstTirettesVer(list)
      - grille_init(list)
    Effets de bord : modifie la grille_init
    """
    for i  in range(7):
        for j in range(7):
            if lstTirettesHor[j][i] and lstTirettesVer[i][j]:
                grille_init[j][i] = 'trou'
            elif lstTirettesVer[i][j] and not(lstTirettesHor[i][j]):
                grille_init[j][i] = 'hor'
            else:
                grille_init[j][i] = 'ver'
            

def placer_une_bille(joueur,grille,i,j):#fonction à effet de bord
    """
    Vérifie si l'endroit où le joueur veut placer sa bille n'est pas un trou et remplace le 'ver'
    ou le 'hor' par le nom du joueur
    Paramètres :
      - joueur (str) : son prénom
      - grille (list) : une liste
      - i (int) : un indice
      - j (int) : un indice
    Effets de bord : modifie la grille  
    """
    if grille[i-1][j-1] == 'ver' or grille[i-1][j-1] == 'hor':
        grille[i-1][j-1] = joueur


def placer_les_billes(listeDesJoueurs,grille_init):
    """
    Demande à chaque joueur de la liste chacun à son tour
    de saisir un numéro de ligne et de colonne entre 1 et 7. Fais appel à la fonction placer_bille
    et place la bille dans la case correspondante si c'est possible. Ensuite affiche la grille en
    appelant la fonction affiche_grille
    Paramètres :
      - listeDesJoueurs (list) : la liste des jouers
      - grille_init (list) : une liste de listes
    """
    for i in range(5):
        for joueur in listeDesJoueurs:
            print(f"A ton tour {joueur} de placer ta  bille numéro {i+1} ")
            ligne_tmp = -1
            while ligne_tmp not in ["1","2","3","4","5","6","7"]:
                ligne_tmp = input('ligne : ')
            ligne = int(ligne_tmp)
            colonne_tmp = -1
            while colonne_tmp not in ["1","2","3","4","5","6","7"]:
                colonne_tmp = input('colonne : ')
            colonne = int(colonne_tmp)
            placer_une_bille(joueur,grille_init,ligne,colonne)
            affiche_grille(grille_init)
            
  
def affiche_grille(grille):#fonction qui affiche
    """
    Affiche chaque élément de la ligne de la grille avec des espaces
    et va à la ligne à la fin de chaque ligne.
    Paramètes :
      - grille (list) : une liste de listes
    >>> grille = [[False, False, False, False], [False, False, False, False], [False, False, False]]
    >>> affiche_grille(grille)
    False False False False 
    False False False False 
    False False False False
    """
    for ligne in grille:
        for case in ligne:
            print(case,end=' ')
        print()        


def gagne(grille,joueur):#fonction qui renvoie un bool
    """
    Vérifie si le joueur à gagner ou pas
    Paramètres :
      - grille (list) : une liste de listes
      - joueur (str) : son prénom
    Valeur de retour :
      - True ou False
    >>>gagne([['hor','toto'],['ver',''hor']],'toto')
    True
    >>>gagne([['titi','toto'],['ver',''hor']],'toto')
    False
    """
    for ligne in grille:
        for case in ligne:
            if case != joueur and case != 'trou' and case != 'hor' and case != 'ver':
                return False
    return True


def liste_joueur(nb_joueur):
    """
    Demande un prénom pour chaque joueur
    Paramètres :
      - nb_joueur (int) : le nombre de joueurs
    Valeur de retour :
      - joueurs (list) : une liste de prénoms des joueurs
    >>> liste_joueur(3)
    Entrez le prénom du joueur 1: manoor
    Entrez le prénom du joueur 2:rania 
    Entrez le prénom du joueur 3:zahra
    [' manoor', 'rania ', 'zahra']
    """
    joueurs = []
    for i in range(1,nb_joueur+1):
        prenom = ''
        while prenom == '':
            prenom = input(f"Entrez le prénom du joueur {i}:")
        joueurs.append(prenom)
    return joueurs    


def nb_joueurs():
    """
    Demande à l'utilisateur de saisir le nombre de joueurs
    Paramètres : aucun
    Valeur de retour :
      - nb_joueur (int) : le nombre de joueurs
    >>> nb_joueurs()
    Entrez le nombre de joueurs:9
    Entrez le nombre de joueurs:6
    Entrez le nombre de joueurs:2
    2    
    """
    nb_joueur_tmp = -1
    while nb_joueur_tmp not in ["2","3","4"]:   
        nb_joueur_tmp = input('Entrez le nombre de joueurs:')
    nb_joueur = int(nb_joueur_tmp) 
    return nb_joueur 
    

def jouer():
    """
    Demande à l'utilisateur la façon de décaler les tirettes
    et modifie la grille horizontale et la grille verticale
    Paramètres : aucun
    Valeur de retour : aucune
    """
    global grille_tirettes_horizontales
    global grille_tirettes_verticales
    HorVer = "toto"
    while HorVer != "Horizontale" and HorVer != "Verticale":
        HorVer = input('Horizontale ou Verticale[Horizontale/Verticale]:')
    if HorVer == "Horizontale":
        n_tmp = -1
        while n_tmp not in ["1","2","3","4","5","6","7"]:
            n_tmp = input('Numéro de ligne :')
        n = int(n_tmp)
        GaucheDroite = "toto"
        while GaucheDroite != "Droite" and GaucheDroite != "Gauche":
            GaucheDroite = input('Droite ou gauche[Droite/Gauche] : ')
        if GaucheDroite == 'Droite':
            lst1 = decale_droite(grille_tirettes_horizontales[n-1])
            grille_tirettes_horizontales[n-1] = lst1
        else:
            lst2 = decale_gauche(grille_tirettes_horizontales[n-1])
            grille_tirettes_horizontales[n-1] = lst2
    else:
        m_tmp = -1
        while m_tmp not in ["1","2","3","4","5","6","7"]:
            m_tmp = input('Numéro de colonne : ')
        m = int(m_tmp)
        HautBas = "toto"
        while HautBas != "Haut" and HautBas != "Bas":
            HautBas = input('Vers le haut ou vers le bas[Haut/Bas] :')
        if HautBas == "Haut":
            lst3 = decale_gauche(grille_tirettes_verticales[m-1])
            grille_tirettes_verticales[m-1] = lst3
        else:        
            lst4 = decale_droite(grille_tirettes_verticales[m-1])
            grille_tirettes_verticales[m-1] = lst4
   
   
def mettre_à_jour(grilleHor,grilleVer,grille_init):
    """
    Met à jour la grille initiale en vérifiant si il y a des trous ou pas dans la grille de tirettes verticales ou
    horizontales
    Paramètres :
      - grilleHor (list) : la grille des tirettes horizontales
      - grilleVer (list) : la grille des tirettes verticales
      - grille_init (list) : la grille initile
    Valeur de retour :
      - lst (list) : liste
    """
    lst = init_grille(7)
    for i in range(7):
        for j in range(7):
            if grilleHor[j][i] and grilleVer[i][j]:
                lst[j][i] = 'trou'
            elif grille_init[j][i] != 'ver' and grille_init[j][i] != 'hor' and grille_init[j][i] != "trou":
                lst[j][i] = grille_init[j][i]
            elif grilleVer[i][j] and not(grilleHor[i][j]):
                lst[j][i] = 'hor'
            else:
                lst[j][i] = 'ver'
    return lst            


#programme principal:
if __name__ == '__main__':
    grille_tirettes_horizontales,grille_tirettes_verticales,grille_initiale = init_grille(7),init_grille(7),init_grille(7)
    trous(grille_tirettes_horizontales)
    trous(grille_tirettes_verticales)
    vrais_trous(grille_tirettes_horizontales,grille_tirettes_verticales,grille_initiale)
    affiche_grille(grille_initiale)
    nombre_de_joueurs = nb_joueurs()
    liste_joueurs = liste_joueur(nombre_de_joueurs)
    placer_les_billes(liste_joueurs,grille_initiale)
    gagnePièges = False     
    while not gagnePièges :
        for joueur in liste_joueurs:
            print(f"A ton tour {joueur} de jouer!")
            jouer(grille_tirettes_horizontales,grille_tirettes_verticales)
            lst2 = mettre_à_jour(grille_tirettes_horizontales,grille_tirettes_verticales,grille_initiale)
            grille_initiale = lst2
            affiche_grille(grille_initiale)
            if gagne(grille_initiale,joueur):
                 print(f"bravo joueur{joueur}")
                 gagnePièges = True
                 break
                 
                 
             