def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return (temps[0]*86400 + temps[1]*3600 + temps[2]*60 + temps[3])

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    min = seconde // 60
    seconde %= 60
    heure = min//60
    min %= 60
    jour = heure//24
    heure %= 24
    return (jour, heure, min, seconde)

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

def sommeTemps(temps1, temps2):
    temps1_seconde, temps2_seconde = tempsEnSeconde(temps1), tempsEnSeconde(temps2)
    temps_total_seconde = temps1_seconde + temps2_seconde
    return secondeEnTemps(temps_total_seconde)

def proportionTemps(temps, proportion):
    temps_proportion_seconde = tempsEnSeconde(temps) * proportion
    return secondeEnTemps(temps_proportion_seconde)

def tempsEnDate(temps):
    année = 1970 + (temps[0] // 365)
    temps_date = (année, temps[0] - 365*(temps[0]//365), temps[1], temps[2], temps[3])
    return temps_date
 
def afficheDate(date=-1):
    mot_pluriel = "s"
    Temps = ["année", "jour", "heure", "minute", "seconde"]
    for i in range(5):
        if date[i] == 0:
            print("", end=" ")
        elif date[i] > 1:
            print(date[i], Temps[i] + mot_pluriel, end=" ")
        else:
            print(date[i], Temps[i], end=" ")

def nombreBisextile(jour):
    année = 1970 
    nbre_année_bisextile = 0
    for i in range(jour // 365):
        if (année % 4 == 0 or (année % 400 == 0)) and not année % 100 == 0:
            nbre_année_bisextile += 1
        année += 1  
    return nbre_année_bisextile

def tempsEnDateBisextile(temps):
    jour_total = temps[0]
    année, jour, heure, min, seconde = tempsEnDate(temps)
    temps_date = (année, jour - nombreBisextile(jour_total), heure, min, seconde)
    return temps_date

def verifie(liste_temps):
    semaine = 0
    mois = 0
    verif = 0
    for i in range(4):
        mois = 0
        for j in range(4):
            semaine = liste_temps[i][j]
            mois += semaine
            if semaine > 48:
                print("Surcharge à la semaine", j + 1, "du mois", i + 1)
                verif += 1
        if mois > 140:
            print("Surcharge au mois", i + 1)
            verif += 1
    if verif == 0:
        print("Le nombre d'heure de travail est convenable")


liste_temps = [[1,2,39,34],[0,1,9,4],[0,29,39,20],[0,31,13,20]]
verifie(liste_temps)