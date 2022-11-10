lunga = ""
breve = ""

BASI = ['A', 'C', 'T', 'G']

posizioni = []

def controllo(seq):
    for base in seq:
        if base not in BASI:
            return False

    return True


while len(lunga) != 20 or not controllo(lunga):
    lunga = input("Inserisci una sequenza da 20 basi: ")

while len(breve) != 3 or not controllo(breve):
    breve = input("Inserisci una sequenza da 3 basi: ")

for pos in range(17):
    if lunga[pos:pos+3] == breve:
        posizioni.append(str(pos))

if len(posizioni) != 0:
    print("* La sequenza lunga contiene la breve")
    print(f"* La breve è presente dalle posizioni {', '.join(posizioni)}")
    print(f"* Compare un totale di {len(posizioni)} volte")
else:
    print("* La sequenza breve non è presente nella lunga")