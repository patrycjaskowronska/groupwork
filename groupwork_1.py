#Zadanie A
import math

#Funkcja licząca objętość sześcianu i jego pole powierzchn

def szescian(a):
    p = 6 * pow(a,2)
    v =pow(a,3)
    return p, v


print(szescian(5))

#funkcja licząca objętość kuli,
def objetosc_kuli(r):
    v = 4/3 * math.pi * pow(r,3)
    return round(v,3)

print(objetosc_kuli(3))

#testy sprawdzające objętość kul

assert objetosc_kuli(5) == round((500/3) * math.pi,3)
assert objetosc_kuli(6) == round(288 * math.pi,3)

