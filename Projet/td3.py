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

def tempsEnDate(temps):
    année = 1970 + (temps[0] // 365)
    mois = (temps[0] % année) // 31
    jour = 0
    if année % 4 == 0 and not année % 100 == 0:
        if mois == 2:
            mois = (temps[0] % année) // 29
            jour = temps[0] % mois
        elif (mois % 2 == 0) or mois == 7:
            mois = (temps[0] % année) // 30
            jour = temps[0] % mois
        else:
            mois = (temps[0] % année) // 30
            jour = temps[0] % mois
    else:
        if mois == 2:
            mois = (temps[0] % année) // 28
            jour = temps[0] % mois
        elif (mois % 2 == 0) or mois == 7:
            mois = (temps[0] % année) // 30
            jour = temps[0] % mois
        else:
            mois = (temps[0] % année) // 30
            jour = temps[0] % mois
    
    temps_date = (année, mois, jour, temps[1], temps[2], temps[3])
    return temps_date

def afficheDate(date = -1):
    mot_pluriel = "s"
    Mois = ["", "janvier", "février", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "décembre"]
    Temps = ["année", "mois", "jour", "heure", "minute", "seconde"]
    for i in range(6):
        if i == 1:
            print(temps[i], , end=" ")
        elif temps[i] == 0:
            print("", end=" ")
        elif temps[i] > 1:
            print(temps[i], Temps[i] + mot_pluriel, end=" ")
        else:
            print(temps[i], Temps[i], end=" ")
    
    
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
tempsEnDate(temps)
afficheDate(tempsEnDate(temps))
afficheDate()