def leggi_input(filename):
    try:
        records = []
        file = open(filename, 'r')

        for line in file.readlines():
            data = line.replace('\n', '').split()

            records.append({
                'paziente': data[0],
                'ora': data[1],
                'glicemia': data[2],
                'temperatura': data[3],
                'battito': data[4]
            })

        return records
    except IOError:
        print(f'Non è possibile aprire il file {filename}')


def main():
    records = leggi_input('glucometers.txt')
    dati = {}
    superamenti = {}

    for record in records:
        if record['paziente'] not in dati:
            dati[record['paziente']] = []

        dati.get(record['paziente']).append({
            'ora': record['ora'],
            'glicemia': int(record['glicemia']),
            'supera?': int(record['glicemia']) >= 200
        })

    for paziente in dati:
        for misura in dati[paziente]:
            if misura['supera?']:
                if paziente not in superamenti:
                    superamenti[paziente] = 1
                else:
                    superamenti[paziente] += 1

    for paziente in list(sorted(superamenti)):
        for misura in dati[paziente]:
            if misura['supera?']:
                print(f'{paziente} {misura["ora"]} {misura["glicemia"]}')

        print()


if __name__ == '__main__':
    main()
