def is_prime(numero):
    if numero < 2:
        return False

    for n in range(2, numero):
        if n == 1:
            continue
        elif numero % n == 0:
            return False

    return True


num = int(input("Inserisci un numero: "))
for i in range(num):
    if is_prime(i):
        print(i)
