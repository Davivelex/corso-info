from math import *

velocita = float(input("Inserire volocità di lancio: ")) / 3.6

velocita_fuga = sqrt(2 * 6.67e-11 * 2.2e14 / 9.4e3)

if velocita < velocita_fuga:
    print("* La persona non ritorna sulla superficie")
else:
    print("* La persona ritorna sulla superficie")