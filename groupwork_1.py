#Zadanie A
import math

#Funkcja licząca objętość sześcianu i jego pole powierzchn

def szescian(a):
    p = 6 * pow(a,2)
    v =pow(a,3)
    return p, v


print(szescian(5))

#funkcja licząca objętość stożka,
def objetosc_stozka(r,h):
    v = 1/3 * math.pi * pow(r,2) * h

    return v
#jest to ostrosłup z czworokątem w podstawie
def objetosc_ostroslupa(a,b,h):
    v = 1/3 * a * b * h

    return v

#testy sprawdzające objętość stozka i ostroslupa

assert objetosc_stozka(4,3) == 16 * math.pi
assert objetosc_ostroslupa(2,2,6) == 8




# testy sprawdzające działanie funkcji dla sześcianu
assert szescian(6) == (216, 216)
assert szescian(4) == (96, 64)