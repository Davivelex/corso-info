v = []

for _ in range(4):
    valore = input('Inserisci un valore: ')
    v.append(float(valore))

m = max([abs(x) for x in v])
for e in v:
    n = abs(round(e * 40 / m))
    if e < 0:
        print(' '*(40-n) + '*'*n + '|')
    else:
        print(' '*40 + '|' + '*'*n)

