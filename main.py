fajlnev="input.txt"

f=open(fajlnev, "r") #read
sorok=f.readlines()
f.close()

print(sorok)

for i in range(len(sorok)):
    sorok[i]=sorok[i].strip()
print(sorok[0])

sum=int(sorok[1])+int(sorok[2])
print(sum)

l1=[2,3,4,6,12,28]
l2=l1[:] #l1 összes eleme
l2[1]=10
print(l1) #[2,10,4]
print(l1[1:3]) #3,4 (elő és második index)
print(l1[4:]) #12,28
print(l1[:2]) #2,3
print(l1[::3]) #2,6
print(l1[1:5:2]) #3,6

l2=[2,3]
del l2
print(l2)

3 in l1 #True
120 in l1 #False
120 not in l1 #True

l=[]
for i in range(10):
    l.append(i**2)

l=[i**2 for i in range(10)]


l=[
    [2,3,3,4]
    [3,4,5,8]
    [3,4,5,10,6]
]
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j])