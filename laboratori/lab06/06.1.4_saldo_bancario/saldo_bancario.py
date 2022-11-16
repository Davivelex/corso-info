def interessi(iniziale, anni, tasso):
    saldo = iniziale
    for _ in range(anni):
        saldo += saldo * tasso

    return saldo


print(f"Il tuo saldo è di {interessi(int(input('Inserisci saldo iniziale: ')), int(input('Inserisci numero di anni: ')), float(input('Inserisci tasso annuo: ')))}")
