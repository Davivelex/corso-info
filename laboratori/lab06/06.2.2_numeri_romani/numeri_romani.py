valore = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def converti(numero):
    totale = 0
    while len(numero) > 0:
        if len(numero) == 1 or numero[0] == numero[1]:
            totale += valore[numero[0]]
            numero = numero[1:]
        else:
            totale += valore[numero[1]] - valore[numero[0]]
            numero = numero[2:]

    return totale


print(f"Conversione: {converti(input('Inserisci numero romano: '))}")
