from random import randint

pile = []


def riempi_pile():
    carte = 45
    while carte > 0:
        impila = randint(1, carte)
        pile.append(impila)
        carte -= impila


def togli_carte():
    nl = []
    nc = len(pile)

    for i in range(len(pile)):
        pile[i] -= 1

    for n in pile:
        if n != 0:
            nl.append(n)

    pile.clear()
    for n in nl:
        pile.append(n)

    pile.append(nc)


riempi_pile()

while pile != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    togli_carte()
    print(pile)
