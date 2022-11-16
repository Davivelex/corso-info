numero = int(input("Inserisci un numero: "))

for n in range(numero):
    if n == 0:
        continue
    elif numero % 2 == 0:
        print("Il numero NON è primo")
        exit()

print("Il numero è primo")