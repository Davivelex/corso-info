import random

deck = list()

NUMBERS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
NUMBERS_VALUE = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                 '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
CLUBS = ['C', 'Q', 'F', 'P']


def generate_deck():
    for number in NUMBERS:
        for club in CLUBS:
            deck.append({
                'number': number,
                'club': club
            })


def write_deck():
    try:
        deck_file = open('mazzo.txt', 'w')
        for card in deck:
            deck_file.write(f"{card['number']} {card['club']}\n")
    except OSError as error:
        print(f'Non è stato possibile aprire o scrivere su file: {error}')


def take_cards(c=5):
    cards = []

    for _ in range(c):
        cards.append(deck.pop())

    return cards


def count_repeats(cards):
    repeats = set()
    what_repeats = list()

    for number in NUMBERS:
        count = 0

        for card in cards:
            if card['number'] == number:
                count += 1

        if count > 1:
            repeats.add(count)
            what_repeats.append({
                'card': number,
                'repeat': repeats
            })

    return repeats, what_repeats


def is_pair(cards):
    return count_repeats(cards)[0] == {2}


def is_double_pair(cards):
    return count_repeats(cards)[0] == {2, 2}


def is_tris(cards):
    return count_repeats(cards)[0] == {3}


def is_flush(cards):
    numbers = sorted([NUMBERS_VALUE[i['number']] for i in cards])

    for i in range(1, 5):
        if numbers[i] - numbers[i - 1] != 1:
            return False

    return True


def is_full_house(cards):
    return count_repeats(cards)[0] == {2, 3}


def is_color(cards):
    first_card = cards[0]

    for card in cards:
        if first_card['club'] != card['club']:
            return False

    return True


def is_poker(cards):
    return count_repeats(cards)[0] == {4}


def is_royal_flush(cards):
    return is_color(cards) and is_flush(cards)


def print_combo(cards):
    combo = "Niente..."

    if is_pair(cards):
        combo = "Coppia"
    elif is_double_pair(cards):
        combo = "Doppia coppia"
    elif is_tris(cards):
        combo = "Tris"
    elif is_flush(cards):
        combo = "Scala"
    elif is_full_house(cards):
        combo = "Full"
    elif is_color(cards):
        combo = "Colore"
    elif is_poker(cards):
        combo = "Poker"
    elif is_royal_flush(cards):
        combo = "Scala reale"

    print(" ".join([f"%2s%s" % (card['number'], card['club']) for card in cards]), combo)


def main():
    generate_deck()
    random.shuffle(deck)
    write_deck()

    while len(deck) >= 5:
        print_combo(take_cards())

main()
