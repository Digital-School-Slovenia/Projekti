# Učiteljska referenčna rešitev – 23 Vmesni mini projekt brez grafike
# Mini upravljalnik nalog (to-do).

naloge = []


def izpisi_meni():
    print("\n--- TO-DO ---")
    print("1 - dodaj nalogo")
    print("2 - izpiši naloge")
    print("3 - označi kot opravljeno")
    print("4 - izbriši nalogo")
    print("0 - konec")


def izpisi_naloge():
    if not naloge:
        print("Seznam je prazen.")
        return
    for i, naloga in enumerate(naloge, start=1):
        status = "✅" if naloga["opravljeno"] else "⬜"
        print(f"{i}. {status} {naloga['besedilo']}")


while True:
    izpisi_meni()
    izbira = input("Izbira: ")

    if izbira == "1":
        besedilo = input("Vnesi nalogo: ")
        naloge.append({"besedilo": besedilo, "opravljeno": False})
    elif izbira == "2":
        izpisi_naloge()
    elif izbira == "3":
        izpisi_naloge()
        indeks = int(input("Katera naloga je opravljena? ")) - 1
        if 0 <= indeks < len(naloge):
            naloge[indeks]["opravljeno"] = True
    elif izbira == "4":
        izpisi_naloge()
        indeks = int(input("Katero nalogo izbrišem? ")) - 1
        if 0 <= indeks < len(naloge):
            naloge.pop(indeks)
    elif izbira == "0":
        print("Konec programa.")
        break
    else:
        print("Neveljavna izbira.")
