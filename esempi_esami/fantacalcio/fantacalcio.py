import random
import math


def leggi_file(filename):
    try:
        file = open(filename, 'r')
        data = []
        for line in file:
            data.append(line.replace('\n', '').split(', '))

        return data
    except IOError:
        print(f'Non è possibile aprire il file {filename}')


def scegli(giocatori, numero, budget, fattore):
    rosa = []

    for i in range(numero):
        max_budget = budget - numero + i + 1

        scelte = list(sorted(list(filter(lambda x: x[1] <= max_budget and x not in rosa, giocatori)),
            key=lambda x: x[1], reverse=True))
        scelte = scelte[0:-int(len(scelte)*math.sqrt(fattore/11))]
        scelta = random.choice(scelte)
        rosa.append(scelta)
        scelte.remove(scelta)
        budget -= scelta[1]

    return rosa, budget

# fattori contiene i quattro parametri per scegliere i giocatori, un numero compreso tra 1 e 10, se questo è alto
# tende a formare una rosa "polarizzata", ovvero con giocatori molto costosi, ma con tanti giocatori economici. Al
# contrario se questo è prossimo all'1 allora la rosa sarà bilanciata, probabilmente avanzano più soldi
def main(fattori):
    portieri = list()
    difensori = list()
    attaccanti = list()
    centrocampisti = list()

    calciatori = leggi_file('fantacalcio.txt')
    for calciatore in calciatori:
        nome, squadra, ruolo, costo = calciatore

        if ruolo == 'portiere':
            portieri.append((nome, int(costo)))
        elif ruolo == 'difensore':
            difensori.append((nome, int(costo)))
        elif ruolo == 'attaccante':
            attaccanti.append((nome, int(costo)))
        elif ruolo == 'centrocampista':
            centrocampisti.append((nome, int(costo)))

    A, B, C, D = fattori

    portieri, rimasto = scegli(portieri, 3, 20, A)
    difensori, rimasto = scegli(difensori, 8, 40 + rimasto, B)
    centrocampisti, rimasto = scegli(centrocampisti, 8, 80 + rimasto, C)
    attaccanti, rimasto = scegli(attaccanti, 6, 120 + rimasto, D)

    print(f'Portieri:         {"".join([f"{g[0]:18} {g[1]:02}  " for g in portieri])}')
    print(f'Difensori:        {"".join([f"{g[0]:18} {g[1]:02}  " for g in difensori])}')
    print(f'Centrocampisti:   {"".join([f"{g[0]:18} {g[1]:02}  " for g in centrocampisti])}')
    print(f'Attaccanti:       {"".join([f"{g[0]:18} {g[1]:02}  " for g in attaccanti])}')


if __name__ == '__main__':
    main([2, 3, 3, 7])
