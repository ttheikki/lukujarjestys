# Omien kurssien editointi
"Omat kurssit" -tiedostossa kerrot, mitkä kurssit haluat vuoden aikana suorittaa. Voit myös asettaa tietyt kurssit suoritettavaksi haluamaasi (tai koulun määrittämään) tiettyy aikaan, ja kertoa, että jonkin kurssin on tultava jotain toista aiemmin.

## Lyhyet ohjeet
1. Avaa haluamasi esimerkkitiedosto taulukkolaskentaohjelmalla (mikä tahansa, joka nimellä "omat_xxx.csv"). Poista turhat tiedot toiselta ja kolmannelta sarakkeelta (eli jollet tiedä niiden olevan oikein, tyhjennä kyseiset sarakkeet).
2. Valitse mieleisesi kurssikoodit ensimmäiselle sarakkeelle. Koodien pitää olla samat kuin kurssitarjottimella ja lukujärjestyksessä, tyyliin BI02 tai ENA07.
3. Jos koulu määrittää tietylle kurssille tietyn jakson ja palkin, merkkaa nuo tiedot kyseisen kurssikoodin perään (jakso toiselle sarakkeelle, palkki kolmannelle).
4. Tarvittaessa määritä ennakkotietovaatimukset (ks. alla). Tämä ei ole pakollista.
5. Tallenna tiedosto csv-muodossa (Numbers-ohjelmassa valitse "Arkisto-Vie-CSV", valitse tiedostonimi; Excelissä tämä toimii yleensä "Tallenna nimellä"-valikosta)
6. Aja ohjelma etsiäksesi lukujärjestyksen. Jos lukujärjestysvaihtoehtoja löytyy helposti (ts., yksikään kurssi ei jää ulos), voit muokata omien kurssien luetteloa esim. pakottamalla jonkun kurssin tiettyyn kohtaan, jne.
7. Oletuksena lukujärjestysvaihtoehtoja tulee 4, ja ne tulostetaan suoraan ruudulle. Jos haluat enemmän (tai vähemmän) vaihtoehtoja, käytä valintaa ´´´-v x´´´, missä x on vaihtoehtojen lukumäärä. Jos haluat vaihtoehdot Excel-tiedostoon (jota pystyy myös lukemaan Numbers-ohjelmalla), käytä valintaa ´´´-o lukujärjestys.xls´´´.  Ohjelmien muista valinnoista saat tietoa [README-tiedostosta](README.md).

## Ennakkotiedot
Jos haluamasi kurssit pitää suorittaa tietyssä järjestyksessä (esim. MAA01 ennen MAA02:sta), voit kirjoittaa tämän toiselle sarakkeelle (esim. MAA02 toiselle sarakkeelle MAA01:n perään). Toisella sarakkeella oleva kurssi pitää myös kirjoittaa erikseen ensimmäiselle sarakkeelle. Esimerkiksi seuraavat rivit mahdollistavat suoritusjärjestyksen MAA01 - MAA02 - MAA03:
MAA01  MAA02
MAA02  MAA03
MAA03

Ohjelma poistaa tarjottimelta ne vaihtoehdot, joissa MAA02 tulee väistämättä ennen MAA01:sta ja MAA03 ennen MAA02:sta. Se ei kuitenkaan ole täydellinen (monimutkaisesta syystä), joten tämä järjestys on hyvä tarkistaa.

Huomaa, että omien kurssien tiedostoon ei pidä kirjoittaa mitään ylimääräistä! Ohjelma päättelee, onko tietyllä rivillä kyse tietyn jakson/palkin pakotuksesta tai kurssijärjestyksen määrityksestä, käytettyjen sarakkeiden lukumäärästä (kaksi tai kolme).

## Kurssien pakotus tiettyyn paikkaan
Saat pakotettua tietyn kurssin tiettyyn jaksoon ja palkkiin kirjoittamalla vastaavat numerot kyseisen kurssin riville toiseen ja kolmanteen sarakkeeseen. Tätä toimintoa käyttämällä ensisijaisesti saat määrättyä ne kurssit, jotka koulu vaatii suorittamaan tietyssä palkissa, mutta toissijaisesti voit sen avulla vaikkapa pyrkiä testaamaan, voisitko saada aikaiseksi lukujärjestyksen, jossa pääset vaikkapa kaverisi kanssa samalle englannin tunnille. Voit toki myös pyrkiä saamaan vapaata johonkin tiettyyn palkkiin esim. harrastusten vuoksi. Tällöin voit käyttää sellaista kurssikoodia, jota ei löydy tarjottimelta (vaikka "RÖH11"), ja laittaa sille kyseisen jakson/palkin.

Joissain tapauksissa koulu katkaisee kaksi kurssia kahtia, ja määrittää niiden paikat - esim. molemmista puoli kurssia jakson 2 palkissa 3 sekä jakson 4 palkissa 2. Ohjelmaan ei voi määrittää puolikkaita kursseja, mutta tämän voi ratkaista pakottamalla toisen kurssin jakson 2 palkkiin 3 ja toisen jakson 4 palkkiin 2.

## Usein vastaan tulleita ongelmia

### Kurssikoodi muuttuu vääräksi Numbersissa (tai Excelissä)
Numbers ja Excel pyrkivät tunnistamaan taulukkoon syötetyn tekstin muodon sen sisällöstä. Siksi Numbers esim. tunnisti RUB12:n 12 ruplaksi. Tämän voi estää pakottamalla kyseisen solun (tai koko rivin/sarakkeen) tekstiksi. Numbersissa se tapahtuu valitsemalla halutut solut, ja etsimällä ohjelman oikella olevasta palkista "solu" ja valitsemalla Datamuodoksi "Teksti".

### Jokin kurssikoodi jää pois kaikista lukujärjestysvaihtoehdoista
Ohjelma ei tarkista syötitkö kurssikoodit oikein. Jos jotakin kurssikoodia ei löydy tarjottimelta (eli se on väärin kirjoitettu), se vain jää pois tarjotuista lukujärjestysvaihtoehdoista.
