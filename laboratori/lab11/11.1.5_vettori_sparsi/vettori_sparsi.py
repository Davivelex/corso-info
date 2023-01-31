def sparse_array_sum(array_a:dict, array_b:dict) -> dict:
    positions = set(array_a.keys()).union(set(array_b.keys()))

    array_c = {}
    for pos in positions:
        array_c[pos] = 0

        if pos in array_a:
            array_c[pos] += array_a[pos]

        if pos in array_b:
            array_c[pos] += array_b[pos]

    return array_c


def main():
    array_a = {5:4, 9:2, 10:9}
    array_b = {5:6, 8:9, 10:1}
    array_c = sparse_array_sum(array_a, array_b)

    print(array_c)


if __name__ == '__main__':
    main()