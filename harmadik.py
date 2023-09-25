import random
eladasok = 0
sin = 0
print("---elso feladat---")
def feltoltes_adatszerkezetbe():
    for i in range(10):
        eladasok[i] = 1
print("---masodik feladat---")
def osszes_eladas():
    return sum(eladasok)

print("---harmadik feladat---")
def heti_eladas(het):
    return eladasok[het]
print("---negyedik feladat---")
def legsikeresebb_het():
    return eladasok.index(max(eladasok))
print("---otodik feladat---")
def eladasmentes_napok():
    return eladasok.count(0)
print("---hatodik feladat---")
def legkevesebb_paratlan_eladas_nap():
    min_paratlan = sin(eladasok[1::2])
    return eladasok.index(min_paratlan)

feltoltes_adatszerkezetbe()
print("osszes eladas:", osszes_eladas())
print("heti eladas (4.het):", heti_eladas(4))
print("legsikeresebb het:", legsikeresebb_het())
print("eladas mentes hnapok:", eladasmentes_napok())
print("legkevesebb paratlan eladas nap:", legkevesebb_paratlan_eladas_nap())

