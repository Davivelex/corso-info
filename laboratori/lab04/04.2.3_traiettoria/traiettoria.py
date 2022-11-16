DELTA_T = 0.01
g = 9.81

s = 0
v0 = float(input("Inserisci velocità iniziale: "))
t = float(input("Secondi simulati: "))
v = v0

print(f"Simulazione     Formula         Tempo")

for i in range(int(t * 100) + 1):
    v = v - g * DELTA_T
    s = s + v * DELTA_T
    formula = -0.5 * g * (i / 100) ** 2 + v0 * (i / 100)

    print(f"{s:.3f}{formula:16.3f}{i/100:16.3f}")
