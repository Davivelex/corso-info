def buffer(v):
    return v[1:] + [v[0]]


def main():
    v1 = [1, 2, 3, 4, 5, 6, 7]
    v2 = buffer(v1)
    print(f'Lista originale {v1}')
    print(f'Lista modificata {v2}')


if __name__ == '__main__':
    main()