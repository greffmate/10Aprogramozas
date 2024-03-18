"""
1. Fájl átnevezése: osztály_név.py

Feladatok:
1. A beolvas fv-ben valósítsd meg, hogy a paraméterben megadott fájlt beolvassa, és térjen vissza a szám listával az átalakítások után
2. A feladat1,2 stb fv-ben valósítsd meg a kért eljárásokat! A fájl beolvasásához használd a beolvas() függvényedet!
3. feladat1(): számold ki a fájlokban található számok összegét a tanult prog tétel segítségével!
4. feladat2(): számold ki a fájlokban található számok átlagát a tanult prog tétel segítségével!
5. feladat3(): számold ki a fájlokban található számok minimumát a tanult prog tétel segítségével!
6. feladat4(): számold ki a fájlokban található számok maximumát a tanult prog tétel segítségével!

Input fájlok használata:
feladat1() -> input1
feladat2() -> input2
feladat3() -> input3
feladat4() -> input3
"""

"---beolvasas---"
def beolvas(filename, elsosor, vege):
    file = open(filename)
    sor = file.readlines()
    file.close()
    szamok = []
    for i in range(elsosor, len(sor)-vege):
        szamok.append(int(sor[i].strip()))
    return szamok

"---1.feladat---"
def feladat1(filename,elsosor,vege):
    lista = beolvas(filename,elsosor,vege)
    osszeg = 0
    for i in range(len(lista)):
        osszeg += lista[i]
    print(osszeg)

"---2.feladat---"
def feladat2(filename,elsosor,vege):
    lista = beolvas(filename,elsosor,vege)
    osszeg = 0
    for i in range(len(lista)):
        osszeg += lista[i]
    atlag = osszeg/len(lista)
    print(atlag)

"---3.feladat---"
def feladat3(filename,elsosor,vege):
    lista = beolvas(filename,elsosor,vege)
    kicsi = lista[0]
    for i in range(1,len(lista)):
        if lista[i]<=kicsi:
            kicsi = lista[i]
    print(kicsi)

"---4.feladat---"
def feladat4(filename,elsosor,vege):
    lista = beolvas(filename,elsosor,vege)
    max = lista[0]
    for i in range(1,len(lista)):
        if lista[i]>=max:
            max = lista[i]
    print(max)

feladat1("doga/input1.txt", 0,0)
feladat2("doga/input2.txt",2,0)
feladat3("doga/input3.txt",1,1)
feladat4("doga/input3.txt",1,1)