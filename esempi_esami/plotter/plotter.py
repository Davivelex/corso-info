mappa = []

# Riempe la mappa 20x20 di '.'
def riempi_mappa():
    for _ in range(20):
        mappa.append(['.'] * 20)


# Stampa la mappa su 20 linee separate
def print_mappa():
    for l in mappa:
        print(''.join(l))

    print()


# Ritorna il carattere in posizione (x, y)
# tendo conto che (0, 0) è in basso a sinistra
# e (19, 19) in alto a destra
def get_position(x, y):
    return mappa[19 - y][x]


# Inserisce il carattere v in posizione (x, y)
def set_position(x, y, v):
    mappa[19 - y][x] = v


def main():
    riempi_mappa()

    with open('plotter.txt', 'r') as file:
        for line in file.readlines():
            line = line.replace('\n', '').split(' ')

            command = line[0]
            argv = [int(x) for x in line[1:]]

            if command == 'P':
                set_position(argv[0], argv[1], '*')
            elif command == 'H':
                for i in range(int(argv[2])):
                    set_position(argv[0] + i, argv[1], '-')
            elif command == 'V':
                for i in range(int(argv[2])):
                    if get_position(argv[0], argv[1] + i) == '-':
                        set_position(argv[0], argv[1] + i, '+')
                    else:
                        set_position(argv[0], argv[1] + i, '|')

    print_mappa()


if __name__ == '__main__':
    main()
