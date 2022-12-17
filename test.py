lista = []

while True:
    n = input('Inserisci numero: ')

    if n == '':
        break

    lista.append(int(n))

massimo = max(lista)

for element in lista:
    print(round(element/massimo * 40))
