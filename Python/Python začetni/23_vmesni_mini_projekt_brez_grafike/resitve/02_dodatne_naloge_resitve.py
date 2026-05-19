"""Rešitve dodatnih nalog – 23 – Vmesni mini projekt brez grafike."""

# Namen: rešitve dodatnih nalog po vrstnem redu iz 04_dodatne_naloge.md.

inventar = [
    {"ime": "meč", "tip": "orožje"},
    {"ime": "ključ", "tip": "orodje"},
    {"ime": "jabolko", "tip": "hrana"},
]


def izpisi_meni():
    print("\n--- INVENTAR AVANTURISTA PLUS ---")
    print("1 - dodaj predmet")
    print("2 - pokaži inventar")
    print("3 - odstrani predmet po številki")
    print("4 - poišči predmet")
    print("5 - počisti inventar")
    print("0 - konec")


def predmet_ze_obstaja(ime_predmeta):
    for predmet in inventar:
        if predmet["ime"].lower() == ime_predmeta.lower():
            return True
    return False


def dodaj_predmet():
    ime = input("Ime predmeta: ").strip()
    tip = input("Tip predmeta: ").strip()

    if ime == "" or tip == "":
        print("Ime in tip morata biti izpolnjena.")
        return

    if predmet_ze_obstaja(ime):
        print("Ta predmet je že v inventarju.")
        return

    inventar.append({"ime": ime, "tip": tip})
    print("Predmet je dodan.")


def izpisi_inventar():
    print("\n--- INVENTAR ---")
    if not inventar:
        print("Inventar je prazen.")
        return

    print(f"V inventarju je {len(inventar)} predmetov.")
    for indeks, predmet in enumerate(inventar, start=1):
        print(f"{indeks}. {predmet['ime']} ({predmet['tip']})")


def odstrani_predmet_po_stevilki():
    if not inventar:
        print("Inventar je prazen.")
        return

    izpisi_inventar()
    vnos = input("Katero številko želiš odstraniti? ").strip()

    if not vnos.isdigit():
        print("Vnesti moraš številko.")
        return

    stevilka = int(vnos)
    if 1 <= stevilka <= len(inventar):
        odstranjen = inventar.pop(stevilka - 1)
        print(f"Odstranjen predmet: {odstranjen['ime']}")
    else:
        print("Takšne številke ni v inventarju.")


def poisci_predmet():
    iskano = input("Vnesi del imena predmeta: ").strip().lower()
    if iskano == "":
        print("Vnos ne sme biti prazen.")
        return

    zadetki = []
    for predmet in inventar:
        if iskano in predmet["ime"].lower():
            zadetki.append(predmet)

    if not zadetki:
        print("Ni zadetkov.")
        return

    print("Najdeni predmeti:")
    for predmet in zadetki:
        print(f"- {predmet['ime']} ({predmet['tip']})")


def pocisti_inventar():
    inventar.clear()
    print("Inventar je zdaj prazen.")


if __name__ == "__main__":
    while True:
        izpisi_meni()
        izbira = input("Izbira: ").strip()

        if izbira == "1":
            dodaj_predmet()
        elif izbira == "2":
            izpisi_inventar()
        elif izbira == "3":
            odstrani_predmet_po_stevilki()
        elif izbira == "4":
            poisci_predmet()
        elif izbira == "5":
            pocisti_inventar()
        elif izbira == "0":
            print("Konec programa.")
            break
        else:
            print("Neveljavna izbira.")
