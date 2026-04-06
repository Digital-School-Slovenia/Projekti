# Rešitve dodatnih nalog – 15 Funkcije prvi koraki


def pozdrav(ime):
    print(f"Živjo, {ime}!")


def kvadrat(stevilo):
    print(stevilo**2)


def v_sekunde(minute):
    print(minute * 60)


def glasno(beseda):
    print(beseda.upper())


def kratica(ime, priimek):
    print(f"{ime[0].upper()}.{priimek[0].upper()}.")


def je_polnoleten(starost):
    if starost >= 18:
        print("Uporabnik je polnoleten.")
    else:
        print("Uporabnik še ni polnoleten.")


def ploscina_pravokotnika(sirina, visina):
    print(sirina * visina)


def trikrat_pozdravi(ime):
    for _ in range(3):
        pozdrav(ime)


# Pet kratkih funkcij za nalogo 9.
# Parameter je podatek, ki ga funkcija sprejme v oklepaju.
def podvoji(stevilo):
    return stevilo * 2


def pozdrav_brez_vejice(ime):
    return f"Hej {ime}"


def je_sodo(stevilo):
    return stevilo % 2 == 0


def dodaj_klicaj(beseda):
    return beseda + "!"


def vecja_crka(beseda):
    return beseda.capitalize()


def tri_vrstice(besedilo):
    print(besedilo)
    print(besedilo.upper())
    print(besedilo.lower())


if __name__ == "__main__":
    print("Naloga 1")
    pozdrav("Matej")

    print("\nNaloga 2")
    kvadrat(6)

    print("\nNaloga 3")
    v_sekunde(5)

    print("\nNaloga 4")
    glasno("python")

    print("\nNaloga 5")
    kratica("Maja", "Novak")

    print("\nNaloga 6")
    je_polnoleten(17)
    je_polnoleten(19)

    print("\nNaloga 7")
    ploscina_pravokotnika(7, 4)

    print("\nNaloga 8")
    trikrat_pozdravi("Eva")

    print("\nNaloga 9")
    print(podvoji(8))
    print(pozdrav_brez_vejice("Ana"))
    print(je_sodo(12))
    print(dodaj_klicaj("Super"))
    print(vecja_crka("dijak"))

    print("\nNaloga 10")
    tri_vrstice("Danes vadim funkcije")
