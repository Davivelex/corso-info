def leggi_file(filename):
    try:
        file = open(filename, 'r', encoding='utf-8')
        data = []

        for line in file.readlines():
            line = list(line.rstrip('\n'))
            data.append(line)

        file.close()
        return data
    except OSError as error:
        exit(str(error))


def check_corridor(i, j, maze):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    corridors = set()

    for d in dirs:
        x = i + d[0]
        y = j + d[1]

        if 0 <= x < len(maze) and 0 <= y < len(maze[0]):
            corridors.add((x, y))

    return corridors


def main():
    maze = leggi_file('../11.2.4_filo_di_arianna/maze.txt')
    corridors = {}

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            adjacent = check_corridor(i, j, maze)

            if len(adjacent) != 0 and maze[i][j] != '*':
                corridors[(i, j)] = adjacent

    print(corridors)


if __name__ == '__main__':
    main()
