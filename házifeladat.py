def szigorúan_monotonon_növekvő(szamlista):
    for i in range(1, len(szamlista)):
        if szamlista[i] <= szamlista[i - 1]:
            return False
        return True


szamlista = [1, 3, 5, 7, 9]
if szigorúan_monotonon_növekvő(szamlista):
    print("A szamlista szigoruan monotonon novekvo.")
else:
    print("A szamlista nem szigorian monotonon novekvo.")