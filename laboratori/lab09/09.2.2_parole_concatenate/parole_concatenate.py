def is_valid(s: set, p1: str, p2: str):
    return p1 not in s and p1[:2] == p2[-2:] and p1 != '*'


def partita(giocatori, numero_giocatori):
    parole = set()
    in_gioco = True

    precedente = input(f'\n{giocatori[0]}, inserisci parola: ')
    parole.add(precedente)

    i = 1
    while in_gioco:
        i = (i + 1) % numero_giocatori

        parola = input(f'{giocatori[i]}, inserisci una parola: ')
        in_gioco = is_valid(parole, parola, precedente)
        precedente = parola
        parole.add(parola)

    print(f'\n{giocatori[i]} hai perso, che delusione! :P')
    print(f'Avete detto {len(parole)} parole, complimenti! ;)')


def main():
    giocare = True

    while giocare:
        giocatori = []
        print('\n------| Parole Concatenate |------')
        numero_giocatori = int(input('Inserisci numero di giocatori: '))
        for i in range(numero_giocatori):
            giocatori.append(input(f'Nome giocatore numero {i+1}: '))

        partita(giocatori, numero_giocatori)

        scelta = input('\nVolete fare una nuova partita (si/no)? ')

        if scelta != 'si':
            giocare = False


if __name__ == '__main__':
    main()
