towns = {}
regions = []

file = open('elenco-comuni-italiani.csv')
for line in file.read().split('\n')[1:]:
    town = line.split(';')
    if town[10] in towns.keys():
        towns[town[10]].append(town[6])
    else:
        towns[town[10]] = [town[6]]

file = open('regioni.txt')
for line in file.read().split('\n'):
    regions.append(line)

for region in regions:
    print(f'*** REGIONE {region} ***')
    print(f'Nella regione {region} ci sono {len(towns[region])} comuni')
    shortest = longest = towns[region][0]
    for town in towns[region]:
        if (len(town) == len(shortest) and town < shortest) or len(town) < len(shortest):
            shortest = town
        if (len(town) == len(longest) and town < longest) or len(town) > len(longest):
            longest = town

    print(f'Il nome più breve è {shortest} e quello più lungo è {longest}\n')

