def fejlec(cim):
    szelesseg = 30
    csillagok = "*"*szelesseg
    kozepso_csillag = "*"*int(((szelesseg-len(cim))/2)-1)
    print(csillagok)
    if len(cim)%2==1:
        print(kozepso_csillag+" "+cim+" "+kozepso_csillag+"*")
    else:
        print(kozepso_csillag+" "+cim+" "+kozepso_csillag)
    print(csillagok)

program_neve ="Programcime"
fejlec(program_neve)

teszt=""
for i in range(2,20):
    teszt+="C"
    fejlec(teszt)
    "---4.feladat---"
def feladat4(filename):
    list = beolvas(filename)
    maximum = list[0]
    for i in range(1, len(list)):
        if list[i] > maximum:
            maximum = list[i]
    print(maximum)