from math import floor

N = 0

while N < 10000 or N > 99999:
    N = int(input("Inserisci un numero di 5 cifre: "))

N = str(N)

for c in N:
    print(c)