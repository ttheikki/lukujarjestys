# -*- coding: utf-8 -*-

def luekurssit(jaksoja,palkkeja, hiljainen):
    import csv
    jkurssit = [[set for i in range(jaksoja)] for j in range(palkkeja)]

    with open('kurssitarjotin.csv') as tarjotin_file:
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


def lueomatkurssit(hiljainen):
    import csv
    with open('omatkurssit.csv') as omat_file:
        csv_reader = csv.reader(omat_file, delimiter=';')
        line_count2 = 0
        okurssit = []
        for row in csv_reader:
            okurssit.append(row)
            line_count2 += 1
        if not hiljainen:
            print(f'Luin {line_count2} omaa kurssia.')

# En osannut lukea suoraan set-muotoon, joten teen tämän nyt näin
    omatkurssit = set()
    pakotetut = set()
    ennakkotiedot = set()
    for j in range(0, line_count2 - 1):
        omatkurssit.add(okurssit[j][0])
        if len(okurssit[j][2]) > 0:
            # Pakota nämä kurssit näille paikoille
            pakotetut.add((okurssit[j][0], okurssit[j][1], okurssit[j][2]))
        else:
            if len(okurssit[j][1]) > 0:
                # Tämän kurssin pitää tulla ennen tätä toista
                ennakkotiedot.add((okurssit[j][0], okurssit[j][1]))


    return omatkurssit, pakotetut, ennakkotiedot
