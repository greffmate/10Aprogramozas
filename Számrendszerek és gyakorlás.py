def fejlec(cim):
    szelesseg=30
    cim = "Programcíme"
    csillagok= "*"*szelesseg
    kozepso_csillag= "*"*int((szelesseg-len(cim))/2)
    print(csillagok)
    print(kozepso_csillag+cim+kozepso_csillag)
    print(csillagok)

program_neve = "Programcíme"
fejlec(program_neve)

#teszt=""
#for i in range(2,20):
#    teszt+="C"
#    fejlec(teszt)

x =11_123_321
print(x+1)

print(0o123)#8as számrendszer
print(0xABBA)#16os számrendszer
print(0b11000000)#2es számrendszer

x=int("345", 36)#tetszőleges számrendszerből váltás 10-esbe
print(x)

x=oct(321)#váltás 8-as szr-be
print(x)

x=hex(40096)# váltás 16-os szr-be

x=bin(168)#váltás 2-es szr-be
print(x)

print(1/100000000)# le-08

str= 'Anya azt mondta hogy: \"Érj haza időben!"\"'
print(str)

x= 6/4
y= 6//4
y= 6//-4
z= 6%4
print(x)
print(y)
print(z)
z= 6%4
zs= 2**5
print(9 % 6 % 2)