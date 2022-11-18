def leggi_input():
    m = input('Inserisci numero di righe: ')
    n = input('Inserisci numero di colonne: ')

    return int(m), int(n)


def genera_tabella(m, n):
    tabella = []

    for _ in range(m):
        tabella.append([0] * n)

    return tabella


def print_tabella(tabella):
    print('\nTabella:')
    for riga in tabella:
        print(' '.join(str(cella) for cella in riga))


def riempi_uno(tabella):
    m = len(tabella)
    n = len(tabella[0])

    for i in range(m):
        for j in range(n):
            tabella[i][j] = 1

    return tabella


def riempi_scacchiera(tabella):
    m = len(tabella)
    n = len(tabella[0])

    for i in range(m):
        for j in range(n):
            if (i + j) % 2 == 0:
                tabella[i][j] = 0
            else:
                tabella[i][j] = 1


def riempi_righe(tabella):
    m = len(tabella)
    n = len(tabella[0])

    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1:
                tabella[i][j] = 0


def riempi_colonne(tabella):
    m = len(tabella)
    n = len(tabella[0])

    for i in range(m):
        for j in range(n):
            if j == 0 or j == n - 1:
                tabella[i][j] = 1


def somma_tabella(tabella):
    m = len(tabella)
    n = len(tabella[0])

    somma = 0
    for i in range(m):
        for j in range(n):
            somma += tabella[i][j]

    return somma


def main():
    m, n = leggi_input()

    tabella = genera_tabella(m, n)
    print_tabella(tabella)

    riempi_uno(tabella)
    print_tabella(tabella)

    riempi_scacchiera(tabella)
    print_tabella(tabella)

    riempi_righe(tabella)
    print_tabella(tabella)

    riempi_colonne(tabella)
    print_tabella(tabella)

    somma = somma_tabella(tabella)
    print(f'\nSomma tabella: {somma}')


if __name__ == '__main__':
    main()
