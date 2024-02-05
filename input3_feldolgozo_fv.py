def beolvas(filename):
    file = open(filename)
    sorok = file.readlines()
    file.close()
    return sorok


def feldolgozo(sorok, elsosor=0, a_vegerol_ennyi_sor_nem_kell=0):
    szamok=[]
    for i in range(1,len(sorok)):
    szamok.append(int(sorok[i].strip()))
    return szamok


szamok=feldolgoz(sorok, 1, 1)
sorok=beolvas("input3")

print(sorok)
szamok=[]


print(szamok)