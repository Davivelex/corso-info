stato = input("Inserisci stato civile (nc = non coniugato, c = coniugato): ")

moltiplicatore = 1

if stato == "c":
    moltiplicatore = 2
elif stato != "nc":
    print("Stato civile non valido!")
    exit()

reddito = float(input("Inserisci reddito: "))
tasse = 0

if 0 <= reddito < 8000 * moltiplicatore:
    tasse = reddito * 0.1
elif 8000 * moltiplicatore <= reddito <= 32000 * moltiplicatore:
    tasse = 800 * moltiplicatore
    tasse += (reddito - 8000 * moltiplicatore) * 0.15
else:
    tasse = 4400 * moltiplicatore
    tasse += (reddito - 32000 * moltiplicatore) * 0.25

print(f"Le tasse dovute sono {tasse}$")