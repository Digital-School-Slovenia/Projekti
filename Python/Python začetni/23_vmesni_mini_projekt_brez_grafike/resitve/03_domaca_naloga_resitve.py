"""Rešitve domače naloge – 23 – Vmesni mini projekt brez grafike."""

# Namen: rešitve domače naloge po vrstnem redu iz 05_domaca_naloga.md.

# Ta program vodi preprost inventar avanturista.

inventar = []


def izpisi_meni():
    print("\n--- DOMAČI INVENTAR ---")
    print("1 - dodaj predmet")
    print("2 - pokaži inventar")
    print("3 - odstrani predmet")
    print("0 - konec")


def dodaj_predmet():
    predmet = input("Vnesi predmet: ").strip()
    if predmet == "":
        print("Prazen predmet ni dovoljen.")
        return

    if predmet.lower() in [ime.lower() for ime in inventar]:
        print("Ta predmet je že v inventarju.")
        return

    inventar.append(predmet)
    print("Predmet je dodan.")


def izpisi_inventar():
    print("\n--- INVENTAR ---")
    if not inventar:
        print("Inventar je prazen.")
        return

    for indeks, predmet in enumerate(inventar, start=1):
        print(f"{indeks}. {predmet}")

    print(f"Skupaj predmetov: {len(inventar)}")


def odstrani_predmet():
    predmet = input("Kateri predmet želiš odstraniti? ").strip()
    if predmet in inventar:
        inventar.remove(predmet)
        print("Predmet je odstranjen.")
    else:
        print("Tega predmeta ni v inventarju.")


if __name__ == "__main__":
    while True:
        izpisi_meni()
        izbira = input("Izbira: ").strip()

        if izbira == "1":
            dodaj_predmet()
        elif izbira == "2":
            izpisi_inventar()
        elif izbira == "3":
            odstrani_predmet()
        elif izbira == "0":
            print("Konec programa.")
            break
        else:
            print("Neveljavna izbira.")

# Največ dela mi je povzročalo preverjanje podvojenih predmetov, zato sem dodal if stavek pred append().
