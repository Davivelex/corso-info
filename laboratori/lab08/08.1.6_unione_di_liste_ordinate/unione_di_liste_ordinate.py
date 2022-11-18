def merge_sorted(a, b):
    lista = []

    while len(a) and len(b):
        if a[0] <= b[0]:
            lista.append(a.pop(0))
        else:
            lista.append(b.pop(0))

    lista += a
    lista += b

    return lista


def main():
    v1 = [1, 4, 9, 16]
    v2 = [4, 7, 9, 9, 11]
    v3 = merge_sorted(v1, v2)

    print(v3)


if __name__ == '__main__':
    main()
