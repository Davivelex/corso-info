parola = input("Inserisci una parola: ")

for l in range(1, len(parola)+1):
    for p in range(0, len(parola)-l+1):
        print(parola[p:p+l])
