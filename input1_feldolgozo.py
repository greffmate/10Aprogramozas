
file = open("input3")
sorok = file.readlines()
file.close()

print(sorok)

szamok=[]
for i in range(len(sorok)):
    szam_str=[i].strip()
    #print(szam_str)
    szam=int(szam_str)
    #print(szam)
    szamok.append(szam)
print(szamok)

osszeg=0
for i in range(len(szamok)):
    osszeg+=szamok[i]
print(osszeg)


#rövidebben
file = open("20240205/input3")
sorok = file.readlines()
file.close()

szamok=[]
for i in range(len(sorok)):
    szam=int(sorok[i].strip())
    szamok.append()
print(szamok)
