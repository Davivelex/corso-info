parola = input("Inserisci parola")

print(''.join(reversed(parola)))
print(''.join(reversed(list(filter(lambda x: x.isupper(), parola)))))

