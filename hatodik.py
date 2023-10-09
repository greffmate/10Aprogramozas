'''
s = input("adj meg egy számot")
if int(s)%2==0:
    print("a szám osztható 2-vel")
'''

str="ez egy mondat. ez egy mondat."

'''
str = input("adj meg egy szöveget")
if "a " in str:
    print("az a betű benne van a szövegben")

for i in range(len(str)):
    if str[i] == "a":
        hely = i
print(hely+1)
'''

mondatok = 0
for i in range(len(str)):
    if str[i] =='.':
        mondatok = mondatok+1
print(f"{mondatok} mondat van")