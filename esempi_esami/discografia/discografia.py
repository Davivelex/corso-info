def leggi_file(filename):
    try:
        file = open(filename, 'r')
        data = []
        for file in file.readlines():
            data.append(file.replace('\n', '').split(';'))

        return data
    except IOError:
        print(f'Impossibile aprire il file {filename}')
        exit(-1)


def main():
    anni = set()
    canzoni = set()

    artisti = leggi_file('artisti.txt')
    for codice, file in artisti:
        discografia = leggi_file(file)
        for canzone in discografia:
            anni.add(canzone[0])
            canzoni.add((
                canzone[0], # anno
                canzone[1], # titolo
                codice      # codice artista
            ))

    for anno in list(sorted(anni)):
        print(f'{anno}:')
        for canzone in canzoni:
            if canzone[0] == anno:
                print(f'{canzone[1]:35}{canzone[2]}')


if __name__ == '__main__':
    main()
