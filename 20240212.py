gomboc = [10, 7, 8, 6, 4, 8, 2]
fagyi = [8, 6, 3, 7, 2, 6, 9]
golyo = [1, 8, 12, 9, 10, 1, 4]

osszes_gomboc = osszes_fagyi = osszes_golyo = 0
legtobb_gomboc = legtobb_fagyi = legtobb_golyo = 0

for g in gomboc:
    osszes_gomboc += g
    if g > legtobb_gomboc:
        legtobb_gomboc = g

for f in fagyi:
    osszes_fagyi += f
    if f > legtobb_fagyi:
        legtobb_fagyi = f

for g in golyo:
    osszes_golyo += g
    if g > legtobb_golyo:
        legtobb_golyo = g

print("Összes gombóc:", osszes_gomboc, "Összes fagyi:", osszes_fagyi, "Összes golyó:", osszes_golyo)
print("Legtöbb gombóc:", legtobb_gomboc, "Legtöbb fagyi:", legtobb_fagyi, "Legtöbb golyó:", legtobb_golyo)
