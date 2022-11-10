A = int(input("Inserire il primo numero: "))
B = int(input("Inserire il secondo numero: "))

somma = A + B
differenza = A - B
prodotto = A * B
valore_medio = somma / 2
distanza = abs(differenza)
massimo = max(A, B)
minimo = min(A, B)

print(f"Somma: {somma}\nDifferenza: {differenza}\nProdotto: {prodotto}\n"
      f"Valore medio: {valore_medio}\nDistanza: {distanza}\nMassimo: {massimo}\nMinimo: {minimo}")