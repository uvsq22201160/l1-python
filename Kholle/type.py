import random as rd

def Ordre():
    a, b = int(input("Saisir une valeur a")), int(input("Saisir une valeur b"))
    if a < b:
        a, b = b, a

    return a, b

def Diviseur():
    a = "Ne divise pas"
    nbre_aleatoire = rd.randint(10, 99)
    nbre_utilisateur = int(input("Saisir un nombre à un chiffre : "))
    if nbre_utilisateur > 1 and (nbre_aleatoire % nbre_utilisateur) == 0:
        a = "Diviseur"

    return a
   
def Permutation(var1, var2):
    if var1 * var2 > 0:
        var1, var2 = var2, var1
    else:
        var1, var2 = var1 ** var2, var1 * var2
    return var1, var2

def PGCD(a,b):
    pgcd = 1
    i = 1
    if a >= b:
        while i < a:
            if (a % i == 0) and (b % i == 0):
                pgcd = i
            i += 1
    else:
        while i < b:
            if (a % i == 0) and (b % i == 0):
                pgcd = i
            i += 1

    return pgcd


def Somme():
    x = int(input("Saisir un entier :\n"))
    somme = 0
    nombre = 0
    nombre_sup100 = 0
    while x >= 0:
        somme += x
        nombre += 1
        if x > 100:
            nombre_sup100 += 1
        x = int(input("Saisir un entier :\n"))

    return somme, nombre, nombre_sup100

def Divisible_par2():
    '''Calcul le nombre de fois de suite que l'entier donné est divisible par deux'''
    x = int(input("Saisir un entier :\n"))
    divisible = 0
    while x % 2 == 0:
        divisible += 1
        x = int(x / 2)

    return divisible

def Diviseurs():
    '''Diviseur propre d'un entier strictement supérieur à 1'''
    x = int(input("Saisir un entier strictement supérieur à 1 :\n"))
    diviseur_liste = [] #liste de tous les divisuers du nombre donné
    verif = 0 #permettra de vérifier si le nombre possède un diviseur, et dans le cas contraire pouvoir afficher qu'il est un nombre premier

    while x < 1: #vérifie que le nombre est bien strictement supérieur à 1
        x = int(input("Veuillez saisir un entier strictement supérieur à 1 :\n"))

    for i in range(2, x): 
        if x % i == 0:
            diviseur_liste.append(i)
            verif += 1

    if verif >= 1:
        print("Les diviseurs de", x, "sont :", Liste_into_number(diviseur_liste))
    else:
        print(x, "est donc une nombre premier")

def Liste_into_number(x):
    '''Transforme les données d'une liste ou d'un tuple en une chaîne de caractère espacée'''
    a = ""
    for i in x:
        a += str(i) + " "

    return a

def hauteurParcourue(nb_marche, h_marche):
    metre = 7 * (5 * 2 * ((h_marche * (10 ** -2)) * nb_marche))
    print("Pour", nb_marche, "marches de", h_marche, "cm, il parcourt", metre,"m par semaine.")

def Longueur():
    nb_marche = int(input("Combien de marches ?\n"))
    h_marche = int(input("Quelle hauteur pour les marches ?\n"))

    return hauteurParcourue(nb_marche, h_marche)