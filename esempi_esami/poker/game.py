from poker import *

players = []
table = []
n_players = 3

for i in range(n_players):
    players.append([])

generate_deck()
random.shuffle(deck)

for i in range(n_players):
    players[i] = players[i] + take_cards(2)

table = table + take_cards(3)
table = table + take_cards(1)
table = table + take_cards(1)

for player in players:
    cards = player + table
    print(count_repeats(cards)[1])

