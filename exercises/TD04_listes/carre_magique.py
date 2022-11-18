carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
carre_pas_mag = [list(x) for x in carre_mag]
carre_pas_mag[3][2] = 7

def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for i in carre:
        print(' '.join([str(j) for j in i]))

def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    Somme_ligne = 0
    Somme_liste = [0] * len(carre)
    for i in range(len(carre)): #valeur des colonnes
        Somme_ligne = 0
        for j in range(len(carre)): #valeur des lignes
            Somme_ligne += carre[i][j]
        Somme_liste[i] = Somme_ligne
    somme = Somme_liste[0]
    for k in range(len(Somme_liste)):
        if Somme_liste[k] != somme:
            somme = -1
    return somme

def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    Somme_colonne = 0
    Somme_liste = [0] * len(carre)
    for i in range(len(carre)): #valeur des colonnes
        Somme_colonne = 0
        for j in range(len(carre)): #valeur des lignes
            Somme_colonne += carre[j][i]
        Somme_liste[i] = Somme_colonne
    somme = Somme_liste[0]
    for k in range(len(Somme_liste)):
        if Somme_liste[k] != somme:
            somme = -1
    return somme

def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    Somme_diagonale_1 = 0
    Somme_diagonale_2 = 0
    Somme_liste = [0] * 2
    for i in range(len(carre)):
        Somme_diagonale_1 += carre[i][i]
        Somme_diagonale_2 += carre[len(carre)-i-1][len(carre)-i-1]
    Somme_liste[0], Somme_liste[1] = Somme_diagonale_1, Somme_diagonale_2
    somme = Somme_liste[0]
    if Somme_liste[0] != Somme_liste[1]:
            somme = -1
    return somme

def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    a, b, c = testLignesEgales(carre), testColonnesEgales(carre), testColonnesEgales(carre)
    if a >= 0 and b >= 0 and c >= 0:
        return True
    else:
        return False

def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon """
    ordre = len(carre)
    x = 0 #nombre entre 1 et n^2 présent dans le carré
    for i in range(1, ordre**2 + 1):
        for j in range(ordre):
            if i in carre[j]:
                x += 1
    if x == ordre**2:
        return True
    else:
        return False

print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))

