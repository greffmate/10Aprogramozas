file = open("input3")
sorok = file.readlines()
file.close()

print(sorok)
szamok=[]
for i in range(1,len(sorok)):
    szamok.append(int(sorok[i].strip()))

print(szamok)