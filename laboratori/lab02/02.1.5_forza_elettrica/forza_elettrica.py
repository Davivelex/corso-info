Q1 = float(input("Inserire carica 1: "))
Q2 = float(input("Inserire carica 2: "))
R = float(input("Inserire distanza: "))

EPSILON = 8.854e-12
PI = 3.14159265358979

forza = (Q1 * Q2) / (4 * PI * EPSILON * (R ** 2))

print(f"La forza tra le particelle è {forza:.02} N")