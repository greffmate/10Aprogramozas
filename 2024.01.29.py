'''
def osszegzes_tetel(l:list)-> int:
    s=0
    for i in range(len(l)):
        s+=l[i]
    return s

print(osszegzes_tetel([2,3,4]))
'''

def osszegzes_osszeadassal(lista:list)->int:
    s=lista[0]
    for i in range(1,len(lista)):
        s=s+lista[i]
    return s
print(osszegzes_osszeadassal([1,2,3,4,5]))

def osszegzes(lista:list,)->int:
    s=1
    for i in range(len(lista)):
        s=s*lista[i]
    return s

print(osszegzes([1,2,3,4,5]))

def megszamlalas(lista:list, condition:bool)->int:
    c=0
    for i in range(len(lista)):
        if condition(lista[i]):
            c+=1
    return c

def paros_e(num:int)->bool:
    return num%2==0

print(megszamlalas([1,2,3,4,5],paros_e))
print(megszamlalas([1,2,3,4,5],lambda num:num%2==0))



osszeadas=lambda num1, num2: num1+num2
print(osszeadas([1,2,3,4,5], osszeadas))

def szelsoertek_kivalasztas(lista:list, condition)->tuple:
    index=0
    ertek=lista[0]
    for i in range(len(lista)):
        if condition(lista[i], ertek):
            index=i
            ertek=lista[i]
    return index,ertek
def kisebb(num1, num2):
    return num1<num2
kisebb_lambda= lambda num1, num2: num1<num2
print(szelsoertek_kivalasztas([2,6,5,3,98,4,-2,5],kisebb))
print(szelsoertek_kivalasztas([2,6,5,3,98,4,-2,5],kisebb_lambda))
print(szelsoertek_kivalasztas([2,6,5,3,98,4,-2,5],lambda num1, num2: num1<num2))


osszeadas= lambda num1, num2: num1+num2

print(osszeadas(2,3))