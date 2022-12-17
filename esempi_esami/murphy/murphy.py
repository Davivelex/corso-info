def leggi_massime(filename):
    try:
        file = open(filename, 'r', encoding='utf-8')
        massime = []

        for massima in file.read().split('\n\n'):
            massime.append([
                massima.split('\n')[0],
                ' '.join(massima.split('\n')[1:])
            ])

        return massime
    except IOError:
        exit(f'Non è possibile aprire il file {filename}')


def leggi_argomenti(filename):
    try:
        file = open(filename, 'r', encoding='utf-8')
        argomenti = []
        


def main():
    massime = leggi_massime('leggi_di_Murphy.txt')

    for massima in massime:
        print(massima)

if __name__ == '__main__':
    main()
