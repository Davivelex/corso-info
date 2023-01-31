def main():
    a = set(input('Inserisci prima stringa: '))
    b = set(input('Inserisci seconda stringa: '))
    alphabet = set('abcdefghijklmnopqrstuvwxyz')

    print('I caratteri che compaiono in entrambe le stringhe sono: ')
    print(a.intersection(b))
    print('I caratteri che compaiono in una ma non nell\'altra: ')
    print(a.difference(b).union(b.difference(a)))
    print('Le lettere alfabetiche che non compaiono in nessuna delle due stringhe: ')
    print(alphabet.difference(a).difference(b))


if __name__ == '__main__':
    main()
