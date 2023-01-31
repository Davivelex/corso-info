def leggi_file(filename):
    try:
        file = open(filename, 'r', encoding='utf-8')
        data = {}

        for line in file.readlines():
            line = ' '.join(line.rstrip('\n').split('"')[:-1]).split(', ')
            data[line[0]] = line[1:]

        file.close()
        return data
    except OSError as error:
        print(str(error))


def decode(rna, genetic_code):
    protein = []

    for i in range(0, len(rna), 3):
        base = rna[i: i + 3]

        for aminoacids in genetic_code:
            if aminoacids == 'start':
                continue

            if base in genetic_code[aminoacids]:
                protein.append(aminoacids)

        if base in genetic_code['stop']:
            break

    return protein

def main():
    genetic_code = leggi_file('codice_genetico.txt')

    rna = input('Inserisci una sequenza di DNA: ')
    protein = []

    for base in range(len(rna)):
        if rna[base:base + 3] in genetic_code['start']:
            protein = decode(rna[base:], genetic_code)
            break

    if len(protein) == 0 or protein[-1] != 'stop':
        print('La sequenza non codifica una proteina')
    else:
        print(''.join(protein))


if __name__ == '__main__':
    main()
