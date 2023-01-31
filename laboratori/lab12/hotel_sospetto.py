from _operator import itemgetter


def parse(x):
    if len(x) == 1:
        return x[0]
    else:
        return x


def read_file(filename):
    try:
        data = []
        file = open(filename)

        for line in file.readlines():
            line = line.rstrip('\n').split(',')

            data.append(parse(line))

        file.close()
        return data
    except OSError as error:
        exit(str(error))


def same_day(person1, person2):
    days1 = set(range(person1['check-in'], person1['check-out'] + 1))
    days2 = set(range(person2['check-in'], person2['check-out'] + 1))

    return not days1.isdisjoint(days2)


def search_person(name, people):
    for person in people:
        if person['nome'] == name:
            return person

    return False


def main():
    presenze_dump = read_file('presenze.txt')
    sospetti = read_file('sospetti.txt')

    presenze = []
    for presenza in presenze_dump:
        presenze.append({
            'nome': presenza[0],
            'telefono': presenza[1],
            'check-in': int(presenza[2]),
            'check-out': int(presenza[3])
        })

    presenze.sort(key=itemgetter('nome'))

    for nome_sospetto in sospetti:
        sospetto = search_person(nome_sospetto, presenze)

        print(f"** Contatti del cliente: {nome_sospetto} **")
        if sospetto is False:
            print(f"    Cliente {nome_sospetto} non presente in archivio")
        else:
            contatti = []
            for contatto in presenze:
                if contatto != sospetto and same_day(sospetto, contatto):
                    contatti.append(contatto)

            if len(contatti) > 0:
                for contatto in contatti:
                    print(f"    Contatto con {contatto['nome']}, telefono {contatto['telefono']}")
            else:
                print(f"    Il cliente {sospetto['nome']} non ha avuto contatti")


if __name__ == '__main__':
    main()
