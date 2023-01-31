from _operator import itemgetter


def parse(x: str):
    if x == '--':
        return [0, 0]
    elif '/' in x:
        return [int(n) for n in x.split('/')]
    else:
        try:
            n = int(x)
            if n > 0:
                return [n, 0]
            else:
                return [0, -n]
        except ValueError:
            return x

def read_file(filename, sep, skip=False):
    try:
        data = []
        file = open(filename, 'r', encoding='utf-8')

        headers = []
        if skip:
            headers = file.readline().rstrip('\n').split(',')

        for line in file.readlines():
            line = line.rstrip('\n').split(sep)
            data.append([parse(x) for x in line])

        file.close()
        return headers, data
    except OSError as error:
        exit(str(error))


def main():
    _, database_dump = read_file('database.txt', ': ')
    headers, dati_dump = read_file('dati_aereoporto_torino.csv', ',', 1)

    database = {}
    fermate = set()
    autisti = set()
    for key, value in database_dump:
        if key[0] == 'F':
            fermate.add(key)
        elif key[0] == 'A':
            autisti.add(key)

        database[key] = value


    dati = []
    for record_dump in dati_dump:
        record = {}

        for index, header in enumerate(headers):
            record[header] = record_dump[index]

        dati.append(record)

    persone_salite = {}
    persone_scese = {}
    for fermata in fermate:
        if fermata not in persone_salite:
            persone_salite[fermata] = 0
            persone_scese[fermata] = 0

        for corsa in dati:
            if fermata in corsa:
                saliti, scesi = corsa[fermata]

                if fermata in corsa:
                    persone_salite[fermata] += saliti
                    persone_scese[fermata] += scesi

    saliti_fermata_max = max(list(persone_salite.items()), key=itemgetter(1))
    scesi_fermata_max = max(list(persone_scese.items()), key=itemgetter(1))

    print(f'La fermata in cui salgono più passeggeri ({saliti_fermata_max[1]}) è {database[saliti_fermata_max[0]]}')
    print(f'La fermata in cui scendono più passeggeri ({scesi_fermata_max[1]}) è {database[scesi_fermata_max[0]]}')


    persone_per_autista = {}
    for autista in autisti:
        if autista not in persone_per_autista:
            persone_per_autista[autista] = 0

        for corsa in dati:
            for fermata in fermate:
                if corsa['ID'] == autista:
                    if fermata in corsa:
                        saliti, _ = corsa[fermata]

                        persone_per_autista[autista] += saliti

    persone_per_autista = list(persone_per_autista.items())
    persone_per_autista.sort(key=itemgetter(1), reverse=True)

    print('\nLista di autisti ordinata in base al numero di passeggeri:')
    for cod_autista, persone in persone_per_autista:
        print(f'   {database[cod_autista]} con {persone} passeggeri')

if __name__ == '__main__':
    main()