#------------------ Kholle numéro 1 ------------------#


# Qestion numéro 1 : L'opératur % calcul le reste de la division de deux entiers et l'opérateur // calcul le quotient de la 
#                    division de deux entiers. Par exemple 21 // 2 donnera comme résultat l'entier 10 et 21 % 2 donnera comme 
#                    résultat l'entier 1. Ces deux opérations donne des entiers de type int.



# Programme 1 :

def Remise():
    '''Ce programme permet de calculer le coût total, avec la remise de 10% ou non, pour l'utilisateur.'''
    quantité_unité = int(input("Saisir la quantité en unité (1 unité coûte 100) :\n")) #demande à l'utilisateur la quantité acheté en unité (1 unité coûte 100)
    cout_total = 0 #initialise le cout total
    if quantité_unité >= 10:
        cout_total = (quantité_unité * 100) - int((quantité_unité * 100 * 0.1)) #calcul du coût total avec remise car le coût est >1000
    else:
        cout_total = quantité_unité * 100
    return cout_total
    

# Programme 2 :

def Clair():
    '''Ce programme permet de renvoyer la lettre la plus haute dans une chaine de caractère.'''
    clair = str(input("Saisir une chaine de caractère composée de lettres minuscules :\n")) #demande à l'utilisateur une chaîne de caractère
    lettre_haute = "a" #initalise la lettre la plus haute (modifié plus tard dans la boucle)
    for lettre in clair: 
        if lettre > lettre_haute:
            lettre_haute = lettre #permet d'incrémenter la lettre la plus haute dans la variable qui sera renvoyée
    return lettre_haute

a = Remise()
print(a)

b = Clair()
print(b)
