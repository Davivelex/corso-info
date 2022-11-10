MATR_A = input("Inserisci prima matricola: ")
MATR_B = input("Inserisci seconda matricola: ")

if MATR_A[1:] <= MATR_B[1:]:
    print(MATR_A)
    print(MATR_B)
else:
    print(MATR_B)
    print(MATR_A)
