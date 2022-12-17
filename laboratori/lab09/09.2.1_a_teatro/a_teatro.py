import random


def leggi_file(filename):
    try:
        data = []
        file = open(filename, 'r', encoding='utf-8')
        for line in file.readlines():
            line = line.replace('\n', '')
            data.append([int(x) for x in line.split(',')])

        return data
    except IOError:
        exit(f'Il file {filename} non esiste')


def scrivi_file(filename, data):
    try:
        file = open(filename, 'w', encoding='utf-8')
        file.writelines([', '.join([str(y) for y in x]) + '\n' for x in data])
    except IOError:
        exit(f'Il file {filename} non esiste')


def get_int(prompt):
    x = input(prompt)
    try:
        return int(x)
    except ValueError:
        print('\n(!) Errore: devi inserisci un numero intero')
        return False


def menu():
    print('\n\nInserisci:'
          '\n  * S per scegliere un posto'
          '\n  * P per comprare per prezzo'
          '\n  * K per salvare i dati'
          '\n  * U per uscire')
    return input('\nComando: ').lower()


def menu_exit(salv):
    if salv:
        return False, True
    else:
        scelta = input('\n(!) Avviso: Sei sicuro di voler uscire senza salvare (Si/No)? ').lower()[0]
        if scelta == 's':
            return False, False
        elif scelta == 'n':
            return True, False
        else:
            print('\n(!) Errore: Risposta non accettabile')
            return False, salv


def main(posti, salv):
    comando = menu()

    if comando == 's':
        x = get_int('Inserisci riga: ')
        y = get_int('Inserisci colonna: ')

        if x is False or y is False:
            return True, salv

        if x < 0 or x > len(posti) or y < 0 or y > len(posti[0]):
            print('\n(!) Errore: Il posto selezionato non esiste')
            return True, salv
        elif posti[x][y] == 0:
            print('\n(!) Errore: Il posto è già occupato')
            return True, salv
        else:
            print(f'Hai prenotato il posto {(x, y)}. Costo: {posti[x][y]} euro')
            posti[x][y] = 0
            return True, False
    elif comando == 'p':
        prezzo = get_int('Inserisci prezzo: ')

        if prezzo is False:
            return True, salv

        disponibili = []

        for i in range(len(posti)):
            for j in range(len(posti)):
                if prezzo == posti[i][j]:
                    disponibili.append((i, j))

        if len(disponibili) == 0:
            print(f'\n(!) Errore: Non sono rimasti posti a {prezzo} euro')
            return True, salv
        else:
            posto = random.choice(disponibili)
            print(f'Ti è stato assegnato il posto {posto}')
            posti[posto[0]][posto[1]] = 0
            return True, False
    elif comando == 'k':
        scrivi_file('posti.txt', posti)
        print('\nDati salvati nel file `posti.txt`')
        return True, True
    elif comando == 'u':
        return menu_exit(salv)
    else:
        print(f'\n(!) Errore: comando `{comando}` non riconosciuto')
        return True, salv


if __name__ == '__main__':
    dati = leggi_file('posti.txt')
    step = salvato = True

    while step:
        step, salvato = main(dati, salvato)

    print('\nArrivederci!')
