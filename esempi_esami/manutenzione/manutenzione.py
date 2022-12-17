def leggi_file(filename):
    try:
        file = open(filename, 'r')
        data = []

        for line in file.readlines():
            data.append(line.replace('\n', '').split(','))

        if len(data) == 1:
            return data[0]
        else:
            return data
    except OSError:
        exit(f'Non è possibile leggere il file {filename}')


def confronto(data_a, data_b):
    gg_a, mm_a, yy_a = [int(x) for x in data_a.split('/')]
    gg_b, mm_b, yy_b = [int(x) for x in data_b.split('/')]

    if yy_a > yy_b:
        return True
    elif yy_a < yy_b:
        return False
    else:
        if mm_a > mm_b:
            return True
        elif mm_a < mm_b:
            return False
        else:
            if gg_a > gg_b:
                return True
            else:
                return False


def print_manutenzione(manutenzione, msg=''):
    print(f'{msg}{manutenzione[0]} in data {manutenzione[1]} costo {manutenzione[2]} euro')


def main():
    manutenzioni = leggi_file('manutenzione.txt')
    parametri = leggi_file('parametri.txt')

    data, comando = parametri
    costosa = ['', '', 0]

    if comando == 'a':
        print(f'Le operazioni effettuate prima del {data}:')
        for manutenzione in manutenzioni:
            if confronto(data, manutenzione[1]):
                print_manutenzione(manutenzione)

            if int(costosa[2]) < int(manutenzione[2]):
                costosa = manutenzione
    else:
        print(f'Le operazioni effettuate dopo del {data}:')
        for manutenzione in manutenzioni:
            if confronto(data, manutenzione[1]):
                print_manutenzione(manutenzione)

            if costosa[2] < manutenzione[2]:
                costosa = manutenzione

    print_manutenzione(costosa, msg='\nLa manutenzione più costosa è stata ')


if __name__ == '__main__':
    main()
