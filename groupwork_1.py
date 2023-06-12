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
    return v

print(objetosc_kuli(3))

# testy sprawdzające działanie funkcji dla sześcianu
assert szescian(6) == (216, 216)
assert szescian(4) == (96, 64)