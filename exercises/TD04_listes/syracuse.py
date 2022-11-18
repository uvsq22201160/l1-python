def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste = [n]
    i = 0
    while liste[i] != 1:
        if liste[i] % 2 == 0:
            liste.append(liste[i]//2)
            i += 1
        else:
            liste.append(liste[i]*3 + 1)
            i += 1
    return liste

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 1 à n_max """
    liste = syracuse(n_max)
    Conjecture = False
    if liste[len(liste) - 1] == 1:
        Conjecture = True
    else:
        Conjecture = False

    return Conjecture

def tempsVol(n):
    """ Retourne le temps de vol de n """
    liste = syracuse(n)
    temps = len(liste) - 1
    return temps

def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    liste_temps = []
    for i in range(n_max):
        liste_temps.append(tempsVol(i + 1))
    return liste_temps

def tempsVolMax(n):
    ''' Retourne le vol possedant le temps maximal des vols de 1 à n '''
    max = 0
    vol = 0
    liste = tempsVolListe(n)
    for i in range(n):
        if liste[i] > max:
            max = liste[i]
            vol = i +1
    return vol, max


def altitude(n):
    ''' Retourne l'altitude maximale d'un vol '''
    liste = syracuse(n)
    max = 0
    for i in range(len(liste)):
        if liste[i] > max:
            max = liste[i]
    return max

def altitudeVol(n_max):
    ''' Retourne les altitudes maximales des vols de 1 à n_max'''
    liste_altitude = []
    for i in range(n_max):
        liste_altitude.append(altitude(i + 1))
    return liste_altitude

def altitudeVolMax(n):
    '''Retourne le vol possedant l'altitude maximale des vols de 1 à n '''
    liste = altitudeVol(n)
    max = 0
    for i in range(n):
        if liste[i] > max:
            max = liste[i]
            vol = i + 1
    return vol, max

