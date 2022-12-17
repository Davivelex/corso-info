def discount(prices, is_pet):
    if not is_pet:
        return prices * 0.2
    else:
        return 0


def main():
    non_pet_item = 0
    discounts = []
    items = []

    while True:
        item = input('Inserisci prodotto: ')
        price = int(input('Inserisci prezzo: '))
        is_pet = input('E\' un animale (si/no)? ') == 'si'

        if not is_pet:
            non_pet_item += 1

        if price == -1:
            break

        items.append([item, price])
        discounts.append(discount(price, is_pet))

    for i in range(len(items)):
        print(f'{items[i][0]:15} {items[i][1]:5}')
        if non_pet_item > 4:
            print(f'{-discounts[i]:21}')
    print('-'*21)
    print('Totale:', sum(items[i][1] + discounts[i] for i in range(len(items))), 'euro')


if __name__ == '__main__':
    main()
