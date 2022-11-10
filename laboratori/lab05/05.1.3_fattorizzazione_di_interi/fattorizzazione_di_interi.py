def is_prime(numero):
    if numero < 2:
        return False

    for n in range(2, numero):
        if n == 1:
            continue
        elif numero % n == 0:
            return False

    return True


def print_prime(n):
    for i in range(0, n):
        if is_prime(i) and n % i == 0:
            print(i)
            print_prime(n // i)
            break


number = int(input("Inserisci numero: "))
print_prime(number)
