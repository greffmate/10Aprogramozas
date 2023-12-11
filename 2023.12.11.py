# Adatok:
#   Fájlban:    Dolgozók nevei szerepelnek
#               Mellette hogy havonta mennyi palacsintát sütöttek meg

# 1) Olvasd be a fájlt megfelelő adatszerkezetbe!

filename="input2.txt"
file=open(filename, "r")
file_lista=file.readlines()
file.close()

print(file_lista)

name_list=[]
pancake_list=[]

for i in range (len(file_lista)):
    lista=file_lista[i].strip()
    lista_parts=lista.split()
    name_list.append(lista_parts[0])

#így is lehet    lista_parts=file_lista[i].strip().split()

    l=[]
    for j in range(1, len(lista_parts)):
        l.append(lista_parts[j])
    pancake_list.append(l)
    print(lista) #brakepoint

#print(name_list)
#print(pancake_list)
#for i in range (len(pancake_list)):
#print(len(pancake_list[i]))


# 2) írd ki az adatokat szépen(!!) az alábbbi fejléccel:
#       "Név\tJanuary\tFebruary\tMarch\tApril\tMay\tJune\tJuly\tAugust\tSeptember\tOctober\tNovember\tDecember"

fejlec="Név\tJanuary\tFebruary\tMarch\tApril\tMay\tJune\tJuly\tAugust\tSeptember\tOctober\tNovember\tDecember"
print(fejlec)

