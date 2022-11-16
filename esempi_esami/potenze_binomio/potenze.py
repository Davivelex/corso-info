from math import factorial


def binomial(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def tartaglia(N):
    li1 = []

    for i in range(0, N + 1):
        li2 = []
        for j in range(0, i + 1):
            li2.append(binomial(i, j))

        li1.append(li2)

    return li1


def print_mono(t, n):
    if n == 0:
        return ''
    if n == 1:
        return t
    else:
        return f'{t}^{n}'


def binomio(a, b, n):
    coefficients = tartaglia(n)[n]
    terms = []

    for i in range(n + 1):
        coefficient = (a ** (n - i)) * (b ** i) * coefficients[i]
        terms.append(f"{coefficient:.1f} {print_mono('x', n-i)} {print_mono('y', i)}")

    return terms


if __name__ == '__main__':
    def main(f):
        lines = [x.replace('\n', '') for x in f.readlines()]
        a, b = [int(n) for n in lines[0].split()]
        ns = [int(n) for n in lines[1:]]

        print(f'Potenze del binomio ({a:.1f}x + {b:.1f}y)^N')
        for n in ns:
            print(f'N = {n}')
            print(' + '.join(binomio(a, b, n)))


    try:
        file = open('potenze.txt', 'r')
        main(file)
    except OSError:
        print('Non è possibile aprire il file')
