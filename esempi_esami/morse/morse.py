morse_file = open('morse.txt', 'r')
comandi_file = open('comandi.txt', 'r')

MORSE_TABLE = {}

for line in morse_file.readlines():
    char, morse = line.split()

    MORSE_TABLE[char] = morse
    MORSE_TABLE[morse] = char


for line in comandi_file.readlines():
    cmd, file = line.split()

    content = open(file, 'r').read()

    if cmd == 'c':
        codifica = []
        for c in content:
            if c.upper() in MORSE_TABLE.keys():
                codifica.append(MORSE_TABLE[c.upper()])

        print(f'Codifica del file {file}:')
        print(' '.join(codifica))
    elif cmd == 'd':
        decodifica = []
        for c in content.split():
            if c in MORSE_TABLE.keys():
                decodifica.append(MORSE_TABLE[c])

        print(f'Decodifica del file {file}:')
        print(''.join(decodifica))
