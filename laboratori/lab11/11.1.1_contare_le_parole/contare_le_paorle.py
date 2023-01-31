def parse(x:str) -> list[str]:
    remove = set()
    r = []

    for y in x.split("'"):
        for c in y:
            c = c.lower()

            if not c.isalpha():
                remove.add(c)

        for c in remove:
            y = y.replace(c, '')

        r.append(y)

    return r


def leggi_file(filename):
    try:
        file = open(filename, encoding='utf-8')

        text = []
        for line in file.readlines():
            for word in line.rstrip('\n').split(' '):
                for _word in parse(word):
                    text.append(_word)

        file.close()
        return text
    except OSError as error:
        exit(str(error))


def main():
    testo = leggi_file('input.txt')
    parole = set(testo)

    for parola in parole:
        print(parola, testo.count(parola))

if __name__ == '__main__':
    main()
