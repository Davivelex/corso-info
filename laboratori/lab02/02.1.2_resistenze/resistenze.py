def serie(r1, r2):
    return r1 + r2


def parallelo(r1, r2):
    return (r1 * r2) / (r1 + r2)


R1 = float(input("Inserisci resistenza 1: "))
R2 = float(input("Inserisci resistenza 2: "))
R3 = float(input("Inserisci resistenza 3: "))

r_eq = serie(R1, parallelo(R2, R3))

print(f"Resistenza equivalente: {r_eq} Ohm")