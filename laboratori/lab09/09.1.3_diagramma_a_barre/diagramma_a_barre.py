v = []

for _ in range(10):
    valore = input('Inserisci un valore: ')
    v.append(float(valore))

m = max(v)
for e in v:
    n = round(e * 40 / m)
    print('*' * n)

