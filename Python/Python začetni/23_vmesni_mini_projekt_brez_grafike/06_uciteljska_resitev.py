# Učiteljska referenčna rešitev – 23 Vmesni mini projekt brez grafike
# Inventar avanturista

inventar = []


def izpisi_meni():
    print("\n--- INVENTAR AVANTURISTA ---")
    print("1 - dodaj predmet")
    print("2 - pokaži inventar")
    print("3 - odstrani predmet")
    print("0 - konec")


def dodaj_predmet():
    predmet = input("Vnesi predmet: ").strip()
    if predmet == "":
        print("Prazen vnos ni dovoljen.")
        return
    inventar.append(predmet)
    print("Predmet je dodan.")


def izpisi_inventar():
    print("\n--- INVENTAR ---")
    if len(inventar) == 0:
        print("Inventar je prazen.")
        return

    for i, predmet in enumerate(inventar, start=1):
        print(f"{i}. {predmet}")

    print(f"Skupaj predmetov: {len(inventar)}")


def odstrani_predmet():
    predmet = input("Kateri predmet želiš odstraniti? ").strip()
    if predmet in inventar:
        inventar.remove(predmet)
        print("Predmet je odstranjen.")
    else:
        print("Tega predmeta ni v inventarju.")


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
