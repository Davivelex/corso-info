CONVERSIONE = {
    'lfl': 30,
    'loz': 33.814,
    'lgal': 0.219969,
    'glb': 0.00220462,
    'min': 39.3701,
    'mft': 3.28084,
    'mmi': 0.00061371
}

POTENZE = {
    'm': 1e-3,
    'c': 1e-2,
    '_': 1,
    'k': 10e3
}

METRICO = []
IMPERIALE = [i[1:] for i in CONVERSIONE.keys()]
for i in CONVERSIONE.keys():
    for j in POTENZE:
        METRICO.append(j+i[0])


metrico = ""
imperiale = ""

print(METRICO)

while metrico not in METRICO:
    metrico = input("Inserisci metrico: ")
    if len(metrico) == 1:
        metrico = '_' + metrico

while imperiale not in IMPERIALE:
    imperiale = input("Inserisci imperiale: ")

if metrico[1:]+imperiale in CONVERSIONE:
    misura = float(input("Inserisci misura: "))
    u_metrico = metrico
    if u_metrico[0] == '_':
        u_metrico = u_metrico[1]

    print(f"{misura} {u_metrico} --> {misura*POTENZE[metrico[0]]*CONVERSIONE[metrico[1:]+imperiale]} {imperiale}")
else:
    print("Non compatibili")