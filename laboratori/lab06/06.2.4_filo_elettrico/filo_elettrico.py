from math import pi


def diameter(wire_gauge):
    return 2 * wire_gauge


def copper_wire_resistance(length, wire_gauge):
    return (4 * 1.678e-8 * length) / (pi * diameter(wire_gauge) ** 2)


def aluminum_wire_resistance(length, wire_gauge):
    return (4 * 2.82e-8 * length) / (pi * diameter(wire_gauge) ** 2)


gauge = float(input("Inserisci raggio filo: "))
le = float(input("Inserisci lunghezza: "))
print(f"Rame: {copper_wire_resistance(le, gauge):.3f} Ohm\nAlluminio: {aluminum_wire_resistance(le, gauge):.3f} Ohm")
