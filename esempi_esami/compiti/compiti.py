def leggi_file(filename):
    try:
        file = open(filename, 'r', encoding='utf-8')

        data = []
        for line in file.readlines():
            line = line.rstrip('\n').split()

            data.append(line)

        file.close()
        return data
    except OSError as error:
        exit(str(error))


def numero_risposte(compito: set):
    count = 0

    for risposta in compito:
        if risposta[-1] != '-':
            count += 1

    return count


def controlla(compito1: set, compito2: set):
    if compito1 == compito2:
        return 0

    if compito1.intersection(compito2) == compito1:
        return 1

    if compito1.intersection(compito2) == compito2:
        return 2

    return -1


def main():
    risposte_dump = leggi_file('risposte.txt')

    compiti = {}
    for compito in risposte_dump:
        risposte = set()

        for domanda, risposta in enumerate(compito[1:]):
            if risposta != '-':
                risposte.add(f'{domanda}:{risposta}')

        compiti[compito[0]] = risposte

    vicini = {}
    posti_dump = leggi_file('posti.txt')
    for fila in posti_dump:
        n = len(fila)
        vicini[fila[0]] = [fila[1]]
        vicini[fila[n-1]] = [fila[n-2]]
        for i in range(1,n-1):
            vicini[fila[i]] = [fila[i-1], fila[i+1]]

    controllati = set()

    for persona in vicini:
        for adiacente in vicini[persona]:
            if f'{persona}:{adiacente}' in controllati:
                continue

            controllati.add(f'{persona}:{adiacente}')
            controllati.add(f'{adiacente}:{persona}')

            hanno_copiato = controlla(compiti[persona], compiti[adiacente])
            if hanno_copiato == 0:
                print(f'Le risposte di {persona} e {adiacente} sono le stesse')
            elif hanno_copiato == 1:
                print(f'{persona} può aver copiato da {adiacente}')
            elif hanno_copiato == 2:
                print(f'{adiacente} può aver copiato da {persona}')


if __name__ == '__main__':
    main()
