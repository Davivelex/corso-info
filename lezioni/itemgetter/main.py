from _operator import itemgetter


def cast_int(x):
    try:
        return int(x)
    except ValueError:
        return x


def read_file(filename):
    try:
        file = open(filename, 'r', encoding='utf-8-sig')

        headers = file.readline().rstrip('\n').split(',')

        data = []
        for line in file.readlines():
            line = line.rstrip('\n').split(',')

            record = {}
            for index, header in enumerate(headers):
                record[header] = cast_int(line[index])

            data.append(record)

        file.close()
        return headers, data
    except IOError as error:
        exit(str(error))


def main():
    headers, data = read_file('ingresso.txt')

    print('Scegli con quali chiavi ordinare:')
    for index, header in enumerate(headers):
        print(f'  {index+1}. {header}')

    keys = input('\nInserisci chiavi separate da spazi: ')
    keys = [int(x) for x in keys.split()]
    keys = list(map(lambda x: headers[x-1], keys))

    data.sort(key=itemgetter(*keys))

    print()
    for person in data:
        print(f"{person['nome di battesimo']}{person['cognome']} ha {person['età']} anni e pesa {person['peso (kg)']}")

if __name__ == '__main__':
    main()
