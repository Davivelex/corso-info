ripetuto = ""
volte = 0

numero = "_"

while numero != "":
    numero = input("")
    if numero == ripetuto:
        volte += 1
    elif volte > 1:
        print(ripetuto)
        volte = 1
    else:
        volte = 1

    ripetuto = numero

