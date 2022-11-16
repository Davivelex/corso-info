mazzo_file = open('mazzo.txt', 'r')
mazzo = [x.replace('\n', '') for x in mazzo_file.readlines()]

VALORE = {
    'Rosso': 5,
    'Verde': 3,
    'Giallo': 1
}

giocatore1 = []
giocatore2 = []
tavolo = []
punti1 = 0
punti2 = 0

for indice, carta in enumerate(mazzo):
    if indice % 2 == 0:
        giocatore1.append(carta)
    else:
        giocatore2.append(carta)

for i in range(15):
    carta1 = giocatore1.pop(0)
    carta2 = giocatore2.pop(0)
    tavolo.append(carta1)
    tavolo.append(carta2)

    print(f'Mano n. {i+1}')
    print(f'Carta giocatore 1: {carta1}')
    print(f'Carta giocatore 2: {carta2}')

    if VALORE[carta1] > VALORE[carta2]:
        print('Risultato: Vince la mano il giocatore 1')
        for carta in tavolo:
            punti1 += VALORE[carta]
        tavolo.clear()
    elif VALORE[carta2] > VALORE[carta1]:
        print('Risultato: Vince la mano il giocatore 2')
        for carta in tavolo:
            punti2 += VALORE[carta]
        tavolo.clear()
    else:
        print('Risultato: Pareggio')

    print(f'Punteggio giocatore 1: {punti1}')
    print(f'Punteggio giocatore 2: {punti2}\n')


if punti1 > punti2:
    print(f'Vince il giocatore 1 con {punti1} punti')
elif punti2 > punti1:
    print(f'Vince il giocatore 2 con {punti2} punti')
else:
    print(f'Pareggio con {punti1} punti')
