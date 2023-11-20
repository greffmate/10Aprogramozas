x=input("x=")
input("y=")

x="ha"*3
print(x)

x= 3 ==2
print(x)

x= 3 !=2
print(x)

x=2

if x==3:
    print("Az x értéke: 3")
elif x<3:
    print("Az x értéke akkor kisebb, mint 3")
else:
    print("Egyik feltétel sem igaz")

#ide

x=5
feltetel= True
while feltetel:
    print("ciklusmag")
    if(x==7):
        feltetel=False
    x+=1
print(x)
'''
i=1
while True:
    print("Szeretem a Puskást!", i)
    i+=1'''

x=5
while x<4:
    pass
else:
    print("nem lépett a ciklusba")

ijk=7
for ijk in range(10):
    print(ijk)
else:
    print("else ág",ijk)


x=3
y=6
print(x>y)
print(not (x>y))
print(not(x<=y))
print(True and True)
print(True and False)
print(True and False and True)
print(True or False or True)

print(1 and 0)
print(1 and 1)
print((1 and 1) and (1 and 1))
print((1 or 1) or (1 or 1))
print((1 or 1) or (1 or 0))
print((1 or 0) or (1 or 0))
print((1 or 0) or (0 or 0))
print((0 or 0) or (0 or 0))

a,b,c,d=1,1,1,1
print((a or b) and (c or d))
print((a and b) or (c and d))

#XOR
print(1 ^ 0)
print(1 ^ 0)

print(1 & 1)
print(3 & 2)
#3: 11
#2: 10
#eredmeny: 10
print(3 | 2)
#3: 11
#2: 10
#eredmeny: 11

print( ~5)
#  5: 101
#  ~5: 010


