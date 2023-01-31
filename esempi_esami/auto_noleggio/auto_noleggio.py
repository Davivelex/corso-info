def leggi_file(filename):
    try:
        file = open(filename, 'r', encoding='utf-8')
        data = []

        headers = file.readline().strip(' ').split(',')

        for line in file.readlines():
            line = line.strip(' ').rstrip('\n').split(',')

            auto = {
                'categoria': line[0],
                'marca': line[1],
                'modello': line[2],
                'colore': line[3],
                'giorni': line[4:]
            }

            data.append(auto)

        file.close()
        return data
    except OSError as error:
        exit(str(error))


def main():
    database = leggi_file('database.txt')
    print(database)


if __name__ == '__main__':
    main()
