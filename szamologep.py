print("1. Összeadás")
print("2. Öszeszorzás")
print("3. Átlag")
while True:
    valaszstr=input("Menüpont száma")
    if valaszstr.isdecimal():
        valasz=int(valaszstr)
        break

def add(x,y):
    sum=x+y
    return sum

def szoroz(x,y):
    sum = x*y
    return sum

def atlag(x,y):
    sum = add(x,y)
    return sum/2

def megad():
    szam1=int(input("Első szám: "))
    szam2=int(input("Második szám: "))
    return(szam1,szam2)

if valasz == 1:
        szam1,szam2=megad()
        print(add(szam1,szam2))
elif valasz == 2:
        szam1,szam2=megad()
        print(szoroz(szam1,szam2))

elif valasz == 3:
         szam1,szam2 = megad()
         print(atlag(szam1,szam2))