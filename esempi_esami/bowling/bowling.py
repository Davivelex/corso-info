def leggi_file(filename):
    file = open(filename)
    data = []
    for line in file.readlines():
        data.append(line.replace('\n', '').split(';'))

    return data


def main():
    punteggi = leggi_file('bowling.txt')

    punti = []
    massimo_nulli = ('', 0)
    massimo_strike = ('', 0)

    for record in punteggi:
        nome = ' '.join(record[0:2])
        tiri = [int(n) for n in record[2:]]

        punti.append((nome, sum(tiri)))
        if tiri.count(0) > massimo_nulli[1]:
            massimo_nulli = (nome, tiri.count(0))
        if tiri.count(10) > massimo_strike[1]:
            massimo_strike = (nome, tiri.count(10))

    for record in list(sorted(punti, key=lambda x: x[1], reverse=True)):
        print(f'{record[0]:18} {record[1]:3d}')

    if massimo_strike[1] != 0:
        print(f'{massimo_strike[0]} ha abbattuto tutti i birilli {massimo_strike[1]} volta/e')
    if massimo_nulli[1] != 0:
        print(f'{massimo_nulli[0]} ha mancato tutti i birilli {massimo_nulli[1]} volta/e')


if __name__ == '__main__':
    main()
