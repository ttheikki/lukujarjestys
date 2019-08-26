# -*- coding: utf-8 -*-

def luekurssit(tarjotintiedosto, jaksoja,palkkeja, hiljainen):
    import csv
    jkurssit = [[set for i in range(jaksoja)] for j in range(palkkeja)]

    with open(tarjotintiedosto) as tarjotin_file:
        csv_reader = csv.reader(tarjotin_file, delimiter=';')
        line_count = 0
        kurssit = []
        for row in csv_reader:
            kurssit.append(row)
            line_count += 1
        if not hiljainen:
            print(f'Luin {line_count} kurssia tarjottimelta.')

    # Tämä on tässä alustamassa tuon joukon. Tämän voisi varmaan tehdä paremminkin
    for j in range(0, jaksoja):
        for k in range(0, palkkeja):
            jkurssit[k][j] = set()

    for row in kurssit:
        # Ottaa mukaan vain tapaukset, kun kurssille on määritetty sekä jakso, että palkki
        if len(row[2]) > 0 and len(row[2]) > 0:
            palkki = int(row[1][0])
            jakso = int(row[2][0])
            # Muokkaa kurssikoodit geneerisiksi poistamalla ryhmänumerot
            jkurssit[palkki - 1][jakso - 1].add(row[0][:len(row[0]) - 2])
    return jkurssit


def lueomatkurssit(omakurssitiedosto, hiljainen):
    import csv
    with open(omakurssitiedosto) as omat_file:
        csv_reader = csv.reader(omat_file, delimiter=';')
        line_count = 0
        okurssit = []
        for row in csv_reader:
            # Ensimmäinen rivi on otsikkoa varten
            if line_count == 0:
                line_count += 1
            else:
                okurssit.append(row)
                line_count += 1
        if not hiljainen:
            print(f'Luin {line_count} omaa kurssia.')

# En osannut lukea suoraan set-muotoon, joten teen tämän nyt näin
    omatkurssit = set()
    pakotetut = set()
    ennakkotiedot = set()
    for j in range(0, line_count - 1):
        omatkurssit.add(okurssit[j][0])
        if len(okurssit[j][2]) > 0:
            # Pakota nämä kurssit näille paikoille
            pakotetut.add((okurssit[j][0], okurssit[j][1], okurssit[j][2]))
        else:
            if len(okurssit[j][1]) > 0:
                # Tämän kurssin pitää tulla ennen tätä toista
                ennakkotiedot.add((okurssit[j][0], okurssit[j][1]))


    return omatkurssit, pakotetut, ennakkotiedot

def tulokset_taulukkoon(tulokset, eiloytyneet, tiedosto):
    import xlwt
    from lukujarjtools import toistuvat_kurssit
    from lukujarjtools import etsi_samat

    firstheaderstyle = xlwt.easyxf('font: name Times New Roman, color-index red, bold on')
    tableheaderstyle = xlwt.easyxf('font: name Times New Roman, color-index black, bold on')
#    lukujarjstyle = xlwt.easyxf('font: name Times New Roman, border: left thin,right thin,top thin,bottom thin')
    lukujarjstyle = xlwt.easyxf('border: left medium,right medium,top medium,bottom medium')

    bflukujarjstyle = xlwt.easyxf('border: left medium,right medium,top medium,bottom medium; font: bold on')

    
    textstyle = xlwt.easyxf('font: name Times New Roman')

    samat = etsi_samat(tulokset)
    jaksoja = len(samat[0])
    palkkeja = len(samat)
    
    wb = xlwt.Workbook()
    j=0
    for vaihtoehto in tulokset:
        j += 1
        ws = wb.add_sheet("".join(['Vaihtoehto ',str(j)]))
        ws.write(0, 0, "".join(['Lukujärjestysvaihtoehto ', str(j)]), style=firstheaderstyle)
        ws.write(1, 0, "Jaksot ovat eri riveillä, palkit eri sarakkeissa.", style=textstyle)
        ws.write(2, 0, "Kaikissa vaihtoehdoissa samoihin paikkoihin tulevat kurssit on lihavoitu (riippuu vaihtoehtojen määrästä).", style=textstyle)
        #k = 0
        # Tämä olisi pythonin tapa tehdä tuo luuppi, mutta halusin käyttää tietoa toisesta tuplesta merkitäkseni eri tavoin kaikissa toistuvat kurssit, joten käytän sitten vain noita tuplejen pituuksia
        # for palkki in vaihtoehto:
        #     ws.write(3, k+1, k+1, style = tableheaderstyle)
        #     k += 1
        #     l = 0
        #     for jakso in palkki:
        #         if k == 1:
        #             ws.write(4+l, 0, l+1, style = tableheaderstyle)
        #         for val in jakso:
        #             ws.write(4+l, k, val, style = lukujarjstyle)
        #         l += 1

        for k in range(0, palkkeja):
            ws.write(4, k+1, k+1, style = tableheaderstyle)
            #k += 1
            #l = 0
            for l in range(0, jaksoja):
                if k == 0:
                    ws.write(5+l, 0, l+1, style = tableheaderstyle)
                for val in vaihtoehto[k][l]:
                    if len(samat[k][l]) == 0:
                        ws.write(5+l, k+1, val, style = lukujarjstyle)
                    else:
                        ws.write(5+l, k+1, val, style = bflukujarjstyle)
                #l += 1
        toistuvat, nahty = toistuvat_kurssit(vaihtoehto)
        if len(toistuvat) > 0:
            for x in toistuvat:
                ws.write(7+l, 0, "".join(['Huomaa, että kurssi ', x, ' esiintyy ', str(nahty[x]), ' kertaa, eli nuo paikat ovat vaihtoehtoisia']), style = textstyle)
                l += 1
        if len(eiloytyneet[j-1]) >0:
            ws.write(7+l, 0, "".join(["En saanut näitä kursseja sopimaan: ", ",".join(eiloytyneet[j-1])]), style = textstyle)

    wb.save(tiedosto)
