def fajl_beolvasas(fajl_nev):
    with open(fajl_nev, 'r') as fajl:
        tartalom = [list(map(int, sor.split())) for sor in fajl.readlines()]
    return tartalom

def menu_megjelenites():
    print("Menüpontok:")
    print("1. Számok összege")
    print("2. Számok soronkénti összege")
    print("3. Számok oszloponkénti összege")
    print("0. Kilépés")

def sorok_osszege_kiiras(adatok):
    for i, sor in enumerate(adatok, start=1):
        sor_osszeg = sum(sor)
        print("{}. sor: {}".format(i, sor_osszeg))

def oszlopok_osszege_kiiras(adatok):
    for i, oszlop_osszeg in enumerate(map(sum, zip(*adatok)), start=1):
        print("{}. oszlop: {}".format(i, oszlop_osszeg))

def main():
    bemenet = fajl_beolvasas("input1.txt")
    
    while True:
        menu_megjelenites()
        valasztas = input("Válassz egy menüpontot (0-3): ")
        
        if valasztas == '0':
            print("Kilépés!")
            break
        elif valasztas == '1':
            osszeg = sum([szam for sor in bemenet for szam in sor])
            print("Az összeg: {}".format(osszeg))
        elif valasztas == '2':
            sorok_osszege_kiiras(bemenet)
        elif valasztas == '3':
            oszlopok_osszege_kiiras(bemenet)
        else:
            print("Érvénytelen választás! Kérlek válassz újra.")

if __name__ == "__main__":
    main()