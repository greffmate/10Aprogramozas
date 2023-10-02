#max kiválasztás

list=[12,325,235,6801,135,5646]
legnagyobb = list[0]
index = 0
for i in range(len(list)):
    if list[i] > legnagyobb:
        legnagyobb = list[i]
print (legnagyobb)
print(index+1)

#keresés
string = 'Máté'
if 'a' in string:
    print('van benne a betű')
else:
    print('nincs benne a betű')