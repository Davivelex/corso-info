def convert_data(x):
    try:
        return float(x)
    except ValueError:
        return x


def leggi_file(filename):
    try:
        data = []
        file = open(filename, 'r', encoding='utf-8')

        for line in file.readlines():
            line = line.rstrip('\n').split(';')
            data.append([convert_data(data) for data in line])

        file.close()
        return data
    except IOError:
        exit(f'Errore: impossibile leggere il file {filename}')



def guida(caselli, partenza):
    for casello in caselli:
        if casello[0] == partenza:
            return casello[1]

def main():
    pedaggi = leggi_file('pedaggi.txt')
    percorsi = leggi_file('percorsi.txt')

    caselli = dict()
    for pedaggio in pedaggi:
        caselli[(pedaggio[0], pedaggio[1])] = pedaggio[2]

    for percorso in percorsi:
        partenza, arrivo = percorso

        costo = 0
        caselli_raggiunti = 0
        attuale = partenza
        raggiungibile = True

        while attuale != arrivo:
            prossimo = guida(caselli, attuale)

            if prossimo is not None:
                costo += caselli[(attuale, prossimo)]
                caselli_raggiunti += 1
                attuale = prossimo
            else:
                raggiungibile = False
                break

        if raggiungibile:
            print(f'Percorso {partenza}-{arrivo}: {caselli_raggiunti} caselli, tariffa totale {costo:.2f} euro')
        else:
            print(f'Percorso {partenza}-{arrivo}: non raggiungibile')

if __name__ == '__main__':
    main()
