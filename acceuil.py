from fltk import *
#GHANEM ZAHRA, RIAZ MANOOR ET RANIA BERGERON

def menu():
    """
    Dessine des rectangles avec le nombre de joueurs puis renvoie
    le nombre de joueurs
    Paramètres : aucun
    Valeur de retour :
      - nb_joueur (int) : le nombre de joueurs
    """
    rectangle(50,50,450,150,remplissage='pink')
    rectangle(50,200,450,300,remplissage='pink')
    rectangle(50,350,450,450,remplissage='pink')
    texte(190,85,"2 joueurs",couleur='black',taille=18)
    texte(190,235,"3 joueurs",couleur='black',taille=18)
    texte(190,385,"4 joueurs",couleur='black',taille=18)
    x,y=attend_clic_gauche()
    nb_joueur = 0
    while nb_joueur not in [2,3,4]:
        if 50<x<450 and 50<y<150:
             nb_joueur=2
             efface_tout()  
        elif 50<x<450 and 200<y<300:
             nb_joueur=3
             efface_tout()
        elif 50<x<450 and 350<y<450:
             nb_joueur=4
             efface_tout()
    return nb_joueur




def couleur(nb_joueur):
    """
    Permet à chaque joueurs de choisir une couleur puis renvoie le nombre de joueurs
    Paramètres : aucun
    Valeur de retour :
      - lst_joueurs (list) : une liste
    """
    lst_joueurs = []
    texte(150, 250, "Choisis ta couleur", couleur='black', taille=18)

    if nb_joueur == 2:
        r1 = rectangle(50,50,150,150, remplissage='blue', epaisseur=1)
        r2 = rectangle(350,350,450,450, remplissage='red', epaisseur=1)
    elif nb_joueur == 3:
        r1 = rectangle(50,50,150,150, remplissage='blue', epaisseur=1)
        r2 = rectangle(350,350,450,450, remplissage='red', epaisseur=1)
        r3 = rectangle(350,50,450,150, remplissage='green', epaisseur=1)
    else:
        r1 = rectangle(50,50,150,150, remplissage='blue', epaisseur=1)
        r2 = rectangle(350,350,450,450, remplissage='red', epaisseur=1)
        r3 = rectangle(350,50,450,150, remplissage='green', epaisseur=1)
        r4 = rectangle(50,350,150,450, remplissage='purple', epaisseur=1)
    i = 0
    while i < nb_joueur:
        x, y = attend_clic_gauche()
        if nb_joueur == 2 :
            if 50 < x < 150 and 50 < y < 150 and 'blue' not in lst_joueurs:
                efface(r1)
                lst_joueurs.append('blue')
            elif 350 < x < 450 and 350 < y < 450 and 'red' not in lst_joueurs:
                efface(r2)
                lst_joueurs.append('red')
            else:
                i -= 1
            i += 1
        elif nb_joueur == 3 :
            if 50 < x < 150 and 50 < y < 150 and 'blue' not in lst_joueurs:
                efface(r1)
                lst_joueurs.append('blue')
            elif 350 < x < 450 and 350 < y < 450 and 'red' not in lst_joueurs:
                efface(r2)
                lst_joueurs.append('red')
            elif 350 < x < 450 and 50 < y < 150 and 'green' not in lst_joueurs:
                efface(r3)
                lst_joueurs.append('green')
            else:
                i -= 1
            i += 1           
        else:
            if 50 < x < 150 and 50 < y < 150 and 'blue' not in lst_joueurs:
                efface(r1)
                lst_joueurs.append('blue')
            elif 50 < x < 150 and 350 < y < 450 and 'purple' not in lst_joueurs:
                efface(r4)
                lst_joueurs.append('purple')
            elif 350 < x < 450 and 50 < y < 150 and 'green' not in lst_joueurs:
                efface(r3)
                lst_joueurs.append('green')
            elif 350 < x < 450 and 350 < y < 450 and 'red' not in lst_joueurs:
                efface(r2)
                lst_joueurs.append('red')
            else:
                i -= 1
            i += 1                
    efface_tout()
    return lst_joueurs



