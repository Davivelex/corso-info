DIRECTIONS = [
    (0, 1),  # Right (0)
    (1, 0),  # Downward (1)
    (0, -1),  # Left (2)
    (-1, 0)  # Upward (3)
]


def move_in_direction(pos, direction):
    x0, y0 = DIRECTIONS[direction]
    x, y = pos

    return x + x0, y + y0


def change_direction(direction):
    return (direction + 1) % 4


def is_corner(spiral, pos):
    n = len(spiral)
    x, y = pos

    return x == n or y == n or spiral[x][y] != 0


def fill_spiral(spiral, fill_number, pos, direction):
    if fill_number == len(spiral) ** 2 + 1:
        return spiral

    x, y = pos[0], pos[1]

    spiral[x][y] = fill_number
    if is_corner(spiral, move_in_direction(pos, direction)):
        direction = change_direction(direction)

    next_pos = move_in_direction(pos, direction)

    return fill_spiral(spiral, fill_number + 1, next_pos, direction)


def gen_empty_spiral(n):
    spiral = []
    for _ in range(n):
        spiral.append([0] * n)

    return spiral


def main():
    spiral = fill_spiral(gen_empty_spiral(20), 1, (0, 0), 0)

    for line in spiral:
        print(' '.join([f'{i:03}' for i in line]))


if __name__ == '__main__':
    main()
