# Rešitve dodatnih nalog – 10 For in range


def izpisi_od_1_do_10():
    for stevilo in range(1, 11):
        print(stevilo)


def izpisi_soda_do_20():
    for stevilo in range(2, 21, 2):
        print(stevilo)


def odstevaj_od_10_do_1():
    for stevilo in range(10, 0, -1):
        print(stevilo)


def petkrat_izpisi(stavek):
    for _ in range(5):
        print(stavek)


def izpisi_postevanko(stevilo):
    for faktor in range(1, 11):
        print(f"{stevilo} x {faktor} = {stevilo * faktor}")


def izpisi_liha_med_1_in_30():
    for stevilo in range(1, 31, 2):
        print(stevilo)


def vsota_do_100():
    skupna_vsota = 0
    for stevilo in range(1, 101):
        skupna_vsota += stevilo
    return skupna_vsota


def poisci_delitelje(stevilo):
    delitelji = []
    for kandidat in range(1, stevilo + 1):
        if stevilo % kandidat == 0:
            delitelji.append(kandidat)
    return delitelji


def vsota_sodih_v_intervalu(zacetek, konec):
    skupna_vsota = 0
    for stevilo in range(zacetek, konec + 1):
        if stevilo % 2 == 0:
            skupna_vsota += stevilo
    return skupna_vsota


if __name__ == "__main__":
    print("Naloga 1")
    izpisi_od_1_do_10()

    print("\nNaloga 2")
    izpisi_soda_do_20()

    print("\nNaloga 3")
    odstevaj_od_10_do_1()

    print("\nNaloga 4")
    petkrat_izpisi("Python je zabaven.")

    print("\nNaloga 5")
    izpisi_postevanko(7)

    print("\nNaloga 6")
    izpisi_liha_med_1_in_30()

    print("\nNaloga 7")
    print(vsota_do_100())

    print("\nNaloga 8")
    print(poisci_delitelje(24))

    print("\nNaloga 9")
    print(vsota_sodih_v_intervalu(4, 18))
