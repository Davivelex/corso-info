n_posti = int(input("Numero di posti: "))
posti = [True] + [False] * n_posti + [True]


def print_posti():
    print(' '.join(['X' if x else '_' for x in posti]))


def distanza(x):
    dist = n_posti

    for i in range(0, n_posti):
        if posti[i]:
            dist = min(dist, abs(i - x))

    for j in range(n_posti + 1, 0, -1):
        if posti[j]:
            dist = min(dist, abs(j - x))

    return dist


def scegli_posto():
    dist_posto_migliore = 0
    indice_posto_migliore = -1

    for indice, posto in enumerate(posti):
        if distanza(indice) > dist_posto_migliore:
            dist_posto_migliore = distanza(indice)
            indice_posto_migliore = indice

    posti[indice_posto_migliore] = True


print_posti()

for _ in range(n_posti):
    scegli_posto()
    print_posti()

