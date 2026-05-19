# Referenčni primer – 15 Funkcije prvi koraki

# Namen: kratek referenčni primer za razlago glavne ideje tega sklopa.


def pozdravi(ime):
    print(f"Živjo, {ime}!")


def izracunaj_obseg_kvadrata(stranica):
    return 4 * stranica


pozdravi("Eva")
obseg = izracunaj_obseg_kvadrata(6)
print("Obseg kvadrata je", obseg)
