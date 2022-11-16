numero = int(input("Inserisci un numero: "))

somma = 0
minimo = massimo = numero

while numero != "":
    numero = int(numero)
    somma += numero
    minimo = min(minimo, numero)
    massimo = max(massimo, numero)

    print(f"* Somma: {somma}\n* Minimo: {minimo}\n* Massimo: {massimo}")
    numero = input("Inserisci un numero: ")

