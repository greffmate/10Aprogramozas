def f(x:int,y:int)->int:
    '''
    f(x,y)=3x+2y
    '''
    return 3*x+2*y
print(f(2,3))

print(f(3,2))

f(x=4,y=8)
print("fjksdadjklsh", end="")

x=print("szia")
print(x)

if( print("valami")==None):
    print("None-nal tért vissza")


def ki(x:any)->None:
    print(x)
    return

x=ki("géza")
if x==None:
    print("nem volt visszatérési érték")

import math as m
def masodfoku(a:float,b:float,c:float):
    '''
    Másodfokú megoldóképlet
    return -1: a = 0
    return -2: diszkrimináns < 0
    return int: 1 zérushely
    return tuple: 2 zérushely
    '''
    if a==0:
        return -1
    d=b**2-4*a*c
    if d<0:
        return -2

    if d==0:
        return (-b  )/  (2*a)
    
    x1=(-b+ m.sqrt(d)  )/  (2*a)
    x2=(-b- m.sqrt(d)  )/  (2*a)

    return x1,x2
x=masodfoku(0,3,1)
if x==-1:
    print("az érték 0 volt")
if x==-2:
    print("a diszkrimináns kisebb, mint 0")
if type(x)==type(tuple()):
    print("2 zérushelyünk van")
if type(x)==type(int()):
    print("1 zérushelyünk van")

#ez igy nem jo megoldas mert a zerushelyunk lehet -1, es -2 is akar, tehat igy nem adunk vissza erteket

class A_NULLA(Exception):
    pass
class DISZKRIMINANS_KISEBB_NULLÁNÁL(Exception):
    pass

def masodfoku_hibadobassal(a:float,b:float,c:float):
    '''
    Másodfokú megoldóképlet
    ha a=0: a = NULLA hiba
    ha a diszkriminans DISZKRIMINANS_KISEBB_NULLÁNÁL hiba
    return int: 1 zérushely
    return tuple: 2 zérushely
    '''
    if a==0:
        raise A_NULLA
    d=b**2-4*a*c
    if d<0:
        raise DISZKRIMINANS_KISEBB_NULLÁNÁL
    if d==0:
        return (-b  )/  (2*a)
    
    x1=(-b+ m.sqrt(d)  )/  (2*a)
    x2=(-b- m.sqrt(d)  )/  (2*a)

    return x1,x2

try:
    x=masodfoku_hibadobassal(0,1,2)
except A_NULLA:
    print("az 'a' értéke 0")
except DISZKRIMINANS_KISEBB_NULLÁNÁL:
    print("A diszkrimináns kisebb nullánál")

print("valami")

def ossezgzes_tetel(l:list)-> int:
    '''
    osszegzes prog. tetel
    return elemek osszege
    '''
    s=0
    for i in range(len(l)):
        s+=l[i]
    return s

print(ossezgzes_tetel([2,3,4]))


def megszamolas(l:list):
    c=0
    for i in range(len(l)):
        c+=1
    return c
print(megszamolas([1,2,34,2,24]))
def maxert(l:list):
    maxert = 0
    maxindex = 0
    for i in range(len(l)):
        if l[i] > maxert:
            maxert = l[i]
            maxindex = i
    return maxert, maxindex
print(maxert([1,4,62,52,532]))
def kereses(l:list):
    kszam = int(input("add meg a parameter elejet"))
    kszam = int(input("add meg a parameter veget"))
    for i in range(len(l)):
        if l[i] == x:
            return i+1, x
print(kereses(l=[23,45,36,21,2], x=3))
def eldontes(l:list, x):
    n = len(x)-1
    i = 1
    while <= N and not (Tl[i])