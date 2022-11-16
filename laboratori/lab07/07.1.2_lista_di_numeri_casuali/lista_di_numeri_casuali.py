from random import randint

numeri = []

for _ in range(10):
    numeri.append(randint(1, 100))

print(' '.join([str(x) for x in numeri]))
print(' '.join([str(x[1]) for x in list(filter(lambda x: x[0] % 2 == 0, enumerate(numeri)))]))
print(' '.join([str(x[1]) for x in list(filter(lambda x: x[1] % 2 == 0, enumerate(numeri)))]))
print(' '.join([str(x) for x in reversed(numeri)]))
print(numeri[0], numeri[9])