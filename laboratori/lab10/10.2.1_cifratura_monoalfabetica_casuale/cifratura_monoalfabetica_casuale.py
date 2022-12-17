ALPHA = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
         'V', 'W', 'X', 'Y', 'Z'}


def leggi_file(filename):
    try:
        file = open(filename, 'r', encoding='utf-8')
        data = file.read()
        file.close()
        return data
    except IOError:
        print(f'Impossibile leggere il file {filename}')


def scrivi_file(filename, data):
    try:
        file = open(filename, 'w', encoding='utf-8')
        file.write(data)
        file.close()
    except IOError:
        print(f'Impossibile scrivere su file {filename}')


def ceaser(string: str):
    string = string.upper()
    to_add = ALPHA.copy()
    text = []

    for element in string:
        if element in to_add:
            text.append(element)
            to_add.remove(element)

    text += list(reversed(list(to_add)))

    return text


def cipher(string, key: list):
    encrypted = []

    for element in string:
        if element.upper() in ALPHA:
            encrypted += key[ord(element.upper()) - ord('A')]
        else:
            encrypted += element

    return ''.join(encrypted)


def decipher(string, key: list):
    decrypted = []

    for element in string:
        if element.upper() in ALPHA:
            decrypted += chr(ord('A') + key.index(element))
        else:
            decrypted += element

    return ''.join(decrypted)


def main():
    key_file = input('Inserisci file chiave: ')
    input_key = leggi_file(key_file)
    key = ceaser(input_key)

    while True:
        print('\n---| Cifratura monoalfabetica casuale |---\n'
              ' * (C) codifica\n'
              ' * (D) decodifica\n'
              ' * (E) esci')
        comando = input('Comando: ').upper()

        if comando == 'E':
            break

        input_file = input('Inserisci file di input: ')
        output_file = input('Inserisci file di output: ')
        if comando == 'C':
            text = leggi_file(input_file)
            ciphertext = cipher(text, key)

            scrivi_file(output_file, ciphertext)
        elif comando == 'D':
            text = leggi_file(input_file)
            deciphertext = decipher(text, key)

            scrivi_file(output_file, deciphertext)
        else:
            print('Comando sconosciuto')


if __name__ == '__main__':
    main()
