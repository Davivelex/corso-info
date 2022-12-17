data = input('Inserisci dati: ')
elenco = [int(x) for x in data.split(':')]

no_min_max = elenco.copy()
no_min_max.remove(min(no_min_max))
no_min_max.remove(max(no_min_max))
print(':'.join([str(x) for x in no_min_max]))

only_pair = elenco.copy()
only_pair = list(filter(lambda x: x % 2 == 0, only_pair))
print(':'.join([str(x) for x in only_pair]))

only_two_digit = elenco.copy()
only_two_digit = list(filter(lambda x: 10 <= x <= 99, only_two_digit))
print(':'.join([str(x) for x in only_two_digit]))
