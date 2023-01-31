def leggi_file(filename):
    try:
        file = open(filename, encoding='utf-8')

        text = file.read()
        file.close()

        return text
    except OSError:
        exit('File not found')


def scrivi_file(filename, testo):
    try:
        file = open(filename, 'w', encoding='utf-8')

        file.write(testo)
        file.close()
    except OSError:
        exit('File not found')


def main():
    testo = leggi_file('raw_text.txt')
    bad_words = leggi_file('bad_words.txt').split('\n')

    for word in bad_words:
        testo = testo.replace(word, '*'*len(word))

    scrivi_file('censored_text.txt', testo)


if __name__ == '__main__':
    main()
