def costruisci_quadrato():
    tabella = []

    for i in range(4):
        riga = []
        for j in range(4):
            n = int(input('Inserisci un numero: '))
            riga.append(n)
        tabella.append(riga)

    return tabella


def verifica1(tabella):
    da_inserire = list(range(1, 17))

    for i in range(4):
        for j in range(4):
            if tabella[i][j] not in da_inserire:
                return False

            da_inserire.remove(tabella[i][j])

    return len(da_inserire) == 0


def verifica2(tabella):
    s = sum(tabella[0])

    for i in range(4):
        if sum(tabella[i]) != s:
            return False

    for j in range(4):
        s1 = 0
        for i in range(4):
            s1 += tabella[i][j]

        if s1 != s:
            return False

    s2 = 0
    for i in range(4):
        s2 += tabella[i][i]

    if s2 != s:
        return False

    s3 = 0
    for i in range(4):
        s3 += tabella[3-i][i]

    if s3 != s:
        return False
    else:
        return True


def main():
    tabella = costruisci_quadrato()
    if verifica1(tabella) and verifica2(tabella):
        print('E\' un quadrato magico')


if __name__ == '__main__':
    main()
