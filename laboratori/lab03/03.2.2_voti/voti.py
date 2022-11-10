LETTERE = ['F', 'D', 'C', 'B', 'A']
SEGNI = ['+', '-']

voto = input("Inserisci un voto: ")
conversione = -1

if (len(voto) == 1 or len(voto) == 2) and voto[0] in LETTERE:
        conversione = LETTERE.index(voto[0])

if len(voto) == 2:
    if voto[1] in SEGNI:
        if conversione == 0:
            conversione = -1
        elif voto[1] == '-':
            conversione = conversione - 0.3
        else:
            conversione = min(4.0, conversione+0.3)

if conversione != -1:
    print(f"Il voto convertito é {conversione}")
else:
    print("Il voto inserito non è valido")
