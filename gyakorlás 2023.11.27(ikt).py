#1. feladat: feltétel szerinti adatbekérés

intervallum_min=3
intervallum_max=15

x = input(f"Adj meg egy értéket [{intervallum_min}..{intervallum_max}]")
x = int(x)
if x > intervallum_min and x < intervallum_max:
    print("Jó számot adtál meg!")
else:
    print("Nem jó számot adtál meg!")

feltetel = False
while not feltetel:
    x = input(f"Adj meg egy értéket [{intervallum_min}..{intervallum_max}]")
    x = int(x)
    if x >= intervallum_min and x <= intervallum_max:
        feltetel = True
    else:
        print("Nem jó számot adtál meg!")


hetnapjai=["hétfő", "kedd"]
hetek=[]
for hetszama in range(x):
    lista=[]
    for nap in hetnapjai:
        ert=int(input(f"Add meg hogy hány támadás érte az állatkertet({hetszama+1}.hét {nap})"))
        lista.append(ert)
    print(lista)
    hetek.append(lista)
print(hetek)

#2. feladat

hetek_str=[]
for i in range(len(hetek)):
    lista=[]
    for j in range(len(hetek[i])):
        lista.append(str(hetek[i][j]))
        hetek_str.append(lista)

for het_szamlalo in range(len(hetek)):
    tamadasok=" ".join(hetek_str[het_szamlalo])
    print(f"{het_szamlalo}.het: {tamadasok}")

for het_szamlalo in range(len(hetek)):
    str_=str_(het_szamlalo+1)+".hét:"
    for nap_szamlalo in range(len(hetek[het_szamlalo])):
        str_+=str(hetek[het_szamlalo] [nap_szamlalo])+ " "
    print(str_)