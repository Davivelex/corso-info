from math import pi, sqrt


def sphere_volume(r):
    return (4/3)*pi*(r**3)


def sphere_surface(r):
    return 4*pi*(r**2)


def cylinder_volume(r, h):
    return pi*(r**2)*h


def cylinder_surface(r, h):
    return 2*pi*r*h + pi*(r ** 2)


def cone_volume(r, h):
    return (1/3)*cylinder_volume(r, h)


def cone_surface(r, h):
    return sqrt(h**2 + r**2) * r * pi + pi*(r ** 2)


raggio = float(input("Inserisci raggio: "))
altezza = float(input("Inserisci altezza: "))

print("Volume sfera: ", sphere_volume(raggio))
print("Superficie sfera: ", sphere_surface(raggio))
print("Volume cilindro: ", cylinder_volume(raggio, altezza))
print("Superficie cilindro", cylinder_surface(raggio, altezza))
print("Volume cono: ", cone_volume(raggio, altezza))
print("Superficie cono: ", cone_surface(raggio, altezza))
