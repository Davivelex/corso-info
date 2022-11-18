def merge(a, b):
    min_len = min(len(a), len(b))
    lista = []

    for i in range(min_len):
        lista.append(a[i])
        lista.append(b[i])

    if len(a) > len(b):
        lista += a[min_len:]
    else:
        lista += b[min_len:]

    return lista


def main():
    v1 = [1, 4, 9, 16]
    v2 = [9, 7, 4, 9, 11, 12, 31, 543]
    v3 = merge(v1, v2)

    print(v3)


if __name__ == '__main__':
    main()
