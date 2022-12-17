dati_albergo = []

with open('dati.txt') as dati:
    for line in dati.readlines():
        line = line.rstrip('\n').split(';')

        record = {
            'nome': line[0],
            'servizio': line[1],
            'prezzo': line[2],
            'data': line[3]
        }

        dati_albergo.append(record)


print(dati_albergo[4]['servizio'])