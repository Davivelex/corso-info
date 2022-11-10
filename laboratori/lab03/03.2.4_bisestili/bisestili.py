anno = 0

while anno < 1851:
    anno = int(input("Inserisci anno: "))

if anno % 4 and anno % 100 != 0 or anno % 400 == 0:
    print(f"Il {anno} è un anno bisestile")
else:
    print(f"Il {anno} non è un anno bisestile")