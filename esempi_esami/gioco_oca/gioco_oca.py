from random import randint


def parse(x):
    """Try to convert a str to int"""
    try:
        return int(x)
    except ValueError:
        return x


def read_file(filename):
    """Read a file and return a data structure that represent its contents"""

    # Handle OSError for file
    try:
        file = open(filename, encoding='utf-8')

        data = []
        for line in file.readlines():
            record = line.rstrip('\n').split()

            # Append to data the list with command and cell, converted to int with parse function
            data.append([parse(x) for x in record])

        # Close file and return the data structure
        file.close()
        return data
    except OSError as error:
        exit(str(error))


def play(player, board, play_round):
    if player['jail'] > 0:
        player['jail'] -= 1

        return print(f"{player['name']} bloccato per {player['jail'] + 1} turni")

    dadi = [randint(1, 6), randint(1, 6)]
    player['cell'] += sum(dadi)

    if player['cell'] > 63:
        player['cell'] -= 2 * (player['cell'] - 63)

    print(f"Turno {play_round}: {player['name']} lancio dadi: {dadi[0]} e {dadi[1]}, casella {player['cell']}")

    if player['cell'] in board:
        command = board[player['cell']]

        if command == 'PRIGIONE':
            player['jail'] = 3
            print("Sei finito in prigione, rimani bloccato per 3 turni")
        elif command == 'SALI':
            player['cell'] += 3
            print(f"Avanzi fino alla casella {player['cell']}")
        elif command == 'SCENDI':
            player['cell'] -= 3
            print(f"Retrocedi fino alla casella {player['cell']}")
        elif command == 'SCHELETRO':
            player['cell'] = 1
            print("Hai incontrato lo scheletro, ritorni alla cesella di partenza!")


def has_win(players):
    for player in players:
        if player['cell'] == 63:
            print(f"Ha vinto {player['name']}")
            return True

    return False


def main():
    board_dump = read_file('tabellone.txt')

    board = dict()
    for command, cell in board_dump:
        board[cell] = command

    # A list with two dict that represent the player of the game
    players = [
        {
            'name': 'Giocatore',
            'cell': 0,
            'jail': 0
        },
        {
            'name': 'Computer',
            'cell': 0,
            'jail': 0
        }
    ]

    who_starts = randint(0, 1)

    play_round = 0
    while True:
        play_round += 1
        play(players[who_starts], board, play_round)
        if has_win(players):
            exit()

        play(players[abs(who_starts - 1)], board, play_round)
        if has_win(players):
            exit()


if __name__ == '__main__':
    main()
