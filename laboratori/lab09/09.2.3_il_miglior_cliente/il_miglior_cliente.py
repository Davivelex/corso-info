def memorizza_dati():
    customers = []
    sales = []

    while True:
        sale = int(input('Inserisci spesa: '))
        if sale == 0:
            break

        customer = input('Inserisci cliente: ')
        sales.append(sale)
        customers.append(customer)

    return customers, sales


def miglior_cliente(customers, sales):
    best = (customers[0], sales[0])

    for i in range(len(customers)):
        if sales[i] > best[1]:
            best = (customers[i], sales[i])

    return best


def main():
    customers, sales = memorizza_dati()
    best_customer = miglior_cliente(customers, sales)

    print(f'Il miglior cliente è {best_customer[0]}, che ha speso {best_customer[1]} euro')


if __name__ == '__main__':
    main()
