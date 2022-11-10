A = int(input("Inserire il primo numero: "))
B = int(input("Inserire il secondo numero: "))

somma = A + B
differenza = A - B
prodotto = A * B
valore_medio = somma / 2
distanza = abs(differenza)
massimo = max(A, B)
minimo = min(A, B)

print("%-15s%.2f" % ("Somma:", somma))
print("%-15s%.2f" % ("Differenza:", differenza))
print("%-15s%.2f" % ("Prodotto:", prodotto))
print("%-15s%.2f" % ("Valore medio:", valore_medio))
print("%-15s%.2f" % ("Distanza:", distanza))
print("%-15s%.2f" % ("Massimo:", massimo))
print("%-15s%.2f" % ("Minimo:", minimo))
