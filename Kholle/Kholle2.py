import random

#---------------- Exercice 1 ----------------#
def nombresZero(entier):
    '''  '''
    liste = (str(entier))
    nombre_zero = 0
    for i in liste:
        if i == '0':
            nombre_zero += 1
    return nombre_zero


#---------------- Exercice 2 ----------------#
def Liste(n):
    '''  '''
    liste = []
    for i in range(n):
        a = random.randint(1,99)
        liste.append(a)
    return liste

def Aleatoire(liste):
    a = random.randint(1,99)
    if a in liste:
        for i in range(len(liste)):
            liste[i] -= a
        return liste
    
    else:
        liste2 = []
        liste3 = []
        proche_plus_petit = liste[0]
        proche_plus_grand = liste[0]
        for i in range(len(liste)):
            for j in range(99):
                if (liste[i]-j) == a:
                    liste2.append([liste[i],j])
        for k in range(len(liste2)):
            if liste2[k][1]<liste2[k-1][1]:
                proche_plus_grand = liste2[k][0]

        for l in range(len(liste)):
            for m in range(99):
                if (liste[l]+m) == a:
                    liste3.append([liste[l],m])
        for n in range(len(liste3)):
            if liste3[n][1]<liste3[n-1][1]:
                proche_plus_petit = liste3[k][0]


        return liste, proche_plus_grand, proche_plus_petit, a

liste = Liste(4)

print(Aleatoire(liste))