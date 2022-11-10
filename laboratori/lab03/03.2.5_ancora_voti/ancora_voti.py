from math import *

voto = float(input("Inserisci voto: "))
conversione = ""

VOTI = ['F', 'D', 'C', 'B', 'A']

while voto < 0 or voto > 4:
    voto = float(input("Voto non valido, riprova: "))

p_intera = floor(voto)
mantissa = voto - p_intera

if mantissa < 0.15:
    conversione = VOTI[p_intera]
elif 0.15 <= mantissa < 0.5:
    conversione = VOTI[p_intera]
    if p_intera != 0:
        conversione += '+'
elif 0.5 <= mantissa < 0.85:
    conversione = VOTI[p_intera + 1]
    conversione += '-'
else:
    conversione = VOTI[p_intera + 1]

print(conversione)
