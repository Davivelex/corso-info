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

    for n in list(filter(lambda x: x != 0, pile)):
        nl.append(n)

    pile.clear()
    for n in nl:
        pile.append(n)

    pile.append(nc)


riempi_pile()
prev = []

while prev != pile:
    prev = pile.copy()
    togli_carte()
    print(pile)
