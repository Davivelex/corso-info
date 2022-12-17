def leggi_personaggi(filename):
    try:
        personaggi = {}
        file = open(filename, 'r')

        tipi = file.readline().replace('\n', '').split(';')
        for line in file.readlines():
            personaggio = line.replace('\n', '').split(';')
            caratteristiche = dict()

            for indice, tipo in enumerate(tipi):
                caratteristiche[tipo] = personaggio[indice]

            personaggi[caratteristiche['Nome']] = caratteristiche

        return personaggi
    except IOError:
        print(f'Non è possibile aprire il file {filename}')
        exit(-1)


def leggi_domande(filename):
    try:
        domande = []
        file = open(filename, 'r')

        for line in file.readlines():
            domande.append(line.replace('\n', '').split('='))

        return domande
    except IOError:
        print(f'Non è possibile aprire il file {filename}')
        exit(-1)


def seleziona(personaggi, domanda):
    rimasti = dict()

    for personaggio in personaggi.values():
        if personaggio[domanda[0]] == domanda[1]:
            rimasti[personaggio['Nome']] = personaggio

    personaggi.clear()
    for rimasto in rimasti:
        personaggi[rimasto] = rimasti[rimasto]


def print_personaggio(personaggio):
    informazioni = f'{personaggio["Nome"]} - '
    caratteristiche = []

    for caratteristica in personaggio:
        if caratteristica != 'Nome':
            informazioni += f'{caratteristica}: {personaggio[caratteristica]}, '

    print(informazioni[:-1])


def main(file_domande):
    personaggi = leggi_personaggi('personaggi.txt')
    domande = leggi_domande(file_domande)

    print('Personaggi del gioco:')
    for nome in personaggi:
        print_personaggio(personaggi[nome])

    for numero, domanda in enumerate(domande):
        print(f'\nMossa {numero+1} - domanda: {domanda[0]} = {domanda[1]}')
        seleziona(personaggi, domanda)
        for nome in personaggi:
            print_personaggio(personaggi[nome])

    if len(personaggi) == 1:
        print('\nGioco terminato, hai vinto! È stato selezionato:')
        print_personaggio(list(personaggi.values())[0])
    else:
        print('\nPeccato, hai perso :-(')

    print('\n\n')


if __name__ == '__main__':
    main('domande1.txt')
    main('domande2.txt')
