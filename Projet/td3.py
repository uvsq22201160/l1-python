import time, calendar

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return temps[0]*86400 + temps[1]*3600 + temps[2]*60 + temps[3]

#temps = (3,23,1,34)
#print(type(temps))
#print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    temps = (seconde//86400, (seconde % 86400) // 3600, (seconde % 3600) // 60, seconde % 60)
    return temps

#temps = secondeEnTemps(100000)
#print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")

#fonction auxiliaire ici

def afficheTemps(temps):
    mot_pluriel = "s"
    Temps = ["jour", "heure", "minute", "seconde"]
    for i in range(4):
        if temps[i] == 0:
            print("", end=" ")
        elif temps[i] > 1:
            print(temps[i], Temps[i] + mot_pluriel, end=" ")
        else:
            print(temps[i], Temps[i], end=" ")

    
#afficheTemps((1,0,14,23)) 

#Demande le temps

def demandeTemps():
    Jour = int(input("nombre de jour(s) : "))
    Heure = int(input("nombre d'heure(s) : "))
    while Heure >= 24:
        Heure = int(input("nombre d'heure(s) PS: moins de 24 : "))
    Minute = int(input("nombre de minute(s) : "))
    while Minute >= 60:
        Minute = int(input("nombre de minute(s) PS: moins de 60 : "))
    Seconde = int(input("nombre de seconde(s) : "))
    while Seconde >= 60:
        Seconde = int(input("nombre de seconde(s) PS: moins de 60 : "))
    
    return (Jour, Heure, Minute, Seconde)

#afficheTemps(demandeTemps())


def sommeTemps(temps1,temps2):
    temps1_seconde, temps2_seconde = tempsEnSeconde(temps1), tempsEnSeconde(temps2)
    temps_total_seconde = temps1_seconde + temps2_seconde

    return secondeEnTemps(temps_total_seconde)

#sommeTemps((2,3,4,25),(5,22,57,1))

def proportionTemps(temps,proportion):
    temps_proportion_seconde = tempsEnSeconde(temps) * proportion

    return secondeEnTemps(temps_proportion_seconde)
    
#afficheTemps(proportionTemps((2,0,36,0),0.2))
'''
def tempsEnDate(temps):
    année = 1970 + (temps[0] // 365)
    mois = (temps[0] % 365) // 31
    jour = 0
    if année % 4 == 0 and not année % 100 == 0:
        if mois == 2:
            mois = (temps[0] % 366) // 29
            jour = temps[0] % mois
        elif (mois % 2 == 0) or mois == 7:
            mois = (temps[0] % 366) // 31
            jour = temps[0] % mois
        else:
            mois = (temps[0] % 366) // 30
            jour = temps[0] % mois
    else:
        if mois == 2:
            mois = (temps[0] % 365) // 28
            jour = temps[0] % mois
        elif (mois % 2 == 0) or mois == 7:
            mois = (temps[0] % 365) // 31
            jour = temps[0] % mois
        else:
            mois = (temps[0] % 365) // 30
            jour = temps[0] % mois
    temps_date = (année, mois, jour, temps[1], temps[2], temps[3])
    return temps_date
'''
'''
def afficheDate(date = -1):
    mot_pluriel = "s"
    Mois = ["", "janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
    Temps = ["année", "mois", "jour", "heure", "minute", "seconde"]
    for i in range(6):
        if i == 1:
            print(Mois[date[i]], end=" ")
        elif i == 0:
            print(date[i], end=" ")
        else:
            if date[i] == 0:
                print("", end=" ")
            elif date[i] > 1:
                print(date[i], Temps[i] + mot_pluriel, end=" ")
            else:
                print(date[i], Temps[i], end=" ")
    
'''
def tempsEnDate(temps):
    année = 1970 + (temps[0] // 365)
    jour = temps[0] % 365
    temps_date = (année, jour, temps[1], temps[2], temps[3])
    return temps_date
 
def afficheDate(date = -1):
    mot_pluriel = "s"
    Temps = ["année", "jour", "heure", "minute", "seconde"]
    for i in range(5):
        if date[i] == 0:
            print("", end=" ")
        elif date[i] > 1:
            print(date[i], Temps[i] + mot_pluriel, end=" ")
        else:
            print(date[i], Temps[i], end=" ")
    
 
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
tempsEnDate(temps)
afficheDate(tempsEnDate(temps))
#afficheDate()

def nombreBisextile(jour):
    année = 1970 
    nbre_année_bisextile = 0
    for i in range(jour // 365):
        if année % 4 == 0 and (not année % 100 == 0):
            nbre_année_bisextile += 1
            année += 1
        
    return nbre_année_bisextile

def tempsEnDateBisextile(temps):
    année = 1970 + (temps[0] // 365)
    jour = (temps[0] % 365) 
    jour_bissextile = jour + nombreBisextile(jour)
    temps_date = (année, jour, temps[1], temps[2], temps[3])
    return temps_date
   
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDateBisextile(temps))