def beolvas(filename):
    file = open(filename, encoding='utf-8')
    sor = file.read()
    file.close()
    dol = sor.split(",")
    lista = []
    for i in range(1,len(dol)-1):
        lista.append(int(dol[i]))
    return(lista)


def feladat1(filename):
    lista = beolvas(filename)
    osszeg = 0
    for i in range(len(lista)):
        osszeg += lista[i]
    return(osszeg)


def feladat2(filename):
    lista = beolvas(filename)
    osszeg = 0
    for i in range(len(lista)):
        osszeg += lista[i]
    atlag =  osszeg/len(lista)
    return(atlag)


def feladat3(filename):
    lista = beolvas(filename)
    minimum = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < minimum:
            minimum = lista[i]
    return(minimum)
    
"---4.feladat---"
def feladat4(filename):
    list = beolvas(filename)
    maximum = list[0]
    for i in range(1, len(list)):
        if list[i] > maximum:
            maximum = list[i]
    print(maximum)
    

print(f"1. Feladat:{feladat1("input")}")
print(f"2. Feladat:{feladat2("input")}")
print(f"3. Feladat:{feladat3("input")}")
print(f"4. feladat:{feladat4('input.txt')}")