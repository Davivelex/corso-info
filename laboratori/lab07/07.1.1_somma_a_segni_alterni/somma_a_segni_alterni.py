numeri = []

i = "_"

while i != "":
    i = input("Inserisci numero: ")

    if i.isdigit() and int(i) >= 0:
        numeri.append(int(i))
    else:
        print("Input non valido")

somma = 0
for indice, numero in enumerate(numeri):
    if indice % 2 != 0:
        somma -= numero
    else:
        somma += numero

print(f"La somma alternata è {somma}")
