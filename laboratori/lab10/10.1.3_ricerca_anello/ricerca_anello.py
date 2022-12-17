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


def main():
    files = input('Inserisci lista file: ')
    word = input('Inserisci parola da cercare: ')

    for filename in files.split(', '):
        data = leggi_file(filename)

        for line in data:
            line = line.replace("\n", "")
            if word.lower() in line.lower():
                print(f'{filename}: {line}')


if __name__ == '__main__':
    main()
