stringa = input("Inserisci una stringa: ")

if stringa.isalnum():
    if stringa.isalpha():
        print("* Contiene solo lettere")
        if stringa.upper() == stringa:
            print("* Contiene solo lettere maiuscole")

        if stringa.islower() == stringa:
            print("* Contiene solo lettere minuscole")
    elif stringa.isdecimal():
        print("* Contiene solo cifre numeriche decimali")
    else:
        print("* Contiene soltanto lettere e cifre")


if stringa.upper()[0] == stringa[0] and stringa[0].isalpha():
    print("* Inizia con una lettera maiuscola")

if stringa[-1] == '.':
    print("* Termina con un punto")