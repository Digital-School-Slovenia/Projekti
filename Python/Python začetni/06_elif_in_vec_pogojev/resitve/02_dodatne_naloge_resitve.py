"""Rešitve dodatnih nalog – 06 – `elif`, `else` in več možnosti odločanja."""

# Namen: rešitve dodatnih nalog po vrstnem redu iz 04_dodatne_naloge.md.

def ocena_v_besedo(ocena):
    if ocena == 5:
        return "odlicno"
    elif ocena == 4:
        return "prav dobro"
    elif ocena == 3:
        return "dobro"
    elif ocena == 2:
        return "zadostno"
    else:
        return "nezadostno"


def opis_temperature(temperatura):
    if temperatura < 0:
        return "zmrzuje"
    elif temperatura < 15:
        return "hladno"
    elif temperatura < 25:
        return "prijetno"
    else:
        return "vroce"


def kategorija_tock(tocke):
    if tocke >= 90:
        return "mojster"
    elif tocke >= 70:
        return "napreden"
    elif tocke >= 40:
        return "zacetnik"
    return "vadba se bo koristila"


print(ocena_v_besedo(4))
print(opis_temperature(18))
print(kategorija_tock(72))
