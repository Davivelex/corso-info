def neighbor_average(values, row, column):
    neighbor_sum = element = 0

    for i in range(max(row-1, 0), min(row+1, len(values))+1):
        for j in range(max(column-1, 0), min(column+1, len(values[0]))+1):
            if i == row and j == column:
                continue

            neighbor_sum += values[i][j]
            element += 1

    return neighbor_sum / element


def main():
    tabella = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f'Neighbor average: {neighbor_average(tabella, 1, 1):.2f}')


if __name__ == '__main__':
    main()
