def genera_tabella():
    tabella = []

    for _ in range(3):
        tabella.append(['.'] * 3)

    return tabella


def print_tabella(tabella):
    for riga in tabella:
        print(' '.join(riga))


def leggi_input(tabella, n_giocatore):
    x = int(input("Inserisci riga: "))
    y = int(input("Inserisci colonna: "))

    if x < 0 or x > 2 or y < 0 or y > 2:
        print('\n(!) Coordinate non valide\n')
        leggi_input(tabella, n_giocatore)
    elif tabella[x][y] != '.':
        print('\n(!) Posto gia\' occupato\n')
        leggi_input(tabella, n_giocatore)
    else:
        if n_giocatore:
            tabella[x][y] = 'x'
        else:
            tabella[x][y] = 'o'


def vincitore(tabella, c):
    for i in range(3):
        check = True
        for j in range(3):
            if tabella[i][j] != c:
                check = False
                break
        if check:
            return True

    for j in range(3):
        check = True
        for i in range(3):
            if tabella[i][j] != c:
                check = False
                break
        if check:
            return True

    check = True
    for i in range(3):
        if tabella[i][i] != c:
            check = False
            break
    if check:
        return True

    check = True
    for i in range(3):
        if tabella[2-i][i] != c:
            check = False
            break
    if check:
        return True

    return False


def main():
    tabella = genera_tabella()
    giocatore = True

    for _ in range(9):
        giocatore = not giocatore
        leggi_input(tabella, giocatore)
        print_tabella(tabella)

        if vincitore(tabella, 'o'):
            break
        elif vincitore(tabella, 'x'):
            break

    if vincitore(tabella, 'o'):
        print('Ha vinto il giocatore 1')
    elif vincitore(tabella, 'x'):
        print('Ha vinto il giocatore 2')
    else:
        print('Pareggio')


if __name__ == '__main__':
    main()
