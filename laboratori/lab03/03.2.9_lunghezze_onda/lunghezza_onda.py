onda = float(input("Inserisci lunghezza d'onda: "))

frequenza = 3e8/onda
tipo = ""

if onda < 1e-11:
    tipo = "Raggi Gamma"
elif 1e-11 <= onda < 1e-8:
    tipo = "Raggi X"
elif 1e-8 <= onda < 4e-7:
    tipo = "Ultravioletti"
elif 4e-7 <= onda < 7e-7:
    tipo = "Luce visibile"
elif 7e-7 <= onda < 1e-3:
    tipo = "Infrarossi"
elif 1e-3 <= onda < 1e-1:
    tipo = "Microonde"
else:
    tipo = "Onde radio"

print("%s %f %f" % (tipo, onda, frequenza))
