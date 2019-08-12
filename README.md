# lukujarjestys
Tässä projektissa ohjelma tekee lukujärjestysvaihtoehtoja annetulle kurssitarjottimelle käyttäjän määrittämillä kurssivaihtoehdoilla.

Ohjelma ratkaisee lukiolaisten usein kohtaaman ongelman: saanko kaikki haluamani kurssit mahtumaan kouluni kurssitarjottimelta valittuihin kursseihin? Mitkä ovat eri vaihtoehdot lukujärjestyksiksi? Entä jos haluan fiksata jonkin tietyn aineen tiettyyn palkkiin, jotta pääsen kaverin kanssa samalle kurssille? Tai sitten haluan johonkin palkkiin hyppytunnin harrastusten vuoksi, voinko vielä sittenkin saada kaikki aineet suoritettua, vai pitäisikö tehdä jotain itseopiskeluna?

Ohjelma vaatii nykyisellään kaksi Excelistä tallennettua .csv-tiedostoa:
- Koulun antaman kurssitarjottimen (kurssitarjotin.csv), jossa ensimmäisellä sarakkeella on kurssikoodit, toisella palkit, ja kolmannella jaksot.
- Opiskelijan kurssit sisältävän listan (omatkurssit.csv), jossa ensimmäisellä sarakkeella on kurssikoodi. Lisäksi toiselle ja kolmannelle sarakkeelle voi asettaa kyseisen kurssin palkin ja jakson, jos ne jo tietää, tai jos ne haluaa yrittää fiksata kyseisiksi. Toisaalta voi toiselle sarakkeelle kirjoittaa toisen kurssikoodin: silloin ohjelma pyrkii asettamaan tämän jälkimmäisen kurssikoodin omaavan kurssin myöhemmälle jaksolle (esim. matematiikka pitää yleensä suorittaa koodijärjestyksessä).

Näiden perusteella ohjelma laskee käyttäjän määräämän määrän lukujärjestysvaihtoehtoja (oletuksena 1000), ja etsii vaihtoehdoista ne, joissa mukaan tulee mahdollisimman suuri osa opiskelijan määräämistä omista kursseista. Näistä tulostetaan ruudulle sitten käyttäjän valitsema määrä (oletuksena 4) "parasta" vaihtoehtoa.

## Asennus Mac-tietokoneelle:
(Ohjeet tarkentuvat vielä. Päätteelle annettavat komennot on kätevintä leikata ja liimata tästä ohjeesta.)

- Avaa Pääte-ohjelma (Launchpad - Muut - Pääte)

- Asenna lukujärjestystiedostot komennolla (kirjoita/leikkaa-liimaa komento Päätteelle, ja paina Enter)

```git clone https://github.com/ttheikki/lukujarjestys.git ~/Documents/lukujarjestys```

Tietokone saattaa pyytää asentamaan komentorivikehitystyökalut. Hyväksy tämä painamalla "Asenna" ja hyväksymällä lisenssitiedot.

- Asenna homebrew:

```/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"```

(ohjelma pyytää salasanaasi - kirjoita se)

- Asenna pythonin kolmosversio:

```brew install python3```

- Editoi haluttua omien kurssien tiedostoa (ks. omat-alkuiset tiedostot) esim. Numbers-ohjelmalla. Editointiohjeet ovat [tällä sivulla](OmatKurssit.md) 

- Vaihda hakemistoon, jonka loit lukujärjestysohjelmalle kirjoittamalla terminaalissa komento

´´´cd ~/Documents/lukujarj´´´

- Aja ohjelma esim. komennolla

```python3 lukujarj.py -t tarjotin_Norssi_Jyvaskyla_2019.csv -i omat_tokaluokka_esim.csv```

- Tarkemmat käyttöohjeet ovat alla.

## Käyttö

```python3 lukujarj.py [parametrit]```

Komentoriviparametrit ovat (vaihda <x>: tilalle numero tai tiedostonimi):

-h tai --kaytto: tämä opaste

-j <x> tai --jaksoja=<x>: jaksojen lukumäärä (oletus=5)

-p <x> tai --palkkeja=<x>: palkkien lukumäärä (oletus=8)

-y <x> tai --yrityksia=<x>: montako vaihtoehtoa käydään läpi (oletus=1000)

-v <x> tai --vaihtoehtoja=<x>: montako parasta vaihtoehtoa näytetään (oletus=4)

-l tai --kerro: kerro vähän prosessin kulusta (auttaa löytämään mahdolliset virheet)

-s tai --hiljainen: näytä pelkästään lukujärjestysvaihtoehdot

-t <x> tai --tarjotin=<x>: käytä kurssitarjotintiedostoa <x> (oletuksena kurssitarjotin.csv)
  
-i <x> tai --omatkurssit=<x>: omien kurssien tiedosto <x> (oletuksena omatkurssit.csv

-o <x> tai --taulukkotiedosto=<x>: vie tulostus taulukkotiedostoon <x> (yleensä .xls-päätteinen)

## Lisäyssuunnitelmia
Tulevaisuudessa tähän voisi vielä lisätä:
- Suora Excel-tiedostojen luku, ja käyttäjän mahdollisuus spesifioida ne
- Mahdollisesti useiden kurssitarjottimien käyttö, jotta voi katsoa kursseja monesta lukiosta
- Erilaisia hintafunktioita eri asioiden optimointiin (esim. kaksi lukujärjestystä mahdollisimman samanlaiset)
- Kunnon graafinen käyttöliittymä, jossa omat kurssit voisi valita hiirellä
