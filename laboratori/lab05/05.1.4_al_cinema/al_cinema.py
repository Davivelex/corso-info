biglietti_rimasti = 100

while biglietti_rimasti > 0:
    richiesta_biglietti = int(input("Inserisci numero biglietti: "))
    if richiesta_biglietti <= 4:
        if biglietti_rimasti >= richiesta_biglietti:
            biglietti_rimasti -= richiesta_biglietti
        else:
            print(f'Sono rimasti solamente {biglietti_rimasti} biglietti')
    else:
        print("Hai richiesto troppi biglietti, il massimo è 4")

print("Biglietti esauriti")