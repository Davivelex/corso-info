A = float(input("Inserisci il valore A: "))
B = float(input("Inserisci il valore B: "))
C = float(input("Inserisci il valore C: "))
D = float(input("Inserisci il valore D: "))
X0 = int(input("Inserisci popolazione prede: "))
Y0 = int(input("Inserisci popolazione predatori: "))
T = int(input("Inserisci numero di intervalli: "))

X = X0
Y = Y0

for i in range(T):
    X1 = X*(1+A-B*Y)
    Y1 = Y*(1-C+D*X)
    X = X1
    Y = Y1
    print(f"Le prede sono {int(X)}")
    print(f"I predatori sono {int(Y)}")

