"""
import sys
filename = sys.argv[1]
print(filename)

letezikafajl = True
try:
    file = open(filename)
except:
    print("A fájl nem létezik")

letezikafajl = False
if letezikafajl:
    sorok = file.readlines()
file.close()

for i in range(len(sorok)):
    print(sorok[i].strip())
"""

"""
if len(sys.argv)<2:
    print("Nem adtál meg fájlnevet")
    print(f"Helyesen py {sys.argv[0]} filename")
"""
import sys
import os

if len(sys.argv)<2:
    print()

elif not os.path.exists(sys.argv[1]):
    print("Nem létezik a fájl!")

else:
    filename = sys.argv[1]
    file = open(filename)
    sorok = file.readlines()
    file.close
