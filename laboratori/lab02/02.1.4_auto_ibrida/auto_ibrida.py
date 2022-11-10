costo = float(input("Prezzo: "))
km_percorsi = float(input("Km percorsi: "))
costo_carburante = float(input("Costo carburante: "))
efficienza = float(input("Efficienza km/l: "))
rivendita = float(input("Valore rivendita dopo 5 anni: "))

costo_uso = km_percorsi / (costo_carburante * efficienza) * 5
print(f"Costo di proprietà: {costo_uso + costo}")