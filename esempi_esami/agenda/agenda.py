def leggi_file(filename, sep=' '):
    try:
        file = open(filename, 'r')
        return [line.replace('\n', '').split(sep) for line in file]
    except IOError:
        print(f'Il file {filename} non è stato trovato')
        exit(-1)


def crea_agenda(dati):
    agenda = []

    for _ in range(365):
        agenda.append([''] * 24)

    for record in dati:
        agenda[int(record[0])][int(record[1])] = record[2]

    return agenda


def main():
    dati = leggi_file('agenda.txt', ';')
    agenda = crea_agenda(dati)

    comandi = leggi_file('comandi.txt', ' ')
    for comando in comandi:
        cmd = comando[0]
        argv = comando[1:]

        if cmd == 'v':
            giorno = int(argv[0])
            for ora, impegno in enumerate(agenda[giorno]):
                if impegno != '':
                    print(f'giorno {giorno} ore {ora:02d}: {impegno}')
        elif cmd == 'i':
            giorno = int(argv[0])
            ora = int(argv[1])
            impegno = ' '.join(argv[2:])

            if agenda[giorno][ora] == '':
                agenda[giorno][ora] = impegno
                print('Appuntamento inserito correttamente')
            else:
                print('Impossibile inserire appuntamento')


if __name__ == '__main__':
    main()
