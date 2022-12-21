def leggi_file(filename):
    try:
        data = []
        file = open(filename, 'r', encoding='utf-8')

        for line in file.readlines():
            line = line.rstrip('\n').split(' ')
            data.append(line)

        file.close()
        return data
    except IOError:
        print(f'Impossibile leggere il file {filename}')\


def is_top(piramidi, i, j):
    dirs = [(1, 1), (1, 0), (1, -1),  (1, 0), (-1, 0), (-1, 1), (-1, 0), (-1, -1)]
    n = len(piramidi)

    for dir_x in dirs:
        check = (i+dir_x[0], j+dir_x[1])

        if 0 <= check[0] < n and 0 <= check[1] < n:
            if piramidi[check[0]][check[1]] >= piramidi[i][j]:
                return False

    return True

def main():
    piramidi = leggi_file('mappa.txt')

    for i in range(len(piramidi)):
        for j in range(len(piramidi)):
            if is_top(piramidi, i, j):
                print(piramidi[i][j], i, j)


if __name__ == '__main__':
    main()
