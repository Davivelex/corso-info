numero = ""

while not numero.isdigit() or not len(numero) == 10:
    numero = input("Inserire numero telefonico: ")

formato = f"({numero[:3]}) {numero[3:6]}-{numero[6:]}"

print(formato)