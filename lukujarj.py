#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import lukujarjtools as lj
import filehandling as f
import sys, getopt
import time
from random import shuffle
from copy import copy, deepcopy

start = time.time()

jaksoja = 5
palkkeja = 8
yrityksia = 1000
vaihtoehtoja = 4
verbose = 0
hiljainen = 0
ulostulo = "näytölle"
tarjotintiedosto = "kurssitarjotin.csv"
omakurssitiedosto = "omatkurssit.csv"

try:
    opts, args = getopt.getopt(sys.argv[1:],"hj:p:y:v:lst:i:o:",["kaytto","jaksoja=","palkkeja=","yrityksia=","vaihtoehtoja=","kerro","hiljainen","tarjotin=","omatkurssit=","taulukkotiedosto="])
except getopt.GetoptError:
    opts=set()
#    print 'lukujarj.py -i <inputfile> -o <outputfile>'
#    sys.exit(2)
for opt, arg in opts:
    if opt in ("-h", "kaytto"):
        print('LUJÄKE: LukuJärjestysKeneraattori')
        print('Komentoriviparametrit ovat (vaihda <x>: tilalle numero):')
        print('-h tai --kaytto: tämä opaste')
        print('-j <x> tai --jaksoja=<x>: jaksojen lukumäärä (oletus=5)')
        print('-p <x> tai --palkkeja=<x>: palkkien lukumäärä (oletus=8)')
        print('-y <x> tai --yrityksia=<x>: montako vaihtoehtoa käydään läpi (oletus=1000)')
        print('-v <x> tai --vaihtoehtoja=<x>: montako parasta vaihtoehtoa näytetään (oletus=4)')
        print('-l tai --kerro: kerro vähän prosessin kulusta (auttaa löytämään mahdolliset virheet)')
        print('-s tai --hiljainen: tulosta pelkät lukujärjestysvaihtoehdot, ei mitään muuta')
        print('-t <x> tai --tarjotin=<x>: käytä kurssitarjotintiedostoa <x> (oletuksena kurssitarjotin.csv)')
        print('-i <x> tai --omatkurssit=<x>: omien kurssien tiedosto <x> (oletuksena omatkurssit.csv')
        print('-o <x> tai --taulukkotiedosto=<x>: vie tulostus taulukkotiedostoon <x> (yleensä .xls-päätteinen) (ei pakollinen, muutoin näyttää tuloksen ruudulla)')
        sys.exit()
    elif opt in ("-j", "--jaksoja"):
        jaksoja = int(arg)
    elif opt in ("-p", "--palkkeja"):
        palkkeja = int(arg)
    elif opt in ("-y", "--yrityksia"):
        yrityksia = int(arg)
    elif opt in ("-v", "--vaihtoehtoja"):
        vaihtoehtoja = int(arg)
    elif opt in ("-l", "--kerro"):
        verbose = 1
    elif opt in ("-s", "--hiljainen"):
        hiljainen = 1
    elif opt in ("-t", "--tarjotin"):
        tarjotintiedosto = arg
    elif opt in ("-i", "--omatkurssit"):
        omakurssitiedosto = arg
    elif opt in ("-o", "--taulukkotiedosto"):
        ulostulo = arg

sopimattomat = [100 for i in range(vaihtoehtoja)]
tulokset = [[[set for j in range(jaksoja)] for k in range(palkkeja)] for i in range(vaihtoehtoja)]
eiloytyneet = [set for i in range(vaihtoehtoja)]

# fiksatut = [[set for i in range(jaksoja)] for j in range(palkkeja)]
# jkurssit = np.empty([palkkeja,jaksoja],dtype=object)
# ok = np.empty([palkkeja, jaksoja], dtype=object)

onnistuneet = 0


omat = [[set for i in range(jaksoja)] for j in range(palkkeja)]

jkurssit = f.luekurssit(tarjotintiedosto, jaksoja, palkkeja, hiljainen)
omatkurssit, pakotetut, ennakkotiedot = f.lueomatkurssit(omakurssitiedosto, hiljainen)

    # Pakota nämä kurssit annetuille paikoille
for x in pakotetut:
    jkurssit[int(x[2])-1][int(x[1])-1] = set([x[0]])
    #jkurssit[int(x[1])-1][int(x[2])-1] = set([x[0]])

# Jätä kurssilistauksesta jäljelle vain ne kurssit, jotka ovat omissa kursseissa
for k in range(0, palkkeja):
    for j in range(0, jaksoja):
        omat[k][j] = lj.intersection(jkurssit[k][j], omatkurssit)

# Siirrä kurssit, joissa toista tarvitaan ennakkotietona, myöhemmäksi. Tämä ei takaa ennakkotietokurssin olevan ennen sitä seuraavaa kurssia, mutta auttaa asiaa.
lj.ennakkotietopoisto(omat, ennakkotiedot, hiljainen, verbose)
        
# Poista vielä kurssit, joille löytyy uniikki palkki, ts., sellainen, jossa ei ole muita omia kursseja
lj.poista_uniikit(omat)

# Tässä on tulos, josta voi itse lähteä karsimaan. Poistamalla kommentit saa sen näkyviin.
#lj.tulosta_lukujarj(omat, set())
for j in range(0,yrityksia):
    if verbose:
        print('Yritys', j+1)

    li = list(omatkurssit)

    eiloydy = set()
    shuffle(li)
    okurssit = deepcopy(omat)
    lj.sekoita(okurssit)
               
    for kurssi in li:
    # Ideana on etsiä kurssi kerrallaan listauksesta se kohta, jossa on vähiten muita kursseja, ja sitten valita se.
        maara, minmaara, minj, mink = lj.etsi_palkit(okurssit, kurssi)
        if minmaara < 99:
        # Tämä on vähän hassu tapa laittaa pelkkä "kurssi" tähän indeksiin, mutta mennee näinkin.
            okurssit[mink][minj] = lj.intersection(okurssit[mink][minj],kurssi)
            lj.poista_uniikit(okurssit)
        else:
            eiloydy.add(kurssi)
    if verbose:
        print('Ei löydy paikkaa', len(eiloydy), 'kurssille')
    # Laita järjestykseen sen mukaan minkä verran oli ei-sopivia kursseja
    k = lj.etsi_minimi(sopimattomat, len(eiloydy))
    if(k > -1):
        k2 = lj.etsi_minimi2(sopimattomat, len(eiloydy))
        if lj.onko_eri(tulokset, okurssit, k2, k):
            onnistuneet = onnistuneet + 1
            # Siirtää tuloksia hiukan eteenpäin
            for l in range(min(vaihtoehtoja,onnistuneet) - 1, k, -1):
                tulokset[l]=tulokset[l-1]
                eiloytyneet[l]=eiloytyneet[l-1]
                sopimattomat[l]=sopimattomat[l-1]
            tulokset[k] = okurssit
            sopimattomat[k]=len(eiloydy)
            eiloytyneet[k]=eiloydy

if ulostulo == "näytölle":
    for j in range(0, vaihtoehtoja):
        print('*************** Lukujärjestysvaihtoehto', j+1,'*******************')
        lj.tulosta_lukujarj(tulokset[j], eiloytyneet[j])
        print('\n')
else:
    f.tulokset_taulukkoon(tulokset, eiloytyneet, ulostulo)

end = time.time()

if not hiljainen:
    print('Laskin', yrityksia,'lukujärjestysvaihtoehtoa', end-start, 'sekunnissa')
