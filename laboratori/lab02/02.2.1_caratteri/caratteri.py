stringa = input("Inserisci stringa: ")

modificata = stringa[:3] + "." * min(len(stringa) - 3, 3) + stringa[6:]

print(modificata)
