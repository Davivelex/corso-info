a = float(input("Inserisci un numero: "))
b = float(input("Inserisci un numero: "))
c = float(input("Inserisci un numero: "))

if a > b:
    if b > c:
        print("decreasing")
    else:
        print("neither")
else:
    if c > b:
        print("increasing")
    else:
        print("neither")
