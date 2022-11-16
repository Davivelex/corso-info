def sussidio(reddito, figli):
    if 30000 <= reddito <= 40000 and figli >= 3:
        return 1000 * figli
    elif 20000 <= reddito <= 30000 and figli >= 2:
        return 1500 * figli
    elif reddito <= 20000:
        return 2000 * figli
    else:
        return 0


while True:
    reddito_input = int(input("Inserisci reddito: "))
    figli_input = int(input("Inserisci numero di figli: "))

    if reddito_input == -1 or figli_input == -1:
        exit()
    else:
        print("Il sussidio per la famiglia è", sussidio(reddito_input, figli_input))

