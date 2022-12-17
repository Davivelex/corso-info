def leggi_file(filename):
    try:
        data = []
        file = open(filename, 'r', encoding='utf-8')
        for line in file.readlines():
            record = line.split(';')
            if len(record) != 4:
                exit(f'Formato del file {filename} non valido')
            else:
                data.append(record)
        file.close()
        return data
    except IOError:
        exit(f'Impossibile aprire il file {filename}')


def main():
    data = leggi_file('dati.txt')

    services = set()
    earnings = dict()

    for record in data:
        services.add(record[1])

    for service in services:
        earnings[service] = 0
        for record in data:
            if record[1] == service:
                earnings[service] += int(record[2])

    for service in earnings:
        amount = earnings[service]

        print(f'{service}: {amount} euro')


if __name__ == '__main__':
    main()
