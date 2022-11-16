from csv import reader


def leggi_csv(filename):
    try:
        file = open(filename, 'r')
        return list(reader(file))
    except IOError:
        print(f'Non è possibile aprire il file {filename}')


def confronto_date(da, a, data):
    da = ''.join(da.split('/')[0:2][::-1])
    a = ''.join(a.split('/')[0:2][::-1])
    data = ''.join(data.split('/')[0:2][::-1])

    if da == '1222' and data >= da:
        return True
    elif a == '0120' and data <= a:
        return True
    else:
        return da <= data <= a


def zodiaco(segni, sportivo):
    for segno in segni:
        if confronto_date(segno[1], segno[2], sportivo[3]):
            return segno[0]


def print_segno(massimo, goal, segno):
    numero = int(50 * (goal / massimo))
    print(f'{segno:15}{"*"*numero}')


def main():
    goal = {}

    segni = leggi_csv('zodiaco.csv')
    for segno in segni:
        goal[segno[0]] = 0

    sportivi = leggi_csv('sportivi.csv')
    for sportivo in sportivi:
        goal[zodiaco(segni, sportivo)] += int(sportivo[1])

    for segno in sorted(segni, key=lambda x: goal[x[0]], reverse=True):
        print_segno(max(goal.values()), goal[segno[0]], segno[0])


if __name__ == '__main__':
    main()
