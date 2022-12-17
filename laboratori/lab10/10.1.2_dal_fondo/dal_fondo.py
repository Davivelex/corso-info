def leggi_file(filename):
    try:
        data = []
        file = open(filename, 'r', encoding='utf-8')
        for line in file.readlines():
            data.append(line)

        file.close()
        return data
    except IOError:
        exit(f'Impossibile aprire il file {filename}')


def scrivi_file(filename, data):
    try:
        file = open(filename, 'w', encoding='utf-8')
        for line in data:
            file.write(line)
        file.close()
    except IOError:
        exit(f'Impossibile scrivere sul file {filename}')


def main():
    data = leggi_file('input.txt')
    data.reverse()
    scrivi_file('input.txt', data)


if __name__ == '__main__':
    main()
