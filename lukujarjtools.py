# -*- coding: utf-8 -*-
# Tällä saa kahden listan leikkauksen
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


# Poistaa omista kursseista ne, joille löytyy jo ainakin yksi uniikki paikka
def poista_uniikit(list1):
    jaksoja = len(list1[0])
    palkkeja = len(list1)
    u = set()
    for k in range(0, palkkeja):
        for j in range(0, jaksoja):
            if len(list1[k][j]) == 1:
                u = u | set(list1[k][j])
    for k in range(0, palkkeja):
        for j in range(0, jaksoja):
            if len(list1[k][j]) != 1:
                list1[k][j] = list(set(list1[k][j])-u)


def maxlen(list1):
    # Etsii listasta maksimipituisen setin
    jaksoja = len(list1[0])
    palkkeja = len(list1)
    ml = 1
    for k in range(0, palkkeja):
        for j in range(0, jaksoja):
            ml = max(ml, len(list1[k][j]))
    return ml


def tulosta_lukujarj(lista, eiloydy):
    jaksoja = len(lista[0])
    palkkeja = len(lista)
    print(' ' *4, end=' ')
    for j in range(1,palkkeja+1):
        print('{:^6}|'.format(j), end='')
    print('\n', '-' * 60)
    for j in range(0, jaksoja):
        print('{:^4}|'.format(j+1), end='')
        for k in range(0, palkkeja):
            if len(lista[k][j])>0:
                for val in lista[k][j]:
                    print('{:^6}|'.format(val), end='')
            else:
                print(' '*5, '|', end='')
#                print(j, '|', val, '|')
        print()
#        print('\n')
    toistuvat, nahty = toistuvat_kurssit(lista)
    if len(toistuvat) > 0:
        for x in toistuvat:
            print('Huomaa, että kurssi', x, 'esiintyy', nahty[x], 'kertaa, eli nuo paikat ovat vaihtoehtoisia')
    if len(eiloydy) > 0:
        print('En saanut näitä kursseja sopimaan: ', eiloydy)




def onko_kaikki(list1, list2):
    # Tarkistaa tuliko kaikki kurssit mukaan
    if len(list2-set(flatten(list1))) == 0:
        return True
    else:
        return False


def flatten(list1):
    jaksoja = len(list1[0])
    palkkeja = len(list1)

    list2 = []
    for j in range(0, jaksoja):
        for k in range(0, palkkeja):
            if len(list1[k][j]) > 0:
                list2.append(list1[k][j][0])
    return list2


# Etsii palkit, joista löytyy kurssi kurssi, ja sijoittaa siinä palkissa olevien kurssien määrän taulukkoon maara
def etsi_palkit(kaikki, kurssi):
    jaksoja = len(kaikki[0])
    palkkeja = len(kaikki)
    minmaara = 100
    minj = 100
    mink = 100
    maara = [[0 for i in range(0, jaksoja)] for j in range(0, palkkeja)]
    for j in range(0, jaksoja):
        for k in range(0, palkkeja):
            if kurssi in kaikki[k][j]:
                maara[k][j] = len(kaikki[k][j])
                # Löytää pienimmän määrän kursseja
                if maara[k][j] < minmaara:
                    minmaara = maara[k][j]
                    minj = j
                    mink = k
    return maara, minmaara, minj, mink


def etsi_ekajakso(list1, kurssi):
    jaksoja = len(list1[0])
    palkkeja = len(list1)
    for j in range(0, jaksoja):
        for k in range(0, palkkeja):
            if len(intersection(list1[k][j],kurssi)) > 0:
                return j


def etsi_vikajakso(list1, kurssi):
    jaksoja = len(list1[0])
    palkkeja = len(list1)
    for j in range(jaksoja-1, -1, -1):
        for k in range(0, palkkeja):
            if len(intersection(list1[k][j],kurssi)) > 0:
                return j


def poista_kurssi(list1, kurssi, alue):
    palkkeja = len(list1)
    for k in range(0, palkkeja):
        for j in alue:
            if kurssi in list1[k][j]:
            # if len(list1[k][j]) != 1:
                list1[k][j].remove(kurssi) # list(set(list1[k][j])-kurssi)

                
def onko_kurssia(list1, kurssi):
    jaksoja = len(list1[0])
    palkkeja = len(list1)
    for j in range(0, jaksoja):
        for k in range(0, palkkeja):
            if kurssi in list1[k][j]:
                return 0
    return 1
    

def ennakkotietopoisto(kaikki,ennakkotiedot, hiljainen, verbose):
    for x in ennakkotiedot:
        ekajakso1 = etsi_ekajakso(kaikki, x[0])
        ekajakso2 = etsi_ekajakso(kaikki, x[1])
        if ekajakso2 <= ekajakso1:
            if verbose:
                print('Poistin kurssin', x[1], 'jaksosta', ekajakso2+1, 'sillä kurssi', x[0], 'on aikaisintaan jaksossa', ekajakso1+1)
            poista_kurssi(kaikki, x[1], range(0, ekajakso1))
        
        if onko_kurssia(kaikki, x[1]):
            if not hiljainen:
                print('Ongelma: esitietojen järjestämisen jälkeen kurssi', x[1], 'puuttuu!')
            break
        vikajakso1 = etsi_vikajakso(kaikki, x[0])
        vikajakso2 = etsi_vikajakso(kaikki, x[1])
        if vikajakso1 >= vikajakso2:
            if verbose:
                print('Poistin kurssin', x[0], 'jaksosta', vikajakso1+1, 'sillä kurssi', x[1], 'on suoritettava viimeistään jaksossa', vikajakso2+1)
            poista_kurssi(kaikki, x[0], range(vikajakso2,len(kaikki[0])))
        if onko_kurssia(kaikki, x[1]):
            if not hiljainen:
                print('Ongelma: esitietojen järjestämisen jälkeen kurssi', x[1], 'puuttuu!')
            break


def etsi_minimi(sopimattomat, maara):
    # Etsii seuraavan indeksin, jossa suurempi sopimattomien määrä kuin maara
    for j in range(0,len(sopimattomat)):
        if(maara < sopimattomat[j]):
            return j
    return -1


def etsi_minimi2(sopimattomat, maara):
    # Etsii seuraavan indeksin, jossa suurempi sopimattomien määrä kuin maara
    for j in range(0,len(sopimattomat)):
        if(maara <= sopimattomat[j]):
            return j
    return -1


def sekoita(list1):
    from random import shuffle
    jaksoja = len(list1[0])
    palkkeja = len(list1)
    for j in range(0, jaksoja):
        for k in range(0, palkkeja):
            l=list(list1[k][j])
            shuffle(l)
            list1[k][j]=set(l)

            
def onko_eri(flist1, list1, mink, maxk):
    jaksoja = len(list1[0])
    palkkeja = len(list1)
    for k in range(mink, maxk+1):
        if flist1[k] == list1:
            return 0
    return 1


def toistuvat_kurssit(list1):
    nahty = {}
    toistuvat = []

    for row in list1:
        for item in row:
            for x in item:
                if x not in nahty:
                    nahty[x] = 1
                else:
                    if nahty[x] == 1:
                        toistuvat.append(x)
                    nahty[x] += 1
    return toistuvat, nahty
