from math import sqrt

linee = set()
posizioni = {}
velocita = {}
distanza = {}
misure = {}

def leggi_file(filename):
    try:
        file = open(filename, 'r', encoding='utf-8')

        data = []
        for line in file.readlines():
            line = line.rstrip('\n').split()
            line = [int(x) for x in line]

            data.append({
                'ID': line[0],
                'linea': line[1],
                'pos': (line[2], line[3]),
                'time': line[4]
            })

        file.close()
        return data
    except OSError as error:
        exit(str(error))

def move(record):
    code = record['ID']
    new_pos = record['pos']
    new_time = record['time']
    old_pos = posizioni[code]
    old_time = misure[code][1]

    spostamento = abs(new_pos[0] - old_pos[0]) + abs(new_pos[1] - old_pos[1])
    delta_t = new_time - old_time

    distanza[code] += spostamento
    velocita[code].append(spostamento / delta_t)
    posizioni[code] = new_pos
    misure[code] = (misure[code][0], new_time)

def format_time(s):
    h = s // 3600
    m = (s % 3600) // 60
    s = s % 60

    return f"{h:02}:{m:02}:{s:02}"


def avg_speed(v):
    return sum(v)/len(v)*3.6


def main():
    database = leggi_file('database.txt')

    for record in database:
        code = record['ID']
        pos = record['pos']
        time = record['time']

        if code not in posizioni:
            posizioni[code] = pos
            distanza[code] = 0
            velocita[code] = []
            misure[code] = (time, time)
            linee.add(code)
        else:
            move(record)

    print('Distanza percorsa dai pullman: ')
    for linea in linee:
        print(f'{linea}: {distanza[linea]} m - Prima misura: {format_time(misure[linea][0])} - Ultimo misura: '
              f'{format_time(misure[linea][1])}')

    print('\nVelocità media dei pullman: ')
    for linea in linee:
        print(f'{linea}: {avg_speed(velocita[linea]):.2f} km/h')


if __name__ == '__main__':
    main()
