from math import sqrt


def crivello(n):
    numbers  = list(range(2, n+1))
    limit = sqrt(n)

    for i in range(2, 17):
        for j in range(2, n):
            if i*j in numbers:
                numbers.remove(i*j)

    return numbers


print(crivello(100000))
