"""Rešitve domače naloge – 10 – Zanka `for` in `range`."""

# Namen: rešitve domače naloge po vrstnem redu iz 05_domaca_naloga.md.

def izpisi_od_1_do_10():
    for stevilo in range(1, 11):
        print(stevilo)


def izpisi_od_10_do_1():
    for stevilo in range(10, 0, -1):
        print(stevilo)


def prestej_ovcke(stevilo_ovck):
    for ovcka in range(1, stevilo_ovck + 1):
        print(f"Ovčka št. {ovcka} skoči čez ograjo!")


def preberi_in_prestej_ovcke():
    stevilo_ovck = int(input("Koliko ovčk želiš prešteti? "))
    prestej_ovcke(stevilo_ovck)


if __name__ == "__main__":
    print("Naloga 1")
    izpisi_od_1_do_10()

    print("\nNaloga 2")
    izpisi_od_10_do_1()

    print("\nNaloga 3")
    prestej_ovcke(5)

    # Če želiš preizkusiti pravi vnos uporabnika, odkomentiraj spodnjo vrstico.
    # preberi_in_prestej_ovcke()

    # Naloga 4 – primer kratkega odgovora:
    # Največ časa sem porabil pri odštevanju nazaj, ker sem moral paziti na korak -1.
