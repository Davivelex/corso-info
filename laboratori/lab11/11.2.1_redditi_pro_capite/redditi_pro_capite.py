def parse(x: str):
    try:
        return int(x)
    except ValueError:
        if x[0] == '$':
            for remove in [' ', '$', ',']:
                x = x.replace(remove, '')

            return parse(x)
        else:
            return x


def leggi_file(filename, sep):
    try:
        file = open(filename, 'r', encoding='utf-8')

        data = []
        for line in file.readlines():
            line = line.rstrip('\n').split(sep)

            data.append([parse(x) for x in line])

        file.close()
        return data
    except OSError as error:
        exit(str(error))


def read_data(nazione, data):
    if nazione in data:
        return f'La nazione {nazione} ha un reddito pro capite di $ {data[nazione]}'
    else:
        return f'La nazione {nazione} non è presente tra i dati'


def main():
    data_dump = leggi_file('rawdata_2004.txt', '\t')

    redditi2004 = {}
    for _, nazione, reddito in data_dump:
        redditi2004[nazione] = reddito

    data_dump = leggi_file('rawdata_2021.csv', ',')

    redditi2021 = {}
    for dato in data_dump:
        redditi2021[dato[0]] = dato[2]

    print('REDDITI 2004')
    while True:
        nazione = input('\nInserisci nazione: ')

        if nazione == 'quit':
            break
        else:
            print(read_data(nazione, redditi2004))

    print('REDDITI 2021')
    while True:
        nazione = input('\nInserisci nazione: ')

        if nazione == 'quit':
            break
        else:
            print(read_data(nazione, redditi2021))


if __name__ == '__main__':
    main()