from csv import reader


def main(indicatore, data):
    indicatori = set()
    records = []
    print('Indicatori della qualità della vita:')
    for record in data:
        indicatori.add(record[5].replace('"', ''))

    print('\n'.join([f' {i + 1}. {s}' for i, s in enumerate(list(sorted(indicatori)))]))
    print(f'\nClassifica secondo l\'indicatore \'{indicatore}\':')
    for record in data:
        if record[5].replace('"', '') == indicatore:
            records.append((record[3], float(record[4])))

    records.sort(key=lambda x: x[1], reverse=True)
    for record in records:
        print(f'{record[0]:30} : {record[1]}')


if __name__ == '__main__':
    try:
        file_indicatore = open('indicatore.txt', 'r')
        file_qdv = open('20201214_QDV2020_001.csv', 'r')

        main(file_indicatore.read().replace('\n', ''),
             [line.replace('\n', '').split(',') for line in file_qdv.readlines()])
    except OSError:
        print('Non è possibile aprire i file')
