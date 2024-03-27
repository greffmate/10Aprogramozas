"""
1. Fájl átnevezése: osztály_név.py

Feladatok:
1. A beolvas fv-ben valósítsd meg, hogy a paraméterben megadott fájlt beolvassa, és térjen vissza a szám listával az átalakítások után
2. A feladat1,2 stb fv-ben valósítsd meg a kért eljárásokat! A fájl beolvasásához használd a beolvas() függvényedet!
3. feladat1(): számold ki a fájlban található számok összegét a tanult prog tétel segítségével!
4. feladat2(): számold ki a fájlban található számok átlagát a tanult prog tétel segítségével!
5. feladat3(): számold ki a fájlban található számok minimumát a tanult prog tétel segítségével!
6. feladat4(): számold ki a fájlban található számok maximumát a tanult prog tétel segítségével!

Kiírások:
feladat1: [eredmény]
feladat2: [eredmény]
feladat3: [eredmény]
feladat4: [eredmény]
A ": " után csak az eremény szerepeljen

A dolgozat python fájlját küldd el a andrasi.norbert@puskas.hu-ra az alábbi tárggyal:
[osztály][filebeolvasas2] név
"""

"---beolvasás---"
def beolvas(filename):
    file = open(filename, encoding='utf-8')
    sor = file.read()
    file.close()
    adatok = sor.split(",")
    lista = []
    for i in range(1,len(adatok)-1):
        lista.append(int(adatok[i]))
    return(lista)

"---1.feladat---"
def feladat1(filename):
    lista = beolvas(filename)
    osszeg = 0
    for i in range(len(lista)):
        osszeg += lista[i]
    return(osszeg)

"---2.feladat---"
def feladat2(filename):
    lista = beolvas(filename)
    osszeg = 0
    for i in range(len(lista)):
        osszeg += lista[i]
    atlag =  osszeg/len(lista)
    return(atlag)

"---3.feladat---"
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
    

print(f"1. feladat:{feladat1('input.txt')}")
print(f"2. feladat:{feladat2('input.txt')}")
print(f"3. feladat:{feladat3('input.txt')}")
print(f"4. feladat:{feladat4('input.txt')}")