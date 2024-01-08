import random

ismetles = True
jegyek = []
while ismetles:
    jegy = input("add meg a diák jegyét [0...100]: ")
    if jegy == "vége":
        ismetles = False
    elif 0 <= int(jegy) <= 100:
        jegyek.append(int(jegy))
    else:
        print("hibás adatbevitel!")

legrosszabb = 101
legjobb = -1
for i in range(len(jegyek)):
    if jegyek[i] < legrosszabb:
        legrosszabb = jegyek[i]
    if jegyek[i] > legjobb:
        legjobb = jegyek[i]

print(f"legjobb jegy: {legjobb}")
print(f"legrosszabb jegy: {legrosszabb}")


minimum = -1
maximum = -1
while not 100 >= minimum >= 0 or not 100 >= maximum >= 0:
    minimum = int(input("add meg a legkisebb értéket, amit látni szeretnél: "))
    maximum = int(input("add meg a legnagyobb értéket, amit látni szeretnél: "))

megfelelo = []
megfelel = 0
for i in range(len(jegyek)):
    if maximum >= jegyek[i] >= minimum:
        megfelelo.append(jegyek[i])
        megfelel += 1

print(f"az intervallumon belül {megfelel} db jegy van:", end=" ")
for i in range(len(megfelelo)):
    print(megfelelo[i], end=" ")
print()


osszeg = 0
for i in range(len(jegyek)):
    osszeg += jegyek[i]
atlag = osszeg / len(jegyek)
print(f"az osztályátlag: {atlag}")


jegyek2 = []
for i in range(len(jegyek)):
    jegyek2.append(random.randint(0, 100))
osszeg2 = 0
for i in range(len(jegyek2)):
    osszeg += jegyek2[i]
atlag2 = osszeg2 / len(jegyek2)
if atlag > atlag2:
    print("az első osztály átlaga a nagyobb.")
elif atlag < atlag2:
    print("a második osztály átlaga a nagyobb.")
else:
    print("a két oszátly átlaga egyenlő.")