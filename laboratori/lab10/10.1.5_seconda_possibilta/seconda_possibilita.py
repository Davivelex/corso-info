def main():
    error = 0
    sum_value = 0

    while True:
        if error == 2:
            break

        try:
            valore = input('Inserisci valore: ')

            if valore == '':
                break
            else:
                sum_value += float(valore)
                error = 0
        except ValueError:
            if error == 0:
                print('(!) errore di inserimento, hai ancora una possibilità')

            error += 1

    print(f'Somma valori: {sum_value}')


if __name__ == '__main__':
    main()
