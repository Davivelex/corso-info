import random
import math

totale = random.randint(10, 100)

# 0 player 1 computer
chi_gioca = random.randint(0, 1)

# 0 random 1 intelligente
modalita = random.randint(0, 1)

if modalita == 0:
    print("Il computer gioca in modalità stupida")
else:
    print("Il computer gioca in modalità intelligente")


def is_pot2(x):
    return math.floor(math.log2(x)) == math.log2(x)


while totale > 1:
    print(f"Sono rimaste {totale} biglie")
    if chi_gioca == 0:
        togliere = int(input("Quante biglie vuoi togliere? "))
        while togliere < 1 or togliere > totale // 2:
            togliere = int(input("Numero non valido, riprova: "))

        totale -= togliere
    else:
        if modalita and not is_pot2(totale):
            togliere = totale - (2 ** math.floor(math.log2(totale)) - 1)
        else:
            togliere = random.randint(1, totale // 2)

        print(f"Il computer toglie {togliere} biglie")
        totale -= togliere

    chi_gioca = not chi_gioca

if chi_gioca == 0:
    print("Hai perso")
else:
    print("Hai vinto")
