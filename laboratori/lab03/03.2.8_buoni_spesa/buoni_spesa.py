spesa = float(input("Inserisci spesa: "))
buono = 0

if 10 <= spesa < 60:
    buono = spesa * 0.08
elif 60 <= spesa <= 150:
    buono = spesa * 0.1
elif 150 <= spesa < 210:
    buono = spesa * 0.12
elif spesa >= 210:
    buono = spesa * 0.14

print(f"Il buono ha il valore di {buono} $")