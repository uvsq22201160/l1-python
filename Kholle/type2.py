import random

#---------------- Exercice 1 ----------------#

def nbEntierSup(liste, entier):
    entier_sup = 0
    for i in range(len(liste)):
        if entier >= liste[i]:
            entier_sup += 1
    return entier_sup

#---------------- Exercice 2 ----------------#

def listeInverse():
    liste = [1+i for i in range(9)]
    x = len(liste)
    for i in range(x):
        print(liste[(x-1)-i], end=" ")

#---------------- Exercice 3 ----------------#

def Diviseur(var1,var2):
    if var1 % var2 == 0:
        return True
    else:
        return False

#---------------- Exercice 4 ----------------#

def Occurence(chaine):
    liste = []
    liste2 = []
    x = 0
    for lettre in chaine:
        x = 0
        for i in range(len(chaine)):
            if lettre == chaine[i]:
                x += 1
        if lettre != " " and not lettre in liste2:
            liste.append([lettre, x])
        liste2.append(lettre)
    return liste

#---------------- Exercice 5 ----------------#

def unQuiBouge():
    liste = [[0]*7 for i in range(7)]
    a, b = random.randint(0,6), random.randint(0,6)
    liste[a][b] = 1
    x, y = random.randint(-1,1), random.randint(-1,1)
    while a < 6 and b < 6:
        while abs(x) == abs(y):
            x, y = random.randint(-1,1), random.randint(-1,1)
        liste[a][b] = 0
        liste[a+x][b+y] = 1
        a, b = a+x, b+y
        print(liste)
    
    print(liste)


#---------------- Exercice 6 ----------------#

def tableMult(n):
    liste = [[0]*(n+2) for x in range(n+2)]
    liste[0][0] = 'x'
    for i in range(2,n+2):
        liste[0][i] = liste[0][i-1] + 1
    for j in range(2,n+2):
        liste[j][0] = liste[j-1][0] + 1
    for k in range(2,n+2):
        for l in range(2,n+2):
            liste[k][l] = (k-1) * (l-1)

    for m in liste:
        print('  '.join([str(n) for n in m]))


#---------------- Crée une fonction qui renvoie si le nombre en parmamètre est premier ----------------#

def Premier(n):
    liste = []
    x = 0
    for i in range(n):
        for j in range(i, n+1):
            if i * j == n:
                liste.append(i)   
    for k in liste:
        x += 1

    if x == 1:
        return True
    else:
        return False

#---------------- Crée une fonction qui supprime les doublons ----------------#

def Doublons(liste):
    dict_liste = set(liste)
    liste_sans_doublons = list(dict_liste)
    return liste_sans_doublons

#---------------- Crée une fonction qui renvoie l'élément le plus fréquent d'une liste ----------------#

def Frequence(liste):
    liste2 = []
    liste3 = []
    for i in liste:
        x = 0
        for j in range(len(liste)):
            if i == liste[j]:
                x += 1
        if not i in liste3:
            liste2.append([i, x+1])
        liste3.append(i)
    
    chiffre = liste2[0][0]
    for k in range(len(liste2)):
        if liste2[k][1] > liste2[k-1][1]:
            chiffre = liste2[k][0]
        elif liste2[k][1] == liste2[k-1][1]:
            if liste2[k][0] > liste2[k-1][0]:
                chiffre = liste2[k][0]
            else:
                chiffre = liste2[k-1][0]
    return chiffre


#---------------- Crée une fonction qui renvoie les chiffres pairs, et les voyelles, d'une liste ----------------#

def Pair(liste):
    liste_pair = []
    voyelles = ['a','e','i','o','u','y']
    for i in liste:
        if type(i) == str:
            if i in voyelles:
                liste_pair.append(i)
        else:
            if i%2==0:
                liste_pair.append(i)
    return liste_pair

print(Pair([2, 'a', 4, 'c', 5, 6, 'f']))


#---------------- Crée une fonction qui renvoie une liste imbriquée de  ----------------#
