def leggi(filename):
    try:
        file = open(filename, 'r', encoding='utf-8')
        data = []

        for line in file.readlines():
            line = line.rstrip('\n').split(',')

            data.append(line)

        file.close()
        return data
    except OSError as error:
        return str(error)


def main():
    scontrino_dump = leggi('scontrino.csv')

    spesa = {}
    for prodotto, costo in scontrino_dump:
        if prodotto not in spesa:
            spesa[prodotto] = {
                'quota': 1,
                'costo': float(costo)
            }
        else:
            spesa[prodotto]['quota'] += 1

    lista_dump = leggi('lista.csv')

    totale_dovuto = 0
    for prodotto, quota in lista_dump:
        quota = int(quota)

        if prodotto in spesa:
            totale_dovuto += spesa[prodotto]['costo'] * min(quota, spesa[prodotto]['quota'])
            spesa[prodotto]['quota'] -= quota
        else:
            spesa[prodotto] = {
                'costo': None,
                'quota': -quota
            }

    totale_speso = 0
    prodotto_mancanti = []
    for prodotto in spesa:
        quota = spesa[prodotto]['quota']
        costo = spesa[prodotto]['costo']

        if quota > 0:
            totale_speso += quota * costo
        else:
            for _ in range(abs(quota)):
                prodotto_mancanti.append(prodotto)

    print(f'Spesa totale: {totale_speso + totale_dovuto:.2f}')
    print(f'Totale dovuto: {totale_dovuto}')

    for prodotto in prodotto_mancanti:
        print(f'   {prodotto}')

if __name__ == '__main__':
    main()
