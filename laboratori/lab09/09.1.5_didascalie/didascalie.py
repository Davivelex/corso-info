nv = int(input('Inseri numero di valori: '))

didascalie = []
valori = []

for _ in range(nv):
    didascalie.append((input('Inserisci didascalia: ')))
    valori.append(int(input('Inserisci valore: ')))

m = max(valori)
for i in range(nv):
    istogramma = '*' * round(valori[i] * 40 / m)
    print(f'{didascalie[i]:>20} {istogramma}')
