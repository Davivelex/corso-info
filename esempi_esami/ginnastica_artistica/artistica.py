def leggi_file(filename):
    data = []

    try:
        file = open(filename, 'r')
        for line in file.readlines():
            atleta = line.replace('\n', '').split(' ')
            data.append({
                'nome': atleta[0],
                'cognome': atleta[1],
                'sesso': atleta[2],
                'nazione': atleta[3],
                'punti': [float(x) for x in atleta[4:]]
            })

            calcola_punteggio(data[-1])
    except IOError:
        print(f'Non e\' possibile aprire il file {filename}')

    return data


def cerca_nazioni(atleti):
    nazioni = set()

    for atleta in atleti:
        nazioni.add(atleta['nazione'])

    return nazioni


def calcola_punteggio(atleta):
    punteggio = sum(atleta['punti']) - min(atleta['punti']) - max(atleta['punti'])
    atleta['punteggio'] = punteggio


def main():
    atleti = leggi_file('punteggi.txt')
    nazioni = cerca_nazioni(atleti)

    classifica_f = list(filter(lambda x: x['sesso'] == 'F', atleti))
    classifica_f = list(sorted(classifica_f, key=lambda x: -x['punteggio']))
    print(classifica_f)
    vincitrice = classifica_f[0]

    classifica_n = list()
    for nazione in nazioni:
        somma = 0
        for atleta in atleti:
            if atleta['nazione'] == nazione:
                somma += atleta['punteggio']

        classifica_n.append({
            'nazione': nazione,
            'punteggio': somma
        })

    classifica_n = list(sorted(classifica_n, key=lambda x: -x['punteggio']))

    print('Vincitrice femminile: ')
    print(f"{vincitrice['nome']} {vincitrice['cognome']}, {vincitrice['nazione']} - "
          f"Punteggio: {vincitrice['punteggio']:.2f}")
    print('\nClassifica complessiva nazioni:')
    for indice, record in enumerate(classifica_n):
        if indice > 2:
            break

        print(f"{indice+1}) {record['nazione']} - Punteggio totale: {record['punteggio']:.2f}")


if __name__ == '__main__':
    main()
