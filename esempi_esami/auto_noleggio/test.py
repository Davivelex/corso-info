oggetti = ['ciao', 'casa', 'cane', 'gatto']
animali = ['cane', 'gatto']

for indice, oggetto in enumerate(oggetti):
    if oggetto in animali:
        oggetti[indice] = 'x'

print(oggetti)
