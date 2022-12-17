D = 2


def leggi_mappa(filename):
    try:
        file = open(filename, 'r')
        mappa = []

        for line in file.readlines():
            mappa.append(line.replace('\n', '').split(' '))

        return mappa
    except IOError:
        exit(f'Impossibile aprire il file {filename}')


def genera_mappa(x, y):
    mappa = []

    for i in range(x):
        mappa.append(['- '] * y)

    return mappa


def print_mappa(mappa):
    for line in mappa:
        print(' '.join(line))


def controllo(mappa, pos):
    x, y = pos
    h = mappa[x][y]

    range_x = range(max(x - D, 0), min(x + D + 1, len(mappa)))
    range_y = range(max(y - D, 0), min(y + D + 1, len(mappa[0])))

    for i in range_x:
        for j in range_y:
            if (i, j) == pos:
                continue

            if h <= mappa[i][j]:
                return False

    return True


def main():
    mappa = leggi_mappa('mappa.txt')
    laser = genera_mappa(len(mappa), len(mappa[0]))

    for x in range(len(mappa)):
        for y in range(len(mappa[0])):
            if controllo(mappa, (x, y)):
                laser[x][y] = mappa[x][y]

    print_mappa(laser)


if __name__ == '__main__':
    main()
