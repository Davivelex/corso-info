def leggi_file(filename):
    try:
        records = []
        file = open(filename, 'r')

        for line in file.readlines():
            records.append(line.replace('\n', '').split())

        return records
    except IOError:
        print(f'Non è possibile aprire il file {filename}')


def main():
    acquisti = leggi_file('acquisti.txt')
    prodotti = leggi_file('prodotti.txt')

    acquisti_per_prodotto = {}

    for prodotto in prodotti:
        prodotto, produttrice = prodotto

        for acquisto in acquisti:
            if acquisto[0] == prodotto:
                if prodotto not in acquisti_per_prodotto:
                    acquisti_per_prodotto[prodotto] = [
                        produttrice,
                        [acquisto[1]]
                    ]
                else:
                    acquisti_per_prodotto[prodotto][1]\
                        .append(acquisto[1])

    for prodotto in acquisti_per_prodotto:
        produttrice, rivenditori = acquisti_per_prodotto[prodotto]

        if len(rivenditori) > 1 or rivenditori[0] != produttrice:
            print(f'Codice prodotto: {prodotto}')
            print(f'Rivenditore ufficiale: {produttrice}')
            print(f'Lista rivenditori: {" ".join(rivenditori)}\n')


if __name__ == '__main__':
    main()
