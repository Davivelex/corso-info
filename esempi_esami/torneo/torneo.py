from operator import itemgetter


def main():
    try:
        # apro il file con i dati
        file = open('partite.txt', 'r', encoding='utf-8')

        # contiene tutte le partite prese dall'input
        partite = list()
        # insieme (univoco) con i nomi delle squadre, utile a ciclare le squadre
        nomi_squadre = set()
        # dizionario in cui la chiave è il nome della squadra e il valore è un
        # dizionario che contiene tutte le info delle squadre (punti, partite giocate, ecc...)
        proprieta = dict()

        # itero sulle linee di input
        for line in file.readlines():
            # splitto le linee per ' : ' e ulteriormente per ' - '
            squadre, punti = line.rstrip('\n').split(' : ')
            squadre = squadre.split(' - ')
            punti = punti.split(' - ')

            # aggiungo il nome delle squadre all'insieme
            nomi_squadre.add(squadre[0])
            nomi_squadre.add(squadre[1])

            # creo il record (in formato dizionario) da mettere nella lista delle partite
            record = {
                'squadra1': squadre[0],
                'squadra2': squadre[1],
                'punti1': int(punti[0]),
                'punti2': int(punti[1]),
            }

            partite.append(record)

        # itero per nome squadra
        for nome_squadra in nomi_squadre:
            # inizializzo ogni variabile a 0 per contare
            numero_partite = 0
            punti = 0
            punti_fatti = 0
            punti_subiti = 0

            # itero le partite
            for partita in partite:
                # Conta le partite che ha giocata la squadra di nome nome_squadra
                if nome_squadra == partita['squadra1'] or nome_squadra == partita['squadra2']:
                    numero_partite += 1

                # Divido i casi in cui la squadra sia la prima a comparire o la seconda (così da attribuire in modo
                # corretto i punti) se la squadra è la seconda si invertono tutti i conteggi

                # la squadra che si controlla è la prima a comparire nella partita
                if nome_squadra == partita['squadra1']:
                    # conto punti subiti e punti fatti
                    punti_fatti += partita['punti1']
                    punti_subiti += partita['punti2']

                    # aggiungo i punti come mi chiedeva il testo (3 vinto, 2 pareggiato, 1 perso)
                    if partita['punti1'] > partita['punti2']:
                        punti += 3
                    elif partita['punti1'] == partita['punti2']:
                        punti += 2
                    else:
                        punti += 1
                # la squadra che si controlla è la seconda a comparire nella partita
                elif nome_squadra == partita['squadra2']:
                    punti_fatti += partita['punti2']
                    punti_subiti += partita['punti1']

                    if partita['punti1'] > partita['punti2']:
                        punti += 1
                    elif partita['punti1'] == partita['punti2']:
                        punti += 2
                    else:
                        punti += 3

            # creo il dizionario con le variabili di conteggio e lo inserisco nel dizionario con la chiave nome squadra
            record = {
                'nome': nome_squadra,
                'partite_giocate': numero_partite,
                'punti': punti,
                'punti_fatti': punti_fatti,
                'punti_subiti': punti_subiti,
                'fattore': round(punti_fatti / punti_subiti, 3)
            }

            proprieta[nome_squadra] = record

        # converto il dizionario delle proprità in lista (per effettuare l'ordinamento impossibile per i dizionari)
        classifica = list(proprieta.values())
        # la funzione itemgatter ordina in base alla chiave 'punti' e in caso di parità con la chiave 'fattore',
        # reversed=True serve per ordinare in senso decrescente
        classifica.sort(key=itemgetter('punti', 'fattore'), reverse=True)

        # stampo l'intestazione
        print('SQUADRA                  GIOCATE    PUNTI       Q      PS      PF')
        print('-----------------------------------------------------------------')

        # stampo le proprietà della squadra con la formattazione delle f-string
        for squadra in classifica:
            print(f"{squadra['nome']:<30} {squadra['partite_giocate']:<7} {squadra['punti']:>2} "
                  f"{squadra['fattore']:>7.3f} {squadra['punti_fatti']:>7} {squadra['punti_subiti']:>7}")

        # chiudo il file
        file.close()

    # gestisco gli errori di lettura file
    except OSError as error:
        print(f'Errore: {error}')


# chiamo il main definito
main()
