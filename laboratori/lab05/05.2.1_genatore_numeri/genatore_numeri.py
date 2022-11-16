A = 32310901
B = 1729
M = 224


def gen_random(old, a, b, m):
    return (a * old + b) % m


old = int(input("Inserisci numero: "))

for _ in range(100):
    old = gen_random(old, A, B, M)
    print(old)

